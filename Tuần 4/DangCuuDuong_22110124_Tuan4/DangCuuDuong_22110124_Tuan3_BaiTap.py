import pandas as pd
data = pd.read_csv("Exercise_dataframe.csv")
#câu 1:Cắt khung dữ liệu từ cột ‘school' cho đến cột ‘guardian’
cau1=data.loc[:,'school':'guardian']
print(cau1)
#câu 2: Tạo hàm lambda để viết hoa các cột có dữ liệu kiểu chuỗi
cau2 = data.copy()
string_colums = data.select_dtypes(include=['object']).columns
cau2[string_colums] = cau2[string_colums].apply(lambda x: x.str.upper())
print(cau2)
#câu 3: In các phần tử cuối cùng của tập dữ liệu
print(data.tail())
#câu 4: In ra kết quả thống kê sex và age theo từng school
cau4=data.groupby('school').agg({'sex':'value_counts','age':'mean'})
print(cau4)
#câu 5: Trung bình, trường học nào có traveltime,studytime cao nhất
traveltime_studytime_mean = data.groupby('school').agg({'traveltime':'mean','studytime':'mean'})
cau5 = traveltime_studytime_mean.idxmax()
print(cau5)
#cau 6: In ra giá trị trung bình, giá trị min và giá trị max của studytime và traveltime
st_time = data['studytime'].agg(['mean','min','max'])
tt_time = data['traveltime'].agg(['mean','min','max'])
print(f"studytime mean:{st_time['mean']}, studytime max:{st_time['max']}  ,studytime min:{st_time['min']}")
print(f"traveltime mean:{tt_time['mean']}, traveltime max:{tt_time['max']}  ,traveltime min:{tt_time['min']}")
#câu 7: . In ra màn hình số absences lớn hơn 5 theo từng trường
cau7 = data[data['absences']>5].groupby('school').size()
print(cau7)
#câu 8 :In ra màn hình những trường có thông tin health bằng thông tin absences
cau8 = data[data['health']==data["absences"]]
print(cau8)
#câu 9:Tạo một dataframe mới bao gồm các cột school, sex, age, studytime, failures, health, absences và lưu dưới tên temp_data_frame.csv
new_data=data[['school', 'sex', 'age', 'studytime', 'failures', 'health', 'absences']]
new_data.to_csv('temp_data_frame.csv', index = False)

#link https://drive.google.com/file/d/1zPwR3ITsoz34EigZX7JsNNrQwBzMKprD/view?usp=sharing