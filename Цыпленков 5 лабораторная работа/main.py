import matplotlib.pyplot as plt
import pandas as pd
import pylab

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# набор массива данных https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/
dataset = pd.read_csv('JEOPARDY_CSV.csv')
dataset.drop(columns='Air Date', inplace=True)
dataset.drop(columns='Category', inplace=True)
dataset.drop(columns='Question', inplace=True)
dataset.drop(columns='Answer', inplace=True)
dataset['Value'] = pd.factorize(dataset['Value'])[0]

# # Формирования набора данных
X = dataset.drop('Round', axis=1)
y = dataset['Round']
X = pd.DataFrame(X, index = X.index, columns = X.columns)


# разбивка выборки на две подвыборки случайно с размером тестовой выборки 0.3
# выносим из функции для использования в разных методах
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# метод k-NN
def kneighbors_metod(x_train, x_test, y_train):
    # метод K-ближайших соседей
    knn_model = KNeighborsClassifier(n_neighbors=5)

    # строим модель на обучающем множестве
    knn_model.fit(x_train, y_train)

    # вызываем метод прогнозирования
    y_pred = knn_model.predict(x_test)
    return y_pred

# Метод Древа решений
def tree_metod(x_train, x_test, y_train):
    tree = DecisionTreeClassifier(max_depth=12)
    tree.fit(x_train, y_train)
    y_pred = tree.predict(x_test)
    return y_pred


# Метод прецептрон
def preceptron(x_train, x_test, y_train):
    mlp = MLPClassifier(random_state = 1, max_iter = 300).fit(x_train, y_train)
    y_pred = pd.Series(mlp.predict(x_test))
    return y_pred

# вывод основных метрик и графиков
def visualization(y_pred, name_metod):
    print('\nОсновные метрики классфикации', name_metod, '\n', classification_report(y_test, y_pred, zero_division=0),
          '\nМатрица неточностей для оценки точности классификации', confusion_matrix(y_test, y_pred),
          '\nОценка модели', name_metod,': оценка точности ', accuracy_score(y_test, y_pred))
    # графики для сравнения значений
    pylab.figure(figsize=(12, 6))
    #pylab.title(name_metod)
    pylab.subplot(1, 2, 1)
    # тестовые значения
    pie_test = pd.crosstab(index=y_test, columns='% observations')
    plt.pie(pie_test['% observations'], labels=pie_test['% observations'].index, autopct='%.0f%%')
    plt.title('Массив тестовых значений')
    pylab.subplot(1, 2, 2)
    # предсказанные значения
    pie_pred = pd.crosstab(index=y_pred, columns='% observations')
    plt.pie(pie_pred['% observations'], labels=pie_pred['% observations'].index, autopct='%.0f%%')
    plt.title(('Массив прогнозируемых значений метода: '+ name_metod))
    plt.show()
    # совпадение тестовых данных и предсказания
    plt.plot(y_test, label=('Тестовое:'))
    plt.plot(y_pred, label=('Предсказанное методом: '+ name_metod))
    plt.legend()
    plt.show()

    # Вывод размера массива
print('\nРазмер массивов\nX train : ', X_train.shape, '\nX test  : ', X_test.shape, '\nY train : ', y_train.shape)
# Выводы методов:
# Дерево решений
visualization(tree_metod(X_train, X_test, y_train), 'Дерево решений')
# Вывод метода KNN
visualization(kneighbors_metod(X_train, X_test, y_train), 'Метод k-NN')
# Вывод метода прецетрон
visualization(preceptron(X_train, X_test, y_train), 'Прецептрон')
