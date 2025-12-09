#!/usr/bin/env python3
import requests
import json
import sys

# Configuration - CHANGE THESE
STUDENT_ID = "22g9lq61e8"  # Your student ID
GITHUB_REPO_URL = "https://github.com/22A91A61E8/divya-2fa-service"
API_ENDPOINT = "https://eajeyq4r3zljoq4rpovy2nthda0vtjqf.lambda-url.ap-south-1.on.aws/"

print("\n" + "=" * 70)
print("GETTING ENCRYPTED SEED FROM INSTRUCTOR API")
print("=" * 70)

# Load your public key
print(f"\n[1] Loading public key...")
try:
    with open("student_public.pem", "r") as f:
        public_key = f.read()
    print(f"    [OK] Public key loaded ({len(public_key)} chars)")
except FileNotFoundError:
    print("    [ERROR] student_public.pem not found!")
    sys.exit(1)

# Prepare request
print(f"\n[2] Preparing API request...")
print(f"    Student ID: {STUDENT_ID}")
print(f"    GitHub Repo: {GITHUB_REPO_URL}")

payload = {
    "student_id": STUDENT_ID,
    "github_repo_url": GITHUB_REPO_URL,
    "public_key": public_key
}

# Call API
print(f"\n[3] Calling instructor API...")
print(f"    Endpoint: {API_ENDPOINT}")

try:
    response = requests.post(API_ENDPOINT, json=payload, timeout=15)
    
    print(f"    HTTP Status: {response.status_code}")
    
    result = response.json()
    
    if "encrypted_seed" in result:
        encrypted_seed = result["encrypted_seed"]
        
        print(f"\n[4] Saving encrypted seed...")
        print(f"    Length: {len(encrypted_seed)} characters")
        
        # Save to file
        with open("encrypted_seed.txt", "w") as f:
            f.write(encrypted_seed)
        
        print(f"    [OK] Saved to encrypted_seed.txt")
        
        print(f"\n[5] Verification:")
        print(f"    First 50 chars: {encrypted_seed[:50]}...")
        print(f"    Last 50 chars: ...{encrypted_seed[-50:]}")
        
        print("\n" + "=" * 70)
        print("SUCCESS!")
        print("=" * 70)
    else:
        print(f"\n[ERROR] {result}")
        sys.exit(1)
        
except Exception as e:
    print(f"    [ERROR] {e}")
    sys.exit(1)
