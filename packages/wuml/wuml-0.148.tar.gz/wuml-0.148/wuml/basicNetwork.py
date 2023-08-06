#!/usr/bin/env python
import os 
import sys

if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')
if os.path.exists('/home/chieh/code/wuML'):
	sys.path.insert(0,'/home/chieh/code/wuML')

import torch
import numpy as np
import sys
from wuml.IO import *
from sklearn import linear_model
from torch import nn
from torch.autograd import Variable
from inspect import signature
import torch.nn.functional as F
import torch.nn as nn
import collections
from wuml import wtype
import marshal

class flexable_Model(torch.nn.Module):
	#	Note that currently batch normalization is automatically included, so eval must be called before running test data
	def __init__(self, dataDim, networkStructure):
		super(flexable_Model, self).__init__()

		self.networkStructure = networkStructure
		inDim = dataDim
		for l, Layer_info in enumerate(networkStructure):
			if wtype(Layer_info) == 'tuple':	# it is a regular layer
				### new batch normalization code
				if wtype(Layer_info[0]) == 'str':
					bn , train_gamma_beta_parameters = Layer_info
					cmd = ('self.l' + str(l) + '_BN = nn.BatchNorm1d(num_features=' + str(inDim) + ', affine=' + str(train_gamma_beta_parameters) + ')')
					exec(cmd)
				else:
					layer_width, activation_function = Layer_info
					φ = activation_function
					outDim = layer_width
					lr = 'self.l' + str(l) + ' = torch.nn.Linear(' + str(inDim) + ', ' + str(outDim) + ' , bias=True)'

					#print(lr)
					#import pdb; pdb.set_trace()
					exec(lr)
					exec('self.l' + str(l) + '.activation = "' + φ + '"')		#softmax, relu, tanh, sigmoid, none



	#self.l0 = torch.nn.Linear(10, 8 , bias=True)	

			#### new batch normalization code
			#elif wtype(Layer_info) == 'str':	# it is a batch norm layer
			#	cmd = ('self.l' + str(l) + '_BN = nn.BatchNorm1d(num_features=' + str(inDim) + ', affine=' + + ')')
			#	#print(cmd)
			#	exec(cmd)

			inDim = outDim


	def forward(self, x):
		self.y0 = x

		for m, layer in enumerate(self.children(),0):
			var = 'self.y' + str(m+1)	
			if type(layer).__name__ == 'Linear':
				if layer.activation == 'none':
					cmd = 'self.yout = ' + var + ' = self.l' + str(m) + '(self.y' + str(m) + ')'
				else:
					cmd = 'self.yout = ' + var + ' = F.' + layer.activation + '(self.l' + str(m) + '(self.y' + str(m) + '))'
				exec(cmd)

				#print(cmd)
				#import pdb; pdb.set_trace()

			#batch Normalization code
			elif type(layer).__name__ == 'BatchNorm1d':
				cmd = 'self.yout = ' + var + ' = self.l' + str(m) + '_BN(self.yout)'
				#print(cmd)
				exec(cmd)

		if torch.isnan(self.yout).any():
			print('\n nan was detected inside a network forward\n')
			import pdb; pdb.set_trace()

		return self.yout


