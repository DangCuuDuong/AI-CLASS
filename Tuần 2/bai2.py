class sinhvien:
    def __init__(self, ma_sv,ten_sv, gioitinh_sv, diem_hp1, diem_hp2, diem_hp3, diem_hp4, diem_hp5):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.gioitinh_sv = gioitinh_sv
        self.diem_hp1 = diem_hp1
        self.diem_hp2 = diem_hp2
        self.diem_hp3 = diem_hp3
        self.diem_hp4 = diem_hp4
        self.diem_hp5 = diem_hp5
        self.diem_tb = self.tinh_diem_trung_binh()
        self.hocluc = self.xep_loai()

    def tinh_diem_trung_binh(self):
        return(self.diem_hp1 +self.diem_hp2 + self.diem_hp3 +self.diem_hp4 +self.diem_hp5)/5
    def xep_loai(self):
        if self.diem_tb >=8 and min(self.diem_hp1, self.diem_hp2,self.diem_hp3,self.diem_hp4 ,self.diem_hp5)>=5:
            return "Giỏi"
        elif 6.5 <= self.diem_tb <= 8 and min(self.diem_hp1, self.diem_hp2,self.diem_hp3,self.diem_hp4 ,self.diem_hp5)>=5:
            return "Khá"
        elif 5<= self.diem_tb <6.5:
            return "Trung bình"
        else:
            return "Yếu"
    def hien_thi_thong_tin(self):
        print(f"Mã SV: {self.ma_sv}, Tên SV: {self.ten_sv}, Giới tính: {self.gioitinh_sv}, Điểm TB: {self.diem_tb}, Học lực: {self.hocluc}")
danh_sach_sinh_vien = []
def hien_thi_dang_sach():
    print("\n Danh sách sinh viên")
    for sv in danh_sach_sinh_vien:
        sv.hien_thi_thong_tin()
def them_sinh_vien():
    for i in range(2):
        print(f"\n Nhập thông tin sinh viên thứ {i+1}")
        ma_sv = input("Mã SV:")
        ten_sv = input("Tên SV:")
        gioitinh_sv = input("Giới tính:")
        diem_hp1 = float(input("Điểm học phần 1:"))
        diem_hp2 = float(input("Điểm học phần 2:"))
        diem_hp3 = float(input("Điểm học phần 3:"))
        diem_hp4 = float(input("Điểm học phần 4:"))
        diem_hp5 = float(input("Điểm học phần 5:"))

        sv =sinhvien(ma_sv, ten_sv, gioitinh_sv, diem_hp1, diem_hp2, diem_hp3, diem_hp4, diem_hp5)
        danh_sach_sinh_vien.append(sv)
def in_dtb_cao_nhat():
    if not danh_sach_sinh_vien:
        print("Danh sách rỗng")
        return
    max_diem_tb = max( sv.diem_tb for sv in danh_sach_sinh_vien )
    sinh_vien_max = [sv for sv in danh_sach_sinh_vien if sv.diem_tb == max_diem_tb]

    print("\n sinh viên có điểm trung bình cao nhất:")
    for sv in sinh_vien_max:
        sv.hien_thi_thong_tin()
them_sinh_vien()
hien_thi_dang_sach()
in_dtb_cao_nhat()