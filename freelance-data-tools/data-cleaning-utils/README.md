# Freelance Data Cleaning Utils – Bộ công cụ kiếm $500+/dự án

3 hàm Python cực mạnh mình dùng hàng ngày để làm sạch dữ liệu cho khách Upwork/Fiverr.

### 1. clean_salary() – Dọn lương bẩn
```python
clean_salary("$50,000.00")     → 50000.0
clean_salary("75k")            → 75000.0
clean_salary("100,000 VND")    → 100000.0
clean_salary("N/A")            → None
```
### 2. is_valid_email() - Email hợp lệ
```python
print(is_valid_email("abc@gmail.com"))           #True
print(is_valid_email("hello.world@company.co.uk")) #True
print(is_valid_email("a@b@c.com"))                #True
print(is_valid_email("không có @"))               #False
print(is_valid_email("abc@"))                     #False
```
### 3. extract_domain() - Trích xuất domain từ email
```python
print(extract_domain("abc@gmail.com"))           # gmail.com
print(extract_domain("hello.world@company.co.uk")) # company.co.uk
print(extract_domain("a@b@c.com"))                # c.com ← đúng!
print(extract_domain("không có @"))               # None
print(extract_domain("abc@"))                     # None
