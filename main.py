import string
import random

if __name__ == "__main__":
    #string 1
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)

    # get length of password from user
    password_length = int(input("Enter password length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)

    # shuffle elemnt of list
    # random.shuffle(s)
    

    print("your password is : ")
    print("".join(random.sample(s,password_length)))
    # print("".join(s[0:plen]))



