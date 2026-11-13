class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.transition_stack = []        

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        if not self.transition_stack:
            while self.main_stack:
                self.transition_stack.append(self.main_stack.pop())
        return self.transition_stack.pop()

    def peek(self) -> int:
        if not self.transition_stack:
            while self.main_stack:
                self.transition_stack.append(self.main_stack.pop())
        return self.transition_stack[-1]


    def empty(self) -> bool:
        return not self.main_stack and not self.transition_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

