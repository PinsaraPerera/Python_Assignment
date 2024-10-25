class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
def string_balance_check(string):

    """
    A string is balance if it has equal number of opening and closing parenthesis. Thats what this function checks.
    """
    
    stack = Stack()

    for character in string:
        if character == "(":
            stack.push(character)
        elif character == ")":
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()

string1 = "((()))"
string2 = "(()"
string3 = "())"
string4 = "()()"
string5 = "((()())())"

print(string_balance_check(string1))
print(string_balance_check(string2))
print(string_balance_check(string3))
print(string_balance_check(string4))
print(string_balance_check(string5))
