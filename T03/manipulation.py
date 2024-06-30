#File manipulation.py for Auto-graded Task 1 on T03
'''
Begining of the pseudocode
Define variable str_manip and store the user input
Define variable len_str to store the length of the str_manip
Call method to display the result of len_str
Define variable last_str to store the last character
Call method to display the result of the str_manip with replacing the last_str with @
Define variable reverse_str3 to store the last three character in reversed order of str_manip
Define varaible extract_str to store the first 3 characters and last 2 characters from str_manip
Call method to display reverse_str3
Call method to display extract_str
End of pseudocode
'''
str_manip = input("Please enter the words:")
len_str = len(str_manip)
print("The length of the input:" + str(len_str))
#Grab last str by the index of the str_manip
last_str = str_manip[len_str-1:len_str]
#print("Last Str:[" + last_str + "][" + str(len(last_str)) + "]")
#Replace all matching last string with @
print("Replaced Str:" + str_manip.replace(last_str,"@"))
#Capture the reverved string until the position length of str_manip -4, i.e. position 3
reverse_str3 = str_manip[:len_str-4:-1]
print("Reversed Str:" + reverse_str3)
#Capture the position from 0 to 3 which is first 3 character, and length -2 to length , total 2 characters)
extract_str = str_manip[0:3] + str_manip[len_str-2:len_str:]
print("Extracted Str:" + extract_str)
                    
                
                  
