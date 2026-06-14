class Node:
    data = None
    next = None
    def __init__(self):
        # self.data =  data_1
        # self.next = next_1
        print("called")

node1 = Node()
node1.data = "krish"

node2 = Node()
node2.data = "is a"

node3 = Node()
node3.data = "bot"

node1.next = node2
node2.next = node3 

# def traverse(node):
#     print(node)

node = node1
while True:
    print(node.data)
    if node.next == None:
        break
    else:
        next_node = node.next
    node = next_node
