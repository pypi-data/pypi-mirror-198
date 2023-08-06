
import numpy as np; np.random.seed(0)
from wplotlib import lines		#pip install wplotlib
from wplotlib import heatMap
from wplotlib import histograms
from wplotlib import scatter

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

import sys
import os

if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')



import wuml 
from wuml.wData import wData
from wuml.type_check import *
from wuml.IO import *

import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import random


def get_label_stats(data, print_stat=True):
	if wtype(data) == 'wData': y = data.Y
	else: y = ensure_numpy(data)

	l = np.unique(y)
	t = len(y)
	table = np.empty((0,3))
	for i in l:
		sn = len(np.where(y == i)[0])
		table = np.vstack((table, np.array([[i, sn, sn/t]])))

	df = pd.DataFrame(table, columns=['class id', 'num sample', 'percentage'])
	if print_stat: jupyter_print(df)
	stat = ensure_wData(df)

	return stat



def get_feature_histograms(X, path=None, title='', ylogScale=False):
	X = ensure_numpy(X)

	if path is not None:
		header = './results/DatStats/'
		wuml.ensure_path_exists('./results')
		wuml.ensure_path_exists(header)

	H = histograms(X, num_bins=10, title=title, fontsize=12, facecolor='blue', α=0.5, path=path, subplot=None, ylogScale=ylogScale)

def identify_missing_labels(labels):
	if labels is None:
		return None

	y = ensure_numpy(labels)
	n = len(y)
	missing_percentage = np.sum(np.isnan(y))/n
	return missing_percentage


def identify_missing_data_per_feature(data):
	df = ensure_DataFrame(data)

	X = df.values
	n = X.shape[0]
	d = X.shape[1]

	mdp = missing_data_counter_per_feature = []
	for column in df:
		x = df[column].values
		missing_percentage = np.sum(np.isnan(x))/n
		mdp.append(missing_percentage)

	return mdp

def missing_data_stats(data, y=None, save_plots=False): 
	if wtype(data) == 'wData':
		y = data.Y

	df = ensure_DataFrame(data)

	header = './results/DatStats/'
	wuml.ensure_path_exists('./results')
	wuml.ensure_path_exists(header)

	missingLabels = identify_missing_labels(y)
	if missingLabels is not None: jupyter_print('\nPercetage of labels missing: %.5f\n'%missingLabels)

	mdp = np.array(identify_missing_data_per_feature(df))*100
	missingTable = pd.DataFrame([mdp], columns=ensure_list(df.columns)).T
	missingTable.rename(columns={0: 'missing %'}, inplace=True)
	jupyter_print(missingTable)


	#	print missingness info
	buffer = io.StringIO()
	df.info(buf=buffer, verbose=True)
	s = str(missingTable) + '\n\n' + buffer.getvalue()
	wuml.write_to(s, header + 'feature_stats.txt')



	textstr = ''
	x = np.arange(1, len(mdp)+1)

	xtick_locations=x
	column_names = df.columns.to_numpy()
	if len(column_names) > 10: 
		column_names = None
		xtick_locations = None

	lp = lines(x, mdp, 'Missing Percentage', 'Feature ID', 'Percentage Missing', imgText=textstr, subplot=211,
				xtick_locations=xtick_locations, xtick_labels=column_names, xticker_rotate=30, figsize=(8,12))	

	#	Show heatmap
	X2 = np.isnan(df.values).astype(int)
	xtick_locations = (x-0.5)
	if column_names is None: xtick_locations = None
	heatMap(X2, title='Missing Data Heat Map', subplot=212, xlabel='Feature ID', xticker_rotate=40, 
				ylabel='Sample ID', xtick_locations=xtick_locations, xtick_labels=column_names,
				outpath= header + 'missing_data_plots.png')
	lp.show()

	return mdp


def get_redundant_pairs(df):
	'''Get diagonal and lower triangular pairs of correlation matrix'''
	pairs_to_drop = set()
	cols = df.columns
	for i in range(0, df.shape[1]):
		for j in range(0, i+1):
			pairs_to_drop.add((cols[i], cols[j]))
	return pairs_to_drop


def get_top_abs_correlations(df, n=5):
	#au_corr = df.corr().abs().unstack()
	au_corr = df.unstack()
	labels_to_drop = get_redundant_pairs(df)
	au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False, key=abs)
	return au_corr[0:n]

