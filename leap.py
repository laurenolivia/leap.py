
def leap_challenge(n):
    
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



print(leap_challenge(-20))
print(leap_challenge(0))
print(leap_challenge(10))             