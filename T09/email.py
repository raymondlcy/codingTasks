# This is for Auto-graded task of T09

### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
class Email():
    
    
    # Initialise the instance variables for emails.

    def _init_(self, email_address,subject_line,email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
emails = []
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    emails.extend(Email("user1@gmail.com", "Welcome to HyperionDev!","This is the first email for testing"))
    emails.extend(Email("user2@gmail.com", "Greate work on the bootcamp!","This is the second email for testing"))
    emails.extend(Email("user3@gmail.com", "Your excellent marks","This is the third email for testing"))

def list_emails():
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    print("Indox:")
    for i, email in enumerate(Email.emails):
        print(f"{i}.{email.subject_line}")

def read_email(index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    if len(Email.emails) >= index >= 0:
        email = Email.emails[index]
        print(f"From:{email.email_address}")
        print(f"Subject:{email.subject_line}")
        print(f"Content:{email.email_content}")
        email.mark_as_read()
        print(f"Email{index} marked as read!")
    else:
        print("Invalid Email number!")
# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        
    elif user_choice == 2:
        # add logic here to view unread emails
            
    elif user_choice == 3:
        # add logic here to quit appplication

    else:
        print("Oops - incorrect input.")

