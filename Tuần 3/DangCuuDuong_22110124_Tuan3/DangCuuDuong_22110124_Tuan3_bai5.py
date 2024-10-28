import numpy as np
def innomon(mssv):
    bangdiem ={ 
            1112233: {"Tin ky thuat": 9.2, "An toan dien": 8.9, "The duc": 4.1},
            1112244: {"Tin ky thuat": 3.7, "The duc": 9.0} 
            }
    if mssv not in bangdiem:
        print("MSSV khong hop le")
        return
    diemSV = bangdiem[mssv]
    monhoc = list(diemSV.keys())
    diemso=np.array(list(diemSV.values()))
    monno= np.array(monhoc)[diemso<5]
    if monno:
        print(f'Sinh vien {mssv} nợ các môn: {','.join(monno)}')
    else:
        print(f'Sinh vien {mssv} không nợ môn nào')
a=int(input("Nhập vào MSSV:"))
innomon(a)
'''LINK: https://drive.google.com/file/d/1PKJdQogjszi_Aol8i8inKBXWzFOeD0qU/view?usp=drive_link'''