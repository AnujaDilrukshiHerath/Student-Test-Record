#Anuja Dilrukshi Herath
#UoW ID:W1790023
#IIT ID:20191180
#Programming principle
#COURSE WORK PART 03

''' I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
    Any code taken from other sources is referenced within my code solution.
    Date:26-07-2020'''

rangelist = [0,20,40,60,80,100,120]
user_choice= ""
x=1
y=1
z=1
a=1
print("-Student Progression Software-")
print("STAFF VERSION \n")
while (user_choice!="q"):
    
    try:
        
        def progress_outcome(Pass,Defer,Fail):
            global x
            global y
            global z
            global a
            
            if (Pass in rangelist and  Defer in rangelist and Fail in rangelist):
                if (Pass + Defer + Fail == 120):
                    if Pass==120:
                        print("Progress")
                        x=x+1
                    elif Pass==100:
                        print("Progress- Module Trailer")
                        y=y+1
                    elif Fail>=80:
                        print("Exclude")
                        z=z+1
                    else:
                        print("Do not Progress-Module Retriever")
                        a=a+1
                else:
                    print("Total Incorrect")
            else:
                print("Range Error")
        pass_credits=int(input("Enter Pass Credits:"))
        defer_credits=int(input("Enter Defer Credits:"))
        fail_credits=int(input("Enter Fail Credits:"))
        progress_outcome(pass_credits,defer_credits,fail_credits)
    except ValueError:
        print("Please enter an Integer")

    prompt= str(input("enter q to quit:"))
    if (prompt=="q"):
        print("-----------------------Data in Vertical Histogram----------------------- \n")
        header=["Progress","Module-Trailer","Excluded","Module-Retriever"]
        print("    ".join(header))
        for b in range(max(x,y,z,a)):
            print ("{0}      {1}      {2}      {3}".format(
                '  *   ' if b < (x-1) else "      ",
                '    *   ' if b < (y-1) else "        ",
                '      *   ' if b < (z-1) else "          ",
                '      *   ' if b < (a-1) else "    "
            ))
        break

        print("------------------------Exit Program----------------------\n")
                        

            
    
