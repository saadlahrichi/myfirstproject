def fun():
    choice = "yes"
    e=[]
    while choice.lower() == "yes":
        g=eval(input("Please enter a new grade: "))
        e.append(g)
        if len(e)==1:
            print("You entered ",len(e), "grade.")
        else:
            print("You entered ",len(e), "grade(s).")
            choice = input("Do you want to add another grade? yes/no ")
            print("The average is ",  (sum(e)/len(e)))

    

def function():
    s=0
    n=0
    g=0
    g=input("Please enter a new grade: ")
    while g!="":
        g=eval(input("Please enter a new grade: "))
        if g>=0:
            s=s+g
            n=n+1
        else:
            print("You entered an incorrect value")
    print("The average is ",  s/n)
    
