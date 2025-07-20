from collections import deque

graph = {}
graph ['Вы'] = ['Алиса', 'Боб', 'Клэр']
graph ['Боб'] = ['Анудж', 'Пегги']
graph ['Алиса'] = ['Пегги']
graph ['Клэр'] = ['Том', 'Джонни']
graph ['Анудж'] = []
graph ['Пегги'] = []
graph ['Том'] = []
graph ['Джонни'] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (person + ' продавец манго')
                return True
        else:
            search_queue += graph[person]
            searched.add(person)
    return False

def person_is_seller(name):
    return name == 'Том'
    
    
search('Вы')