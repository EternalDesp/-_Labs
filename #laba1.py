#laba1
import pandas as pd
import numpy as np
DATA_URL = "https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/data/"
DF = pd.read_csv(DATA_URL + "adult.data.csv")
print(DF.head())
print("Количество столбцов:",len(DF.columns))
#1 Ответ: 15 столбцов
DF.info()
#2 Ответ: пропусков нет

print(len(DF['race'].unique()))
#3 Ответ: 5
print(DF['hours-per-week'].median())
#4 Ответ: медиана 40
salary_DF = DF[DF['salary'] == '>50K']
gc = salary_DF['sex'].value_counts()
print(gc)
#5 Ответ: Male
#6 Ответ: пропусков нет, но если бы были
DF.fillna(DF.mode().iloc[0], inplace=True)
