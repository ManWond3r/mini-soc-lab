

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

* [x] Set up the Ubuntu virtual machine.
* [x] Start the SSH service.
* [x] Generate a controlled failed SSH login.
* [x] Observe authentication failure events in system logs.
* [ ] Resolve the log-filtering issue in the Python detector.
* [ ] Implement and verify IP-based counting.
* [ ] Test the five-attempt alert threshold.
* [ ] Document test results and lessons learned.

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
