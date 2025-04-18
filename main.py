class Stack:

    def __init__(self, list_: list = None):
        self.stack = list_ if list_ else []

    def is_empty(self):
        return not self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    

def check_balanced_brackets(brackets: str) -> bool:

    brackets_map = {')': '(', '}': '{', ']': '['}
    for item in brackets:
        if item not in set(brackets_map.keys() | brackets_map.values()):
            raise ValueError('The sequence has unexpected elements')
        
    stack = Stack()
    for item in brackets:
        if item in brackets_map.values():
            stack.push(item)
        elif item in brackets_map.keys():
            if stack.is_empty() or stack.peek() != brackets_map[item]:
                return False
            else:
                stack.pop()
    if stack.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    
    expressions = [
        r'(((([{}]))))',
        r'[([])((([[[]]])))]{()}',
        r'{{[()]}}',
        r'}{}',
        r'{{[(])]}}',
        r'[[{())}]'
    ]

    try:
        for item in expressions:
            if check_balanced_brackets(item):
                print('Сбалансированно')
            else:
                print('Несбалансированно')
    except Exception as e:
        print('Error:', e)