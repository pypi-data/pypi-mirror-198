#!/usr/bin/env python

import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')
if os.path.exists('/home/chieh/code/wuML'):
	sys.path.insert(0,'/home/chieh/code/wuML')

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn import preprocessing
import pandas as pd
import numpy as np

#if os.path.exists('/home/chieh/code/wPlotLib'):
#	sys.path.insert(0,'/home/chieh/code/wPlotLib')

from wuml.IO import *
from wuml.data_stats import *
from wuml.wData import *
from wuml.type_check import *

np.set_printoptions(precision=4)
np.set_printoptions(threshold=30)
np.set_printoptions(linewidth=300)
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=sys.maxsize)

#import pdb; pdb.set_trace()


#	data here should be wData
def remove_rows_with_missing_labels(data):
	df = data.df.copy()
	label_column = ensure_DataFrame(data.Y, columns='label')
	newDF = pd.concat([df,label_column], axis=1)

	newDF = newDF.dropna(subset=['label'])	# remove the row with missing label
	newLabel = (newDF['label']).values

	del newDF['label']
	data.Y = newLabel
	data.df = newDF
	data.X = newDF.values
	data.shape = newDF.shape

	return data


def remove_rows_with_too_much_missing_entries(data, threshold=0.6, newDataFramePath=''):
	'''
		If a row is kept if it has more than "threshold" percentage of normal data
		data is a pandas format, it can be converted this way
		pd.DataFrame(data=data[1:,1:],    # values
						index=data[1:,0],    # 1st column as index
						columns=data[0,1:])  # 1st row as the column names
	'''
	df = ensure_DataFrame(data)

	X = df.values
	n = X.shape[0]
	d = X.shape[1]

	pth = './results/'
	ensure_path_exists('./results')
	#ensure_path_exists(pth)

	#	Obtain a decimated dataframe
	limitPer = int(d * threshold)
	df_decimated = df.dropna(thresh=limitPer, axis=0)
	oldID = df.index.values.tolist()
	newID = df_decimated.index.values.tolist()
	removed_samples = set(oldID).difference(newID)

	#	Record the results
	output_str = 'Original dataFrame dimension : %d samples,  %d dimensions\n'%(n, d)
	output_str += 'Deciated dataFrame dimension : %d samples,  %d dimensions\n'%(df_decimated.values.shape[0], df_decimated.values.shape[1])
	output_str += 'Removed Rows missing at least these percentage of entries : %.3f\n'%(1-threshold)

#	#	Record the removed features 
	output_str += '\nID of Removed Rows\n'
	output_str += str(removed_samples)

	write_to(output_str, pth + 'row_decimation_info.txt')
	if newDataFramePath != '': df_decimated.to_csv(path_or_buf=newDataFramePath, index=False)

	df_decimated = wData(dataFrame=df_decimated)
	return df_decimated


def remove_columns_with_too_much_missing_entries(data, threshold=0.6, newDataFramePath=''):
	'''
		If a column is kept if it has more than "threshold" percentage of normal data
		data is a pandas format, it can be converted this way
		pd.DataFrame(data=data[1:,1:],    # values
						index=data[1:,0],    # 1st column as index
						columns=data[0,1:])  # 1st row as the column names
	'''
	df = ensure_DataFrame(data)

	X = df.values
	n = X.shape[0]
	d = X.shape[1]

	pth = './results/'
	ensure_path_exists('./results')
	#ensure_path_exists(pth)

	#	Obtain a decimated dataframe
	limitPer = int(n * threshold)
	df_decimated = df.dropna(thresh=limitPer, axis=1)
	oldColumns = df.columns.values.tolist()
	newColumns = df_decimated.columns.values.tolist()
	removed_columns = set(oldColumns).difference(newColumns)

	#	Record the results
	output_str = 'Original data dimension : %d samples,  %d dimensions\n'%(n, d)
	output_str += 'Deciated data dimension : %d samples,  %d dimensions\n'%(df_decimated.values.shape[0], df_decimated.values.shape[1])
	output_str += 'Removed Columns missing at least these percentage of entries : %.3f\n'%(1-threshold)

	#	Record the removed features 
	output_str += '\nRemoved Columns + Missing Percentage'

	if len(removed_columns) > 0:
		max_width = len(max(removed_columns, key=len))
		for column in removed_columns:
			x = df[column].values
			missing_percentage = np.sum(np.isnan(x))/n
			output_str += (('\n\t%-' + str(max_width) + 's\t%.2f')%(column, missing_percentage))
	
		#	Record the retained features 
		output_str += '\n\nRetained Columns + Missing Percentage'
		for column in df_decimated:
			x = df_decimated[column].values
			missing_percentage = np.sum(np.isnan(x))/n
			output_str += (('\n\t%-' + str(max_width) + 's\t%.2f')%(column, missing_percentage))
	else:
		output_str += '\n\tNo columns were removed.'
		

	write_to(output_str, pth + 'column_decimation_info.txt')
	if newDataFramePath != '': df_decimated.to_csv(path_or_buf=newDataFramePath, index=False)

	return ensure_data_type(df_decimated, type_name=type(data).__name__)

