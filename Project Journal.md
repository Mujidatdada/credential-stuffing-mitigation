Project Update: Mitigating Credential Stuffing Attacks on Fintech APIs

Project Goals

The core objective of this project is to mitigate credential stuffing attacks on a fintech-style API using:

AWS WAF: to detect and block abnormal request patterns.

CloudWatch Logs: for visibility into WAF activity.

Python Scripts: to simulate credential stuffing attempts.

Wireshark: for low-level traffic analysis.

Original Objective: Mitigate credential stuffing attacks on fintech APIs using AWS WAF logging and rate-limiting.

Progress So Far

Phase 1: Research

Conducted foundational research on credential stuffing:

Referenced OWASP Top 10 and Verizon DBIR findings.

Identified attack patterns and detection strategies.

Phase 2: Attack Simulation

Developed a vulnerable Flask API simulating a login endpoint.

Wrote Python scripts to simulate credential stuffing via repeated login attempts.

Captured network traffic with Wireshark to analyze request rates. (I encountered a roadblock here, but after trouble shooting including trying other alternatives like TCPdump, i was able to successfully capture the traffic after changing the interface from "Wi-Fi" to "Adapter for loopback")

Phase 3: AWS WAF Integration

Created a rate-based rule in AWS WAF:
"Conditions: >5 requests/minute from a single IP
Action: BLOCK
Scope: REGIONAL (attached to ALB)"

Current Roadblock

Despite proper configuration, no WAF logs are appearing in CloudWatch Logs.

Attempted Configuration

Created log group: aws-waf-logs-credstuff-defense

IAM policy: AWSWAFLoggingPolicy (allows logs:PutLogEvents)

Ran CLI command:
"aws wafv2 put-logging-configuration \
  --logging-configuration file://logging-config.json \
  --region eu-north-1"

 "An error occurred (WAFInvalidParameterException) when calling the PutLoggingConfiguration operation: Error reason: The ARN isn't valid. A valid ARN begins with arn: and includes other information separated by colons or slashes., field: LOG_DESTINATION, parameter: arn:aws:logs:eu-north-1:619071353592:log-group:CredStuffDefenseLogs"

I HAVE TRIED TROUBLESHOOTING

WebACL scope set to REGIONAL 

WebACL correctly attached to ALB

IAM permissions for WAF logging

Log group name and ARN in config match

Key Question

How can I debug AWS WAF → CloudWatch Logs pipeline when logs do not appear despite correct configuration?

**Possible Areas to Explore**

AWS WAF internal delays?

Region mismatch?

Alternative logging destinations (e.g., Kinesis Data Firehose)?

AWS Support best practices for WAF log delivery troubleshooting?

**In addition to the logging issue, I’ve encountered another critical problem:**

Manual or scripted credential stuffing attempts are not triggering the WAF rule.

Context
A rate-based rule is set to block IPs with >5 requests per minute.
I used a Python script (stimulate_attack.py) to send 10 rapid login requests with the same invalid credentials.
Requests are reaching the API (confirmed via Flask logs and Wireshark).
But no WAF blocks occur, and requests are not counted toward the rate-based rule.

If you've encountered this issue and resolved it, please share your insights.
