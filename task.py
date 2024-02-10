s1="Rohan"
print(s1[::-1])

print(s1.replace("an","it"))

print('a' in s1)

tuple = ('R', 'O', 'H', 'A', 'N')
s2=str(tuple)
print(s2, type(s2))

list1 = ['R', 'O', 'H', 'A', 'N']
s3=str(list1)
print(s3, type(s3))

set = {'R', 'O', 'H', 'A', 'N'}
s4=str(set)
print(s4, type(s4))


print(s1.upper(),s1.lower())
print(s1.split("o"))

tuple=(12,15,26,48,96,25)
print(max(tuple),min(tuple),len(tuple),sum(tuple))

list1=[63,23,59,84,12,547,97]
print(max(list1),min(list1),len(list1),sum(list1))

listc=list(list1)
print(listc,type(listc))


dr={'name':'Rohan', 'age':20, 'grade':'AA'}
print(dr.values())
print(dr.get('age'))
dr['age']=30
print(dr.get('age'))
dr.update({'grade':'AB'})
print(dr.get('grade'))
print('gender' in dr)


set1={1, 2, 3} 
set2={3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.issubset(set2))


subject={}
subject['math']= {"Monica" , "Phoebe" , "Rachel" , "Jenice"}
subject['science']={"Chandler" , "Joey" , "Rohan" , "Ross", "Gunther"}
print(subject)

subject['math'].add("Rohan")
print(subject['math'])

subject['science'].remove("Joey")
print(subject['science'])

print(subject['math'].intersection(subject['science']))

country={
    'USA': {'New York': 8398748, 'Los Angeles': 3990456, 'Chicago': 2705994},
    'Japan': {'Tokyo': 37393129, 'Yokohama': 3726167, 'Osaka': 2691097},
    'India': {'Mumbai': 18414230, 'Delhi': 16198434, 'Bangalore': 1055449}
}

original_list = [1, 2, 3, 4, 5, 6, 7]
even_indices = original_list[::2]
odd_indices = original_list[1::2]
print(even_indices)
print(odd_indices)

a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)
 
lst = [1, 2, 3, 2, 1]
print(lst == lst[::-1]) 

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3=sum((tuple1, tuple2),())
print(tuple3,type(tuple3))