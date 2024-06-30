#File numbers.py for Auto-graded Task 2 on T03
'''
Begining of the pseudocode
Define variable num1 and store the first input integer
Define variable num2 and store the second input integer
Define variable num3 and store the third input integer
Call method to display the sum of three integers
Call method to display the result of num1 - num2
Call method to display the result of num3 X num1
Call method to display the result of sum of all interger and divied by num3
End of pseudocode
'''
num1 = int(input("Please enter the first integer:"))
num2 = int(input("Please enter the second integer:"))
num3 = int(input("Please enter the third integer:"))
#Store the sum of all input
total_num = num1 + num2 + num3
#Display the result of sum for three input
print("Sum of three integers=" + str(total_num))
#Display the result of num1 - num2
print("First integer minus Second integer=" + str(num1-num2))
#Display the result of num1 * num3
print("Third integer multiply by First integer=" + str(num3*num1))
#Display the result of num1 - num2
print("Sum of three integers divided by Third integer " + str((total_num)/num3))


                
                  
