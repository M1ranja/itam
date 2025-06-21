
import unittest
from fastapi.testclient import TestClient
from app.interfaces.api import app

client = TestClient(app)

class TestAssetBehavior(unittest.TestCase):
    def test_full_asset_flow(self):
        asset = {
            "id": "behav-001",
            "type": "Router",
            "purchase_date": "2024-05-01",
            "status": "active"
        }

        # Given: Asset data آماده است

        # When: دارایی اضافه می‌شود
        response_post = client.post("/assets", json=asset)
        self.assertEqual(response_post.status_code, 200)

        # Then: باید بتوان دارایی را بازیابی کرد
        response_get = client.get(f"/assets/{asset['id']}")
        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(response_get.json(), asset)

        # When: درخواست دارایی با id ناموجود
        response_not_found = client.get("/assets/invalid-id")
        self.assertEqual(response_not_found.status_code, 404)

if __name__ == "__main__":
    unittest.main()
