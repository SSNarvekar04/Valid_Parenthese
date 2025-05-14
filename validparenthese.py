# Valid Parenthese 
def is_valid(s:str)->bool:
    stack =[]
    bracket={')':'(',
             '}':'{',
             ']':'['
             }
    for char in s:
        if char in bracket.values():   # for opening bracket
            stack.append(char)
        elif char in bracket:          # for closing bracket

            if not stack or stack [-1]!= bracket[char]:
                return False
            stack.pop()
        else:
            return False
        
    return len(stack)==0

s1="{[()]}"
print(is_valid(s1))
s2="{[(]}"
print(is_valid(s2))