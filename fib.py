
def fib_challenge(n):
    
    if n < 0:            
        return -1
    if n == 0 or n == 1:
        return n
                                          
    prev = 0                            
    current = 1
    for i in range(n-1):                
        next_num = (prev + current)     
        prev = current                  
        current = next_num
    
    return current  


print(fib_challenge(-20))
print(fib_challenge(0))
print(fib_challenge(10))             