import re
from typing import Optional

def clean_salary(salary_str: Optional[str]) -> Optional[float]:
    """
    Dọn sạch chuỗi lương bẩn → trả về float hoặc None.
    
    Hỗ trợ: "$50,000.00", "75k", "100,000 VND", "N/A", khoảng trắng...
    
    Examples:
        >>> clean_salary("$50,000.00")
        50000.0
        >>> clean_salary("  75k  ")
        75000.0
        >>> clean_salary("N/A")
        None
    """
    if salary_str is None or str(salary_str).strip() == "":
        return None

    text = str(salary_str).strip().lower()

    if text in {"n/a", "na", "null", "-"}:
        return None

    # Quét sạch mọi ký tự không phải số, chấm, k, K
    text = re.sub(r'[^0-9.kK]', '', text)

    # Xử lý k/K → nhân 1000
    if text.endswith('k'):
        text = text[:-1] + '000'

    try:
        return float(text)
    except ValueError:
        return None