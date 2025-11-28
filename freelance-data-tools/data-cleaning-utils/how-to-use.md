import pandas as pd
from utils import clean_salary, extract_domain

df['salary_clean'] = df['salary_raw'].apply(clean_salary)
df['domain'] = df['email'].apply(extract_domain)
