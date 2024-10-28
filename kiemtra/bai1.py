import pandas as pd
import matplotlib.pyplot as plt

#câu 1
df = pd.read_csv("chipotle.tsv.txt", sep = '\t')
#câu 2
df['item_price']= df['item_price'].str.replace('$','').astype(float)
sanphamhon10=df[df['item_price'] > 10].drop_duplicates(subset=['item_name'])
print(sanphamhon10)
print("........")
#câu 3
cau3=df.sort_values(by='item_name')
print("........")
print(cau3)
#câu 4
cau4=df.sort_values(by='item_price')
print("........")
print(cau4.tail(1))
#câu 5
cau5=df[df['item_name'] == 'Veggie Salad Bowl']
order_vs = cau5['order_id'].nunique()
tong_vs= cau5['quantity'].sum()
print("........")
print(' tổng số Veggie Salad Bowl được đặt là:', tong_vs)
#câu 6
top_5 = df.groupby('item_name').sum()['quantity'].nlargest(5)
plt.figure(figsize=(15,10))
top_5.plot(kind='bar',color='r')
plt.title('5 sản phẩm được mua nhiều nhất', color = 'navy')
plt.xlabel('Tên sản phẩm',color='brown')
plt.ylabel('Tần suất mua hàng',color='b')
plt.show()
#câu 7
soluongdathang = df.groupby('order_id').sum()['quantity']
plt.figure(figsize=(15,10))
plt.scatter(soluongdathang.index, soluongdathang.values)
plt.title('Số lượng mặt hàng được đặt trên mỗi đơn hàng')
plt.xlabel('order_id')
plt.ylabel('quantity')
plt.show()
