# Valid parentheses

def valid_parentheses(string):
    stack=[]
    for i in string:
        if i in ['[','{','(']:
            stack.append(i)
        else:
            if(len(stack)==0):
                return False
            if(i==']'):
                if(stack[-1]!='['):
                    return False
                else:
                    stack.pop()
            elif(i=='}'):
                if(stack[-1]!='{'):
                    return False
                else:
                    stack.pop()
            elif(i==')'):
                if(stack[-1]!='('):
                    return False
                else:
                    stack.pop()
    if(len(stack)!=0):
        return False
    return True

#test cases
print(valid_parentheses("()"))
print(valid_parentheses("({(}))"))