def decimate_data_with_missing_entries(data, column_threshold=0.6, row_threshold=0.6,newDataFramePath=''):
	'''
		It will automatically remove rows and columns of a dataFrame with missing entries.
	'''

	dfo = ensure_DataFrame(data)
	dfSize = 'Data size:' + str(dfo.shape)

	mdp = np.array(identify_missing_data_per_feature(dfo))
	#x = np.arange(1, len(mdp)+1)
	colnames = dfo.columns.to_numpy()

	lp = wplotlib.bar(colnames, mdp, 'Before Missing Percentage', 'Feature ID', 'Percentage Missing', 
						imgText=dfSize, subplot=121, ylim=[0,1], xticker_rotate=90, figsize=(10,5))
						

	df = remove_columns_with_too_much_missing_entries(dfo, threshold=column_threshold)
	df_decimated = remove_rows_with_too_much_missing_entries(df, threshold=row_threshold, newDataFramePath=newDataFramePath)
	dfSize = 'Data size:' + str(df_decimated.shape)

	mdp = np.array(identify_missing_data_per_feature(df_decimated))
	#x = np.arange(1, len(mdp)+1)
	colnames = df.columns.to_numpy()
	wplotlib.bar(colnames, mdp, 'After Missing Percentage', 'Feature ID', 'Percentage Missing', 
					imgText=dfSize, subplot=122, ylim=[0,1], xticker_rotate=90)
	lp.show()

	return df_decimated

def center_data(X):
	return X - X.mean(axis=0)


def center_and_scale(wuData, return_type=None, also_return_mean_and_std=False, mean=None, std=None):
	wuData = ensure_wData(wuData)
	X = ensure_numpy(wuData)
	if also_return_mean_and_std:
		μ = np.mean(wuData.X, axis=0)
		σ = np.std(wuData.X, axis=0)


	if mean is None and std is None:
		X = preprocessing.scale(X)
	elif mean is not None:
		X = X - mean
		if std is not None:
			X = X/std

	if type(wuData).__name__ == 'wData': 
		wuData.df = pd.DataFrame(data=X, columns=wuData.df.columns)
	elif type(wuData).__name__ == 'ndarray': 
		wuData.df = pd.DataFrame(data=X)
	elif type(wuData).__name__ == 'DataFrame': 
		wuData.df = pd.DataFrame(data=X, columns=wuData.columns)
	else:
		raise ValueError('Error: Cannot center data since %s is not a recongized data type.'%type(wuData).__name__)

	wuData.X = wuData.df.values

	if return_type is None:
		return_data = ensure_data_type(wuData, type_name=type(wuData).__name__)
	else:
		return_data = ensure_data_type(wuData, type_name=return_type)

	if also_return_mean_and_std:
		if mean is None and std is None: return [return_data, μ, σ]
		else: return [return_data, mean, std]
	else:
		return return_data



def center_scale_with_missing_data(X, replace_nan_with_0=False): 
	'''
		For each column, find μ, σ while ignoring the entries that are zero. 
	'''
	d = X.shape[1]
	ignore_column_with_0_σ = []
	for i in range(d):
		x = X[:,i]
		ẋ = x[np.invert(np.isnan(x))]
		ẋ = ẋ - np.mean(ẋ)
		σ = np.std(ẋ)

		if σ < 0.00001:
			ignore_column_with_0_σ.append(i)
		else:
			X[np.invert(np.isnan(x)), i] = ẋ/σ

	for i in ignore_column_with_0_σ:
		X = np.delete(X, i , axis=1)	# delete column with σ=0

	if replace_nan_with_0:
		X = np.nan_to_num(X)

	return X, ignore_column_with_0_σ



