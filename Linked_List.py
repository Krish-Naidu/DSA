class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

def traverseAndPrint(head: Node) -> None: 
  currentNode = head
  while currentNode != None:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def reverse_traverse(tail:Node) -> None:
    currentNode1 = tail
    while currentNode1 != None:
        print(currentNode1.data, end=" -> ")
        currentNode1 = currentNode1.prev
    print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
#### to make it circular list 
# node5.next = node1

node1.prev = None
node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4

return_value = traverseAndPrint(node1)
print(return_value)

# reverse_traverse(node5)

