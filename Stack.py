class Stack:
    internal_list = []

    def push(self, element:str) -> None:
        self.internal_list.append(element)


    def pop(self) -> str:
        element = self.internal_list.pop(-1)
        return element


my_stack = Stack()
my_stack.push("krish")
my_stack.push("is")
my_stack.push("a")
my_stack.push("bot")

my_stack.pop()
my_element = my_stack.pop()

print(my_element)