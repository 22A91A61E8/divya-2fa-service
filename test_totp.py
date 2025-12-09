from pathlib import Path
from totp_utils import generate_totp_code, verify_totp_code

hex_seed = Path("seed.txt").read_text().strip()
code = generate_totp_code(hex_seed)
print("Code:", code)
print("Valid?", verify_totp_code(hex_seed, code))
