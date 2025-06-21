
import unittest
from datetime import date
from app.models.asset import ITAsset
from app.services.asset_service import AssetService

class TestAssetService(unittest.TestCase):
    def setUp(self):
        self.service = AssetService()
        self.sample_asset = ITAsset(
            id="123",
            type="Laptop",
            purchase_date=date(2023, 1, 1),
            status="active"
        )

    def test_create_asset(self):
        created = self.service.create_asset(self.sample_asset)
        self.assertEqual(created, self.sample_asset)
        self.assertIn("123", self.service.assets)

    def test_get_asset_existing(self):
        self.service.create_asset(self.sample_asset)
        found = self.service.get_asset("123")
        self.assertEqual(found, self.sample_asset)

    def test_get_asset_non_existing(self):
        found = self.service.get_asset("999")
        self.assertIsNone(found)

if __name__ == "__main__":
    unittest.main()
