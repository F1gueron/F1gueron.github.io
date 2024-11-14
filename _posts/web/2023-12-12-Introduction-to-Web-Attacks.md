---
title: "Introduction to Web Attacks"
date: 2023-12-12 12:00:00 -0000
categories: [web]
tags: [fundamentals, web, tools]
---

# Introduction to Web Attacks

Web attacks are malicious activities targeting websites and web applications. These attacks can lead to data breaches, unauthorized access, and other security issues. Understanding common web attacks is crucial for pentesters as this is most common attack vector.

## Common Types of Web Attacks

### 1. SQL Injection (SQLi)
SQL Injection involves inserting malicious SQL queries into input fields, allowing attackers to manipulate the database. This can lead to unauthorized data access, data modification, or even deletion.
[SQLI]({{ "/web/sqli/" | relative_url }})

### 2. Cross-Site Scripting (XSS)
XSS attacks occur when attackers inject malicious scripts into web pages viewed by other users. This can result in data theft, session hijacking, and other malicious activities.
[XSS]({{ "/web/xss/" | relative_url }})

### 3. Cross-Site Request Forgery (CSRF)
CSRF attacks trick users into performing actions they did not intend to, such as changing account settings or making unauthorized transactions, by exploiting the trust a web application has in the user's browser.

### 4. Server-Side Template Injection (SSTI)
SSTI attacks exploit vulnerabilities in server-side template engines to execute arbitrary code on the server. This can lead to data leaks, server compromise, and other security risks.
[SSTI]({{ "/web/ssti/" | relative_url }})

### 5. Local File Inclusion (LFI) and Remote File Inclusion (RFI)
LFI and RFI attacks involve including files from the server or remote locations, allowing attackers to execute arbitrary code, access sensitive information, or compromise the server.
[LFI/RFI]({{ "/web/lfi-rfi/" | relative_url }})

# Tools

Some of the most popular tools used for web attacks are:

 - [Gobuster](https://www.kali.org/tools/gobuster/)
 - [Dirb](https://www.kali.org/tools/dirb/)
 - [WFuzz](https://www.kali.org/tools/wfuzz/)
 - [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
 - [SQLMap](https://github.com/sqlmapproject/sqlmap)
 - [Gopherus](https://github.com/tarunkant/Gopherus)
 - Wappalyzer
 - Whatweb
 - BurpSuite
 - CeWL
 - WPScan 
 - Feroxbuster

## Conclusion

Web attacks pose significant risks to web applications and their users. By understanding common attack vectors and implementing preventive measures, developers can enhance the security of their applications and protect against potential threats.

