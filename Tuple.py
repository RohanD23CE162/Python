
### Exercises: Level 1

empty_tuple = ()
sisters = ('Alice', 'Bob')
brothers = ('Charlie', 'David')
siblings = brothers + sisters
num_siblings = len(siblings)
family_members = ('Father', 'Mother') + siblings
print("Number of siblings:", num_siblings)
print("Family members:", family_members)

### Exercises: Level 2
father, mother, *rest_siblings = family_members
print("Unpacked siblings and parents:", father, mother, rest_siblings)

fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Broccoli', 'Spinach')
animal_products = ('Chicken', 'Beef', 'Milk')

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
middle_index = len(food_stuff_tp) 
middle_item = food_stuff_tp[middle_index]
print("Middle item:", middle_item)

first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("First three items:", first_three_items)
print("Last three items:", last_three_items)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

estonia_nordic = 'Estonia' in nordic_countries
print("Is 'Estonia' a Nordic country?", estonia_nordic)

iceland_nordic = 'Iceland' in nordic_countries
print("Is 'Iceland' a Nordic country?", iceland_nordic)
