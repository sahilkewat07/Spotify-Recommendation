#Series
# import pandas as pd
# arr = [2,6,2,8]
# var = pd.Series(arr)
# print(var)
# print(type(var))




fileW = open("dj.txt", "a")
fileW.writelines("which is located at Roorkee")
fileW.close()


f = open("dj.txt","r")
#cont = f.read()
#print(cont)
cont2 = f.readlines()

print(cont2)
f.close()

#by using with function we do not need to close file explicitly