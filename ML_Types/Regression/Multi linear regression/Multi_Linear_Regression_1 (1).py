
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
        self.echops = 6000
        
    # Training the model using algorithm
    def gradient_descent(self,x_train_data, y_train_data, parameters):
        temp1 = temp2 = temp3 = 0
        theta_values = np.array([])
          # Add 1 to first position in x_train_data
        x_train_data = np.column_stack((np.ones((x_train_data.shape[0], 1)), x_train_data))
        cost_fun = np.array([])

        for i in range(self.echops):
            # cost_function = (1/2m)*(sumation(H(x[i]) - y[i]))
            # Gradient descent = theta = theta - ((alpha/m) * (sumation(H(x[i]) - y[i]))
            temp1 = (np.dot(x_train_data, parameters)) - y_train_data
            temp1 = np.dot(x_train_data.transpose(), temp1)
            temp2 = (self.l_rate/len(x_train_data)) * temp1
            parameters = parameters - temp2
            theta_values = np.append(theta_values, parameters)
            temp3 = (np.dot(x_train_data, parameters) - y_train_data)**2
            temp1 = np.sum(temp3) / 2 * len(x_train_data)
            cost_fun = np.append(cost_fun,temp1)
    
        return parameters, theta_values, cost_fun

    # testing the model on test data set
    def prediction(self,parameters,x_test_data):
            x_test_data = np.column_stack((np.ones((x_test_data.shape[0], 1)), x_test_data))
            print("test", x_test_data.shape)
            print("para", parameters.shape)
            return np.dot(x_test_data,parameters)

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
                x = [theta[i+(6000*j)] for i in range(len(cost_fun))]
                y = [cost_fun[i] for i in range(len(cost_fun))]
                plt.plot(x,y)
                plt.show()

            plt.title("theta_0 Vs theta_1")
            x = [theta[i] for i in range(len(cost_fun))]
            y = [theta[i+6000] for i in range(len(cost_fun))]
            plt.plot(x,y)
            plt.show()
            
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

    df = pd.read_csv('airfoil_self_noise.dat.txt', delimiter='\t')
    df.columns = ['Frequency', 'AngleOfAttack', 'ChordLength', 'FreeStreamVelocity', 'SuctionSideDisplacementThickness', 'ScaledSoundPressureLevel']

    for name in df.columns:
        if 'ScaledSoundPressureLevel' == name :     
            pass
        else:
            temp = 0
            temp_arr = np.array([])
            df[name] = (df[name] - df[name].mean()) / np.nanstd(df[name])

    x_data_set = np.array(pd.DataFrame(df, columns = ['Frequency', 'AngleOfAttack', 'ChordLength', 'FreeStreamVelocity', 'SuctionSideDisplacementThickness']))
    y_data_set = np.array(pd.DataFrame(df, columns = ['ScaledSoundPressureLevel']))

    print(len(x_data_set), len(y_data_set))
    size = [x_data_set.shape]
    columns = size[0][1]
    train_size = int(np.ceil((len(y_data_set) * 70) / 100))
    test_size = int(len(y_data_set) - train_size)

    x_train_data = np.array(x_data_set[:train_size])
    y_train_data = np.array(y_data_set[:train_size])
    x_test_data = np.array(x_data_set[train_size:])
    y_test_data = np.array(y_data_set[train_size:])

    size = [x_train_data.shape]
    size = size[0][1] + 1
    parameters = np.zeros((size, 1), dtype='f')
    
    m_l = MultiLinear()
    theta_vector, theta_values, cost_fun = m_l.gradient_descent(x_train_data, y_train_data, parameters)
    print(theta_vector)
    prediction = m_l.prediction(theta_vector,x_test_data)  
    accuracy =  m_l.accuracy(y_test_data, prediction)
    print(accuracy)
    
    m_l.theta_0_vs_iterations(cost_fun, theta_values, size)
    m_l.iterations_vs_cost_fun(cost_fun)
    

if __name__ == '__main__':
    main()

