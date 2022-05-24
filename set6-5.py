#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    
    #Remove pass and write your logic here
    x = [int(i) for i in num_str]
    ans = []
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            if sum(x[i:j+1]) ==10:
                s = ""
                for y in x[i:j+1]: s+=str(y)
                ans.append(s)
            elif sum(x[i:j])>10: break
    return ans
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)