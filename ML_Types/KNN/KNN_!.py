import pandas as pd
import numpy as np

df = pd.read_csv("bank.csv", delimiter=';')

for name in df.columns:
    if df[name].dtype != "int64":
        df[name] = pd.get_dummies(df[name])


x_data_set = np.array(pd.DataFrame(df, columns = ['contact', 'campaign']))
y_data_set = np.array(pd.DataFrame(df, columns = ['y']))

train_size = int(np.ceil((len(y_data_set) * 70) / 100))
test_size = int(len(y_data_set) - train_size)

x_train_data = np.array(x_data_set[:train_size])
y_train_data = np.array(y_data_set[:train_size])
x_test_data = np.array(x_data_set[train_size:])
y_test_data = np.array(y_data_set[train_size:])
print(y_train_data)
size = [x_train_data.shape]
size = size[0][1] + 1

x_train_data = x_train_data[:2000]
y_train_data = y_train_data[:2000]
x_test_data = x_test_data[:500]
y_test_data = y_test_data[:500]


y_pred = np.array([])

for i in range(int(len(x_test_data))):
    distance = np.array([])
    length = x_train_data.shape[1]
    for j in range(int(len(x_train_data))):
        temp = 0
        for k in range(length):
            temp += np.square(x_test_data[i][k] - x_train_data[j][k])
        distance = np.append(distance, temp)
    print("distance.shape : ",distance.shape)
    sorted_data = np.sort(distance)

    k = 5
    neighbors = np.array([])
    for i in range(k):
        neighbors = np.append(neighbors, distance[i])

    count_0 = 0
    count_1 = 0
    for i in range(len(neighbors)):
        if neighbors[i] == 1:
            count_0 += 1
        elif neighbors[i] == 0:
            count_1 += 1


    if count_0 > count_1:
        y_pred = np.append(y_pred, 1)
    else:
        y_pred = np.append(y_pred, 0)


print("y_pred = ",y_pred)

acc = 0
count_1 = 0
for i in range(len(y_pred)):
    if y_pred[i] == y_test_data[i]:
        count_1 +=1

acc = (count_1 / len(y_test_data)) * 100
print("accuracy = ", acc )