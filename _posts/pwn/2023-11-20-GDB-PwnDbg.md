---
layout: page
title: "Introduction to GDB PwnDbg"
date: 2023-11-20 12:00:00 -0000
categories: [tools]
tags: [gdb, pwn]
permalink: /pwn/gdb-pwndbg/
---

## Introduction

In this post, we will explore the integration of GDB with PwbDbg and how it can enhance your debugging experience.

## Setting Up

To get started, ensure you have both GDB and PwbDbg installed on your system. Follow these steps to set up the environment:

1. Install GDB:
    ```sh
    sudo apt-get install gdb
    ```

2. Install PwbDbg:
    ```sh
    # Installation instructions for PwbDbg
    ```

## Basic Usage

Here are some basic commands to get you started with GDB and PwbDbg:

```bash
gdb-pwndbg <./file>
```

```bash
gdb-pwndbg 
file <fiel>
```

Functions:

```bash
info funtions
disassemble <function>
break <function> #breakpoint
x $eax #shows stack
next #or n   next instruction
continue
delete <breakpoint>
break *<function>+<instructionNumber>
x $<memory adress> #to see value
set <memory adress> = <value>
```

Use cyclic to find the offset:

```bash
Cyclic -l <chain> #in x86 8 bytes, in x64 16 bytes #there is a pwntools template to automate it
```

- x86:
    
    We can find the return address in the EIP
    
- x64:
    
    We can find the return address in the 8 first bytes of RSP