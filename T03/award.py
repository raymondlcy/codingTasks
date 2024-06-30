#File award.py for Auto-graded Task 3 on T03
'''
Begining of the pseudocode
Define variable swimming and store the minutes for swimming section
Define variable cycling and store the minutes for cycling section
Define variable running and store the minutes for running section
Define variable total_time and calculate the result of the total for all section
if total_time <= 100
    award = Provinical colours
elseif total_time <= 105
    award = Provincial half colours
elseif total_time <= 110
    award = Provincial scroll
else
    award = No award
end if
End of pseudocode
'''
swimming    = int(input("Please enter the swimming result(minutes):"))
cycling     = int(input("Please enter the cycling result(minutes):"))
running     = int(input("Please enter the running result(minutes):"))
#Store the sum of all input
total_time = swimming + cycling + running
#Display the result of sum for three input
print("Overall time:" + str(total_time) + " minutes!")
if total_time <= 100: # less or equal to 100 mintues
    print("The participant will receive Provincial colours!")
elif total_time <= 105: # less or equal to 105 mintues but greater than 100
    print("The participant will receive Provincial half colours!")
elif total_time <= 110: # less or equal to 110 but greater than 105
    print("The participant will receive Provincial scroll!")
else: # greater than 110
    print("The participant will receive No award!")


                
                  
