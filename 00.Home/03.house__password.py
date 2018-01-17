import re
def house_password():
    password= input('please input the password:')
    m=re.findall('[a-z]',password)
    n=re.findall('[A-Z]',password)
    q=re.findall('[0-9]',password)
    if (10<=len(password)<=64) and (len(m) and len(n) and len(q)) :
        return True
    else:
        return False

print(house_password())
