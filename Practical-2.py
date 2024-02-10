#A)list and its methods
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("IT Companies:", it_companies)
it_companies.append('Intel')
print("IT Companies:", it_companies)
back_end = ['Node', 'Express', 'MongoDB']
newl=[]
newl.extend([it_companies, back_end])
print(f"New List:",newl)
print("it_companies List After Addition:", it_companies)
it_companies.remove('Facebook')
print("It companies after removing Facebook:", it_companies)
print(it_companies.reverse())
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

#B)
list1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]
word1 = list1[8][2]
print("Word 1:", word1)
word2 = list1[4][0].capitalize()
print("Word 2:", word2)
new_list = [list1] * 5
print("Repeated list:", new_list)

# C)
original = [1, 2, 3, 4, 5]
copied = original[:]
print("Original List:", original)
print("Copied List:", copied)

# D)
tuple = (1, 2, 3, 4, 5)
print("Sum of all values in Tuple:", sum(tuple))
print("Maximum value in Tuple:", max(tuple))
print("Minimum value in Tuple:", min(tuple))
