#lex_auth_01269438947391897654

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)
list_of_marks = list(list_of_marks)
def find_more_than_average():
    a = sum(list_of_marks)/len(list_of_marks)
    c=0 
    for i in list_of_marks:
        if i>a: c+=1
    return 100*(c/len(list_of_marks))
    #Remove pass and write your logic here

def sort_marks():
    x = list(list_of_marks)
    x.sort()
    return x
    #Remove pass and write your logic here

def generate_frequency():
    ans = []
    for i in range(26):
        ans.append(list_of_marks.count(i))
    return ans
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())