def run_SGD(loss_function, model_parameters, trainLoader, device, early_exit_loss_threshold=0.000000001,
				X_dataType=torch.FloatTensor, Y_dataType=torch.FloatTensor,
				model=None, lr=0.001, print_status=True, max_epoch=1000,
				on_new_epoch_call_back=None):


	optimizer = torch.optim.Adam(model_parameters, lr=lr)	
	scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau( optimizer, factor=0.5, min_lr=1e-10, patience=50, verbose=False)

	# For all loss check https://neptune.ai/blog/pytorch-loss-functions
	if type(loss_function).__name__ == 'str':
		if loss_function == 'mse':
			loss_function = nn.MSELoss()
		elif loss_function == 'L1':
			loss_function = nn.L1Loss()
		elif loss_function == 'CE':
			loss_function = nn.CrossEntropyLoss()
		elif loss_function == 'hindge':
			loss_function = nn.HingeEmbeddingLoss()

	paramLen = len(signature(loss_function).parameters) # number of arguments


	for epoch in range(max_epoch):

		loss_list = []	
		for (i, data) in enumerate(trainLoader):
			[x, y, ind] = data

			x = Variable(x.type(X_dataType), requires_grad=False)
			y = Variable(y.type(Y_dataType), requires_grad=False)
			x= x.to(device, non_blocking=True )
			y= y.to(device, non_blocking=True )
			optimizer.zero_grad()

			if model is not None:
				ŷ = model(x)
				ŷ = torch.squeeze(ŷ)
				y = torch.squeeze(y)

				if paramLen == 4:
					loss = loss_function(x, y, ŷ, ind)
				elif paramLen == 3:
					loss = loss_function(x, y, ind)
				elif paramLen == 2:
					#loss = loss_function(y, ŷ)
					loss = loss_function(ŷ,y)
			else:
				try:
					loss = loss_function(x, y, ind)
				except:
					loss = loss_function(x, y)

			if torch.isnan(loss): import pdb; pdb.set_trace()

			loss.backward()
			optimizer.step()

			loss_list.append(loss.item())

		loss_avg = np.array(loss_list).mean()
		scheduler.step(loss_avg)

		if loss_avg < early_exit_loss_threshold: break;
		if print_status:
			txt = '\tepoch: %d, Avg Loss: %.4f, Learning Rate: %.8f'%((epoch+1), loss_avg, scheduler._last_lr[0])
			write_to_current_line(txt)

		if on_new_epoch_call_back is not None:
			on_new_epoch_call_back(loss_avg, (epoch+1), scheduler._last_lr[0])

		if model is not None:
			if "on_new_epoch" in dir(model):
				early_exit = model.on_new_epoch(loss_avg, (epoch+1), scheduler._last_lr[0])
				if early_exit: break



