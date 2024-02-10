# A) String Operations:
s1='Rohan'
print("Reversed String is :", s1[::-1])
print("Replaced String is : ", s1.replace('an', 'it')) 
s2="Rohit"
print("Merged String is : ", s1+ " and "+s2+" = ",s1+s2)
print("Is  'n' present in Rohan? : ", 'n' in s1)
strng='Hello World, Python Programming'
print("Split String by Space : ", strng.split())
print("Split String by Character : ", strng.split(','))

#B) Dictionaries Operations:
d={'Name':'Rohan','Age':25,'City':'Nadiad'}
print("Dictionary Before Updating : ", d)
d['Name']='Rohit'
d['Salary']=60000
del d['Age']
print("After Update/Delete Operation : ",d)
key,value=d.popitem()
print("Key Popped from the Dictionary : ", key,"Value Popped from the Dictionary :   ", value)
print("Pop Item Operation : ",d.pop())
print("Get Value of Key Name : ", d.get('Name'))
d.clear()
print("After Clearing the Dictionary : ",d)

d1={'a':1,'b':2}
d2={'c':3,'d':4}
d3={'e':5,'f':6}
merged = d1 | d2 | d3
print(merged)
