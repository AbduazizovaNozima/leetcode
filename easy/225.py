class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return "Stack is empty"
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


myStack = MyStack()

myStack.push(1)
myStack.push(2)
myStack.top()
myStack.pop()
myStack.empty()

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Top: ", myStack.top)
print("isEmpty: ", myStack.empty())
