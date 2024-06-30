#File pattern.py for Practical Task 2 on T04
'''
Begining of the pseudocode

Define variable max to store the maximum count to 10

Create for loop from 1 to 10
    if count <= half of max (5)
        display * accordingly to count
    else
        display * accordingly to maximum - count


End of pseudocode
'''

max =10
for i in range (1,max):
    if i <= max/2:
        print("*"*i)
    else:
        print("*" * (max-i))


