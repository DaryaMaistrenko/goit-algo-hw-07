# Завдання 1-3: Реалізація двійкового дерева пошуку (BST) і алгоритмів для нього

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для знаходження найбільшого значення у двійковому дереві пошуку
def find_max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.value

# Функція для знаходження найменшого значення у двійковому дереві пошуку
def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value

# Функція для знаходження суми всіх значень у двійковому дереві пошуку
def find_sum_of_values(node):
    if node is None:
        return 0
    return node.value + find_sum_of_values(node.left) + find_sum_of_values(node.right)

# Приклад створення дерева
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(30)

# Використання функцій для завдань 1-3
max_value = find_max_value(root)
min_value = find_min_value(root)
total_sum = find_sum_of_values(root)

print(f"Найбільше значення в дереві: {max_value}")
print(f"Найменше значення в дереві: {min_value}")
print(f"Сума всіх значень у дереві: {total_sum}")

# Завдання 4: Реалізація системи коментарів

class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False
    
    # Метод для додавання відповіді
    def add_reply(self, reply):
        self.replies.append(reply)
    
    # Метод для видалення відповіді
    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True
    
    # Метод для відображення коментаря та його відповідей
    def display(self, indent=0):
        print(' ' * indent + f"{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(indent + 4)

# Приклад використання системи коментарів
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Видаляємо коментар Андрія
reply1.remove_reply()

# Відображення структури коментарів
root_comment.display()