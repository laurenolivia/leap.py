
def leap_challenge(n):
    
    if n < 0:            
        return -1
    if n == 0 or n == 1:
        return n
                                        #begins by summing 0, 1    
    prev = 0                            #applying concept of singly linked list with prev == head
    current = 1
    for i in range(n-1):                #iterate through n-1 to return what last value would be, rather than executing calculation on the last value
        next_num = (prev + current)     
        prev = current                  
        current = next_num
    return current  

print(leap_challenge(-20))
print(leap_challenge(0))
print(leap_challenge(10))             