class basicNetwork:
	def __init__(self, costFunction, X, 
						Y=None, networkStructure=[(3,'relu'),(3,'relu'),(3,'none')], early_exit_loss_threshold=0.000000001, 
						on_new_epoch_call_back = None, max_epoch=1000, 	X_dataType=torch.FloatTensor, 
						Y_dataType=torch.FloatTensor, learning_rate=0.001, pickled_network_info=None,
						network_usage_output_type='Tensor', network_usage_output_dim='none', network_info_print=True,
						override_network_input_width_as=None): 
		'''
			X : This should be wData type
			possible activation functions: softmax, relu, tanh, sigmoid, none
			pickled_network_info: if a network info package is passed as this argument, we create a new network strip of unnecessary stuff
			network_usage_output_dim: network output dimension, 0, 1 or 2
		'''
		if get_commandLine_input()[1] == 'disabled': max_epoch = 10

		self.network_usage_output_type = network_usage_output_type
		self.network_usage_output_dim = network_usage_output_dim
		self.early_exit_loss_threshold = early_exit_loss_threshold
		if pickled_network_info is None:
			#	X should be in wuml format
			self.trainLoader = X.get_data_as('DataLoader')

			self.lr = learning_rate
			self.max_epoch = max_epoch
			self.X_dataType = X_dataType
			self.Y_dataType = Y_dataType
			self.costFunction = costFunction
			self.NetStructure = networkStructure
			self.on_new_epoch_call_back = on_new_epoch_call_back #set this as a callback at each function
			self.network_output_in_CPU_during_usage = False
			if X.label_type == 'discrete': 
				self.Y_dataType = torch.int64		#overide datatype if discrete labels

			if override_network_input_width_as is None:	#This is done during customized complex nework structures
				self.model = flexable_Model(X.shape[1], networkStructure)
			else:
				self.model = flexable_Model(override_network_input_width_as, networkStructure)


		else:
			self.costFunction = costFunction
			self.on_new_epoch_call_back = on_new_epoch_call_back #set this as a callback at each function

			θ = pickled_network_info
			self.lr = θ['lr']
			self.max_epoch = θ['max_epoch']
			self.X_dataType = θ['X_dataType']
			self.Y_dataType = θ['Y_dataType']
			self.NetStructure = θ['NetStructure']
			self.model = θ['model']
			self.network_output_in_CPU_during_usage = True

		self.device = wuml.get_current_device()
		self.model.to(self.device)		# store the network weights in gpu or cpu device

		self.out_structural = None
		self.info(printOut=network_info_print)
		self.network_info_print = network_info_print


		#	Catch some errors
		if costFunction == 'CE' and X.label_type == 'continuous':
			print("\n the data label_type should not be continuous when using 'CE' as costFunction during classification!!!\n")
		elif costFunction == 'hindge' and X.label_type == 'continuous':
			print("\n the data label_type should not be continuous when using 'hindge' as costFunction during classification!!!\n")

	def output_network_data_for_storage(self):
		net = {}
		net['name'] = self.__class__.__name__
		#net['cfunction'] = marshal.dumps(self.costFunction.__code__)
		#if self.on_new_epoch_call_back is None: net['on_new_epoch_call_back'] = None
		#else: net['on_new_epoch_call_back'] = marshal.dumps(self.on_new_epoch_call_back.__code__)

		net['lr'] = self.lr
		net['max_epoch'] = self.max_epoch
		net['X_dataType'] = self.X_dataType
		net['Y_dataType'] = self.Y_dataType
		net['NetStructure'] = self.NetStructure
		net['model'] = self.model
		net['network_output_in_CPU_during_usage'] = self.network_output_in_CPU_during_usage
		return net


	def parameters(self):
		return self.model.parameters()

	def info(self, printOut=True):
		
		info_str ='Network Info:\n'
		info_str += '\tLearning rate: %.3f\n'%self.lr
		info_str += '\tMax number of epochs: %d\n'%self.max_epoch
		info_str += '\tCost Function: %s\n'%wuml.get_function_name(self.costFunction)
		info_str += '\tTrain Loop Callback: %s\n'%str(self.on_new_epoch_call_back)
		info_str += '\tDevice type: %r\n'%self.device
		info_str += '\tNetwork Structure\n'
		for i in self.model.children():
			try:
				info_str += ('\t\t%s , %s\n'%(i,i.activation))
			except:
				info_str += ('\t\t%s \n'%(i))
		
		if printOut: wuml.jupyter_print(info_str)
		return info_str

	def predict(self, data):
		return self.__call__(data, output_type='ndarray')

	def __call__(self, data, output_type='Tensor', out_structural=None):
		'''
			out_structural (mostly for classification purpose): None, '1d_labels', 'one_hot'
		'''
		if out_structural is None: out_structural = self.out_structural
		if wtype(data) == 'ndarray': 
			x = torch.from_numpy(data)
			x = Variable(x.type(self.X_dataType), requires_grad=False)
			x= x.to(self.device, non_blocking=True )
		elif wtype(data) == 'Tensor': 
			x = data
			x= x.to(self.device, non_blocking=True )
		elif wtype(data) == 'wData': 
			x = data.get_data_as('Tensor')
		elif wtype(data)=='DataFrame':
			x = torch.from_numpy(data.values)
			x = Variable(x.type(self.X_dataType), requires_grad=False)
			x= x.to(self.device, non_blocking=True )
		else:
			raise ValueError('\n\tError torch network input as %s is unrecognized'%wtype(data))

		yout = self.model(x)

		if self.network_usage_output_dim == 0 or self.network_usage_output_dim == 1:
			yout = torch.squeeze(yout)
		if self.network_usage_output_dim == 2:
			yout = torch.atleast_2d(yout)


		if out_structural == '1d_labels':
			_, yout = torch.max(yout, 1)
		elif out_structural == 'one_hot':
			_, yout = torch.max(yout, 1)
			yout = wuml.one_hot_encoding(yout, output_data_type='same')
		elif out_structural == 'softmax':
			m = nn.Softmax(dim=1)
			yout = m(yout)

		if output_type == 'ndarray' or self.network_usage_output_type == 'ndarray':
			return yout.detach().cpu().numpy()
		elif self.network_output_in_CPU_during_usage:
			return yout.detach().cpu()

		return yout


	def eval(self, output_type='ndarray', out_structural=None):		#	Turn this on to run test results
		self.network_usage_output_type = output_type
		if out_structural is not None: self.out_structural = out_structural
		self.model.eval()

	def train(self, print_status=True):
		param = self.model.parameters()
		[ℓ, TL, mE, Dev] = [self.costFunction, self.trainLoader, self.max_epoch, self.device]
		[Xtype, Ytype] = [self.X_dataType, self.Y_dataType]

		run_SGD(ℓ, param, TL, Dev, model=self.model, lr=self.lr, print_status=print_status,
				max_epoch=mE, X_dataType=Xtype, Y_dataType=Ytype, early_exit_loss_threshold=self.early_exit_loss_threshold,
				on_new_epoch_call_back = self.on_new_epoch_call_back)

	def fit(self, X,Y):
		self.train(print_status=self.network_info_print)

