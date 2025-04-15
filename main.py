class Stack:

    def __init__(self, list_: list = []):
        self.stack = list_

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    

def check_balanced_brackets(brackets: str) -> str:

    brackets_map = {')': '(', '}': '{', ']': '['}
    for item in brackets:
        if item not in [item for pair in brackets_map.items() for item in pair]:
            raise ValueError('The sequence has unexpected elements')
        
    stack = Stack()
    for item in brackets:
        if item in brackets_map.values():
            stack.push(item)
        elif item in brackets_map.keys():
            if stack.is_empty() or stack.peek() != brackets_map[item]:
                return 'Несбалансированно'
            else:
                stack.pop()
    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'
        

if __name__ == "__main__":
    
    expression_1 = r'(((([{}]))))'
    expression_2 = r'[([])((([[[]]])))]{()}'
    expression_3 = r'{{[()]}}'
    expression_4 = r'}{}'
    expression_5 = r'{{[(])]}}'
    expression_6 = r'[[{())}]'

    try:
        print(check_balanced_brackets(expression_1))
        print(check_balanced_brackets(expression_2))
        print(check_balanced_brackets(expression_3))
        print(check_balanced_brackets(expression_4))
        print(check_balanced_brackets(expression_5))
        print(check_balanced_brackets(expression_6))
    except Exception as e:
        print('Error:', e)