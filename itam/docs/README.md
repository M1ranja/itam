# پروژه مدیریت دارایی‌های فناوری اطلاعات (ITAM)

## ساختار پروژه
itam_project/
├── app/                            # منطق اصلی پروژه
│   ├── models/                     # مدل‌های داده‌ای (مثلاً ITAsset)
│   │   └── asset.py
│   ├── services/                   # سرویس‌های مدیریتی (منطق تجاری)
│   │   └── asset_service.py
│   └── interfaces/                # رابط‌های ورودی/خروجی (API و رابط‌ها)
│       └── api.py
│
├── docs/                           # مستندات پروژه
│   ├── README.md                   # راهنمای اجرای پروژه (فایل فعلی)
│   ├── CHANGES.md                 # گزارش تغییرات و نسخه‌ها
│   ├── SQM.md                      # گزارش شاخص‌های کیفیت کد
│   ├── test_report.md              # گزارش اجرای تست‌ها
│   └── DOCUMENTS_INDEX.md         # فهرست مستندات پروژه
│
├── tests/                          # تست‌های پروژه
│   ├── test_unit_asset_service.py         # تست‌های واحد برای سرویس‌ها
│   ├── test_integration_api.py            # تست‌های یکپارچه‌سازی برای API
│   └── test_behavior_asset_flow.py        # تست‌های رفتاری (جریان واقعی کار)
│
├── main.py                         # نقطه شروع اجرای پروژه با Uvicorn
├── requirements.txt                # لیست کتابخانه‌های مورد نیاز (FastAPI و ...)

---

## نحوه اجرا

1. نصب پکیج‌ها:
    ```bash
    pip install -r requirements.txt
    ```

2. اجرای پروژه:
    ```bash
    uvicorn app.interfaces.api:app --reload
    ```

پروژه روی `http://127.0.0.1:8000` اجرا می‌شود.


 مستندات خودکار OpenAPI در آدرس زیر در دسترس است:

    ```
    http://127.0.0.1:8000/docs
    ```
---

## نحوه اجرای تست‌ها (اختیاری)

اگر می‌خواهید تست‌ها را اجرا کنید، ابتدا `pytest` را نصب کنید:

```bash
pip install pytest


2. اطمینان از تنظیم مسیر ماژول‌ها (در ویندوز PowerShell):

    ```bash
    $env:PYTHONPATH = "."
    pytest
    ```

    یا در CMD:

    ```cmd
    set PYTHONPATH=.
    pytest
    ```

    در صورت موفقیت، پیغام `7 passed` یا مشابه آن نمایش داده خواهد شد.

---

## تکنولوژی‌های استفاده‌شده

- Python 3.13+
- FastAPI
- Pydantic
- Uvicorn
- pytest
- httpx (برای تست‌های API)
- Starlette (بخش زیرساخت FastAPI)

---


