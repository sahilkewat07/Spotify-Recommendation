import numpy as np
arr = np.array([4,6,9,4,1])
print(arr)

print()
for i in arr:
    print(i)
print()
###############################
'''
arrApp= []
for i in range(1,5):
    val = int(input("Enter number: "))
    arrApp.append(val)
print(arrApp)
print(np.array(arrApp))
'''
##################################

print("Printing dimensions");
print(arr.ndim)
arr10Dim = np.array([1,2,3,5],ndmin=10)
print(arr10Dim)
print("Dimension: ", arr10Dim.ndim, "\n")

#################################
# Array containing zero
arr0=np.zeros(4)
print(arr0)
print("Dimension : ",arr0.ndim)
print()

arr3Row4Col = np.zeros((3,4))
print(arr3Row4Col)
print("Dimension : ", arr3Row4Col.ndim, "\n")

#################################
#Array having value 1
arr1=np.ones(4)
print(arr1, " and Dimension: ", arr1.ndim, "\n")

arr3Row4Col_1 = np.ones((3,4))
print(arr3Row4Col_1, "and Dimension: ", arr3Row4Col_1.ndim, "\n")
