

# Mini SOC Lab: SSH Login Detection

**Status:** In Progress
**Category:** Cybersecurity | Security Monitoring | Python | Linux

## Overview

This project is a hands-on cybersecurity lab built to explore how a Security Operations Center (SOC) monitors systems and detects suspicious login activity.

Using an Ubuntu virtual machine, I am building a Python-based detector that reads SSH authentication logs, counts failed login attempts by source IP address, and raises an alert when an IP reaches a defined threshold.

## Objectives

* Understand Linux authentication logs and SSH services.
* Generate controlled failed-login events in a virtual lab.
* Use Python to parse and analyze security logs.
* Group failed login attempts by source IP address.
* Trigger alerts when repeated failed attempts exceed a threshold.
* Practice troubleshooting and documenting security tools.

## Lab Environment

* **Operating system:** Ubuntu Linux
* **Virtualization:** Oracle VirtualBox
* **Target machine:** `ubuntu-victim`
* **Programming language:** Python 3
* **Log source:** systemd journal
* **Service monitored:** OpenSSH

## Planned Features

* Read SSH authentication events.
* Identify failed password attempts.
* Extract source IP addresses.
* Count attempts within a defined time window.
* Alert when an IP reaches five failed attempts.

## Progress

* [x] Set up the Ubuntu virtual machine in VirtualBox.
* [x] Start the SSH service.
* [x] Generate controlled failed SSH login events.
* [x] Identify failed-password events in the system journal.
* [x] Build a Python detector for failed SSH logins.
* [x] Extract source IP addresses and count failed attempts.
* [x] Implement a ten-minute lookback window.
* [x] Verify alert generation at the five-attempt threshold.
* [ ] Implement continuous monitoring of new SSH events.
* [ ] Test that events outside the detection window do not trigger alerts.
* [ ] Improve error handling and document further test results.

**Current status:** The Python detector successfully counts failed-password events by source IP within a ten-minute lookback window and raises an alert when the threshold of five attempts is reached. Continuous monitoring is not yet implemented.


### Milestone 1: SSH Failed-Login Detection

**Status:** Completed and tested

Implemented a Python script that reads SSH authentication events from the Ubuntu system journal, identifies failed-password events, extracts source IP addresses, and counts attempts by IP.

**Test scenario:** Generated five controlled failed SSH login events from the local machine.

**Expected result:** An alert when an IP reaches five failed attempts.

**Observed result:**

```text
Total failed-password events: 5
IP: 127.0.0.1 | Failed attempts: 5
[ALERT] 127.0.0.1 has 5 failed attempts!
```

**Outcome:** The detector successfully identified the five events, grouped them under the source IP, and triggered the expected alert.

**Current limitation:** The script counts matching events since midnight rather than using a rolling time window. It also scans existing journal entries when run, rather than continuously monitoring new events.

**Next improvement:** Implement a configurable rolling time window and test how the detector handles events outside that window.


## Security and Testing

All login tests are performed in a controlled virtual lab. The initial failed-login test uses the loopback address `127.0.0.1`, which refers to the local machine.

This project is for educational purposes and does not involve testing systems without authorization.

## Lessons Learned

This section will document troubleshooting findings, how the log source was identified, and how the detection logic was tested and improved.

## Future Improvements

* Detect repeated login attempts over configurable time windows.
* Improve log parsing and error handling.
* Export alerts to a structured log or report.
* Explore additional security monitoring and incident response techniques.

## Disclaimer

This is a learning project and is not intended to replace a production security monitoring system.
