def fun():
    choice = "yes"
    e=[]
    while choice.lower() == "yes":
        g=eval(input("Please enter a new grade: "))
        e.append(g)
        if len(e)==1:
            print("You entered ",len(e), "grade.")
        else:
            print("You entered ",len(e), "grades.")
            choice = input("Do you want to add another grade? yes/no ")
            print("The average is ",  (sum(e)/len(e)))

    

def function():
    s=0
    n=0
    g=0
    while g!=-1:
        g=eval(input("Please enter a new grade: "))
        s=s+g
        n=n+1
    print("The average is ",  s/n)

    
