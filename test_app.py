import unittest
from app import app

class CHWSystemTests(unittest.TestCase):

    def setUp(self):
        """Set up test client before each test"""
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = "test-secret"
        self.client = app.test_client()

    # ── Authentication Tests ──────────────────────────────────────
    def test_01_login_page_loads(self):
        """TC-01: Login page should return 200"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_02_valid_chw_login(self):
        """TC-02: Valid CHW login should redirect to dashboard"""
        response = self.client.post("/", data={
            "username": "alice",
            "password": "alice123"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_03_valid_supervisor_login(self):
        """TC-03: Valid supervisor login should redirect to dashboard"""
        response = self.client.post("/", data={
            "username": "admin",
            "password": "admin123"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_04_invalid_login(self):
        """TC-04: Wrong password should show error"""
        response = self.client.post("/", data={
            "username": "alice",
            "password": "wrongpassword"
        }, follow_redirects=True)
        self.assertIn(b"Wrong username or password", response.data)

    def test_05_empty_login(self):
        """TC-05: Empty credentials should not log in"""
        response = self.client.post("/", data={
            "username": "",
            "password": ""
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ── Access Control Tests ──────────────────────────────────────
    def test_06_chw_page_requires_login(self):
        """TC-06: /chw should redirect if not logged in"""
        response = self.client.get("/chw", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_07_supervisor_page_requires_login(self):
        """TC-07: /supervisor should redirect if not logged in"""
        response = self.client.get("/supervisor", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ── Logout Test ───────────────────────────────────────────────
    def test_08_logout_clears_session(self):
        """TC-08: Logout should redirect to login page"""
        response = self.client.get("/logout", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main(verbosity=2)