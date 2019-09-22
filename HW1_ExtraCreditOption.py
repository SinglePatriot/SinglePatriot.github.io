#Aviral Malhotra's Homework Assignment

# Algorithm
# Let's start with an example
#Say I have 16 slices and 5 people. If one of them limits to 2 slices, there are 14 slices and 4 people remaining. 14/4=3.5 . So will allocate 3 slices for 2 people and 4 slices for 2 person.
# inputs - number of pizza slices, no. of people and number of people limited to 2 slices
# outputs - no of pizza slices per person in category 1, number of people in category 1, number of pizza slices per person in category 2, number of people in category 2
# So let's start coding, as i have a basic picture on what i have been given and what i need to find

total_people = int(input("How many people are sharing?"))
pizza = int(input("How many pizzas will be ordered?"))
limit = int(input("How many will limit themselves to two slices?"))
people = total_people - limit
total_slices =  pizza*8
slices = pizza*8 - limit*2 #slices represent the remaining slices to be distributed excluding the slices given to the people with a limit of 2 slices
divide = (slices/(people))
basic = int(divide)
number_of_pizza_slices_per_person_in_category_1 = basic
number_of_pizza_slices_per_person_in_category_2 = basic + 1

#total number of slices = (Number of people limited to 2 slices * 2 slices) + (number of people in category 1 * number of pizza slices per person in category 1) + (number of people in category 2 * number of pizza slices per person in category 2)
#For example, as mentioned in the 16 slices and 5 people case, 16 = 1*2 + 2*3 + 2*4
#Using the same formula, but with different variables, the variables are mentioned below assuming x as the number of people in category 1,

#total_slices = limit*2 + x*basic + (people-x)*(basic+1)    #This is the algorthm I made to calculate x
#rearranging the equation, to find out x
x= (total_slices - 2*limit - people*basic - people) / (-1)

number_of_people_in_category_1 = int(x)
number_of_people_in_category_2 = int(people - x)
#We have finally found all the output we need, now let's put it in the required interface
print("You will divide", total_slices, "slices --", limit, "will have 2,", number_of_people_in_category_1, "will have", number_of_pizza_slices_per_person_in_category_1, ", and", number_of_people_in_category_2, "will have", number_of_pizza_slices_per_person_in_category_2)
