import pandas as pd

# Đọc file CSV
data = pd.read_csv("C:\\Users\\DELL\\OneDrive\\Desktop\\AI\\Tuần 4\\lớp\\Data_Frame.csv")
print(data)
trungbinhbiachauluc = data.groupby('continent')['beer_servings'].mean()
chaulucuongnhieunhat = trungbinhbiachauluc.idxmax()
print("Châu lục uống nhiều nhất:",chaulucuongnhieunhat)

trungbinhruouchauluc = data.groupby('continent')['wine_servings'].describe()
print(trungbinhruouchauluc)

c = data.groupby('continent')['wine_servings'].sum()
print(c)
d = data['wine_servings'].describe()['max','min','mean']
print(d)