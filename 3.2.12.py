phase = "Full"
distance = 228000
date = 31
eclipse = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#There are (at least) three special types of full moons:
#
# - Super Moon: the full moon occurs when the moon is at its
#   closest approach to earth (less than 230,000km away).
# - Blue Moon: the second full moon in a calendar month. In
#   other words, any full moon on the 29th, 30th, or 31st of
#   a month.
# - Blood Moon: a lunar eclipse during a full moon.
#
#Write a program that will print out the type of moon --
#"Full Moon", "Super Moon", "Blue Moon", "Blood Moon", based
#on the values of the variables above. Note that for the moon
#to be any of these special kinds of moons, it must also be
#full.
#
#Note, though, that multiple modifiers can be true at the same
#time. We could have a Super Blue Moon, a Blue Blood Moon, or
#even a Super Blue Blood Moon.
#
#Always print those modifiers in that order. If any of these
#special modifiers is present, do not include the word "Full".
#If none of them are present, but the moon is Full, then print
#"Full Moon". If none of them are present at all, print "Moon".

if distance < 230000 and phase == "Full":
    super_moon = True
else:
    super_moon = False

if date in (29,30,31)and phase == "Full":
    blue_moon = True
else:
    blue_moon = False


if phase == "Full" and eclipse == True:
    blood_moon = True
else: 
    blood_moon = False


if phase != "Full" and super_moon == False and blue_moon == False and blood_moon == False:
    print_out = "Moon"
elif phase == "Full" and super_moon == False and blue_moon == False and blood_moon == False:
    print_out = "Full Moon"
elif super_moon == True and blue_moon == False and blood_moon == False:
    print_out = "Super Moon"
elif super_moon == True and blue_moon == True and blood_moon == False:
    print_out = "Super Blue Moon"
elif super_moon == True and blue_moon == True and blood_moon == True:
    print_out = "Super Blue Blood Moon"
elif super_moon == False and blue_moon == True and blood_moon == False:
    print_out = "Blue Moon"
elif super_moon == False and blue_moon == True and blood_moon == True:
    print_out = "Blue Blood Moon"
elif super_moon == True and blue_moon == False and blood_moon == True:
    print_out = "Super Blood Moon"
elif super_moon == False and blue_moon == False and blood_moon == True:
    print_out = "Blood Moon"

print(print_out)