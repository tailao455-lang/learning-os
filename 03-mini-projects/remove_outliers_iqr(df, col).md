---
name: "\U0001F680 Mini Project"
about: Bắt đầu một dự án nhỏ hoàn chỉnh cho portfolio
title: "[Mini Project] Data Cleaning Utils – Loại bỏ outliers bằng IQR"
labels: enhancement, portfolio
assignees: tailao455-lang

---

### Tên dự án
Data Cleaning Utils – Bộ công cụ làm sạch dữ liệu cho Freelance Data Analyst

### Mục tiêu chính
- [x] Viết hàm remove_outliers_iqr() Loại bỏ outliers bằng IQR
- [x] Code sạch, có docstring, type hints, dễ dùng với Pandas
- [x] Tạo README đẹp để up portfolio

### Tech stack sẽ dùng
- [x] Python thuần (không cần cài thêm thư viện)
- [x] pandas

### Features chính
- [x] remove_outliers_iqr() – Loại bỏ outliers bằng IQR
- [x] Kiểm tra cột và mảng(hoặc kiểu dữ liệu) 
- [x] Công thức IQR:
      
      Q1 = df[col].quantile(0.25)
      Q3 = df[col].quantile(0.75)
      IQR = Q3 - Q1
    
      lower = Q1 - whisker * IQR
      upper = Q3 + whisker * IQR
- [x] Sử dụng median() để bắt outliers quá lớn

      median_val = df[col].median()
      extreme_upper = median_val * max_multiplier

### Deadline tự đặt
2025-11-30 → HOÀN THÀNH SỚM 100%!!!

### Link reference
https://github.com/tailao455-lang/learning-os/blob/main/freelance-data-tools/data-cleaning-utils/utils.py

