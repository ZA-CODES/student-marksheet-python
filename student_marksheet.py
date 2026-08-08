#PROJECT- STUDENTS MARK SHEET

#percentage
def percentage(a,b,c,d,e,):
    percent=((a+b+c+d+e)*100/500)
    print("percent:",percent,"%")

    
    
    if (percent>=90):
        print("first division")
        print("grade:A+")
    elif (percent>=80):
         print("second divison")
         print("grade:B+")
    elif (percent>=70):
           print("second division")
           print("grade:B")
    elif (percent>=40):
         print("third division")
         print("grade:C")
    else:
        print("fail")
#total numbers:
def total(a,b,c,d,e,):
     addition=((a+b+c+d+e))
     print("TOTAL:",addition)


subjects=("HINDI","ENGLISH","MATHS","PHYSICS","CHEMISTRY")


name=input("enter your name:")
rollno=input(("enter your roll number:"))
std=int(input("class:"))

std=int(input("class:"))
school=input("school name:")
a =int(input(f"{subjects[0]} :"))
while 0<a>100:
     print("invalid marks! marks should be between o and 100")
     a=int(input("marks again"))
b =int(input(f"{subjects[1]} :"))
while  0<b>100:
     print("invalid marks! marks should be between o and 100")
     a=int(input("marks again"))
c =int(input(f"{subjects[2]} :"))
while 0<c>100:
     print("invalid marks! marks should be between o and 100")
     a=int(input("marks again"))
d =int(input(f"{subjects[3]} :"))
while 0<d>100:
     print("invalid marks! marks should be between o and 100")
     a=int(input("marks again"))
e =int(input(f"{subjects[4]} :"))
while  0<e>100:
     print("invalid marks! marks should be between o and 100")
     a=int(input("marks again"))
print("=========score card========")
print("CGBSE RESULT OF 2025-26")
print("NAME :",name)
print("ROLL NUMBER :",rollno)
print("CLASS :",std)
print("SCHOOL :",school)
print(f"{subjects[0]}:{a}")
print(f"{subjects[1]}:{b}")
print(f"{subjects[2]}:{c}")
print(f"{subjects[3]}:{d}")
print(f"{subjects[4]}:{e}")
percentage(a,b,c,d,e)       
total(a,b,c,d,e)
print("class" ,std, "result 2026")
print("=========================")

