import math
import numpy as np
def giaipt(*bien):
    if len(bien) ==2:
        a,b = bien
        if a == 0:
            if b == 0:
                return"Phương trình vô số nghiệm"
            else:
                return"Phương trình vô nghiệm"
        else:
            x=np.roots([a,b])
            return f"Phương trình có nghiệm là x={x[0]}"
    elif len(bien) == 3:
        a,b,c = bien
        if a==0:
            return giaipt(b,c)
        else:
            dt = pow(b,2)-4*a*c
            if dt > 0:
                x=np.roots([a,b,c])
                return f"Phương trình có hai nghiệm phân biệt x1={x[0]}, x2{x[1]}"
            elif dt == 0:
                x=np.roots([a,b,c])
                return f"Phương trình có  nghiệm kép x={x[0]}"
            else:
                return"Phương trình vô nghiệm"  
    else:
        return "Đầu vào không hợp lệ"
def nhap():
    bien = input("Nhap các hệ số các nhau bằng dấu cách:").split()
    bien = [float(a) for a in bien]
    if len(bien)==2:
        print(giaipt(bien[0],bien[1]))
    elif len(bien)==3:
        print(giaipt(bien[0],bien[1],bien[2]))
    else:
        print("Chỉ nhập 2 hoặc 3 hệ số")
nhap() 
'''LINK: https://drive.google.com/file/d/1GStP_CP1zlQyTg0QNmg3hg0Tso8bM0fQ/view?usp=drive_link'''