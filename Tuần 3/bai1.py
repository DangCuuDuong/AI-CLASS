
import numpy as np
a = np.array([-2, 6, 3, 10, 15, 48])
nhom1 = a[2:5:2]
nhom2 =a[1:6:2]
nhom3 = a[3:6]
nhom4 = a[5:2:-1]

print(nhom1, nhom2, nhom3, nhom4)