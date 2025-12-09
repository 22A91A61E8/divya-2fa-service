import requests
import json

STUDENT_ID = "22g9lq61e8"
GITHUB_REPO_URL = "https://github.com/22A91A61E8/divya-2fa-service"
API_ENDPOINT = "https://eajeyq4r3zljoq4rpovy2nthda0vtjqf.lambda-url.ap-south-1.on.aws/"

print("\n" + "=" * 70)
print("GETTING ENCRYPTED SEED FROM INSTRUCTOR API")
print("=" * 70)

print("\n[1] Loading public key...")
with open("student_public.pem", "r") as f:
    public_key = f.read()
print(f"    [OK] Public key loaded ({len(public_key)} chars)")

print("\n[2] Preparing API request...")
print(f"    Student ID: {STUDENT_ID}")
print(f"    GitHub Repo: {GITHUB_REPO_URL}")

payload = {
    "student_id": STUDENT_ID,
    "github_repo_url": GITHUB_REPO_URL,
    "public_key": public_key
}

print("\n[3] Calling instructor API...")
try:
    response = requests.post(API_ENDPOINT, json=payload, timeout=15)
    print(f"    HTTP Status: {response.status_code}")
    
    result = response.json()
    print(f"    Response keys: {list(result.keys())}")
    
    if "encrypted_seed" in result:
        encrypted_seed = result["encrypted_seed"]
        
        print("\n[4] Saving encrypted seed...")
        print(f"    Length: {len(encrypted_seed)} characters")
        
        with open("encrypted_seed.txt", "w") as f:
            f.write(encrypted_seed)
        
        print("    [OK] Saved to encrypted_seed.txt")
        
        print("\n[5] Verification:")
        print(f"    First 50 chars: {encrypted_seed[:50]}...")
        print(f"    Last 50 chars: ...{encrypted_seed[-50:]}")
        
        print("\n" + "=" * 70)
        print("SUCCESS! Encrypted seed obtained.")
        print("=" * 70)
    else:
        print(f"\n[ERROR] API response: {json.dumps(result, indent=2)}")

except Exception as e:
    import traceback
    print(f"[ERROR] {e}")
    traceback.print_exc()

