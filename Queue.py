class Queue:
    internal_list = []

    def enqueue(self, element:str) -> None:
        self.internal_list.append(element)


    def dequeue(self) -> str:
        self.internal_list.pop(0)


my_queue = Queue()
my_queue.enqueue("krish")
my_queue.enqueue("is")
my_queue.enqueue("a")
my_queue.enqueue("bot")

element = my_queue.dequeue()
print(element)