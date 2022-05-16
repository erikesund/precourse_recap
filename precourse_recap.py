from functools import total_ordering


price_of_sauce = 90
price_of_spaghetti = 50
price_of_herbs = 20

dish_cost_pence = price_of_herbs + price_of_sauce + price_of_spaghetti
cost_in_pounds = dish_cost_pence / 100

print("One meal will cost £" + str(cost_in_pounds) + " to make.")

num_of_diners = input("How many people will be eating tonight?\n")
total_cost = cost_in_pounds * int(num_of_diners)

print("Thank you, the total food cost for tonight will be £" + str(total_cost) +".")

