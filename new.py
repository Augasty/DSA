import copy

# array shallow copy
arr1 = [1,2,3]
arr2 = arr1  #arr2 = arr1.copy() will also create a shallow copy
arr2.append(8)
print(arr1)
print(arr2)
# [1, 2, 3, 8]
# [1, 2, 3, 8]
# as arr2 just references to arr1, any changes in arr2 will change arr1 and vice versa

# array deep copy
arr3 = [1,2,3]
arr4 = copy.deepcopy(arr3)
arr4[2] = 'sayak'
print(arr3)
print(arr4)
# [1, 2, 3]
# [1, 2, 'sayak']
# in deep copy, arr4 has a completely new array, so, old array arr3 is not effected when arr4 is changed

# numbers, strings always deepcopy
num0 = 8
print(type(num0))
num1 = num0       # copy.copy(num0) also won't give a shallow copy, as num0 is not an object, it is an int
num1 = 6
print(num1,num0)