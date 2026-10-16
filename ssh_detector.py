
#!/usr/bin/env python3

import subprocess
import re
from collections import Counter

THRESHOLD = 5

result = subprocess.run(
    [
        "journalctl",
        "-u", "ssh",
        "--since", "10 minutes ago",
        "--no-pager",
        "-o", "cat",
    ],
    capture_output=True,
    text=True,
)

if result.returncode != 0:
    print("Could not read SSH logs.")
    print(result.stderr)
    raise SystemExit(1)

failed_lines = [
    line for line in result.stdout.splitlines()
    if "Failed password" in line
]

ip_counts = Counter()

for line in failed_lines:
    match = re.search(r"from (\d{1,3}(?:\.\d{1,3}){3})", line)
    if match:
        ip_counts[match.group(1)] += 1

print("=== MINI SOC: SSH DETECTOR ===")
print(f"Total failed-password events: {len(failed_lines)}")

if not ip_counts:
    print("No source IPs found in failed-password events.")

for ip, count in ip_counts.most_common():
    print(f"IP: {ip} | Failed attempts: {count}")

    if count >= THRESHOLD:
        print(f"[ALERT] {ip} has {count} failed attempts!")
    else:
        print(f"[INFO] {ip} is below the threshold.")
