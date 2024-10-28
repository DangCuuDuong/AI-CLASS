import pandas as pd
import matplotlib.pyplot as plt

# Đọc file CSV
data = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\AI\\Tuần 4\\lớp\\Example1_data.csv")
print("Câu 1: In ra 5 hàng đầu tiên và 5 hàng cuối cùng")
print(data.head(5))
print(data.tail(5))
print("Câu 2: Làm sạch tập dữ liệu (loại bỏ giá trị thiếu nếu có)")
dataclean = data.dropna()
print(dataclean)
print("Câu 3: Tìm tên công ty có xe đắt nhất")
cau3 = data.loc[data['price'].idxmax(), 'company']
print("Câu 4: In tất cả thông tin chi tiết về xe Toyota ")
cau4 = data[data['company'] == 'toyota']
print(cau4)
print("Câu 5: Đếm tổng số xe mỗi cty xe")
cau5 = data['company'].value_counts()
print(cau5)
print("câu 6: tìm giá xe cao nhất của mỗi công ty")
cau6 = data.groupby('company')['price'].max()
print(cau6)
print("câu 7: tìm số km trung bình của mỗi hãng sản xuất oto")
cau7=data.groupby('company')['average-mileage'].mean()
print(cau7)
print("câu 8: sắp xếp tất cả các xe theo cột giá")
cau8 = data.sort_values( by = "price",ascending=False)
print(cau8)


Xe_Duc = {'Company': ['Mercedes', 'Ford', 'Audi', 'BMW'], 'Price': [23845, 135925, 71400, 171995]}
data_duc = pd.DataFrame(Xe_Duc)

Xe_Nhat = {'Company': ['Nissan', 'Toyota', 'Honda', 'Mitsubishi'], 'Price': [23600, 29995, 58900, 61500]}
data_nhat = pd.DataFrame(Xe_Nhat)

cau9 = pd.concat([data_duc, data_nhat])
print(cau9)


plt.plot(djia_data["company"], djia_data["price"])
plt.show