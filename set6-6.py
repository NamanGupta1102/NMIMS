#lex_auth_01269443477535129681

def find_duplicates(list_of_numbers):
    x = set()
    for i in range(len(list_of_numbers)-1):
        if list_of_numbers[i] in list_of_numbers[i+1:]:
            x.add(list_of_numbers[i])
    return list(x)
    
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)