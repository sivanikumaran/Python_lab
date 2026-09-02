import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])
print("Original array:", array)
print("Mean of the array:", np.mean(array))
print("Maximum of the array:", np.max(array))
print("Minimum of the array:", np.min(array))

arr = np.array([10, 20, 30, 40, 50]) 
print("3rd element:", arr[2])
print("First 3 elements:", arr[:3]) 
print("New array:")
arr[2] =35
print(arr)

arr1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("arr1:",arr1)
print("Shape of the array:", arr1.shape)
print("Sum of all elements:", np.sum(arr1))
print("Sum of each row:", np.sum(arr1, axis=1))\
    
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("Element 5:", arr2[1,1])
print("last column:", arr2[:,2])
print("Secound row:", arr2[1, :])
print(arr2[:,0])
print(arr2[2,:])
print(arr2[ 1: , 1: ])
