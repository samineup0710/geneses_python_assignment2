list1 = [1, 5, 7, 12, 15]

print("The given list is:", list1)
for i in range(len(list1)):
    """printing the each element of list at its specific index"""
    print("List item is {} at {} index".format(list1[i], i))

    """finding its elements square"""
    sqr = list1[i] * list1[i]
    print("The square of {} is {}".format(list1[i], sqr))
   
   