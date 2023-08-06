#!/usr/bin/env python

import numpy as np
import sklearn.metrics
import sklearn.metrics.pairwise
from scipy.stats.stats import pearsonr  
from sklearn.metrics.cluster import normalized_mutual_info_score
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from wuml.opt_gaussian import *
import pandas as pd
import numpy as np
#import ppscore as pps
import wuml
from wuml import wtype
from torch import nn
import torch


from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


# compute normalized HSIC between X,Y
# if sigma_type = mpd, it uses median of pairwise distance
# if sigma_type = opt, it uses optimal
def HSIC(X,Y, X_kernel='Gaussian', Y_kernel='Gaussian', sigma_type='opt', normalize_hsic=True, gamma_x=None, gamma_y=None):	

	#X = X.detach().cpu().numpy()
	#Y = Y.detach().cpu().numpy()

	if wtype(X) == 'Tensor':
		return HSIC_Tensor(X,Y, X_kernel=X_kernel, Y_kernel=Y_kernel, sigma_type=sigma_type, normalize_hsic=normalize_hsic, gamma_x=gamma_x, gamma_y=gamma_y)
	else:
		return HSIC_numpy(X,Y, X_kernel=X_kernel, Y_kernel=Y_kernel, sigma_type=sigma_type, normalize_hsic=normalize_hsic, gamma_x=gamma_x, gamma_y=gamma_y)





# compute normalized HSIC between X,Y
# if sigma_type = mpd, it uses median of pairwise distance
# if sigma_type = opt, it uses optimal
def HSIC_Tensor(X,Y, X_kernel='Gaussian', Y_kernel='Gaussian', sigma_type='opt', normalize_hsic=True, gamma_x=None, gamma_y=None):	

	def get_γ(X,Y, sigma_type):
		if X_kernel == 'linear' and Y_kernel == 'linear': return [0,0]

		pdist = nn.PairwiseDistance(p=2)

		self.x_pd = torch.cdist(X, X)
		self.y_pd = torch.cdist(Y, Y)

		σᵪ = torch.median(self.x_pd)
		σᵧ = torch.median(self.y_pd)
			
		if σᵪ == 0: σᵪ = 0.1
		if σᵧ == 0: σᵧ = 0.1

		γᵪ = 1.0/(2*σᵪ*σᵪ)
		γᵧ = 1.0/(2*σᵧ*σᵧ)

		return [γᵪ, γᵧ]

	def double_center(Ψ):
		HΨ = Ψ - np.mean(Ψ, axis=0)								# equivalent to Γ = Ⲏ.dot(Kᵧ).dot(Ⲏ)
		HΨH = (HΨ.T - np.mean(HΨ.T, axis=0)).T
		return HΨH

	def get_Kᵪ(X, Y, X_kernel, γ):
		if X_kernel == 'linear': 
			#Kᵪ = X.dot(X.T)
			Kᵪ = torch.mm(X, X.t())
		elif X_kernel == 'Gaussian':
			Mx = self.x_pd
			Kᵪ = torch.exp(-γ*(Mx*Mx))
			#Kᵪ = sklearn.metrics.pairwise.rbf_kernel(X, gamma=γ)

		return Kᵪ

	def get_Kᵧ(X, Y, X_kernel, γ):
		if Y_kernel == 'linear': 
			#Yₒ = OneHotEncoder(categories='auto', sparse=False).fit_transform(Y)
			#Kᵧ = Yₒ.dot(Yₒ.T)
			Kᵧ = torch.mm(Y, Y.t())
		elif X_kernel == 'Gaussian':
			My = self.y_pd
			Kᵧ = torch.exp(-γ*(My*My))

			#[γᵪ, γᵧ] = get_γ(X, Y, sigma_type)
			#Kᵧ = sklearn.metrics.pairwise.rbf_kernel(Y, gamma=γ)

		return Kᵧ

	n = X.shape[0]
	if Y.dim() == 1: Y = torch.unsqueeze(Y, dim=0).t()
	if X.dim() == 1: X = torch.unsqueeze(X, dim=0).t()
	Y = Y.float()

	[γᵪ, γᵧ] = get_γ(X, Y, sigma_type)

	Kᵪ = get_Kᵪ(X, Y, X_kernel, γᵪ)
	Kᵧ = get_Kᵧ(X, Y, X_kernel, γᵧ)

	HKᵪ = Kᵪ - torch.mean(Kᵪ, dim=0)					# equivalent to		HKᵪ = H.dot(Kᵪ)
	HKᵧ = Kᵧ - torch.mean(Kᵧ, dim=0)                  # equivalent to		HKᵧ = H.dot(Kᵧ)

	Hᵪᵧ= torch.sum(HKᵪ.t()*HKᵧ)			# same as HKᵪH = double_center(Kᵪ)

	if Hᵪᵧ == 0: return 0
	if not normalize_hsic: return Hᵪᵧ/(n*n)

	Hᵪ = torch.sqrt(torch.sum(HKᵪ.t()*HKᵪ))			# same as HKᵪH = double_center(Kᵪ)
	Hᵧ = torch.sqrt(torch.sum(HKᵧ.t()*HKᵧ))			# same as HKᵪH = double_center(Kᵪ)

	H = Hᵪᵧ/( Hᵪ * Hᵧ )
	return H