def split_training_validation_test(data, label=None, data_name=None, data_path=None, save_as='none', train_valid_test_percent_split=[0.8, 0.1, 0.1], xdata_type="%.4f", ydata_type="%d"):
#	train_valid_test_percent_split: must add up to equal to 1

	TVT = train_valid_test_percent_split
	test_percentage = TVT[1] + TVT[2]
	[X_train, X_rest, y_train, y_rest] = split_training_test(data, label=label, test_percentage=test_percentage, xdata_type=xdata_type, ydata_type=ydata_type)

	test_percentage2 = TVT[2]/test_percentage
	[X_validate, X_test, y_validate, y_test] = split_training_test(X_rest, label=label, test_percentage=test_percentage2, xdata_type=xdata_type, ydata_type=ydata_type)

	return [X_train, y_train, X_validate, y_validate, X_test, y_test]



def split_training_test(data, label=None, data_name=None, data_path=None, save_as='none', test_percentage=0.1, xdata_type="%.4f", ydata_type="%d"):
	X = ensure_numpy(data)
	Y = None

	if label is not None: Y = label
	if type(data).__name__ == 'wData' and data.Y is not None: Y = data.Y
	if Y is None: raise ValueError('Error: The label Y is currently None, did you define it?')

	input_dat_list = [X, Y]

	if type(data).__name__ == 'wData':
		if len(data.extra_data_dictionary['numpy']) > 0:
			input_dat_list.extend(data.extra_data_dictionary['numpy'])

	split_list = train_test_split(*input_dat_list, test_size=test_percentage, random_state=30)
	#X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_percentage, random_state=42)
	X_train = split_list[0]
	X_test = split_list[1]
	y_train = split_list[2]
	y_test = split_list[3]
	

	if data_path is not None:
		Train_dat = data_path + data_name + '_train.csv'
		Train_label_dat = data_path + data_name + '_train_label.csv'
	
		Test_dat = data_path + data_name + '_test.csv'
		Test_label_dat = data_path + data_name + '_test_label.csv'
	
	
		if save_as == 'ndarray':
			np.savetxt(Train_dat, X_train, delimiter=',', fmt=xdata_type) 
			np.savetxt(Train_label_dat, y_train, delimiter=',', fmt=ydata_type) 
	
			np.savetxt(Test_dat, X_test, delimiter=',', fmt=xdata_type) 
			np.savetxt(Test_label_dat, y_test, delimiter=',', fmt=ydata_type) 
		elif save_as == 'DataFrame':
			XTrain_df = pd.DataFrame(data=X_train, columns=data.df.columns)
			XTest_df =  pd.DataFrame(data=X_test, columns=data.df.columns)
	
			XTrain_df['label'] = y_train
			XTest_df['label'] = y_test
	
			XTrain_df.to_csv(Train_dat, index=False, header=True)
			XTest_df.to_csv(Test_dat, index=False, header=True)

	# if there are extra data for training
	if len(split_list) > 4:	xDat = split_list[4:][::2]	# get all the training extra data
	else: xDat = None
	
	X_train = ensure_wData(X_train, column_names=data.df.columns, extra_data=xDat)
	X_train.Y = y_train
	X_train.label_type = data.label_type
	X_train.initialize_pytorch_settings(data.xtorchDataType, data.ytorchDataType)
	X_train.label_column_name = data.label_column_name

	if len(split_list) > 4:	xDat = split_list[4:][1::2]	# get all the test extra data
	else: xDat = None

	X_test = ensure_wData(X_test, column_names=data.df.columns, extra_data=xDat)
	X_test.Y = y_test
	X_test.label_type = data.label_type
	X_test.initialize_pytorch_settings(data.xtorchDataType, data.ytorchDataType)
	X_test.label_column_name = data.label_column_name

	return [X_train, X_test, y_train, y_test]