def feature_wise_correlation(data, n=10, label_name=None, get_top_corr_pairs=False, num_of_top_dependent_pairs_to_plot=0):
	'''
		if label_name is label string, then it only compares the features against the label
		num_of_top_dependent_pairs_to_plot: if > 0, it will plot out the most correlated pairs
	'''

	df = ensure_DataFrame(data)
	if n > df.shape[1]: n = df.shape[1]

	if label_name is not None and label_name not in df.columns:
		raise ValueError('\n\tError : %s is an unrecognized column name. \nThe list of names are %s'%(label_name, str(df.columns)))

	corrMatrix = df.corr()
	topCorr = get_top_abs_correlations(corrMatrix, n=n).to_frame()
	if not get_top_corr_pairs and label_name not in df.columns: 
		outDF = corrMatrix
	elif label_name is None:
		outDF = topCorr
	else:
		corrVector = corrMatrix[label_name].to_frame()
		topCorr = corrVector.sort_values(label_name, key=abs, ascending=False)
		topCorr = topCorr[1:n]
		outDF = topCorr

	if num_of_top_dependent_pairs_to_plot>0:
		subTopCorr = topCorr.head(num_of_top_dependent_pairs_to_plot)
		idx = subTopCorr.index
		idx = idx.to_frame().values
		
		for i, item in enumerate(idx):
			if len(item) == 1:
				α = item
				β = label_name
				A = df[α].to_numpy()
				B = df[label_name].to_numpy()

			elif len(item) == 2:
				α, β = item
			
				A = df[α].to_numpy()
				B = df[β].to_numpy()
	
			corV = subTopCorr.values[i]
			textstr = r'Order ID: %d, Correlation : %.3f' % (i+1, corV)

			lp = scatter(A, B, α + ' vs ' + β, α, β, imgText=textstr, figsize=(10,5))		# (width, height)


	return ensure_data_type(outDF, type_name=type(data).__name__)


def feature_wise_HSIC(data, n=10, label_name=None, get_top_dependent_pairs=False, num_of_top_dependent_pairs_to_plot=0):
	'''
		if label_name is label string, then it only compares the features against the label
		num_of_top_dependent_pairs_to_plot: if > 0, it will plot out the most correlated pairs
	'''
	X = ensure_numpy(data)
	df = ensure_DataFrame(data)
	d = X.shape[1]

	if n > df.shape[1]: n = df.shape[1]
	if label_name is not None and label_name not in df.columns:
		raise ValueError('Error : %s is an unrecognized column name. \nThe list of names are %s'%(label_name, str(df.columns)))


	lst = list(range(d))
	pair_order_list = itertools.combinations(lst,2)
	depMatrix = np.eye(d)
	for α, β in list(pair_order_list):
		x1 = np.atleast_2d(X[:,α]).T
		x2 = np.atleast_2d(X[:,β]).T

		joinX = ensure_DataFrame(np.hstack((x1,x2)))
		joinX = joinX.dropna()
		withoutNan = joinX.values
		depMatrix[α,β] = depMatrix[β,α] = wuml.HSIC(withoutNan[:,0], withoutNan[:,1], sigma_type='mpd')

	depM_DF = ensure_DataFrame(depMatrix, columns=df.columns, index=df.columns)
	topCorr = get_top_abs_correlations(depM_DF, n=n).to_frame()
	if not get_top_dependent_pairs and label_name not in df.columns: 
		outDF = depM_DF
	elif label_name is None:
		outDF = topCorr
	else:
		corrVector = depM_DF[label_name].to_frame()
		topCorr = corrVector.sort_values(label_name, key=abs, ascending=False)
		topCorr = topCorr[1:n]
		outDF = topCorr

	if num_of_top_dependent_pairs_to_plot>0:
		subTopCorr = topCorr.head(num_of_top_dependent_pairs_to_plot)
		idx = subTopCorr.index
		idx = idx.to_frame().values
		
		for i, item in enumerate(idx):
			if len(item) == 1:
				α = item
				β = label_name
				A = df[α].to_numpy()
				B = df[label_name].to_numpy()

			elif len(item) == 2:
				α, β = item
			
				A = df[α].to_numpy()
				B = df[β].to_numpy()
	
			corV = subTopCorr.values[i]
			textstr = r'Order ID: %d, Correlation : %.3f' % (i+1, corV)
			lp = scatter(A, B, α + ' vs ' + β, α, β, imgText=textstr, figsize=(10,5))		# (width, height)


	return ensure_data_type(outDF, type_name=type(data).__name__)



def HSIC_of_feature_groups_vs_label_list(data, data_compared_to):
	'''
		Compare the entire "data" to each column of "data_compared_to"
	'''
	
	X = ensure_numpy(data)
	Ys = ensure_numpy(data_compared_to)
	Ys_df = ensure_DataFrame(data_compared_to)
	num_of_Ys = Ys.shape[1]

	hsic_list = []
	for i in range(num_of_Ys):
		hsic_list.append(wuml.HSIC(X, Ys[:,i])) #, sigma_type='mpd'

	df = ensure_DataFrame(np.array(hsic_list))
	df.index = Ys_df.columns
	df.columns = ['feature_group']
	df = df.sort_values('feature_group', axis=0, ascending=False)
	
	return ensure_wData(df)
