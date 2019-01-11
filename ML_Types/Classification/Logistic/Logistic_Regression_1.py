
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, accuracy_score
class MultiLinear:
    
    def __init__(self):
         # Learning Rate
        self.l_rate = 0.001
         # Total iterations
        self.echops = 10000
        
    # Training the model using algorithm
    def gradient_descent(self,x_train_data, y_train_data, parameters):
        theta_values = np.array([])
        cost_fun = np.array([])
          # Add 1 to first position in x_train_data
        x_train_data = np.column_stack((np.ones((x_train_data.shape[0], 1)), x_train_data))
        theta_values = np.array([])
        
        for i in range(self.echops):          
            
            z = np.dot(x_train_data, parameters)
            sigmoid = (1 + (1/np.exp(-z)))
#             h_x =  
            temp1 = sigmoid - y_train_data
            
            temp2 = np.dot( x_train_data.T, temp1)
            temp2 = np.dot(temp2, self.l_rate) / len(x_train_data)
            parameters = parameters - temp2
            theta_values = np.append(theta_values, parameters)
#             print("sig", 1 - sigmoid)
#             print("Val_log",np.log(np.abs(1 - sigmoid)))
#             temp1 = (-y_train_data  np.log(sigmoid)
            cost_function = (np.dot(-y_train_data.T , np.log(sigmoid)) - np.dot((1 - y_train_data).T , np.log(np.abs(1 - sigmoid))))
            cost_fun = np.append(cost_fun, cost_function)
        print("cf", cost_fun.shape)
        return parameters, theta_values, cost_fun
    
    # testing the model on test data set
    def prediction(self,parameters,x_test_data):
            x_test_data = np.column_stack((np.ones((x_test_data.shape[0], 1)), x_test_data))
            prediction = np.zeros((x_test_data.shape[0], 1), dtype=float)

            z = np.dot(x_test_data, parameters)
            sigmoid = 1 + (1/np.exp(-z))
            
            for i in range(len(sigmoid)):
                if sigmoid[i][0] >= 0.5 :
                    prediction[i][0] = 1                    
                else : 
                    prediction[i][0] = 0
            prediction = np.reshape(prediction,(len(prediction), 1))
            print("pred", prediction.shape)
            print(prediction)
            return prediction
                    
    # Find accuracy 
    def accuracy(self, y_data_test, y_pred_test):
        
        
            print("y", y_data_test.shape)
            print("y pred", y_pred_test.shape)
            total_error = 0
            for i in range(len(y_data_test)):
                total_error += abs((y_pred_test[i] - y_data_test[i]) / y_data_test[i])
            total_error = (total_error / len(y_data_test))
            accuracy = 1 - total_error
            return accuracy * 100
    

        
    def theta_0_vs_iterations(self, cost_fun, theta, size):
            for j in range(0,size):
                print("for values from", j)
                x = [theta[i+(self.echops)*j] for i in range(len(cost_fun))]
                print("c_f",cost_fun.shape)
                print("theta",theta.shape)

                y = [cost_fun[i] for i in range(len(cost_fun))]
                plt.plot(x,y)
                plt.show()

#             plt.title("theta_0 Vs theta_1")
#             x = [theta[i] for i in range(len(cost_fun))]
#             y = [theta[i+6000] for i in range(len(cost_fun))]
#             plt.plot(x,y)
#             plt.show()
            
    def iterations_vs_cost_fun(self,cost_fun):
        print("iterations_vs_cost_fun",cost_fun.shape)
        plt.title("iterations Vs Cost Function")
        x = range(self.echops)
        y = [cost_fun[i] for i in range(len(cost_fun))]
        plt.plot(x,y, c = "purple")
        plt.show()

            
    def test_vs_predict(self, x_test_data, y_test_data, y_predict):
        plt.title("x_test vs vs y_test vs y_predicted")
        plt.xlabel("x_test")
        plt.ylabel("y_test")
        x = [x_test_data[0:] for i in range(len(x_test_data))]
        y = [y_test_data[i] for i in range(len(x_test_data))]
        z = [y_predict[i] for i in range(len(y_predict))]
        print(len(x), len(y))
        plt.scatter(x, y, alpha=0.5)
        plt.plot(x,z, c = "purple")
        plt.show()

    
    
def main():   
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from pandas.api.types import is_numeric_dtype
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, accuracy_score
    df = pd.read_csv('bank.csv',  delimiter=';')

    for name in df.columns:
        if df[name].dtype != "int64":
            df[name] = pd.get_dummies(df[name])  

    for name in df.columns:
            if 'y' == name :     
                pass
            else:
                temp = 0
                temp_arr = np.array([])
                df[name] = (df[name] - df[name].mean()) / np.nanstd(df[name])

    
    x_data_set = np.array(pd.DataFrame(df, columns = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing',
           'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays',
           'previous', 'poutcome']))
    y_data_set = np.array(pd.DataFrame(df, columns = ['y']))
    
    
    train_size = int(np.ceil((len(y_data_set) * 70) / 100))
    test_size = int(len(y_data_set) - train_size)

    x_train_data = np.array(x_data_set[:train_size])
    y_train_data = np.array(y_data_set[:train_size])
    x_test_data = np.array(x_data_set[train_size:])
    y_test_data = np.array(y_data_set[train_size:])
    print(y_test_data)
    size = [x_train_data.shape]
    size = size[0][1] + 1

    parameters = np.zeros((size, 1), dtype='f')
    
    
    m_l = MultiLinear()
    theta_vector, theta_values, cost_fun = m_l.gradient_descent(x_train_data, y_train_data, parameters)
    theta_vector = np.reshape(theta_vector,(len(theta_vector), 1))
    theta_values = np.reshape(theta_values,(len(theta_values), 1))
    cost_fun = np.reshape(cost_fun,(len(cost_fun), 1))


    prediction = m_l.prediction(theta_vector,x_test_data) 
    prediction_train= m_l.prediction(theta_vector,x_train_data)  

    train_acc = round(float(100 - np.mean(np.abs(prediction_train - y_train_data)) * 100))
    test_acc = round(float(100 - np.mean(np.abs(prediction - y_test_data)) * 100))

    accuracy =  m_l.accuracy(y_test_data, prediction)
    print("Accuracy = ","Test data : ",test_acc,"     train data: ",train_acc)
    
#     plt.scatter(x_test_data, y_test_data, c = 'red')
#     plt.plot(x_train_data, y_train_data, c = 'blue')
#     plt.show()
    
    m_l.theta_0_vs_iterations(cost_fun, theta_values, size)
    m_l.iterations_vs_cost_fun(cost_fun)
    

if __name__ == '__main__':
    main()

