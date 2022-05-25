#lex_auth_01269446157664256093

def check_prime(number):
    
    #remove pass and write your logic here. if the number is prime return true, else return false
    for i in range(2,number):
        if number%i == 0: return False
    return True

def rotations(num):
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
	num = str(num)
	li = [num]
	for i in range(1,len(num)):
	    li.append( li[i-1][1:] + li[i-1][0] )
	li = list(map(int,li))
	return li

def get_circular_prime_count(limit):
    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    c = 0
    for i in range(2,limit):
        r  = rotations(i)
        x = [ check_prime(i) for i in r]
        if False not in x: 
            # print(i)
            c+=1
    return c

#Provide different values for limit and test your program
print(get_circular_prime_count(100))
