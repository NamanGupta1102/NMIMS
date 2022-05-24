#lex_auth_012694465248329728100

def validate_name(name):
    if len(name)<1 or len(name)>15: return False
    for i in name:
        if not i.isalpha(): return False
    
    return True
    #Start writing your code here

def validate_phone_no(phno):
    x = set(phno)
    if len(x) == 1: return False
    if len(phno) != 10: return False
    for i in phno:
        if not i.isdigit(): return False
    return True
    #Start writing your code here

def validate_email_id(email_id):
    #Start writing your code here
    if email_id[-4:] != '.com': 
        # print("com")
        return False
    if email_id.count('.com') !=1: return False
    x = email_id.split('@')
    if len(x) !=2: return False
    # print(x[1])
    if not( x[1][:-4] == 'gmail' or x[1][:-4] == 'yahoo' or x[1][:-4] == 'hotmail'):
        # print("domain")
        return False
    return True
def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    x =0 
    if not validate_name(name):
        x+=1 
        print("Invalid Name")
    if not validate_phone_no(phone_no):
        x+=1 
        print("Invalid phone number")
    if not validate_email_id(email_id):
        x+=1 
        print("Invalid email id")
    if x == 0: print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")