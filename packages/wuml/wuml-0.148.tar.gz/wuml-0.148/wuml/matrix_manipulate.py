
import numpy as np
from wuml.type_check import *

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

#	X must be symmetrical
# columns of the output V are the eigenvector such that : Q = V Λ Vᵀ
def eigh(Q, q='all', eig_order='largest_first'):
	if np.allclose(Q, Q.T) == False:
		raise ErrorType('The input for eigh function must be symmetric matrix.')

	σ, U = np.linalg.eigh(Q)
	if q == 'all': q = Q.shape[0]

	if eig_order == 'smallest_first':
		V = U[:, 0:q]
		λ = σ[0:q]
	else: 
		reversedU = U[:, ::-1]
		V = reversedU[:, 0:q]
		λ = np.flip(σ)[0:q]

	Λ = np.diag(λ)	

	###	debug code
	#print('Original Matrix')
	#print(Q,'\n')
	#print('Constructed Matrix')
	#print(V.dot(Λ).dot(V.T), '\n')
	#print('QV')
	#print(Q.dot(V), '\n')
	#print('VΛ')
	#print(V.dot(Λ), '\n')
	#import pdb; pdb.set_trace()
	return [V, λ, Λ] # columns of V are the eigenvector such that : Q = V Λ Vᵀ


def double_center(Ψ):
	Ψ = ensure_numpy(Ψ)
	HΨ = Ψ - np.mean(Ψ, axis=0)								# equivalent to Γ = Ⲏ.dot(Kᵧ).dot(Ⲏ)
	HΨH = (HΨ.T - np.mean(HΨ.T, axis=0)).T
	return HΨH

def ensure_vector_is_a_column_format(data):
	X = ensure_numpy(data)
	X = np.atleast_2d(X)
	if X.shape[0] < X.shape[1]:
		return X.T
	return X

def get_np_column(data, column_id):
	X = ensure_numpy(data)
	return np.atleast_2d(X[:,column_id]).T

def sort_matrix_rows_by_a_column(X, column_names):
	df = ensure_DataFrame(X)
	sorted_df = df.sort_values(by=column_names)

	return sorted_df

def one_hot_encoding(Y, output_data_type='same'): 
	'''
		output_data_type : 'same' implies to use the same data type as input
							else use the data type you want, i.e., 'ndarray' , 'Tensor', 'DataFrame'
	'''
	Y1 = wuml.ensure_numpy(Y)

	Y1 = np.reshape(Y1,(len(Y1),1))
	Yₒ = OneHotEncoder(categories='auto', sparse=False).fit_transform(Y1)

	if output_data_type == 'same':
		Yₒ = wuml.ensure_data_type(Yₒ, type_name=wtype(Y))
	else:
		Yₒ = wuml.ensure_data_type(Yₒ, type_name=output_data_type)

	return Yₒ

def one_hot_to_label(Yₒ):
	Y = np.argmax(Yₒ, axis=1)
	return Y

def compute_Degree_matrix(M, output_type=None):
	if output_type is None: output_type = wtype(M)

	Mnp = ensure_numpy(M)
	D = np.diag(np.sum(Mnp, axis=0))

	return ensure_data_type(D, type_name=output_type)


def randomly_shuffle_rows_of_matrix(X):
	X = wuml.ensure_numpy(X)
	np.random.shuffle(X)
	return X


