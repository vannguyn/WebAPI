import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_endpoints():
    # 1. Test GET / (Root)
    try:
        print("\Testi GET / ")
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error at GET /: {str(e)}")

    # 2. Test GET /health
    try:
        print("\n Test GET /health")
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error at GET /health: {str(e)}")

    # 3. Test POST /generate (Case: Success)
    try:
        print("\nTest POST /generate ")
        payload = {
            "prompt": "What is AI?",
            "max_tokens": 20
        }
        response = requests.post(f"{BASE_URL}/generate", json=payload)
        print(f"Status: {response.status_code}")
        print(f"Result: {response.json().get('result')}")
    except Exception as e:
        print(f"Error at POST /generate: {str(e)}")

    # 4. Test POST /generate (Case: Empty prompt - Error Handling)
    try:
        print("\nTest POST /generate (Empty prompt)")
        payload = {"prompt": "", "max_tokens": 10}
        response = requests.post(f"{BASE_URL}/generate", json=payload)
        print(f"Status: {response.status_code} (Expected 400)")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error during validation test: {str(e)}")

    print("\n--- Test Completed ---")

if __name__ == "__main__":
    test_endpoints()