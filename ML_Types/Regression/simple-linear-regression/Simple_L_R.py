# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# class LinearTrainer:
#
#     def __init__(self):
#         self.alpha = 0.0012
#         self.echops = 2000
#
#     # Find the value of parameters
#     def train(self, f_x_train_data, f_y_train_data, f_x_test_data, f_y_test_data, f_theta_0, f_theta_1):
#         t0_arr = np.array([])
#         t1_arr = np.array([])
#         j_t0_arr = np.array([])
#         accu_test = np.array([])
#         val1 = 0
#         val2 = 0
#         pred = 0
#         error_value = 0
#         for i in range(self.echops):
#
#
#             for j in range(len(f_x_train_data)):
#                 pred = f_theta_0 + f_theta_1 * f_x_train_data[j]
#                 val1 += (pred - f_y_train_data[j])
#                 val2 += (pred - f_y_train_data[j]) * f_x_train_data[j]
#                 temp = ((pred - f_y_train_data[j]) ** 2)
#                 error_value =  temp / (2 * len(f_x_train_data))
#             print("cost error is ", error_value, i , "/", self.echops)
#             f_theta_0 = f_theta_0 - (self.alpha * val1) / len(f_x_train_data)
#
#             f_theta_1 = ((f_theta_1 - (self.alpha * val2) / len(f_x_train_data)))
#             # print('theta 0 is ', f_theta_0, 'theta 1 is ', f_theta_1, i , "/", self.echops)
#             t0_arr = np.append(t0_arr, f_theta_0)
#             t1_arr = np.append(t1_arr, f_theta_1)
#             j_t0_arr = np.append(j_t0_arr, val1)
#
#         j_t0_arr = np.column_stack((j_t0_arr))
#
#         return [f_theta_0, f_theta_1], t0_arr, t1_arr, j_t0_arr
#
#     # Predict the value of label in test data set by parameter values from train function
#     def classify(self, f_x_test_data, f_theta_0, f_theta_1):
#         f_y_pred = np.array([])
#         for i in range(len(f_x_test_data)):
#             y_pred_val = f_theta_0 + f_theta_1 * f_x_test_data[i]
#             f_y_pred = np.append(f_y_pred, y_pred_val)
#
#         return f_y_pred
#
#     # Find the accuracy of predicted values by comparing them with original labels in test dataset
#     def accuracy(self, f_y_test_data, y_pred):
#         total_error = 0
#         accu = np.array([])
#         for i in range(len(f_y_test_data)):
#             total_error += (abs((y_pred[i] - f_y_test_data[i]) / f_y_test_data[i]))
#
#         total_error = total_error / len(f_y_test_data)
#         f_accuracy = (1 - total_error) * 100
#
#         return f_accuracy
#
#         # Feature scaling using Standardisation
#
#     def standard(self, X, mean, standard_deviation):
#         result = np.array([])
#         for i in range(len(X)):
#             X_std = (X[i] - mean) / standard_deviation
#             result = np.append(X_std, result)
#         return result
#
#     # def error_vs_accuracy(self, accu):
#     #     plt.plot([i * 100 for i in range(len(self.echops))], [accu[i] for i in range(len(accu))], color='purple')
#     #     plt.xlabel("x_test")
#     #     plt.ylabel("y_test")
#     #     plt.title("x_test vs y_test")
#     #     plt.show()
#
#     def standard(self, X, mean, standard_deviation):
#         result = np.array([])
#         for i in range(len(X)):
#             X_std = (X[i] - mean) / standard_deviation
#             result = np.append(X_std, result)
#         return result
#
#     # def x_train_vs_y_predict(self, x_train, y_train, x_test, y_pred):
#     #     plt.plot([x_train[i] for i in range(len(x_train))], [y_train[i] for i in range(len(y_train))], color='purple')
#     #     plt.scatter([x_test[i] for i in range(len(x_test))], [y_pred[i] for i in range(len(y_pred))])
#     #     plt.xlabel("y_test")
#     #     plt.ylabel("x_test")
#     #     plt.title("x_test vs y_predicted")
#     #     plt.show()
#     #
#     # def x_test_vs_y_predict(self, x_test, y_test, y_pred):
#     #     plt.scatter([x_test[i] for i in range(len(x_test))], [y_test[i] for i in range(len(y_test))], color='purple')
#     #     plt.plot([x_test[i] for i in range(len(x_test))], [y_pred[i] for i in range(len(y_pred))])
#     #     plt.xlabel("x_train")
#     #     plt.ylabel("y_predict")
#     #     plt.title("x_test vs y_predicted")
#     #     plt.show()
#     #
#     # def theta_0_vs_iterations(self, theta_0):
#     #     plt.plot(range(len(theta_0)), [theta_0[i] for i in range(len(theta_0))])
#     #     plt.xlabel("Number_of_iterations")
#     #     plt.ylabel("theta_0")
#     #     plt.title("theta_0 vs Number_of_iterations")
#     #     plt.show()
#     #
#     # def theta_1_vs_iterations(self, theta_1):
#     #     plt.plot(range(len(theta_1)), [theta_1[i] for i in range(len(theta_1))])
#     #     plt.xlabel("Number_of_iterations")
#     #     plt.ylabel("theta_1")
#     #     plt.title("theta_1 vs Number_of_iterations")
#     #     plt.show()
#     #
#     # def error_vs_echops(self, error, echops):
#     #     plt.plot((range(echops)), [error[i] for i in range(len(error))])
#     #     plt.xlabel("echops")
#     #     plt.ylabel("error")
#     #     plt.title("error vs echops")
#     #     plt.show()
#
#
# def main():
#     l_t = LinearTrainer()
#     import pandas as pd
#     import numpy as np
#     import seaborn as sns
#
#     # Import data into dataframe
#     df = pd.read_csv("weatherHistory.csv")
#
#     df.rename(columns={"Temperature (C)": "Temperature"}, inplace=True)
#     df['Humidity'] = df['Humidity'].fillna(df.Humidity.mean())
#     df['Temperature'] = df['Temperature'].fillna(df.Temperature.mean())
#
#     # Histrogram of the feature varibale
#     #     plt.hist(df['Humidity'])
#     #     plt.show()
#
#     #     # Distplot of the feature varibale
#     #     sns.distplot(df['Humidity'])
#     #     plt.show()
#
#     #     # Histrogram of the target varibale
#     #     plt.hist(df['Temperature'])
#     #     plt.show()
#
#     #     # Distplot of the feature varibale
#     #     sns.distplot(df['Temperature'])
#     #     plt.show()
#
#     #     # now transforming feature variable
#     #     target = (np.sqrt((df['Humidity'])))
#     #     print ('Skewness is', target.skew())
#     #     sns.distplot(target)
#
#     #     # Boxplot to find the outliers in the Temp column
#     #     sns.boxplot(df['Temperature'])
#
#     #     # Boxplot to find the outliers in the Huminity column
#     #     sns.boxplot(df['Humidity'])
#
#     #     # Boxplot to find the outliers in whole dataset
#     #     sns.boxplot(df)
#
#     #    # Boxplot to find the outliers in the Temperature column and Humidity column
#     #     sns.boxplot(df['Temperature'])
#     #     plt.show()
#     #     sns.boxplot(df['Humidity'])
#     #     plt.show()
#
#     #     sns.boxplot(df)
#     #     plt.show()
#
#     train_size = int(np.ceil((len(df) * 70) / 100))
#     test_size = int(len(df) - train_size)
#
#     x_train_data = np.array(df["Humidity"][:train_size])
#     y_train_data = np.array(df["Temperature"][:train_size])
#
#     x_test_data = np.array(df["Humidity"][train_size:])
#     y_test_data = np.array(df["Temperature"][train_size:])
#
#     theta_0 = 1
#     theta_1 = 1
#
#     parameters, theta_0_arr, theta_1_arr, j_t_arr = l_t.train(x_train_data, y_train_data, x_test_data, y_test_data,
#                                                               theta_0, theta_1)
#     print(parameters[0], parameters[1])
#
#     y_pred = l_t.classify(x_test_data, parameters[0], parameters[1])
#
#     accuracy = l_t.accuracy(y_test_data, y_pred)
#     print("Acc", accuracy)
#
#     # l_t.x_train_vs_y_predict(x_train_data, y_train_data, x_test_data, y_pred)
#     # l_t.x_test_vs_y_predict(x_test_data, y_test_data, y_pred)
#     # l_t.theta_0_vs_iterations(theta_0_arr)
#     # l_t.theta_1_vs_iterations(theta_1_arr)
#
#
# if __name__ == '__main__':
#     main()
