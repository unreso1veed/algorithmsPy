from os import listdir
from os.path import isfile, join
from collections import deque

def printname(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)

printname("pics")

#odyssey.png
#a.png
#space.png 

#Рекурсия - Поиск в глубину. Разница в порядке добавления в стэк папок - в первом случае папка добавляется в очередь, 
#а во втором добавляется и сразу проверяется. Но есть важное НО - 
#Поиск в глубину НЕ МОЖЕТ использоваться для нахождения кратчайшего пути! 
# (ПОИСК В ГЛУБИНУ СРАЗУ ЗАХОДИТ НА МАКСИМАЛЬНУЮ ГЛУБИНУ)

def printnames(dir):
    for file in sorted(listdir(dir)):       #Перерать все файлы и все папки в текущей папке
        fullpath = join(dir, file)                  
        if isfile(fullpath):                #Если это файл, то вывести его имя
            print(file)
        else:
            return printnames(fullpath)     #Если это папка, вызвать для нее функцию рекурсивно, чтобы провести поиск папок/файлов
        
printnames("pics")

#a.png
#space.png
#odyssey.png
