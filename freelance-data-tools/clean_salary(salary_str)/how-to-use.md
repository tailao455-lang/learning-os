import pandas as pd
from utils import clean_salary

df = pd.read_csv("employees.csv")
df['salary_clean'] = df['salary_raw'].apply(clean_salary)