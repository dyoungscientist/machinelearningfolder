"""
import numpy as np
arr = np.array ([1, 2, 3, 4, 5])
print ("Array:", arr)

arr.shape 
print (arr.shape)
arr.dtype
print (arr.dtype)
arr.ndim
print (arr.ndim)
arr + 5 
arr * 2 
print (arr + 5)
print ( arr * 2)


import numpy as np
arrOpp= np.array([12.5, 8.0, 20.0])
np.sum 
arrOpp = np.sum ([12.5, 8.0, 20.0])
print (arrOpp)
arrOpp = np.mean ([12.5, 8.0, 20.0])
print (arrOpp)
arrOpp =np.max ([12.5, 8.0, 20.0])
print (arrOpp)
"""
# random data practice 
import numpy as np
x = np.min ([1, 40, 25, 69, 5, 3, 66, 76, 89, 90])
print (x)
x = np.max ([1, 40, 25, 69, 5, 3, 66, 76, 89, 90])
print (x)
x = np.mean ([1, 40, 25, 69, 5, 3, 66, 76, 89, 90])
print (x)
x = np.std ([1, 40, 25, 69, 5, 3, 66, 76, 89, 90])
print (x)

# indexing and slicing
import numpy as np
arrIndx = np.array ([ 10, 20, 30, 40, 50 ])
# to slice the nxt 3 elements
print (arrIndx[:3])
print (arrIndx[-2:])
print (arrIndx[::-1])
print (arrIndx[:-2])
print (arrIndx [::-3])