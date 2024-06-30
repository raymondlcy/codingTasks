
#File dob_task.py for Practical Task 1 on T08
#Define name and dob list to store the input
#DOB.txt 
#First line contains name with seperator "|"
#Second line contains DOB with seperator "|"
firstName = []
lastName = []
days = []
months = []
years = []

with open('DOB.txt', 'r') as fileInput:
    #readIns = fileInput.readlines()

    for readIns in fileInput.readlines():
        # split the input by seperator space
        readIn = readIns.split(' ') 
        # create list to store the value of First name, Last name, day / month / year of birthday with stripping unnecessary spacing characters
        firstName.append(readIn[0].strip())
        lastName.append(readIn[1].strip())
        days.append(readIn[2].strip())
        months.append(readIn[3].strip())
        years.append(readIn[4].strip())
    
# print name section
print("Name")
for i in range((len(firstName))):
    strOut = firstName[i] + " " + lastName[i]
    print(strOut)

# print DOB section with newline
print("")
print("Birthdate")

for i in range((len(days))):
    strOut = days[i] + " " + months[i] + " " + years[i] 
    print(strOut)