def Conversion(expression):
    operators = ['+','-','/','*','(',')','^']
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
    stack = []
    output = ''
    for char in  expression:
        if char not in operators:
            output += char
        elif char == '(':
            stack.append('(')
        elif char == ')':
            while stack and stack[-1]!= '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!= '(' and precedence[char]<= precedence[stack[-1]]:
                output+=stack.pop()
            stack.append(char)
    while stack:
        output+= stack.pop()
    return output

test = 'a+b*(c^d-e)^(f+g*h)-i'
print(Conversion(test))