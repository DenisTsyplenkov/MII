import numpy as num
import matplotlib.pyplot as plt

N = int(input('Введите размерность матрицы N больше 3-х: '))

K = int(input('Введите K: '))

#защита от дурака
if N < 4:
    raise ValueError('N должна быть больше 3')
    exit()
if N % 2 != 0:
    raise ValueError('Требуется чётная размерность N!')
    exit()

#Формирование матрицы
A = num.eye(N)
A = num.random.randint(low=-10, high=10, size=(N, N))


#формирование подматриц
B = A[:int(N/2), :int(N/2)]
C = A[:int(N/2), int(N/2):]
D = A[int(N/2):, :int(N/2)]
E = A[int(N/2):, int(N/2):]

print(f'A = \n{A}\n')
print(f'B = \n{B}\n')
print(f'C = \n{C}\n')
print(f'D = \n{D}\n')
print(f'E = \n{E}\n')

F = A.copy()

sumEK = 0;
for i in E[:, ::2]:
    for j in i:
        if j > K:
            sumEK += j
print(f'Сумма элементов, больших К, в нечетных столбцах E: {sumEK}')

prodEP = 1
lastIndex=int(N/2)-1
i = int(1)
for i in range(lastIndex):
    prodEP *= E[0, i] * E[i, lastIndex] * E[lastIndex, i + 1] * E[i + 1, 0]
    i+1
print(f'Произведение элементов периметра: {prodEP}')

print(F)

if sumEK > prodEP:
    print("Сумма элементов, больших К, в нечетных столбцах E больше, чем "
          "произведение элементов периметра матрицы E => меняем С и E симметрично")
    Cf = num.flip(C, axis=1)
    Ef = num.flip(E, axis=1)
    F = num.vstack([num.hstack([B, Cf]), num.hstack([D, Ef])])
    print(F)

else:
    print("Сумма элементов, больших К, в нечетных столбцах С меньше, чем\n"
          "произведение элементов периметра матрицы E=> меняем С и B несимметрично")
    F = num.hstack([num.vstack([C, D]), num.vstack([B, E])])
    print(F)

detA = num.linalg.det(A)
print(f'Определитель матрицы А: {detA}')

diagonaliF = sum(num.diagonal(F)) + sum(num.diagonal(num.flip(F, axis=1)))
print(f'Сумма диагональных элементов матрицы F: {diagonaliF}')

expression = []
if detA > diagonaliF:
    print("Определитель А больше суммы диагоналей F:")
    expression = A * num.linalg.inv(A) - K * num.linalg.inv(F)
else:
    print("\nОпределитель А меньше суммы диагоналей F:")
    G = num.tril(A)
    expression = (num.transpose(A) + G - num.transpose(F)) * K

print("\nРезультат выражения:")
print(expression)

plt.subplot(2, 2, 1)
plt.imshow(F[:int(N/2), :int(N/2)], cmap='rainbow', interpolation='bilinear')

plt.subplot(2, 2, 2)
plt.imshow(F[:int(N/2), int(N/2):], cmap='rainbow', interpolation='bilinear')

plt.subplot(2, 2, 3)
plt.imshow(F[int(N/2):, :int(N/2)], cmap='rainbow', interpolation='bilinear')

plt.subplot(2, 2, 4)
plt.imshow(F[int(N/2):, int(N/2):], cmap='rainbow', interpolation='bilinear')

plt.show()

plt.subplot(2, 2, 1)
plt.plot(F[:int(N/2), :int(N/2)])

plt.subplot(2, 2, 2)
plt.plot(F[:int(N/2), int(N/2):])

plt.subplot(2, 2, 3)
plt.plot(F[int(N/2):, :int(N/2)])

plt.subplot(2, 2, 4)
plt.plot(F[int(N/2):, int(N/2):])

plt.show()