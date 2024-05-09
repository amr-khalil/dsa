
def steps(n):
    """
        '*  '
        '** '
        '***'
    """
    for i in range(1, n+1):
        print(i*'*' + ((n-i) * ' '))
    
def steps_reverse(n):
    """
        '  *'
        ' **'
        '***'
    """
    for i in range(1, n+1):
        print(((n-i) * ' '  + i*'*'))



if __name__ == "__main__":
    steps(100)