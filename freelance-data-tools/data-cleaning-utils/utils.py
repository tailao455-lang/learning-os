import re
from typing import Optional

def is_valid_email(email: str) -> bool:
    """Kiểm tra email hợp lệ theo quy tắc cơ bản."""
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
    """Dọn sạch lương bẩn → float hoặc None."""
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
