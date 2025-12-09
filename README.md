# PKI-Based 2FA Microservice

A lightweight and secure microservice for two-factor authentication using RSA encryption and TOTP codes, packaged with Docker and suitable for cloud-native systems.

---

## Features

- RSA 4096-bit encryption for secure TOTP seed exchange
- TOTP-based 2FA generation and validation (RFC 6238)
- REST API for decrypting seeds, generating codes, and verifying tokens
- Containerized using Docker for consistent deployment
- Persistent Docker volumes for storing decrypted seeds and logs
- Automated cron job for scheduled TOTP logging
- Multi-stage Docker build for optimized image size

---

## Tech Stack

- Python 3.11+
- FastAPI or Flask (based on your implementation)
- pyotp
- cryptography (RSA)
- Docker & Docker Compose

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/22A91A61E8/pki-2fa-microservice.git
cd pki-2fa-microservice
2. Install dependencies (local development)
bash
Copy code
pip install -r requirements.txt
3. Generate RSA Keys
bash
Copy code
openssl genpkey -algorithm RSA -out student_private.pem -pkeyopt rsa_keygen_bits:4096
openssl rsa -pubout -in student_private.pem -out student_public.pem
Use the public key to request the encrypted TOTP seed.

Running with Docker Compose
bash
Copy code
docker-compose build
docker-compose up -d
Service URL:

arduino
Copy code
http://localhost:8000
API Endpoints
Method	Endpoint	Description
POST	/decrypt-seed	Decrypts RSA-encrypted seed
GET	/generate-2fa	Generates the current TOTP code
POST	/verify-2fa	Verifies a TOTP code
GET	/health	Health check endpoint

Example Usage
Generate current TOTP
bash
Copy code
curl http://localhost:8000/generate-2fa
Verify a TOTP code
bash
Copy code
curl -X POST http://localhost:8000/verify-2fa \
  -H "Content-Type: application/json" \
  -d '{"code":"123456"}'
Student Information
Name: Divya Eeli
Roll No: 22A91A61E8

