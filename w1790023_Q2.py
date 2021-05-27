#Anuja Dilrukshi Herath
#UoW ID:W1790023
#IIT ID:20191180
#Programming Principle
#COURSE WORK PART 02

''' I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
    Any code taken from other sources is referenced within my code solution.
    Date:24-07-2020'''

pr = 0      #Progresscount
pmt = 0     #Trailingcount
dnpmr = 0   #Retrievercount
e = 0       #Excludedcount

print("-Student Progression Software-")
print("STUDENT VERSION \n")

while True :
    try :
        
        pass_value = int(input('Enter the pass credit : '))    #pass_value is pass credit
        if pass_value not in range(0,130,20):  
            print('Range error')    #outcome 'Range Error'.             
            continue
        
        defer_value = int(input('Enter the defer credit : '))  #defer_value is defer credit
        if defer_value not in range(0,130,20): 
            print('Range error')    #outcome 'Range Error'.
            continue
        
        fail_value = int(input('Enter the fail credit : '))    #fail_value is fail credit
        if fail_value not in range(0,130,20): 
            print('Range error')    #outcome 'Range Error'.
            continue
        
        if pass_value+defer_value+fail_value != 120 :
            print('Total Error')    #outcome 'Total Error'. 
        else :
            if pass_value==120 :
                print('Progress')                         #output 'Progress count'
                pr += 1
                
            if pass_value==100 and (defer_value==20 or fail_value==20) :
                print('Progress-module Trailer')          #output 'Progress-module Trailer count'
                pmt += 1
                
            if (pass_value==80 or pass_value==60 or pass_value==40 or pass_value==20 or pass_value==0) and (defer_value==120 or defer_value==100 or defer_value==80 or defer_value==60 or defer_value==40 or defer_value==20 or defer_value==0) and (fail_value==60 or fail_value==40 or fail_value==20 or fail_value==0):    
                print('Do not progress module retriever') #output 'Do not progress module retriever count'
                dnpmr += 1
                
            if (pass_value==40 or pass_value==20 or pass_value==0) and (defer_value==40 or defer_value==20 or defer_value==0) and (fail_value==120 or fail_value==100 or fail_value==80) :
                print('Exclude')                          #output 'Exclude count'
                e += 1
            proceed = input("If you want to quit press 'q' : ")
            if proceed == 'q' :
                break
        
    except :
        print('Integer Required')   #outcome 'Integer Required'.

print('Progress count',pr,': '+'*'*pr)
print('Trailing count',pmt,': '+'*'*pmt)
print('Retriever count',dnpmr,': '+'*'*dnpmr)
print('Excluded count',e,': '+'*'*e)
print(pr+pmt+dnpmr+e,'outcomes in Total.')
        
