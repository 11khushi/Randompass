import random
import string
def rpassword():
    length=int(input("Enter your password length:"))
    lowerd=string.ascii_lowercase
    upperd=string.ascii_uppercase
    digitd=string.digits
    symbold=string.punctuation
    combine=lowerd+upperd+digitd+symbold
    x=random.sample(combine,length)
    password = "".join(x)
    print(password)
    rpassword()
rpassword()