def gen_10_fold_data(data=None, data_name=None, data_path='./data/'):
	#	if data is provided, data must be wData type

	#	Load the data 
	if data is None and data_name is not None:
		xpath = data_path + data_name
		X = np.loadtxt(xpath + '.csv', delimiter=',', dtype=np.float64)			
		Y = np.loadtxt(xpath + '_label.csv', delimiter=',', dtype=np.int32)			
	else:
		if wuml.wtype(data) != 'wData': raise ValueError('Unknown dataType %s'%wtype(data))

		X = data.X
		Y = data.Y

	#	if data_name is not None then we need to save it to file
	if data_name is not None:
		xpath = data_path + data_name
		fold_path = xpath + '/'
		if os.path.exists(fold_path): 
			pass
		else:
			os.mkdir(fold_path)

	kf = KFold(n_splits=10, shuffle=True)
	kf.get_n_splits(X)
	loopObj = enumerate(kf.split(X))
	all_data_list = [] 

	for count, data in loopObj:
		[train_index, test_index] = data

		X_train, X_test = X[train_index], X[test_index]
		Y_train, Y_test = Y[train_index], Y[test_index]

		all_data_list.append([X_train, Y_train, X_test, Y_test])

		if data_name is not None:
			np.savetxt( fold_path + data_name + '_' + str(count+1) + '.csv', X_train, delimiter=',', fmt='%.6f') 
			np.savetxt( fold_path + data_name + '_' + str(count+1) + '_label.csv', Y_train, delimiter=',', fmt='%d') 
			np.savetxt( fold_path + data_name + '_' + str(count+1) + '_test.csv', X_test, delimiter=',', fmt='%.6f') 
			np.savetxt( fold_path + data_name + '_' + str(count+1) + '_label_test.csv', Y_test, delimiter=',', fmt='%d') 

	return all_data_list

def rearrange_sample_to_same_class(X,Y):
	l = np.unique(Y)
	newX = np.empty((0, X.shape[1]))
	newY = np.empty((0))

	for i in l:
		indices = np.where(Y == i)[0]
		newX = np.vstack((newX, X[indices, :]))
		newY = np.hstack((newY, Y[indices]))

	return [newX, newY]


#	Relating all samples to the most likely one, with p(X1) > p(Xi) for all i
#	Given X1 X2 with p(X1)/p(X2)=2  the weight for X1 = 1, and X2 = 2
def get_likelihood_weight(data, weight_names=None):
	X = ensure_numpy(data)
	weight_names = ensure_list(weight_names)

	Pₓ = wuml.KDE(X)
	logLike = Pₓ(X, return_log_likelihood=True)
	max_likely = np.max(logLike)
	ratios = np.exp(max_likely - logLike)

	return wuml.wData(X_npArray=ratios, column_names=weight_names)

def map_data_between_0_and_1(data, output_type_name='wData', map_type='linear'): # map_type: linear, or cdf
	X = ensure_numpy(data)

	if map_type=='linear':
		min_max_scaler = preprocessing.MinMaxScaler()
		newX = min_max_scaler.fit_transform(X)
	else:
		n = X.shape[0]
		d = X.shape[1]
	
		newX = np.zeros(X.shape)
	
		for i in range(d):
			column = X[:,i]
			residual_dat = column[np.isnan(column) == False]
			minV = np.min(residual_dat) - 3
	
			if len(residual_dat) < 5:
				print('Error: column %d only has %d samples, you must at least have 6 samples for kde'%(i, len(residual_dat)))
				print('\nTry Removing this feature')
				sys.exit()
	
			if len(np.unique(residual_dat)) == 1:
				newX[:,i] = np.ones(n)
			else:
				Pₓ = wuml.KDE(residual_dat)
				for j, itm in enumerate(X[:,i]):
					if np.isnan(itm):
						newX[j,i] = np.nan
					else:
						newX[j,i] = Pₓ.integrate(minV, X[j,i])


	#	This ensures that the columns labels are copied correctly
	if type(data).__name__ == 'ndarray': 
		df = pd.DataFrame(newX)
	elif type(data).__name__ == 'wData': 
		df = pd.DataFrame(newX)
		df.columns = data.df.columns
	elif type(data).__name__ == 'DataFrame': 
		df = pd.DataFrame(newX)
		df.columns = data.columns
	elif type(data).__name__ == 'Tensor': 
		X = data.detach().cpu().numpy()
		df = pd.DataFrame(X)

	output = ensure_data_type(df, type_name=output_type_name)
	if output_type_name=='wData': 
		try: 
			output.Y = data.Y
			output.label_column_name = data.label_column_name
		except: pass

	return output


