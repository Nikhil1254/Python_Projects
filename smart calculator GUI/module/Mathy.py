responses=["My name is JARVIS.","Thanks","Sorry,this is beyond my ability."]

def extract_numbers_from_text(text):
    l=[]
    for t in text.split():
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def myname():
    return(responses[0])

def sorry():
    return(responses[2])

operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"SUBTRACT":sub,"MINUS":sub,"SUBTRACTION":sub,
            "MULTIPLICATION":multiply,"MULTIPLY":multiply,"DIVISION":divide,"DIVIDE":divide,
            "LCM":lcm,"HCF":hcf}

commands={"NAME":myname}
