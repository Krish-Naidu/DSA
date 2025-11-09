class Queue:
    internal_list = []

    def enqueue(self, element:str) -> None:
        self.internal_list.append(element)

# The only difference between Stack and queue is the index value you pass in pop.
    def dequeue(self) -> str:
        return self.internal_list.pop(0)

def main():
    print("Hellow")
    my_queue = Queue()
    my_queue.enqueue("krish")
    my_queue.enqueue("is")
    my_queue.enqueue("a")
    my_queue.enqueue("bot")

    my_queue.dequeue()
    my_queue.dequeue()
    element = my_queue.dequeue()
    print(element)

if __name__ == "__main__":
    main()