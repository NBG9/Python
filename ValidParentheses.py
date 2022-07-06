def validParentheses(string):

    if len(string) %2 != 0:
        return False

    stack = []
    dict = {
        ']': '[',
        '}': '{',
        ')': '('
    }

    for i in string:
        if i in dict:
            if stack and stack[-1] == dict[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    return len(stack) == 0

# Test case 1
print(validParentheses('()[]'))

# Sample Output --> True

# Test case 2
print(validParentheses('()]'))

# Sample Output --> False
