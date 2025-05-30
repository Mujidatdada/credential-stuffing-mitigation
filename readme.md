# Credential Stuffing Mitigation on Fintech APIs using AWS WAF

## Project Overview

This project demonstrates how to mitigate credential stuffing attacks on fintech APIs by leveraging AWS WAF's rate-based rules and logging features. It includes a vulnerable Flask API, a Python script to simulate credential stuffing attacks, and AWS infrastructure configuration to protect the API.

## Project Goals

- Implement rate-limiting on API requests using AWS WAF to block or throttle suspicious activity.
- Enable AWS WAF logging to CloudWatch to monitor and analyze attack patterns.
- Provide a reproducible attack simulation to validate the effectiveness of protections.

## Technologies Used

- AWS WAF (Web Application Firewall)
- AWS CloudWatch Logs
- Python (Flask API & attack simulation)
- Wireshark (network traffic analysis)

## Setup & Installation

1. **Deploy the Flask API:**

   # (example) Run locally
   python app.py

2. **Configure AWS WAF:**

Create a WebACL with rate-based rules (e.g., limit to 5 requests per minute).

Attach the WebACL to your Application Load Balancer (ALB).

Create CloudWatch log groups for WAF logs.

Assign necessary IAM permissions to allow WAF to write logs.

3. **Run the attack simulator:**
python attack_simulator.py --target http://localhost:5000/login

## Testing the WAF Rule ##

The WAF rate-based rule has been configured but is not yet tested with live attack traffic.

Planned to simulate credential stuffing attacks once logging confirms correct setup.

Testing will verify if WAF blocks or rate-limits suspicious requests as expected.

## Troubleshooting & Current Status ##
WAF logs are currently not appearing in CloudWatch despite configuration.

Verified:

WebACL is attached to ALB.

IAM permissions for logging are set.

Log groups created in CloudWatch.

Manual API calls have not triggered WAF, so logs do not appear.

Seeking guidance on debugging AWS WAF logging pipelines.
