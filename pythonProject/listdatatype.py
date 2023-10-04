values = [1, 2, "hii", 8]
# list is a datatype that allow multiple values and be of different data type
print(values[0])  # 1
print(values[2])  # hii
# In the python if we want to print the last value of a list then we can print by:
print(values[-1])
print(values[0:-1])  # [2,"hii"]
# if we have to insert value in list then
values.insert(3, "i am good")  # [1, 2, 'hii', 'i am good', 8]
print(values)
# if we have to add data in the last then :
values.append("bye")
print(values)  # [1, 2, 'hii', 'i am good', 8, 'bye']

# for updating
values[2] = "HII"
# for deleting
del values[1]
print(values)  # [1, 'HII', 'i am good', 8, 'bye']
# tuple datatype is same as list but is immutable means we can't update the list
values = (1, 4, "good", 2.5)
print(values[2])
"""values[2] = "GOOD"   values[2] = "GOOD"
TypeError: 'tuple' object does not support item assignment """

# dictionary datatype
dic = {5: "hii", "a": "sanjoli", 6: "verma", "age": 27}
print(dic[5], dic["a"], dic[6], dic["age"])

# adding value into empty dictionary at run time
dict = {}
dict["firstname"] = "Anand"
dict["lastname"] = "verma"
print(dict)

""" type of data type in python
1. numeric
2. list
3. string
4. tuple
5. dictionary
"""
