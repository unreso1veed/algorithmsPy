# Сортировка массива по возрастанию


def findSmallest(arr):      #Нахождение минимального элемента массива
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index        


def selectionSort(arr):  #Сортировка выбором
    newArr = []
    copiedArr = list(arr) # Копирует массив перед изменением
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr) # Находит наименьший элемент в массиве и добавляет его в новый массив
        newArr.append(copiedArr.pop(smallest))
    return newArr  

print (selectionSort([1, 2, 12, 4, 87]))  