# SearchEverythingPro.py
#A python script to search a file for the user input


#Return the previous, current and next line of the searched input


#Write the current line into a new file.



# Requirements
#The file to be searched must be provided by the user


#The file to which the result is to be stores must also be provided by the user


#By default I have provided a RESULT file and TWO LOG FILES


#MAKE SURE TO PLACE THE FILES IN THE SAME FOLDER AS THE PYTHON SCRIPT

-----------------------------------------------------------------------------------------------

#CURRENTLY DESIGNED FOR LOG FILES, 

HENCE IF THE FILE CONTAINS REPEATED LINES,

THEN PREVIOUS LINES/AFTER LINES MAY NOT BE ACCURATE.

SINCE LOG FILES DEALS WITH TIME AND DATE,

ITS ASSUMED THAT EVERY LINE WILL HAVE

SOME CHANGE IN IT.

-------------------------------------------------------------------------------------------------

#EITHER WAY THE CURRENT LINE i.e THE LINE WHICH

CONTAINS THE USER INPUT IS ASSURED TO BE RETURNED

AND WRITTEN INTO A NEW FILE

-------------------------------------------------------------------------------------------------




# Usecase
#Suppose you work for a company and a server fails for a particular time
 and fixes itself back to normal
 
 
#You are asked to find when exactly the server failed and hence you are
 provided with the server log files
 
 
#The server logfiles shows an "ERROR" keyword whenever the server failed
 so your job is basically to find all those lines
 
 
#But the logfile contains Thousands of lines and its pretty much impossibble
 to look for each of the ERROR keywords
 
 
#In such situations SeRitchEverything helps you to find the ERROR keyword 
 in the file, retrieve its entire line, also retrieve its previous and next lines
 for further clarification on what happened before and after the server failed
 
 
#Finally the result i.e the entire line of the searched input is written into 
 a new file.
 
 
 enjoy :)
  



