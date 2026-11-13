from collections import deque

class MyStack:

    def __init__(self):
        self.main_queue = deque()
        self.transition_queue = deque()
        self.topElem = None

    def push(self, x: int) -> None:
        self.main_queue.append(x)
        self.topElem = x

    def pop(self) -> int:
        while len(self.main_queue) > 1:
            self.transition_queue.append(self.main_queue.popleft())
        
        popped = self.main_queue.popleft()
        self.topElem = None

        while len(self.transition_queue) > 0:
            nextPopped = self.transition_queue.popleft()
            self.main_queue.append(nextPopped)
            self.topElem = nextPopped
        
        return popped

    def top(self) -> int:
        return self.topElem

    def empty(self) -> bool:
        return len(self.main_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


