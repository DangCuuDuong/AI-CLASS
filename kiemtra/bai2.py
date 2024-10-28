import pandas as pd
import matplotlib.pyplot as plt

# câu 1
df=pd.read_csv('wind.data.txt', delim_whitespace=True)
# câu 2 
df['date']= pd.to_datetime(df[['Yr', 'Mo', 'Dy']].astype(str).agg('-'.join, axis=1), format='%y-%m-%d')
print(df[['Yr', 'Mo', 'Dy', 'date']].head())
# câu 3
df.set_index('date', inplace=True)
print(df.head)
#Câu 4
dulieuthieu=df.iloc[:, 3:].isnull().sum()
dulieuco=df.iloc[:, 3:].notnull().sum()
print("So luong gia tri hien co")
print( dulieuco)
print("So luong gia tri thieu")
print(dulieuthieu)
#câu 5
tocdogiotrungbinh = df.iloc[:, 3:].mean().mean()
print("toc do gio trung binh:")
print(tocdogiotrungbinh)
#câu 6
loc_stats = df.iloc[:, 3:].agg(['min', 'max', 'mean', 'std'])
print(loc_stats)
#Câu 7
tocdogio_thang1= df[df.index.month==1]
tocdogiotrungbinh_thang1=tocdogio_thang1.iloc[:, 3:].agg(['mean'])
print(tocdogiotrungbinh_thang1)
#câu 8
Thongketheonam = df.groupby('Yr').agg(['min', 'max', 'mean', 'std'])
print('Thống kê theo năm:')
print(Thongketheonam)

Thongketheothangnam = df.groupby(['Yr','Mo']).agg(['min', 'max', 'mean', 'std'])
print('Thống kê theo tháng năm:')
print(Thongketheothangnam)

df['week']=df.index.isocalendar().week
Thongketheotuanthangnam = df.groupby(['Yr','Mo','week']).agg(['min', 'max', 'mean', 'std'])
print('Thống kê theo tuần – tháng – năm:')
print(Thongketheotuanthangnam)



