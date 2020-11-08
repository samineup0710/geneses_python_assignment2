""" create a list"""
list1 = [2,56,78,20,34,9,23,8,31] 
print(list1)
"""lets initialize summation variable to 0 to store sum """
summation = 0
""" looping through each list items"""
for i in range(len(list1)):
    summation += list1[i]   
    i += 1                               #increment the list index by 1  
print("The total sum of list is:", summation)
