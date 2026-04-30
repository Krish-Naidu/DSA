class Stack:
    internal_list = []

    def push(self, element:str) -> None:
        self.internal_list.append(element)


    def pop(self) -> str:
        element = self.internal_list.pop(-1)  #Python array has a default pop method that removes the last element of the list and returns it.
        # We can also specify an index to pop a specific element.
        return element


my_stack = Stack()
my_stack.push("krish")
my_stack.push("is")
my_stack.push("a")
my_stack.push("bot")

my_stack.pop()
my_element = my_stack.pop()

print(my_element)