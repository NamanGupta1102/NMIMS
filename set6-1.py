#lex_auth_01269442114344550475

def is_palindrome(word):
    
    #Remove pass and write your logic here
    word = word.lower()
    n = len(word)
    for i in range(n//2):
        if word[i] != word[n-i-1]:
            return False
    return True
#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")