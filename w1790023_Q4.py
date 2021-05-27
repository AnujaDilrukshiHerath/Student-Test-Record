#Anuja Dilrukshi Herath
#UoW ID:W1790023
#IIT ID:20191180
#Programming principle
#COURSE WORK PART 04

''' I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
    Any code taken from other sources is referenced within my code solution.
    Date:27-07-2020'''


passed = 0
failed = 0
defered = 0
pass_credits=[120,100,100,80,60,40,20,20,20,0]
defer_credits=[0,20,0,20,40,40,40,20,0,0]
fail_credits=[0,0,20,20,20,40,60,80,100,120]

x=1
y=1
z=1
a=1
count = 0


rangelist = [0,20,40,60,80,100,120]
user_choice= ""


print("-Student Progression Software-")
print("STAFF VERSION \n")

while (count <10):
    try:
        def progress_outcome(Pass,Defer,Fail):
            global x
            global y
            global z
            global a
            global count
            if (Pass + Defer + Fail == 120):
                if (Pass==120):
                    print("Progession Outcome: Progress \n")
                    x=x+1
                elif (Pass==100):
                    print("Progession Outcome: Progress- Module Trailer \n")
                    y=y+1
                elif (Fail >=80):
                    print("Progession Outcome: Exclude \n")
                    z=z+1
                else:
                    print("Progession Outcome: Do not Progress-Module Retriever \n")
                    a=a+1
                count+=1
            
        passed=pass_credits[count]
        defered=defer_credits[count]
        failed=fail_credits[count]
        progress_outcome(passed,defered,failed)
        
    except ValueError:
        print("Please enter an Integer")
        total = 120
    

print("-----------------------Data in Horizontal Histogram-----------------------\n")
print("Progress ", (x-1), ":", (x-1) * "*","\nTrailer  ", (y-1) , ":" , (y-1) * "*",
      "\nRetriever", (z-1) , ":" , (z-1) * "*","\nExcluded ", (a-1) , ":",(a-1) * "*")
Outcome_total= (x-1)+(y-1)+(z-1)+(a-1)
print (Outcome_total,"Outcomes in total. \n")

print("-----------------------Data in Vertical Histogram----------------------- \n")
###https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
header=["Progress","Module-Trailer","Excluded","Module-Retriever"]
print("    ".join(header))
for b in range(max(x,y,z,a)):
    print ("{0}      {1}      {2}      {3}".format(
        '  *   ' if b < (x-1) else "      ",
        '    *   ' if b < (y-1) else "        ",
        '      *   ' if b < (z-1) else "          ",
        '      *   ' if b < (a-1) else "    "
    ))
            
                        
print("------------------------Exit Program----------------------\n")
            
    

