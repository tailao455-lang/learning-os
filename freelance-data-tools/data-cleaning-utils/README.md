# Freelance Data Cleaning Toolkit

Bộ 4 hàm Python mình dùng hàng ngày để làm sạch dữ liệu cho khách Upwork/Fiverr.

| Hàm                     | Mục đích                                    | Giá trị mỗi job       |
|-------------------------|---------------------------------------------|------------------------|
| `clean_salary()`        | Dọn lương bẩn ($50k → 50000.0, N/A → None)  | $300–$800            |
| `extract_domain()`      | Lấy domain từ email                         | $200–$500            |
| `is_valid_email()`      | Kiểm tra email hợp lệ                       | Hỗ trợ                |
| `remove_outliers_iqr()` | Loại outliers siêu mạnh (IQR + median guard) | $500–$2000           |

### 1. clean_salary() – Dọn lương bẩn
```python
clean_salary("100,000 VND")    → 100000.0
clean_salary("N/A")            → None
```
### 2. is_valid_email() - Email hợp lệ
```python
print(is_valid_email("abc@gmail.com"))           #True
print(is_valid_email("abc@"))                     #False
```
### 3. extract_domain() - Trích xuất domain từ email
```python
print(extract_domain("abc@gmail.com"))           # gmail.com
print(extract_domain("abc@"))                     # None
```
### 4. remove_outliers_iqr() - Loại bỏ outliers bằng IQR
```python
df_clean = remove_outliers_iqr(df, "salary", whisker=1.5, max_multiplier=10)
# → Loại 2 (100k và 200k) → giữ 5 dòng
