import pandas as pd

file_path = "example_data.xlsx"
df = pd.read_excel(file_path)

print("=== Общая информация ===")
print(df.info())

print("\n=== Статистика числовых данных ===")
print(df.describe())

average_salary = df["Salary"].mean()
print(f"\nСредняя зарплата: {average_salary:.2f}")

average_age_by_department = df.groupby("Department")["Age"].mean()
print("\n=== Средний возраст по отделам ===")
print(average_age_by_department)

employees_above_30 = df[df["Age"] > 30]
print("\n=== Сотрудники старше 30 лет ===")
print(employees_above_30)
