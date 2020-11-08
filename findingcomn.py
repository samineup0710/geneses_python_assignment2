"""create a list1"""
list1 = [1, 4, 5, 7, 1, 6, 3, 5]

"""create a list2"""
list2 = [1, 3, 5, 7, 8, 3, 2, 7]

"""removing duplicate using set conversion method for list1"""
duprem_list1 = set(list1)
print("duplicate removed set1:", duprem_list1)

"""removing duplicate using set conversion method for list2"""
duprem_list2 = set(list2)
print("duplicate removed set2:", duprem_list2)

"""finding the common items using set intersection method"""
common_items = duprem_list1.intersection(duprem_list2)

"""converting set to list again"""
print("common items in lists:", list(common_items))