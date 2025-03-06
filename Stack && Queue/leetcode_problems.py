# Implement Stack Using a List
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


# Check to see if a string of parentheses is balanced or not.
def is_balanced_parentheses(parentheses):
    stack: Stack = Stack()
    for char in parentheses:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty() or stack.pop() != "(":
                return False
    return stack.is_empty()