# compute normalized HSIC between X,Y
# if sigma_type = mpd, it uses median of pairwise distance
# if sigma_type = opt, it uses optimal
def HSIC_numpy(X,Y, X_kernel='Gaussian', Y_kernel='Gaussian', sigma_type='opt', normalize_hsic=True, gamma_x=None, gamma_y=None):	
	X = wuml.ensure_numpy(X)
	Y = wuml.ensure_numpy(Y)

	def get_γ(X,Y, sigma_type):
		if X_kernel == 'linear' and Y_kernel == 'linear': 
			return [0,0]

		if sigma_type == 'mpd': 
			σᵪ = np.median(sklearn.metrics.pairwise_distances(X))		
			σᵧ = np.median(sklearn.metrics.pairwise_distances(Y))
			
			if σᵪ == 0: σᵪ = 0.1
			if σᵧ == 0: σᵧ = 0.1
		else: 
			optimizer = opt_gaussian(X,Y, Y_kernel=Y_kernel)
			optimizer.minimize_H()
			σᵪ = optimizer.result.x[0]
			σᵧ = optimizer.result.x[1]
			if σᵪ < 0.01: σᵪ = 0.01		# ensure that σ is not too low
			if σᵧ < 0.01: σᵧ = 0.01		# ensure that σ is not too low

		γᵪ = 1.0/(2*σᵪ*σᵪ)
		γᵧ = 1.0/(2*σᵧ*σᵧ)

		if gamma_x is not None: γᵪ = gamma_x
		if gamma_y is not None: γᵧ = gamma_y

		return [γᵪ, γᵧ]

	def double_center(Ψ):
		HΨ = Ψ - np.mean(Ψ, axis=0)								# equivalent to Γ = Ⲏ.dot(Kᵧ).dot(Ⲏ)
		HΨH = (HΨ.T - np.mean(HΨ.T, axis=0)).T
		return HΨH

	def get_Kᵪ(X, Y, X_kernel, γ):
		if X_kernel == 'linear': 
			Kᵪ = X.dot(X.T)
		elif X_kernel == 'Gaussian':
			Kᵪ = sklearn.metrics.pairwise.rbf_kernel(X, gamma=γ)

		return Kᵪ

	def get_Kᵧ(X, Y, X_kernel, γ):
		if Y_kernel == 'linear': 
			#Yₒ = OneHotEncoder(categories='auto', sparse=False).fit_transform(Y)
			#Kᵧ = Yₒ.dot(Yₒ.T)
			Kᵧ = Y.dot(Y.T)
		elif X_kernel == 'Gaussian':
			[γᵪ, γᵧ] = get_γ(X, Y, sigma_type)
			Kᵧ = sklearn.metrics.pairwise.rbf_kernel(Y, gamma=γ)

		return Kᵧ


	if len(X.shape) == 1: X = np.reshape(X, (X.size, 1))
	if len(Y.shape) == 1: Y = np.reshape(Y, (Y.size, 1))
	n = X.shape[0]
	[γᵪ, γᵧ] = get_γ(X, Y, sigma_type)

	Kᵪ = get_Kᵪ(X, Y, X_kernel, γᵪ)
	Kᵧ = get_Kᵧ(X, Y, X_kernel, γᵧ)

	HKᵪ = Kᵪ - np.mean(Kᵪ, axis=0)					# equivalent to		HKᵪ = H.dot(Kᵪ)
	HKᵧ = Kᵧ - np.mean(Kᵧ, axis=0)                  # equivalent to		HKᵧ = H.dot(Kᵧ)

	Hᵪᵧ= np.sum(HKᵪ.T*HKᵧ)							# same as HKᵪH = double_center(Kᵪ)
	#Hᵪᵧ= HKᵪ.T*HKᵧ							
                                                    #		  Hᵪᵧ = np.sum(HKᵪH*Kᵧ)
	if Hᵪᵧ == 0: return 0
	if not normalize_hsic: return Hᵪᵧ/((n-1)*(n-1))

	Hᵪ = np.sqrt(np.sum(HKᵪ.T*HKᵪ))					#note wrong if Hᵪ = np.linalg.norm(HKᵪ)	b/c it is equivalent to np.sqrt(np.sum(KᵪH*KᵪH))
	Hᵧ = np.sqrt(np.sum(HKᵧ.T*HKᵧ))						

	#import pdb; pdb.set_trace()
	H = Hᵪᵧ/( Hᵪ * Hᵧ )
	return H

