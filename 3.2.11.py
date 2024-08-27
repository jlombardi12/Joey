cut = "Emerald"
clarity = "VS"
color = "E"
carat = 1.1
budget = 500
preferred_cuts = ["Emerald", "Cushion", "Princess", "Oval"]
base_cost = 0 # creating variable
clarity_dict = {
 "IF": 16,
  "VVS": 8,
  "VS": 4,
  "SI": 2,
  "I": 1
}
color_coff = (ord("D") - ord(color))*-.02

color_cost = 100 - (100*color_coff) 


clarity_coff = clarity_dict[clarity]

clarity_cost = color_cost * clarity_coff

final_price = clarity_cost * carat
#Diamonds are typically evaluated according to four aspects:
# - Cut: The way the diamond is cut
# - Clarity: How clear or flawless the diamond is, rated
#   as F (the best), IF, VVS, VS, SI, or I (the worst)
# - Color: How colorless the diamond is, rated from "D" (the
#   best) to "Z" (the worst)
# - Carat: How large the diamond is, weighed in carats


#Imagine you're shopping for a diamond. You have your
#preferred cuts, and you have a budget in mind. You're shown
#a diamond whose characteristics are represented by the cut,
#color, clarity, and carat variables above. You'll buy the
#diamond if its cost is less than your budget, and if its
#cut is one of your preferred cuts.
#
#At this store, every diamond has a base cost of 100.
#
#For every color rating worse than "D", the cost decreases by
#2%. An "F" color diamond would be worth 0.96 * the diamond
#cost otherwise because "F" is two colors worse than "D".
#
#A diamond's value is doubled for every level of clarity above
#I. A "VVS"-clarity diamond is worth 8 * the diamond cost
#otherwise because "VVS" is three levels higher than I, and
#doubling its value three times raises its value by 8x total.
#
#After finding its price based on color and clarity, its price
#is multiplied by its weight in carats.
#
#Your program should print "I'll take it!" if you will buy the
#diamond, "No thanks" if you will not. To purchase it, its price
#must be less than your budget and its cut must be one of your
#preferred cuts.
#
#HINT: You can find the number of characters between two
#characters by using the ord() function. ord("E") - ord("D")
#is 1; ord("Z") - ord("D") is 22.
#
#HINT 2: We haven't covered lists, but we did cover how to
#see if an item is present in a list using the 'in' operator
#in chapter 2.3.
print(color_cost)
print(clarity_cost)
print(final_price)


if final_price > budget or cut not in preferred_cuts:
    print("No thanks")
elif final_price <= budget and cut in preferred_cuts:
    print("I'll take it!")