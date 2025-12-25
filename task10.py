"""
first print the list 1 to 10
print the first five elements of the list 1 2 3 4 5
reverse the first five element 5 4 3 2 1
"""
original_list = [1,2,3,4,5,6,7,8,9,10]
print(f"original_list {original_list}")
first_five = original_list[:5]
print(f"first five is:{first_five}")
reversed_list = first_five[::-1]
print(f"reversed extracted element: {reversed_list}")
