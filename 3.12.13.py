car_value = 30000
purchase_year = 2018
car_age = 2
driver_age = 32
electric = True
emissions_passed = False

#You're writing some code to determine how much it will cost
#to renew the tag on your license plate. Why? Because I just
#had to pay my tag renewal, and if I have to deal with this
#mess, so do you. 😛
#
#Georgia's tag renewal policies are unnecessarily
#complicated. I've simplified them to make this problem even
#doable. They are:
#
# - Everyone pays $20.
# - If you purchased your car before 2013 (in 2012 or earlier),
#   you also pay 1% of its current value in additional tax.
# - If the car is electric, you pay an additional $200 fee.
#   (This is real.)
# - To renew, you must have passed an annual emissions check,
#   unless your car is electric, or if you're 65 or over and
#   the car's age is 10 years or older.
#
#Your code should print one of two messages. If the person
#needs to pass an emissions test in order to renew their tag,
#it should print, "You must pass an emissions test first."
#This would be the message to print if emissions_passed is
#False and if they are not eligible for either exemption
#mentioned above.
#
#If the person is eligible to renew their tag, the code should
#print: "Your renewal fee is $__.", where __ is the renewal
#cost. Round the renewal fee to the nearest integer. This will
#be $20, plus $200 if the car is electric, plus 1% of car_value
#if the purchase_year is less than or equal to 2012.


base_cost = 20

if purchase_year <= 2012:
    old_car_tax = .01*car_value
else:
    old_car_tax = 0

if electric == True:
    electric_cost = 200
else:
    electric_cost = 0


tag_cost = base_cost + old_car_tax + electric_cost


if (driver_age >= 65 and car_age >= 10) or electric == True:
    emissions_passed_needed = False
else:
    emissions_passed_needed = True 

if emissions_passed_needed == True and emissions_passed == False:
    message = "You must pass an emissions test first."
else:
    message = "Your renewal fee is $"+str(tag_cost) + "."


print(message)
    
