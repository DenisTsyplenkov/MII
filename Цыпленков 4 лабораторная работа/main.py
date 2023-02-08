import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from collections import Counter


# собственный метод статистики
def self_made(k, x_train, x_test, y):
    y_pred = []

    for i in range(len(x_test)):
        distances = []
        for j in range(len(x_train)):
            dist = np.sqrt(np.sum((np.array(x_train)[j, :] - np.array(x_test)[i]) ** 2))
            distances.append(dist)

        distances = np.array(distances)

        k_distances = np.argsort(distances)[:k]

        values = y[k_distances]
        y_pred.append(Counter(values).most_common(1)[0][0])

    return y_pred

# реализация через scikit
def kneighbors_scikit(k, X, y):
    # разбивка выборки на две подвыборки случайно с размером тестовой выборки 0.3
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # стандартизация
    scaler = StandardScaler().fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    # метод K-ближайших соседей
    knn = KNeighborsClassifier(n_neighbors=k)

    # строим модель на обучающем множестве
    knn.fit(x_train, y_train)

    # вызываем метод прогнозирования
    y_pred = knn.predict(x_test)

    return x_train, x_test, y_test, y_test, y_pred

# функция обработки данных
def data_classification(dataset):

    X = dataset.iloc[:, 1:3]
    y = dataset.iloc[:, 3]

    x_train = dataset.iloc[:(int)(0.7 * len(dataset)), 1:3]
    x_test = dataset.iloc[(int)(0.7 * len(dataset)):, 1:3]
    y_pred = self_made(7, x_train, x_test, y)
    y_test = dataset.iloc[(int)(0.7 * len(dataset)):, 3]
    print('Статистика по методу k-NN используя собственный метод')
    print(classification_report(y_test, y_pred))

    _train, X_test, Y_test, Y_test, Y_pred = kneighbors_scikit(7, X, y)
    print('Статистика по методу k-NN используя scikit')
    print(classification_report(Y_test, Y_pred))

    return x_test, X_test, y_pred, Y_pred

# функция отрисовки графиков
def visualization(x_test, X_test, points_color, points_color_scikit):
    f, ax = plt.subplots(2, 1, figsize=(8, 8))

    ax[0].scatter(x_test['сладость'][:], x_test['хруст'][:], c=points_color)
    ax[0].set_title('Статистика по методу k-NN используя собственный метод')

    ax[1].scatter(X_test[:, 0], X_test[:, 1], c=points_color_scikit)
    ax[1].set_title('Статистика по методу k-NN используя scikit')

    plt.show()


# читаем csv файл
dataset = pd.read_csv('input_data.csv')
# обрабатываем данные и получаем значения для постройки графика
print('Статистика с исходными данными')
x_test, X_test, y_pred, Y_pred = data_classification(dataset)

# определяем цвета для точек на графике
points_color = [label.replace("Фрукт", "orange", 1)
                .replace("Овощ", "green", 1)
                .replace("Протеин", "brown", 1) for label in y_pred]

points_color_scikit = [label.replace("Фрукт", "orange", 1)
                       .replace("Овощ", "green", 1)
                       .replace("Протеин", "brown", 1) for label in Y_pred]

# рисуем график
visualization(x_test, X_test, points_color, points_color_scikit)

# читаем данные с дополнительным классом
extended_dataset = pd.read_csv('extended_data.csv')
# обрабатываем данные с дополнительным классом
print('Статистика данных с дополнительным классом')
x_test, X_test, y_pred, Y_pred = data_classification(extended_dataset)

points_color = [label.replace("Фрукт", "orange", 1)
                     .replace("Овощ", "green", 1)
                     .replace("Протеин", "brown", 1)
                     .replace("Снэки", "yellow", 1) for label in y_pred]

points_color_scikit = [label.replace("Фрукт", "orange", 1)
                            .replace("Овощ", "green", 1)
                            .replace("Протеин", "brown", 1)
                            .replace("Снэки", "yellow", 1) for label in Y_pred]
# рисуем график расширенных данных
visualization(x_test, X_test, points_color, points_color_scikit)