def NMI(Y, Ŷ, round_to=3):
	return np.round(normalized_mutual_info_score(Y, Ŷ), round_to)

def accuracy(Y, Ŷ):
	if type(Y).__name__ == 'Tensor': 
		Y = Y.cpu().numpy()

	if type(Ŷ).__name__ == 'Tensor': 
		Ŷ = Ŷ.cpu().numpy()


	if type(Y).__name__ != 'ndarray' or type(Ŷ).__name__ != 'ndarray': 
		print('Error: Y must be numpy array or Tensor')
		exit()

	Y = np.squeeze(Y)
	Ŷ = np.squeeze(Ŷ)
	return accuracy_score(Y, Ŷ)

#	the probability our pronouncement of positive is correct
def precision(y_true, y_pred):
	y_true = wuml.ensure_numpy(y_true).astype(int)
	y_pred = wuml.ensure_numpy(y_pred).astype(int)

	if len(np.unique(y_true)) != 2: 
		raise ValueError('Error : precision function currently only takes binary labels')

	P = precision_score(y_true, y_pred)
	return P

#	the probability that we catch a positive event
def recall(y_true, y_pred):
	y_true = wuml.ensure_numpy(y_true).astype(int)
	y_pred = wuml.ensure_numpy(y_pred).astype(int)
	if len(np.unique(y_true)) > 2: raise ValueError('Error : recall function currently only takes binary labels')

	return recall_score(y_true, y_pred)


def binary_auc(y, prob_of_positive_event):
	return roc_auc_score(y, prob_of_positive_event)

if __name__ == '__main__':
	X, y = load_breast_cancer(return_X_y=True)
	clf = LogisticRegression(solver="liblinear", random_state=0).fit(X, y)
	print(roc_auc_score(y, clf.predict_proba(X)[:, 1]))
	print(roc_auc_score(y, clf.decision_function(X)))
	import pdb; pdb.set_trace()






