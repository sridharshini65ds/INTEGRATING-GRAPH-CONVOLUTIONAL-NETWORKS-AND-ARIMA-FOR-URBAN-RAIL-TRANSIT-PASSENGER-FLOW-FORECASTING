import numpy as np
from math import sqrt
import csv

def Get_All_Data(TG,time_lag,TG_in_one_day,forecast_day_number,TG_in_one_week):

	metro_enter = []
	with open('in_' + str(TG) + 'min.csv') as f:
		data = csv.reader(f, delimiter=",")
		for line in data:
			line=[int(x) for x in line]
			metro_enter.append(line)

	def get_train_data_enter(data,time_lag,TG_in_one_day,forecast_day_number,TG_in_one_week):
		data = np.array(data)
		data2 = np.zeros((data.shape[0], data.shape[1]))
		a = np.max(data)
		b = np.min(data)
		for i in range(len(data)):
			for j in range(len(data[0])):
				data2[i, j] = round((data[i, j]-b)/(a-b), 5)

		X_train_1 = [[] for i in range(TG_in_one_week, len(data2[0]) - time_lag+1 - TG_in_one_day*forecast_day_number)]
		Y_train = []
		for index in range(TG_in_one_week, len(data2[0]) - time_lag+1 - TG_in_one_day*forecast_day_number):
			for i in range(276):
				temp=data2[i,index-TG_in_one_week: index + time_lag-1-TG_in_one_week].tolist()
				temp.extend(data2[i,index-TG_in_one_day: index + time_lag-1-TG_in_one_day])
				temp.extend(data2[i,index: index + time_lag-1])
				X_train_1[index-TG_in_one_week].append(temp)
			Y_train.append(data2[:,index + time_lag-1])
		X_train_1,Y_train = np.array(X_train_1), np.array(Y_train)
		print(X_train_1.shape,Y_train.shape)

		X_test_1 = [[] for i in range(len(data2[0]) - TG_in_one_day*forecast_day_number,len(data2[0])-time_lag+1)]
		Y_test = []
		for index in range(len(data2[0]) - TG_in_one_day*forecast_day_number,len(data2[0])-time_lag+1):
			for i in range(276):
				temp = data2[i, index-TG_in_one_week: index + time_lag-1-TG_in_one_week].tolist()
				temp.extend(data2[i, index-TG_in_one_day: index + time_lag-1-TG_in_one_day])
				temp.extend(data2[i, index: index + time_lag-1])
				X_test_1[index-(len(data2[0]) - TG_in_one_day*forecast_day_number)].append(temp)
			Y_test.append(data2[:, index + time_lag-1])
		X_test_1,Y_test = np.array(X_test_1), np.array(Y_test)
		print(X_test_1.shape, Y_test.shape)

		Y_test_original = []
		for index in range(len(data[0]) - TG_in_one_day*forecast_day_number,len(data[0])-time_lag+1):
			Y_test_original.append(data[:, index + time_lag-1])
		Y_test_original = np.array(Y_test_original)

		print(Y_test_original.shape)

		return X_train_1,Y_train,X_test_1,Y_test,Y_test_original,a,b


	X_train_1,Y_train,X_test_1,Y_test,Y_test_original,a,b=get_train_data_enter(metro_enter,time_lag,TG_in_one_day,forecast_day_number,TG_in_one_week)
	print(a,b)

	#deal with outflow data. Similar with the inflow data while not including the testing data for outflow

	metro_exit = []
	with open('out_' + str(TG) + 'min.csv') as f:
		data = csv.reader(f, delimiter=",")
		for line in data:
			line = [int(x) for x in line]
			metro_exit.append(line)

	def get_train_data_exit(data,time_lag,TG_in_one_day,forecast_day_number,TG_in_one_week):
		data = np.array(data)
		data2 = np.zeros((data.shape[0], data.shape[1]))
		a = np.max(data)
		b = np.min(data)
		for i in range(len(data)):
			for j in range(len(data[0])):
				data2[i, j]=round((data[i, j]-b)/(a-b), 5)
		X_train_1 = [[] for i in range(TG_in_one_week, len(data2[0]) - time_lag+1 - TG_in_one_day*forecast_day_number)]
		for index in range(TG_in_one_week, len(data2[0]) - time_lag+1 - TG_in_one_day*forecast_day_number):
			for i in range(276):
				temp=data2[i, index-TG_in_one_week: index + time_lag-1-TG_in_one_week].tolist()
				temp.extend(data2[i, index-TG_in_one_day: index + time_lag-1-TG_in_one_day])
				temp.extend(data2[i, index: index + time_lag-1])
				X_train_1[index-TG_in_one_week].append(temp)
		X_train_1 = np.array(X_train_1)
		print(X_train_1.shape)

		X_test_1 = [[] for i in range(len(data2[0]) - TG_in_one_day*forecast_day_number, len(data2[0])-time_lag+1)]
		for index in range(len(data2[0]) - TG_in_one_day*forecast_day_number, len(data2[0])-time_lag+1):
			for i in range(276):
				temp = data2[i,index-TG_in_one_week: index + time_lag-1-TG_in_one_week].tolist()
				temp.extend(data2[i, index-TG_in_one_day: index + time_lag-1-TG_in_one_day])
				temp.extend(data2[i, index: index + time_lag-1])
				X_test_1[index-(len(data2[0]) - TG_in_one_day*forecast_day_number)].append(temp)
		X_test_1 = np.array(X_test_1)
		print(X_test_1.shape)
		return X_train_1, X_test_1

	X_train_2, X_test_2 = get_train_data_exit(metro_exit, time_lag, TG_in_one_day, forecast_day_number, TG_in_one_week)

	#deal with graph data. involve the adjacency matrix
	adjacency = []
	with open('adjacency.csv') as f:
		data = csv.reader(f, delimiter=",")
		for line in data:
			line = [float(x) for x in line]
			adjacency.append(line)
	adjacency = np.array(adjacency)
	# use adjacency matrix to calculate D_hat**-1/2 * A_hat *D_hat**-1/2
	I = np.matrix(np.eye(276))
	A_hat = adjacency+I
	D_hat = np.array(np.sum(A_hat, axis=0))[0]
	D_hat_sqrt = [sqrt(x) for x in D_hat]
	D_hat_sqrt = np.array(np.diag(D_hat_sqrt))
	D_hat_sqrtm_inv = np.linalg.inv(D_hat_sqrt)# get the D_hat**-1/2
	#D_A_final = D_hat**-1/2 * A_hat *D_hat**-1/2
	D_A_final = np.dot(D_hat_sqrtm_inv, A_hat)
	D_A_final = np.dot(D_A_final, D_hat_sqrtm_inv)
	print(D_A_final.shape)
	def get_train_data_graph(data,D_A_final,time_lag,TG_in_one_day,forecast_day_number,TG_in_one_week,):
		data = np.array(data)
		data2 = np.zeros((data.shape[0], data.shape[1]))
		a = np.max(data)
		b = np.min(data)
		for i in range(len(data)):
			for j in range(len(data[0])):
				data2[i,j]=round((data[i,j]-b)/(a-b),5)
		X_train_1 = [[] for i in range(TG_in_one_week, len(data2[0]) - time_lag+1 - TG_in_one_day*forecast_day_number)]
		for index in range(TG_in_one_week, len(data2[0]) - time_lag+1 - TG_in_one_day*forecast_day_number):
			for i in range(276):
				temp=data2[i,index: index + time_lag-1]
				X_train_1[index-TG_in_one_week].append(temp)
			X_train_1[index-TG_in_one_week] = np.dot(D_A_final, X_train_1[index-TG_in_one_week])
		X_train_1= np.array(X_train_1)
		print(X_train_1.shape)

		X_test_1 = [[] for i in range(len(data2[0]) - TG_in_one_day*forecast_day_number,len(data2[0])-time_lag+1)]
		for index in range(len(data2[0]) - TG_in_one_day*forecast_day_number,len(data2[0])-time_lag+1):
			for i in range(276):
				temp = data2[i,index: index + time_lag-1]
				X_test_1[index-(len(data2[0]) - TG_in_one_day*forecast_day_number)].append(temp)
			X_test_1[index-(len(data2[0]) - TG_in_one_day*forecast_day_number)] = np.dot(D_A_final, X_test_1[index-(len(data2[0]) - TG_in_one_day*forecast_day_number)])
		X_test_1 = np.array(X_test_1)
		print(X_test_1.shape)

		return X_train_1,X_test_1

	X_train_3, X_test_3 = get_train_data_graph(metro_enter, D_A_final, time_lag, TG_in_one_day, forecast_day_number, TG_in_one_week)

	#deal with meteorology data including the weather and PM data
	Weather = []
	with open(str(TG) + ' min after normolization.csv') as f:
		data = csv.reader(f, delimiter=",")
		for line in data:
			line = [float(x) for x in line]
			Weather.append(line)

	def get_train_data_weather_PM(data, time_lag, TG_in_one_day, forecast_day_number, TG_in_one_week,):
		data = np.array(data)

		X_train_1 = [[] for i in range(TG_in_one_week, len(data[0]) - time_lag+1 - TG_in_one_day*forecast_day_number)]
		for index in range(TG_in_one_week, len(data[0]) - time_lag+1 - TG_in_one_day*forecast_day_number):
			for i in range(len(data)):
				#For meteorology data，we only consider today's data, namely recent pattern.
				X_train_1[index-TG_in_one_week].append(data[i,index: index + time_lag-1])
		X_train_1 = np.array(X_train_1)
		print(X_train_1.shape)

		X_test_1 = [[] for i in range(len(data[0]) - TG_in_one_day*forecast_day_number, len(data[0])-time_lag+1)]
		for index in range(len(data[0]) - TG_in_one_day*forecast_day_number, len(data[0])-time_lag+1):
			for i in range(len(data)):
				X_test_1[index-(len(data[0]) - TG_in_one_day*forecast_day_number)].append(data[i, index: index + time_lag-1])
		X_test_1 = np.array(X_test_1)
		print(X_test_1.shape)
		return X_train_1,X_test_1

	X_train_4, X_test_4 = get_train_data_weather_PM(Weather, time_lag, TG_in_one_day, forecast_day_number, TG_in_one_week)

	return X_train_1, Y_train, X_test_1, Y_test, Y_test_original, a, b, X_train_2, X_test_2, X_train_3, X_test_3, X_train_4, X_test_4