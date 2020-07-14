
#SearchEverythingPro.py
#Python Script to search a file | return its current, previous and next line | write the obtained result i.e the current line into a new file.

while True:
    fname1 = input("Enter Original File Name : ")    #File Name 1 which contains the data to be SEARCHED.    
    fname2 = input("Enter New File Name : ")    #File Name 2 in which you are going to store the RESULTS



    try:
        file1 = open(fname1)        #Open File1   
        file2 = open(fname2, "w")   #Open File2
    except:
        file1 = open(fname1+".txt")
        file2 = open(fname2+".txt", "w")
    
    





    lst = [] #List to store the lines of the file as elements
    a = input("Enter the Text : ") #User Input
    x = 0 #Line Counter





    #Loop to read the entire file
    #and store the lines of the file
    #as elements in the list
    #Also to find the length of the resultant List
    #Which is the Total number of lines in the File
    for k in file1:
        lst.append(k)
    list_length = len(lst)

    




    #Main Loop
    for i in lst:
        x=x+1 #Line Counter starts to count
    
        if(i.find(a)!=-1): #To check if user input exists in the line
            ind = lst.index(i)  #To find the index of the line in the list
            before=ind-1 #To print previous line
            after=ind+1 #To print after line


        

        
            print("---------------------------------------------------------------------------------------------------")
            print("***** Match found at line ",x,"*****")
            print(" ")
            print(" ")
            print("*****Writing it to new file*****")
            print(" ")
            print(" ")

        

        
            if not before ==-1: #to check If the index of previous line is -ve
                print("Previous Line : ", lst[ind-1])
                print(" ")
                print(" ")
            if before == -1:
                print("No Previous Line")


            

            
            print(" ")
            print(" ")
            print("Current Line : ", lst[ind])
            print(" ")
            print(" ")


        

        
            if after<list_length:   #to check If the index of after line is out of range in list
                print("After Line : ", lst[ind+1])
                print("-------------------------------------------------------------------------------------------------")
                print(" ")
                print(" ")
            if not after<list_length:
                print("End Of Line")
                print(" ")
                print(" ")


            

            file2.write(i) #to write the results into a new file
        
        
        else:   #in case no match
            print("No match in line ",x)
            print(" ")
            print(" ")

            continue
    
    
    




    #to close both the file
    file1.close()
    file2.close()





    #TO QUIT THE TERMINAL
    print("END OF THE SCRIPT, OPEN YOUR RESULT FILE TO FIND THE RESULTS")
    print(" ")
    print(" ")
    print("Enter 0 to QUIT THE TERMINAL")
    print(" ")
    print(" ")
    print("Enter 1 to CONTINUE")
    print(" ")
    print(" ")
    quitt = int(input())
    if quitt == 0:
        quit()
    elif quitt == 1:
        continue
    else:
        print("INVALID INPUT!")
        print(" ")
        print(" ")
        print("ABORTING...")
        quit()

    
