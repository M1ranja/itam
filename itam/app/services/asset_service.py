
from app.models.asset import ITAsset

class AssetService:
    """
    سرویس مدیریت دارایی‌ها در حافظه.

    دارایی‌ها به صورت دیکشنری با کلید شناسه ذخیره می‌شوند.
    """
    def __init__(self):
        self.assets = {}

    def create_asset(self, asset: ITAsset) -> ITAsset:
        """
        ایجاد و ذخیره یک دارایی جدید.

        Args:
            asset (ITAsset): دارایی جدید برای ذخیره

        Returns:
            ITAsset: دارایی ذخیره شده
        """
        self.assets[asset.id] = asset
        return asset

    def get_asset(self, asset_id: str) -> ITAsset | None:
        """
        بازیابی دارایی بر اساس شناسه.

        Args:
            asset_id (str): شناسه دارایی

        Returns:
            ITAsset | None: دارایی یافت شده یا None در صورت عدم وجود
        """
        return self.assets.get(asset_id, None)
