import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv("Exercise_dataframe.csv")

# 1. Cắt khung dữ liệu từ cột 'school' cho đến cột 'guardian'
df_filtered = df.loc[:, 'school':'guardian']
print("1. Dữ liệu từ cột 'school' đến cột 'guardian':")
print(df_filtered)

# 2. Tạo hàm lambda để viết hoa các cột có dữ liệu kiểu chuỗi
df_capitalized = df.copy()
string_columns = df.select_dtypes(include=['object']).columns
df_capitalized[string_columns] = df[string_columns].apply(lambda x: x.str.upper())
print("2. Các cột có dữ liệu kiểu chuỗi đã viết hoa:")
print(df_capitalized)

# 3. In các phần tử cuối cùng của tập dữ liệu
print("3. Các phần tử cuối cùng của tập dữ liệu:")
print(df.tail())

# 4. In ra kết quả thống kê sex và age theo từng school
grouped_by_school = df.groupby('school').agg({'sex': 'value_counts', 'age': 'mean'})
print("4. Kết quả thống kê sex và age theo từng trường:")
print(grouped_by_school)

# 5. Trung bình, trường học nào có traveltime, studytime cao nhất
traveltime_studytime_mean = df.groupby('school').agg({'traveltime': 'mean', 'studytime': 'mean'})
highest_traveltime_studytime = traveltime_studytime_mean.idxmax()
print("5. Trường học có traveltime cao nhất và studytime cao nhất:")
print(traveltime_studytime_mean)
print(f"Traveltime cao nhất: {highest_traveltime_studytime['traveltime']}")
print(f"Studytime cao nhất: {highest_traveltime_studytime['studytime']}")

# 6. In ra giá trị trung bình, giá trị min và giá trị max của studytime và traveltime
studytime_stats = df['studytime'].agg(['mean', 'min', 'max'])
traveltime_stats = df['traveltime'].agg(['mean', 'min', 'max'])
print("6. Giá trị trung bình, min, max của studytime và traveltime:")
print(f"Studytime - Mean: {studytime_stats['mean']}, Min: {studytime_stats['min']}, Max: {studytime_stats['max']}")
print(f"Traveltime - Mean: {traveltime_stats['mean']}, Min: {traveltime_stats['min']}, Max: {traveltime_stats['max']}")

# 7. In ra màn hình số absences lớn hơn 5 theo từng trường
absences_greater_than_5 = df[df['absences'] > 5].groupby('school').size()
print("7. Số absences lớn hơn 5 theo từng trường:")
print(absences_greater_than_5)

# 8. In ra màn hình những trường có thông tin health bằng absences
health_equals_absences = df[df['health'] == df['absences']]
print("8. Những trường hợp có health bằng absences:")
print(health_equals_absences)

# 9. Tạo một dataframe mới gồm các cột school, sex, age, studytime, failures, health, absences và lưu thành file CSV
new_df = df[['school', 'sex', 'age', 'studytime', 'failures', 'health', 'absences']]
new_df.to_csv('temp_data_frame.csv', index=False)
print("9. Đã lưu dataframe mới thành file temp_data_frame.csv")
