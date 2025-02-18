---
layout: post
title: "UnderPass"
date: 2025-02-18 09:00:00 +0100
categories: [writeup, easy]
tags: [machine]
---
<p>
    <a href="https://app.hackthebox.com/machines/641">
        <img src="https://labs.hackthebox.com/storage/avatars/456a4d2e52f182847fb0a2dba0420a44.png" width="500"
        alt="Descripción">
    </a>
</p>

# UnderPass Writeup

## Table of Contents

1. [Service Enumeration](#1-service-enumeration)
2. [Web Recon](#2-web-recon)
3. [Radius UI](#3-radius-ui)
4. [Privilege Escalation](#4-privilege-escalation)

## 1. Service Enumeration

First, we start with the usual `nmap`. As usual, we have port 80 open, so we add it to /etc/hosts and navigate to the page. 
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213112515.png" width="700"
    alt="Descripción">
</p>

## 2. Web Recon

We land onto a page that displays the Apache2 Default Page.
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250218091510.png" width="700"
    alt="Descripción">
</p>
As we can't do anything here, we start looking for subdomains and web directory searching.
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213112506.png" width="700"
    alt="Descripción">
</p>
We don't find any valid subdomain or directory to search. So we go one step back and do another port enumeration, in this case, UDP ports.
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213112349.png" width="700"
    alt="Descripción">
</p>
As we can see, we find port 161, which belongs to SNMP open, so we start to enumerate this service and start to search for some info.
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213112306.png" width="700"
    alt="Descripción">
</p>
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213112605.png" width="700"
    alt="Descripción">
</p>
Here, the port is giving us a clue, and it's saying that it has a [daloradius server](https://www.daloradius.com/), and after searching what this is, we start looking for that server in the web server.
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213112621.png" width="700"
    alt="Descripción">
</p>
In the first search, we can find a docker-compose.yml and looking at it, we can find some credentials, but I tried them on the SSH and none of them work, so we continue the dirsearch.
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213112833.png" width="700"
    alt="Descripción">
</p>

Finally, we find a login page. Here I tried all the password combinations from the .yml from before, but as in the SSH, none worked, so the next step we take is to look for the default credentials and test them. It worked!!
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213113132.png" width="700"
    alt="Descripción">
</p>
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250217162626.png" width="700"
    alt="Descripción">
</p>

## 3. Radius UI

<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250217162558.png" width="700"
    alt="Descripción">
</p>

After a long time of trying different things and getting comfortable with the Radius UI, I found the user listing page and tried to create a new user to log in to the page and see that page as a normal user, but it didn't work. So I tried to crack the password of the user **svcMosh**.
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213120007.png" width="700"
    alt="Descripción">
</p>
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213120236.png" width="700"
    alt="Descripción">
</p>
With `Hashcat` it is super easy to crack it, and trying to log in to SSH with these credentials will work and will let us take the user flag.

## 4. Privilege Escalation

For privilege escalation, as always, the first thing is to see if we have some sudo permissions by the command `sudo -l`.
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250218091613.png" width="700"
    alt="Descripción">
</p>

As we can see, mosh-server can be run as sudo for this user, so that will be the privilege escalation vector.

After a bit of researching of mosh and mosh-server, with the proper syntax, it is a very simple command to get a shell with root user, so we just run this command and get the root flag.
<p align="center">
    <img src="assets/img/writeupImgs/underpass/Pasted image 20250213122427.png" width="700"
    alt="Descripción">
</p>

Done!!
