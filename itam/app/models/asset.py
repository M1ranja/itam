
from pydantic import BaseModel
from datetime import date

class ITAsset(BaseModel):
    """
    مدل نماینده دارایی فناوری اطلاعات (IT Asset).

    Attributes:
        id (str): شناسه یکتا دارایی
        type (str): نوع دارایی (مانند Laptop، Monitor و ...)
        purchase_date (date): تاریخ خرید دارایی به فرمت YYYY-MM-DD
        status (str): وضعیت دارایی (active, inactive, ... )
    """
    id: str
    type: str
    purchase_date: date
    status: str
