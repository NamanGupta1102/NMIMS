#lex_auth_01269441810970214471

def check_double(number):
    n = []
    d = []
    n[:0]= str(number)
    d[:0] = str(number*2)
    d = [int(i) for i in d]
    n = [int(i) for i in n]
    d.sort()
    n.sort()
    return d==n
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(125874))