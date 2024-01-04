### Exercises: Level 1 

empty_list = []

list_with_items = [1, 2, 3, 4, 5, 6]

list_length = len(list_with_items)

first_item = list_with_items[0]
middle_item = list_with_items[len(list_with_items) // 2]
last_item = list_with_items[-1]

mixed_data_types = ['John', 25, 175, 'Single', '123 Main Street']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print("IT Companies:", it_companies)

num_companies = len(it_companies)
print("Number of IT Companies:", num_companies)

print("First Company:", it_companies[0])
print("Middle Company:", it_companies[len(it_companies) // 2])
print("Last Company:", it_companies[-1])

it_companies[1] = 'NewCompany'
print("Modified IT Companies:", it_companies)

it_companies.append('Intel')

it_companies.insert(len(it_companies) // 2, 'Nvidia')

it_companies[4] = it_companies[4].upper()

joined_companies = '#;&nbsp; '.join(it_companies)
print("Joined IT Companies:", joined_companies)

company_to_check = 'Apple'
print(f"{company_to_check} exists in the list: {company_to_check in it_companies}")

it_companies.sort()

it_companies.reverse()

first_three_companies = it_companies[:3]

last_three_companies = it_companies[-3:]

middle_companies = it_companies[len(it_companies) // 4:len(it_companies) * 3 // 4]

it_companies.pop(0)

middle_index = len(it_companies) // 2
it_companies.pop(middle_index)

it_companies.pop()

it_companies.clear()

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python', 'SQL')

### Exercises: Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Min Age:", min_age)
print("Max Age:", max_age)

ages.extend([min_age, max_age])
print("Ages List After Addition:", ages)

middle_index = len(ages) // 2
median_age = (ages[middle_index - 1] + ages[middle_index]) / 2 if len(ages) % 2 == 0 else ages[middle_index]
print("Median Age:", median_age)


average_age = sum(ages) / len(ages)
print("Average Age:", average_age)


age_range = max_age - min_age
print("Age Range:", age_range)


min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)
print("Min-Average Difference:", min_average_diff)
print("Max-Average Difference:", max_average_diff)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_countries = countries[len(countries) // 2 - 1 : len(countries) // 2 + 1] if len(countries) % 2 == 0 else [countries[len(countries) // 2]]
print("Middle Country(ies):", middle_countries)

half_index = len(countries) // 2
first_half_countries = countries[:half_index + 1] if len(countries) % 2 != 0 else countries[:half_index]
second_half_countries = countries[half_index + 1:]
print("First Half Countries:", first_half_countries)
print("Second Half Countries:", second_half_countries)

first_three, *scandic_countries = countries

print("First Three Countries:", first_three)
print("Scandic Countries:", scandic_countries)
