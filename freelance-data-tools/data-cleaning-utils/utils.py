import re
import pandas as pd
from typing import Optional


def is_valid_email(email: str) -> bool:
    """Kiểm tra email hợp lệ (quy tắc cơ bản nhưng cực kỳ hiệu quả)."""
    if not isinstance(email, str) or '@' not in email:
        return False
    parts = email.split('@', 1)
    if len(parts) != 2:
        return False
    local_part, domain_part = parts
    if len(local_part) == 0:
        return False
    if '.' not in domain_part:
        return False
    if len(domain_part.split('.')[-1]) < 2:
        return False
    return True


def clean_salary(salary_str: Optional[str]) -> Optional[float]:
    """Chuyển mọi định dạng lương bẩn → float sạch hoặc None."""
    if salary_str is None or str(salary_str).strip() == "":
        return None

    text = str(salary_str).strip().lower()
    if text in {"n/a", "na", "null", "-"}:
        return None

    text = re.sub(r'[^0-9.kK]', '', text)
    if text.endswith('k'):
        text = text[:-1] + '000'

    try:
        return float(text)
    except ValueError:
        return None


def extract_domain(email: str) -> Optional[str]:
    """Trích xuất domain từ email (sau @ cuối cùng)."""
    if not is_valid_email(email):
        return None
    return email.split('@')[-1]


def remove_outliers_iqr(
    df: pd.DataFrame,
    col: str,
    whisker: float = 1.5,
    max_multiplier: float = 10.0
) -> pd.DataFrame:
    """
    Loại bỏ outliers bằng IQR + bảo vệ chống dữ liệu skewed nặng.
    Trả về DataFrame MỚI (không sửa gốc).
    """
    if col not in df.columns:
        raise ValueError(f"Cột '{col}' không tồn tại")
    if not pd.api.types.is_numeric_dtype(df[col]):
        raise ValueError(f"Cột '{col}' phải là kiểu số")

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - whisker * IQR
    upper = Q3 + whisker * IQR

    median_val = df[col].median()
    extreme_upper = median_val * max_multiplier

    mask = df[col].between(lower, min(upper, extreme_upper))

    removed = (~mask).sum()
    print(f"Loại bỏ {removed:,} outliers khỏi '{col}' "
          f"(IQR {whisker=}, max {max_multiplier}x median) → "
          f"giữ lại {mask.mean()*100:.1f}% dữ liệu")

    return df[mask].copy()
