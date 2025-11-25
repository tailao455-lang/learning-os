import numpy as np

# Bài tập 1
# Tạo array 1D (Vector)
vector_1d = np.array([1, 2, 3, 4, 5]) 
print(f"Vector: {vector_1d}")
# Output: [1 2 3 4 5]

# Tạo array 2D (Matrix)
matrix_2d = np.array([[10, 11, 12], [20, 21, 22]])
print(f"Matrix:\n{matrix_2d}")
# Output:
# [[10 11 12]
#  [20 21 22]]
print("Matrix:\n ", matrix_2d[0,1:3])




# Bài tập 2
sales_data = np.array([
    [150, 180, 170],  # Chi nhánh A: Ngày 1, Ngày 2, Ngày 3
    [130, 200, 190]   # Chi nhánh B: Ngày 1, Ngày 2, Ngày 3
])
# Tính tổng theo hàng (axis=1)
# Kết quả là một vector 1D chứa tổng doanh thu của mỗi hàng (chi nhánh)
tong_cac_chi_nhanh = sales_data.sum(axis=1)
print(f"Tổng các chi nhánh:\n {tong_cac_chi_nhanh}")
# Lấy doanh thu tất cả ngày 2 là cột 1
print("Doanh thu các chi nhánh ngày 2:\n ", sales_data[:,1])
#Tạo Vector 1D chứa tất cả và sử dụng Reshape biến thành ma trận 3 hàng x 2 cột
vector_1d = sales_data.reshape(-1)
print(f"Vector 1D:\n {vector_1d}")
matrix_2d = vector_1d.reshape(3,2)
print(f"Ma trận 3x2:\n {matrix_2d}")



# Bài tập 3
items_sold = [50, 30, 10]
unit_cost = [20000, 15000, 25000]

# Tính chi phí từng sản phẩm
items_cost = np.array(items_sold) * np.array(unit_cost)
print(f"Chi phí từng sản phẩm:\n {items_cost}")
# Tính tổng chi phí
total_cost = np.sum(items_cost)
print(f"Tổng chi phí: {total_cost}")
# Tổng trung bình
average_cost = np.mean(items_cost)
print(f"Tổng trung bình của 3 loại: {average_cost}")