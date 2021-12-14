# Библиотека по работе с матрицами

Матрица для работы с матрицами при помощи языка Python.
Далее будут приведены примеры по работе с библиотекой

1. Задать матрицу можно также как и обычный двумерный список в Python
```python
a = [[1, 2],
     [0, 1],
     [2, 3]]
```
2. Печать матрицы для выведения промежуточных результатов. Второй параметр отвечает за кол-во символов выделяемых на каждый элемент(включая квадратные скобки)
```python
import matrix

a = [[1, 2],
     [0, 1],
     [2, 3]]

matrix.matrix_print(a, 5)
print()
matrix.matrix_print(a, 9)
```
Результат:
```
 [1]  [2] 
 [0]  [1] 
 [2]  [3] 

   [1]      [2]   
   [0]      [1]   
   [2]      [3]   
```
3. Транспонирование матрицы. На вход принимает матрицу. Возвращает транспонированную
```python
import matrix

a = [[1, 2],
     [0, 1],
     [2, 3]]

matrix.matrix_print(a, 5)
print()
matrix.matrix_print(matrix.transpose(a), 5)
```
Результат:
```
 [1]  [2] 
 [0]  [1] 
 [2]  [3] 

 [1]  [0]  [2] 
 [2]  [1]  [3] 
```
4. Умножение матрицы на число. Первым параметром принимает матрицу, вторым число на которое будет проиведенно умножение(по умолчанию равно 2)
```python
import matrix

a = [[1, 2],
     [0, 1],
     [2, 3]]
b = matrix.multiplication_matrix_scalar(a, 3)
matrix.matrix_print(a, 5)
print()
matrix.matrix_print(b, 5)
```
Результат:
```
 [1]  [2] 
 [0]  [1] 
 [2]  [3] 

 [3]  [6] 
 [0]  [3] 
 [6]  [9] 
```
5. Умножение матриц друг на друга. Первым и вторым аргументом принмает матрицы размера (m × n) на (n × k). Возвращает матрицу размера (m × k)
```python
import matrix

a = [[1, 2],
     [0, 1],
     [2, 3]]
b = [[2, 5, 1],
     [6, 7, 1]]

c = matrix.matrix_multiplication(a, b)
print()
matrix.matrix_print(c, 5)
```
Результат:
```
 [14] [19] [3] 
 [6]  [7]  [1] 
 [22] [31] [5] 
```
