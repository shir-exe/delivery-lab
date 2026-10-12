import unittest
from app import health_payload


class TestHealth(unittest.TestCase):

    def test_health_payload_status(self):
        actual_payload = health_payload()
        self.assertEqual(actual_payload["status"], "ok")

    def test_health_payload_version(self):
        actual_payload = health_payload()
        self.assertIn("version", actual_payload)


if __name__ == "__main__":
    unittest.main()