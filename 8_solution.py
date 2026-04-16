# prime number 
# prime = [ 2,5,6,8,98,23]
# is_prime = True 
# for i in prime:
#     if i > 1:
#         for j in range(2, i):
#             if(prime % j) == 0:
#                 is_prime = False 
#                 break
    
    
number = 28
is_prime = True
if number > 1 :
    for i in range(2,number):
        if(number % i) == 0:
            is_prime = False 
            break
print(is_prime)        