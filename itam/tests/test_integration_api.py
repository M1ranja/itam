
import unittest
from fastapi.testclient import TestClient
from app.interfaces.api import app

client = TestClient(app)

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.asset_data = {
            "id": "001",
            "type": "Monitor",
            "purchase_date": "2024-01-01",
            "status": "active"
        }

    def test_add_asset(self):
        response = client.post("/assets", json=self.asset_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.asset_data)

    def test_get_asset_success(self):
        client.post("/assets", json=self.asset_data)
        response = client.get(f"/assets/{self.asset_data['id']}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.asset_data)

    def test_get_asset_not_found(self):
        response = client.get("/assets/nonexistent")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Asset not found")

if __name__ == "__main__":
    unittest.main()
