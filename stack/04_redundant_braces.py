def redundant_braces(string) -> bool:
    """count redundant braces"""
    stack = []
    
    for ch in string:
        if ch == ')':
            count = 0
            while stack[-1] != '(':
                popped = stack.pop()
                if popped in ['+', '-', '*', '/']:
                    count += 1
            stack.pop()
            if count == 0:
                return 1
        else:
            stack.append(ch)
    
    return 0                
        
        
if __name__ == "__main__":
    print(redundant_braces("(a + (a+b))")) # 0
    print(redundant_braces("((a*b)+(c+d))")) # 0
    print(redundant_braces("((a+b))")) # 1