#	n = 300
#	
#	#	Perfect Linear Data
#	dat = np.random.rand(n,1)
#	plinear_data = np.hstack((dat,dat)) + 1
#	df = pd.DataFrame(data=plinear_data, columns=["x", "y"])
#
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	XP_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(plinear_data[:,0]).T))
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	YP_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(plinear_data[:,1]).T))
#
#	plinear_pc = np.round(pearsonr(plinear_data[:,0], plinear_data[:,1])[0], 2)
#	plinear_nmi = np.round(normalized_mutual_info_score(XP_data_nmi, YP_data_nmi),2)
#	plinear_hsic = np.round(ℍ(plinear_data[:,0], plinear_data[:,1], sigma_type='opt'),2)	
#	plinear_pps = np.round(pps.score(df, "x", "y")['ppscore'],2)
#
#	print('Linear Relationship:')
#	print('\tCorrelation : ', plinear_pc)
#	print('\tNMI : ', plinear_nmi)
#	print('\tpps : ', plinear_pps)
#	print('\tHSIC : ', plinear_hsic)
#
#
#	#	Linear Data
#	dat = np.random.rand(n,1)
#	linear_data = np.hstack((dat,dat)) + 0.04*np.random.randn(n,2)
#	df = pd.DataFrame(data=linear_data, columns=["x", "y"])
#
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	XL_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(linear_data[:,0]).T))
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	YL_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(linear_data[:,1]).T))
#
#	linear_pc = np.round(pearsonr(linear_data[:,0], linear_data[:,1])[0], 2)
#	linear_nmi = np.round(normalized_mutual_info_score(XL_data_nmi, YL_data_nmi),2)
#	linear_hsic = np.round(ℍ(linear_data[:,0], linear_data[:,1], sigma_type='opt'),2)	
#	linear_pps = np.round(pps.score(df, "x", "y")['ppscore'],2)
#
#	print('Linear Relationship:')
#	print('\tCorrelation : ', linear_pc)
#	print('\tNMI : ', linear_nmi)
#	print('\tpps : ', linear_pps)
#	print('\tHSIC : ', linear_hsic)
#
#	#	Sine Data
#	dat_x = 9.3*np.random.rand(n,1)
#	dat_y = np.sin(dat_x)
#	sine_data = np.hstack((dat_x,dat_y)) + 0.06*np.random.randn(n,2)
#	df = pd.DataFrame(data=sine_data, columns=["x", "y"])
#	sine_pc = np.round(pearsonr(sine_data[:,0], sine_data[:,1])[0],2)
#
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	Xsine_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(sine_data[:,0]).T))
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	Ysine_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(sine_data[:,1]).T))
#
#	sine_nmi = np.round(normalized_mutual_info_score(Xsine_data_nmi, Ysine_data_nmi),2)
#	sine_hsic = np.round(ℍ(sine_data[:,0], sine_data[:,1], sigma_type='opt'),2)
#	sine_pps = np.round(pps.score(df, "x", "y")['ppscore'],2)
#
#	print('Sine Relationship:')
#	print('\tCorrelation : ', sine_pc)
#	print('\tNMI : ', sine_nmi)
#	print('\tpps : ', sine_pps)
#	print('\tHSIC : ', sine_hsic)
#
#
#	#	Parabola Data
#	dat_x = 4*np.random.rand(n,1) - 2
#	dat_y = 0.05*dat_x*dat_x
#	para_data = np.hstack((dat_x,dat_y)) + 0.01*np.random.randn(n,2)
#	df = pd.DataFrame(data=para_data, columns=["x", "y"])
#
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	Xp_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(para_data[:,0]).T))
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	Yp_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(para_data[:,1]).T))
#
#	para_pc = np.round(pearsonr(para_data[:,0], para_data[:,1])[0],2)
#	para_nmi = np.round(normalized_mutual_info_score(Xp_data_nmi, Yp_data_nmi),2)
#	para_hsic = np.round(ℍ(para_data[:,0], para_data[:,1], sigma_type='opt'),2)
#	para_pps = np.round(pps.score(df, "x", "y")['ppscore'],2)
#	
#	print('Parabola Relationship:')
#	print('\tCorrelation : ', para_pc)
#	print('\tNMI : ', para_nmi)
#	print('\tpps : ', para_pps)
#	print('\tHSIC : ', para_hsic)
#
#	#	Random uniform Data
#	unif_data = np.random.rand(n,2)
#	df = pd.DataFrame(data=unif_data, columns=["x", "y"])
#
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	Xr_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(unif_data[:,0]).T))
#	enc = KBinsDiscretizer(n_bins=10, encode='ordinal')
#	Yr_data_nmi = np.squeeze(enc.fit_transform(np.atleast_2d(unif_data[:,1]).T))
#
#
#	unif_pc = np.round(pearsonr(unif_data[:,0], unif_data[:,1])[0],2)
#	unif_hsic = np.round(ℍ(unif_data[:,0], unif_data[:,1], sigma_type='opt'),2)
#	unif_nmi = np.round(normalized_mutual_info_score(Xr_data_nmi, Yr_data_nmi),2)
#	unif_pps = np.round(pps.score(df, "x", "y")['ppscore'],2)
#	
#	print('Random Relationship:')
#	print('\tCorrelation : ', unif_pc)
#	print('\tNMI : ', unif_nmi)
#	print('\tpps : ', unif_pps)
#	print('\tHSIC : ', unif_hsic)
#
#
#	plt.figure(figsize=(13,3))
#
#	plt.subplot(151)
#	plt.plot(plinear_data[:,0], plinear_data[:,1], 'bx')
#	plt.title('$\\rho$ : ' + str(plinear_pc) + ' , HSIC : ' + str(plinear_hsic) + '\npps : ' + str(plinear_pps) + ' , nmi : ' + str(plinear_nmi))
#
#	plt.subplot(152)
#	plt.plot(linear_data[:,0], linear_data[:,1], 'bx')
#	plt.title('$\\rho$ : ' + str(linear_pc) + ' , HSIC : ' + str(linear_hsic) + '\npps : ' + str(linear_pps) + ' , nmi : ' + str(linear_nmi))
#	
#	plt.subplot(153)
#	plt.plot(sine_data[:,0], sine_data[:,1], 'bx')
#	plt.title('$\\rho$ : ' + str(sine_pc) + ' , HSIC : ' + str(sine_hsic) + '\npps : ' + str(sine_pps) + ' , nmi : ' + str(sine_nmi))
#
#	plt.subplot(154)
#	plt.plot(para_data[:,0], para_data[:,1], 'bx')
#	plt.title('$\\rho$ : ' + str(para_pc) + ' , HSIC : ' + str(para_hsic) + '\npps : ' + str(para_pps) + ' , nmi : ' + str(para_nmi))
#
#	plt.subplot(155)
#	plt.plot(unif_data[:,0], unif_data[:,1], 'bx')
#	plt.title('$\\rho$ : ' + str(unif_pc) + ' , HSIC : ' + str(unif_hsic) + '\npps : ' + str(unif_pps) + ' , nmi : ' + str(unif_nmi))
#
#	plt.tight_layout()
#	plt.show()


