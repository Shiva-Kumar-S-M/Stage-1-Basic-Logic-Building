

#Numpy tutorial for creating arrays 

# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))
# print(np.__version__)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)
# print(np)

# import numpy as np
# a=np.array([[1,2],[3,4]])
# print(a)
# print(a.ndim)

# import numpy as np
# b=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[5,6,4]]])
# print(b)
# print(b.ndim)

# import numpy as np
# c=np.array([1,2,3,4],ndmin=5)
# print(c)
# print(c.ndim)


#Numpy array indexing and slicing
#numpy uses less byte of memory as compared to list
#It uses contiguos memory allocation
#There is no data
#Applications
#mathamatics(matlab),Plotting,Backend,Machine learning

# import numpy as np
# a=np.array([1,2,3])
# print(a)
# print(a.size)

# import numpy as np
# a=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print(a)
# print(a[0,3])
# print(a[0,:])
# a[0,4]=123
# print(a)
import numpy as np
# a=np.array([[[1,2,3],[4,5,6]],[[7,7,9],[3,5,4]]])
# print(a)
# print(a[1,0,2])
# a[0,1,1]=10
# print(a)

a=np.zeros((2,3))
print(a)