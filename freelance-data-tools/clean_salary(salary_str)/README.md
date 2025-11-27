# Mini Project: Data Cleaning Utils for Freelance Data Analyst

Hàm Python cực mạnh giúp làm sạch dữ liệu lương – thứ mà khách hàng freelancer trả $300–$800 để bạn làm mỗi ngày!

### clean_salary() – Vũ khí kiếm tiền số 1
```python
clean_salary("$50,000.00")     → 50000.0
clean_salary("  75k  ")        → 75000.0
clean_salary("100,000 VND")    → 100000.0
clean_salary("N/A")            → None