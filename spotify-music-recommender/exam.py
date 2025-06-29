import numpy as np
import pandas as pd
arr1 = np.array([[1,2], [4,5], [89,10]])
for i in arr1:
    print(i)
print(arr1[1][1])

arr2 = arr1[0:2, 0:1]
print(arr2)

sr = {"sr1":pd.Series([2,4,6]), "sr2": pd.Series([5,7,9])};
dff = pd.DataFrame(sr)
print(dff)

data = {"Math":45, "Sci": 520, "com":58}
sa = pd.Series(data)
print(sa)


arr = np.array([100, 200, 300])
s = pd.Series(arr)
print(s)