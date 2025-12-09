 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import sys
import os

print("=" * 60)
print("SEED VALIDATION SCRIPT")
print("=" * 60)

# Check encrypted seed
try:
    with open("encrypted_seed.txt", "r") as f:
        encrypted = f.read().strip()
    
    print("\n[OK] Encrypted seed file found")
    print(f"  Length: {len(encrypted)} characters")
    print(f"  First 50 chars: {encrypted[:50]}...")
    print(f"  Last 10 chars: ...{encrypted[-10:]}")
    
    # Validate base64
    try:
        encrypted_clean = "".join(encrypted.split())
        missing_padding = len(encrypted_clean) % 4
        if missing_padding:
            encrypted_clean += "=" * (4 - missing_padding)
        decoded = base64.b64decode(encrypted_clean)
        print(f"  [OK] Valid base64 (decodes to {len(decoded)} bytes)")
        print(f"  [OK] Ciphertext byte length: {len(decoded)} (expected ~256 for RSA-4096)")
    except Exception as e:
        print(f"  [ERROR] Invalid base64: {e}")
        
except FileNotFoundError:
    print("[ERROR] encrypted_seed.txt not found!")
    sys.exit(1)

# Check decrypted seed
if os.path.exists("/data/seed.txt"):
    try:
        with open("/data/seed.txt", "r") as f:
            hex_seed = f.read().strip()
        
        print(f"\n[OK] Decrypted seed file found at /data/seed.txt")
        print(f"  Length: {len(hex_seed)} characters")
        print(f"  Content: {hex_seed}")
        
        # Validate hex format
        if len(hex_seed) == 64:
            print(f"  [OK] Length is correct (64 characters)")
        else:
            print(f"  [ERROR] Length is wrong (expected 64, got {len(hex_seed)})")
        
        if all(c in "0123456789abcdef" for c in hex_seed.lower()):
            print(f"  [OK] Contains only valid hex characters (0-9, a-f)")
        else:
            print(f"  [ERROR] Contains invalid characters")
            
    except FileNotFoundError:
        print("[ERROR] /data/seed.txt not found!")
else:
    print(f"\n[WARNING] /data/seed.txt not found!")
    print("  (Run /decrypt-seed endpoint first or check if running in Docker)")

print("\n" + "=" * 60)
