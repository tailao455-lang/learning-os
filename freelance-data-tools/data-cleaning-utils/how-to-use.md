### Cách dùng nhanh
```python
from utils import *

df['salary'] = df['salary_raw'].apply(clean_salary)
df['domain'] = df['email'].apply(extract_domain)
df_clean = remove_outliers_iqr(df, "salary", whisker=1.5)
