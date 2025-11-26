import numpy as np

exam_scores = np.array([
    [85, 92, 78],  # Student 1 (Math, Physics, Chemistry)
    [90, 88, 95],  # Student 2
    [75, 80, 82]   # Student 3
])
# Tính tổng điểm trung bình của các học sinh
average_scores = np.mean(exam_scores, axis=0)
print(f"Điểm trung bình theo môn học:\n {average_scores}" )
# Tổng điểm của các học sinh
total_scores = np.sum(exam_scores, axis=1)
print(f"Tổng điểm của các học sinh: \n {total_scores}")
# Tạo 1 ma trận đơn vị
I_3x3 = np.identity(3)
# Tích 2 ma trận
result = exam_scores@I_3x3
print(f"Kết quả tích 2 ma trận:\n {result}")