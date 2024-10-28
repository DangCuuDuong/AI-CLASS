import numpy as np
def in_mon_no(ma_sinh_vien):
    bang_diem =  { 
        1112233: {"Tin ky thuat": 9.2, "An toan dien": 8.9, "The duc": 4.1},
        1112244: {"Tin ky thuat": 3.7,"The duc": 9.0} 
    }

    if ma_sinh_vien not in bang_diem:
        print (f"Mã sinh viên {ma_sinh_vien} không tồn tại")
        return
    diem_sinh_vien = bang_diem[ma_sinh_vien]
    mon_hoc = list(diem_sinh_vien.keys())
    diem_so = np.array(list(diem_sinh_vien.values()))
    
    # Tìm các môn nợ (điểm < 5)
    mon_no = np.array(mon_hoc)[diem_so < 5]

    if mon_no:
        print(f"Sinh viên {ma_sinh_vien} nợ các môn: {','.join(mon_no)}")
    else:
        print(f"sinh viên {ma_sinh_vien} không nợ môn nào.")
a = int(input("Nhập vào mã số sinh viên:"))
in_mon_no(a)


    