def use_cdf_to_map_data_between_0_and_1(data, output_type_name='wData'):
	print("This function is deprecated, instead use wuml.map_data_between_0_and_1(data, map_type='linear')")

	X = ensure_numpy(data)
	n = X.shape[0]
	d = X.shape[1]

	newX = np.zeros(X.shape)

	for i in range(d):
		column = X[:,i]
		residual_dat = column[np.isnan(column) == False]
		minV = np.min(residual_dat) - 3

		if len(residual_dat) < 5:
			print('Error: column %d only has %d samples, you must at least have 6 samples for kde'%(i, len(residual_dat)))
			print('\nTry Removing this feature')
			sys.exit()

		if len(np.unique(residual_dat)) == 1:
			newX[:,i] = np.ones(n)
		else:
			Pₓ = wuml.KDE(residual_dat)
			for j, itm in enumerate(X[:,i]):
				if np.isnan(itm):
					newX[j,i] = np.nan
				else:
					newX[j,i] = Pₓ.integrate(minV, X[j,i])


	#	This ensures that the columns labels are copied correctly
	if type(data).__name__ == 'ndarray': 
		df = pd.DataFrame(newX)
	elif type(data).__name__ == 'wData': 
		df = pd.DataFrame(newX)
		df.columns = data.df.columns
	elif type(data).__name__ == 'DataFrame': 
		df = pd.DataFrame(newX)
		df.columns = data.columns
	elif type(data).__name__ == 'Tensor': 
		X = data.detach().cpu().numpy()
		df = pd.DataFrame(X)

	output = ensure_data_type(df, type_name=output_type_name)
	if output_type_name=='wData': 
		try: 
			output.Y = data.Y
			output.label_column_name = data.label_column_name
		except: pass

	return output

# X has to be in wData type
def get_N_samples_from_each_class(data, N, output_as='wData'):
	type_check_with_error(data, 'wData', function_name=get_N_samples_from_each_class.__name__)
	X = data.X
	Y = data.Y

	newX = np.empty((0, X.shape[1]))
	newY = np.empty(0)
	unique_classes = np.unique(Y)
	for i in unique_classes:
		Xsub = data.get_all_samples_from_a_class(i)
		Xsub = wuml.randomly_shuffle_rows_of_matrix(Xsub)
		Xsub = Xsub[0:N,:]
		newX = np.vstack((newX, Xsub))

		newY = np.hstack((newY, np.full((N), i)))

	if output_as == 'wData': return wData(X_npArray=newX, Y_npArray=newY, label_type='discrete')
	elif output_as == 'ndarray': return [newX, newY]
	else:
		raise ValueError('Error: The function get_N_samples_from_each_class does not output data type %s.'%output_as)

#	Make sure that the vector sums up to 1
#	If there's a negative value within the vector, we increase the whole vector by the most negative value
def map_vector_to_distribution_data(x, method='raise by negative constant'):
	x = ensure_numpy(x)
	mx = np.min(x)

	if mx < 0:
		if method == 'raise by negative constant':
			x = x - mx + 0.00001*np.random.rand()
		elif method == 'set negative to 0':
			x[x<0] = 0
		elif method == 'set negative to small noise':
			x[x<0] = 0.00001*np.random.rand()
			
	return np.squeeze(x/np.sum(x))



def normalize(data, norm='l2', ensure_positive_values_method=None, return_new_copy=False):
	wuml.type_check_with_error(data, 'wData', function_name='process.normalize')

	X = data.X
	if ensure_positive_values_method == 'raise by most negative':
		xm = np.reshape(np.min(X, axis=1), (X.shape[0],1 ))
		xm2 = np.matlib.repmat(xm, 1, X.shape[1])
		X = X - xm2


	Xn = preprocessing.normalize(X, norm=norm)
	new_df = pd.DataFrame(Xn, columns=data.df.columns)

	if return_new_copy:
		return wuml.wData(dataFrame=new_df)
	else:
		data.update_DataFrame(new_df)
