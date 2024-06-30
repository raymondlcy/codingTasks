#File holiday.py for Practical Task 1 on T06
#Function for calculate flight cost according to cities
def plane_cost(city_flights):
    price = 0
    #Default have four cities with selected price, other cities will cost 1000
    if city_flights == "Manchester":
        price = 20
    elif city_flights == "Paris":
        price = 30
    elif city_flights == "Rome":
        price = 40
    elif city_flights == "Tokyo":
        price = 600
    else :
        price = 1000
    return price

#Function for calculate hotel cost, default 150 per night
def hotel_cost(num_nights):
    pricePerNight = 150
    return num_nights * pricePerNight

#Function for calculate car rental cost, default 100 per day
def car_rental(rental_days):
    rent_per_day = 100
    return rental_days * rent_per_day

# Function for hinting cities option for user input
def cityOptions():
    print("Please choose your city of travel:")
    print("Manchester - $20")
    print("Paris - $30")
    print("Rome - $40")
    print("Tokyo - $600")
    print("Others - $1000")

#Function for adding flight cost, hotel cost and car rental
def holiday_cost(cityChoice,num_nights,rental_days):
    return plane_cost(cityChoice) + hotel_cost(num_nights) + car_rental(rental_days)

    
# Get input from user and calculate chosen shape
cityOptions()
cityChoice = input("Please enter your choice:")
numNights = int(input("Please enter number of days for staying in hotel - $150 per night:"))
rentalDays = int(input("Please enter number of days for hiring car - $100 per day:"))
#Display the detailed breakdown of all cost
print(f"Flight to {cityChoice} = ${str(plane_cost(cityChoice))}")
print(f"Staying {str(numNights)} nights in Hotal = ${str(hotel_cost(numNights))}")
print(f"Hiring {str(rentalDays)} days of car = ${str(car_rental(rentalDays))}")
#Display the total cost 
print(f"Total cost of the holiday = ${str(holiday_cost(cityChoice,numNights,rentalDays))}") 
    