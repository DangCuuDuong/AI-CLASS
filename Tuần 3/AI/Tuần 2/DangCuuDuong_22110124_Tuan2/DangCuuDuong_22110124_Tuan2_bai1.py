import math
def giai_pt(*bien):
    if len(bien) == 2:
        a,b = bien
        if a == 0:
            if b == 0:
                return "Phương trình vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            x = -b/a
            return f"Phương trình có nghiệm là x = {x}"
    elif len(bien) == 3:
        a,b,c = bien
        if a == 0:
            return giai_pt(b,c)
        else:
            delta = b**2 - 4 * a * c
            if delta > 0:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                return f"Phương trình có hai nghiệm phân biệt x1 ={x1}, x2={x2}"
            elif delta==0:
                x = -b /(2*a)
                return f"Phương trình có nghiệm kép x = {x}"
            else:
                return "Phương trình vô nghiệm"
    else:
        return "Đầu vào không hợp lý"
def nhap():
    bien = input("Nhập các hệ số (cách nhau bằng khoảng cách): ").split()
    bien = [float(a) for a in bien]
    if len(bien) == 2:
        print(giai_pt(bien[0], bien[1]))
    elif len(bien)== 3:
        print(giai_pt(bien[0], bien[1],bien[2]))
    else:
        print("Chỉ nhập 2 hoặc 3 hệ số")
nhap()

''' LINK VIDEO https://drive.google.com/file/d/1XeHv9KJd7VwaAEoz5kbmh1dYvPQGWaea/view?usp=sharing '''