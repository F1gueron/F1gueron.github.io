---
layout: post
title: "GreenHorn"
date: 2024-07-23 18:58:00 +0100
categories: [writeup, easy]
tags: [machine, web-exfiltration]
---

<p>
    <a href="https://app.hackthebox.eu/machines/617">
        <img src="https://labs.hackthebox.com/storage/avatars/b7d9a9b075fd49c8509866fe24f58dbb.png" width="500"
        alt="Descripción">
    </a>
</p>


# Sea Writeup

## Table of Contents
1. [Service Enumeration](#1-service-enumeration)
2. [Web Recon](#2-web-recon)
3. [Exploiting CVE-2023-30253](#3-exploiting-cve-2023-30253)
4. [Lateral Movement](#4-lateral-movement)
5. [Privilege Escalation](#5-privilege-escalation)

## 1. Service Enumeration

As usual, we start with an Nmap scan to identify open ports and services.

We can find ports 22, 80 and 3000 open, so lets dig deeper into them.

## 2. Web Recon

### Port 80

At port 80, we land at this page:

<p>
    <img src="assets/img/writeupImgs/greenhorn/1_682nYEuoPoQoCulJJN4c0Q.webp" width="700"
    alt="Descripción">
</p>



This contains nothing more than a static page and a login page, in which we can test the default credentials but wont give us anything, so lets move onto port 3000.

### Port 3000

In this port, we land here:

<p>
    <img src="assets/img/writeupImgs/greenhorn/1_a4CNbUWlKD8Mw2VAggjTuA.webp" width="700"
    alt="Descripción">
</p>

After a bit of searching, we can find a pass.php inside GreenAdmin repository. 
``data/settings/pass.php``

<p>
    <img src="assets/img/writeupImgs/greenhorn/1_bqvusxcQsuymXqQdHDZggQ.webp" width="700"
    alt="Descripción">
</p>

We can see this is a hash, so we should try to decode it with hashcat or john.

After decoding it with **rockyou**, we can see the password is ``iloveyou1``. This is the password for the first login page.

<p>
    <img src="assets/img/writeupImgs/greenhorn/1_Tb80_TsYddOEegQzJg3LoQ.webp" width="700"
    alt="Descripción">
</p>

In this page, we can identify the modules section, and after trying to upload a reverse shell, the throws an error that only .zip can be uploaded, we can search in [this github](https://github.com/pentestmonkey/php-reverse-shell?source=post_page-----48a6d80366ca--------------------------------) a way to get a reverse shell with a .zip file.

After uploading the reverse shell, we can get a shell as www-data.

## 3. Lateral Movement

As www-data, we cant see the user.txt file, so we need to get a shell as the user ``junior`` which we can see has a home directory.

We can try to get a shell as junior with the password we found before, this will give us a shell as junior and now we can read the user.txt file.

## 4. Privilege Escalation

Here, we can see a file called ``OpenVas.pdf`` which contains a blurred password.

<p>
    <img src="assets/img/writeupImgs/greenhorn/1_ERXj35wPyOIuIrMxt6JA4w.webp" width="700"
    alt="Descripción">
</p>

We can use [this tool](https://github.com/spipm/Depix) to get the password. 

<p>
    <img src="assets/img/writeupImgs/greenhorn/1_EnQASSdXYIjMBIUKoj1HMg.webp" width="700"
    alt="Descripción">
</p>

This password would let us log in as **root** and get the root flag.

Done!!