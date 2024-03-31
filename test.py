import unittest
import requests

class TestWebsiteLoading(unittest.TestCase):

    def test_atg_world_website_loading(self):
        url = "https://atg.world"
        print("Connecting to", url)
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for non-200 status codes
            print("Status code:", response.status_code)
            self.assertEqual(response.status_code, 200, "atg.world website did not load properly")
            print("atg.world website loaded successfully!")
        except requests.RequestException as e:
            print("Error connecting to the atg.world website:", e)
            self.fail("Failed to load the atg.world website")

    def test_www_domain_hello_world(self):
        url = "http://www.example.com"  # Replace with the actual www domain
        print("Connecting to", url)
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for non-200 status codes
            print("Status code:", response.status_code)
            self.assertEqual(response.status_code, 200, "Hello world on www domain did not load properly")
            print("Hello world on www domain loaded successfully!")
        except requests.RequestException as e:
            print("Error connecting to the www domain:", e)
            self.fail("Failed to load hello world on www domain")

if __name__ == '__main__':
    unittest.main()
