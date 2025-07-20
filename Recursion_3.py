#Рекурсия состоит из базового и рекурсивного случая //
def countdown(i):
    print(i)
    if i <= 1: # Базовый случай нужен для того, чтобы функция не вызывала себя бесконечно => т.е была циклична
        return
    else:
        countdown(i - 1)    #Рекурсивный случай
countdown(3)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

x = 5
print(fact(x))

# Вычисление суммы элементов массива 
def arrSum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + arrSum(arr[1:])
    
arr = [1, 2, 3, 4, 5]
print(arrSum(arr))

# Переворот строки
def stringReflection(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + stringReflection(string[:-1])
    
string = "привет"
print(stringReflection(string))
