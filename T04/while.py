#File while.py for Practical Task 1 on T04
'''
Begining of the pseudocode

Define variable user_input and set to empty
Define variable sum to calculate the sum of all input
Define variable count for counting the number of input

Create while loop with condition user_input not equal to "-1"
    Create input prompt to collect integer
        if user_input != "-1"
            add integer value to sum
            add 1 to count
        else
            break
    end loop
    print Average amount =sum divide by count , if count > 0 


End of pseudocode
'''

user_input = ""     #Empty variable user_input to enable must enter the loop
sum = 0             #Preset sum to zero
count = 0           #Preset count to zero
while user_input != "-1":   #Stay in loop when user_input not equal to "-1"" 
    user_input = input("Please enter an integer:")  #Get user input 
    if user_input != "-1":                          #State action for input not equal to "-1"
        sum += int(user_input)                      #Add value to Sum
        count += 1                                  #Add 1 to count
    else:
        break                                       #break if input equal "-1"
#print(f"Sum:{str(sum)}")
#print(f"Count:{str(count)}")
if count > 0:
    print(f"Average:" + str(sum/count))
else:
    print("Average:" + str(count))
                  
