# Mini SOC Lab — Testing Log

## Test 001: SSH Authentication Logging

**Objective:** Verify that Ubuntu records failed SSH authentication attempts.

**Method:** Attempted SSH logins using an invalid username against the local machine at `127.0.0.1`.

**Observed result:** The system journal recorded invalid-user events, authentication failures, and failed-password messages.

**Outcome:** Passed.

## Test 002: Failed-Login Detection

**Objective:** Verify that the Python detector can find failed-password events and group them by source IP.

**Method:** Ran `ssh_detector.py` with elevated privileges so it could read the system journal.

**Observed result:** The detector identified failed-password events and counted them under `127.0.0.1`.

**Outcome:** Passed.

## Test 003: Ten-Minute Lookback and Alert Threshold

**Objective:** Verify that the detector counts recent failed-password events and alerts when an IP reaches five attempts.

**Configuration:**

* Detection window: 10 minutes
* Alert threshold: 5 failed attempts per IP

**Method:** Generated controlled failed SSH login attempts in the local Ubuntu lab, then ran the detector.

**Observed result:**

```text
=== Mini SOC: SSH Detector ===
Detection window: 10 minutes ago
Total failed-password events: 6
IP: 127.0.0.1 | Failed attempts: 6
[ALERT] 127.0.0.1 has 6 failed attempts within detection window!
```

**Outcome:** Passed. The detector counted six matching events and raised an alert because the count exceeded the threshold.

## Current Limitations

* The script performs a lookback when manually executed; it does not continuously monitor new events.
* The current test uses the loopback address, so it validates local detection rather than detection of remote attackers.
* The ten-minute lookback needs additional testing to confirm that older events are excluded as expected.

## Next Steps

* Implement continuous monitoring.
* Test events inside and outside the ten-minute window.
* Improve alert handling and error reporting.
<img width="1152" height="1080" alt="Screenshot 2026-10-16 165036" src="https://github.com/user-attachments/assets/e0069569-b785-47ab-b4e9-b33825c2f1f0" />
