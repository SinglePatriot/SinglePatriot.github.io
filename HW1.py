# Algorithm
# Let's start with an example
#Say I have 16 slices and 3 people. 16/3=5.33. So will allocate 5 slices for 2 people and 6 slices for 1 person.
# inputs - number of pizza slices, no. of people
# outputs - no of pizza slices per person in category 1, number of people in category 1, number of pizza slices per person in category 2, number of people in category 2
# So let's start coding, as i have a basic picture on what i have been given and what i need to find

people = int(input("How many people are sharing?"))
pizza = int(input("How many pizzas will be ordered?"))
slices = pizza*8
divide = (slices/people)
basic = int(divide)
number_of_pizza_slices_per_person_in_category_1 = basic
number_of_pizza_slices_per_person_in_category_2 = basic + 1

#total number of slices = (number of people in category 1 * number of pizza slices per person in category 1) + (number of people in category 2 * number of pizza slices per person in category 2)
#For example, as mentioned in the 16 slices and 3 people case, 16 = 5*2 + 6*1
#Using the same formula, but with different variables, the variables are mentioned below assuming x as the number of people in category 1,

#slices = basic * x + (basic+1) * (people - x)
#rearranging the equation, to find out x
x= ((slices - (people * basic) - people) / (-1))

number_of_people_in_category_1 = int(x)
number_of_people_in_category_2 = int(people - x)
#We have finally found all the output we need, now let's put it in the required interface
print("You will divide", slices, "slices --", number_of_people_in_category_1, "will have", number_of_pizza_slices_per_person_in_category_1, "and", number_of_people_in_category_2, "will have", number_of_pizza_slices_per_person_in_category_2)
