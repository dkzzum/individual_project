class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next: Node | None = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    # Удаление первого эл. списка
    def pop_front(self) -> None:
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next

    # Добавление эл. в конец списка
    def push_back(self, data) -> None:
        node: Node = Node(data)
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next = node

        self.tail = node

    # Добавление эл. в начало списка
    def push_front(self, data) -> None:
        node: Node = Node(data)
        node.next = self.head

        self.head = node
        if self.tail is None:
            self.tail = node

    # Удаление последнего эл.
    def pop_back(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return

        node: Node = self.head
        while node.next != self.tail:
            node = node.next

        node.next = None
        self.tail = node

    # Метод возвращающий эл. списка по индексу
    def get_node(self, index: int):
        if index < 0:
            return None

        node: Node = self.head
        n = 0
        while node and node.next and n != k:
            node = node.next
            n += 1

        return node if n == k else None

    # Метод вставляющий новый эл. по указанному индексу
    def insert(self, k: int, data):
        left: Node = self.head
        if left is None:
            return

        right = self.get_node(k + 1)
        node: Node = Node(data)

        left.next = node
        node.next = right

        if right is None:
            self.tail = node

    # Удаляет промежуточныe эл. списке
    def erase(self, k: int):
        if k < 0:
            return None
        if k == 0:
            self.pop_front()
            return

        left: Node = self.get_node(k - 1)
        if left is None:
            return

        node: Node = left.next
        if node is None:
            return

        right: Node = node.next
        left.next = right

        if node == self.tail:
            self.tail = left

    def __len__(self) -> int:
        i = 0
        node: Node = self.head
        while node:
            i += 1
            node = node.next

        return i


if __name__ == '__main__':
    lili = LinkedList()
    lili.push_front(1)
    lili.push_back(3)
    lili.push_front(5)
    lili.push_back(7)

    l = LinkedList()
    print(len(l))
    print(lili)
