# Создать базовый класс «список» на основе обычного массива с  функциями
# вставки и удаления элементов. Реализовать на базе списка производные классы
# стека и очереди. Для каждого класса провести модульное тестирование основных методов класса.


# Создадим класс Mylist для добавления, удаления и нахождения количества элементов в списке
class MyList:
    # Создадим пустой список и назовём его _items
    def __init__(self):
        self._items = []

    # Создадим функцию, которая вставляет элемент в конец списка
    def insert(self, item):
        self._items.append(item)

    # Создадим функцию удаления элемента из списка.
    def remove(self, item):
        self._items.remove(item)

    # Создадим функцию, которая выводит все элементы из списка
    def get_items(self):
        return self._items.copy()

    # Создадим функцию, которая выводит количество элементов в списке
    def size(self):
        return len(self._items)

# Создадим класс для стака
class Stack(MyList):
    # Создадим функцию, которая удаляет элемент на вершину стека
    def push(self, item):
        self.insert(item)

    # Создадим функцию, которая удаляет и возращает элемент с вершины стека
    def pop(self):
        if self.size() == 0:
            raise IndexError("Ошибка")
        return self._items.pop()

    # Создадим функцию, которая возвращает элемент с вершины стека без удаления его
    def peek(self):
        if self.size() == 0:
            raise IndexError("Ошибка")
        return self._items[-1]

# Создадим класс для очереди
class Queue(MyList):
    # Добавляем элемент в конец очереди
    def enqueue(self, item):
        self.insert(item)

    # Удаляем и возвращаем элемент из начала очереди.
    def dequeue(self):
        if self.size() == 0:
            raise IndexError("Ошибка")
        return self._items.pop(0)

    # Возвращаем элемент из начала очереди без удаления его
    def front(self):
        if self.size() == 0:
            raise IndexError("Ошибка")
        return self._items[0]

# Продемонстрируем как работает наш список:
myList = MyList()
myList.insert(5)
myList.insert(4)
myList.insert(3)
myList.insert(8)
myList.insert(12)
print(myList.get_items())
print(myList.size())

# Cтек
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())

# Очередь
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.front())
