class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original linked list:")
current = head
while current:
    print(current.data, end=" ")
    current = current.next

head = reverse_linked_list(head)

print("\nReversed linked list:")
current = head
while current:
    print(current.data, end=" ")
    current = current.next