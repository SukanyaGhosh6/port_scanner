# Simple Network Port Scanner

## What’s This All About?

So, I was sitting around , thinking, “I wonder how port scanners really work?” You know, those tools that tell you if a port is open or closed on a network. You see them in action in all kinds of cybersecurity stuff, like when hackers or security researchers try to find vulnerabilities on a machine. I got really curious and decided to build my own basic port scanner to understand it better. And here we are — my very own **Simple Network Port Scanner**!

This little Python script is designed to check if certain ports on a target system are open or closed. It's not fancy, but it does the job, and it was a fun way to get my hands dirty in some basic networking and cybersecurity concepts. So, let me take you through it and show you how it works!

## How Does It Work?

At a very high level, a port scanner does one simple thing: it tries to connect to specific ports on a machine and sees if it’s successful or not. If the scanner can establish a connection to a port, that means the port is open. If it can’t connect, the port is closed. Simple enough, right?

This script does just that. I decided to keep it simple to understand the basics and get some hands-on experience with Python’s `socket` module (which is like a bridge between Python and network communication). Here’s how the script works:

1. **Targeting**: You provide the IP address (or `0.0.0.0` if you want to scan the local system), and you also specify a range of ports you want to check (from 1 to 1023 is a good start).
2. **Port Checking**: The script goes through each port in the range and attempts to connect to it.
3. **Timeout**: If the connection is successful, the script tells you that the port is open. If the connection times out, it moves on. This is done very quickly, but I set a 1-second timeout to avoid hanging around too long if a port doesn’t respond.
4. **Result**: After it finishes, you get a list of open ports.

And that’s it! It’s like sending a little “hello” to a port and seeing if it answers.

## Features

- **Simple Port Scanning**: It checks if ports in a specified range are open or closed.
- **Speedy Scan**: The scan runs pretty quickly (even with a fair range of ports) because it moves to the next one if there’s no response in 1 second.
- **Works Locally**: If you pass `0.0.0.0` as the target IP, it will check the local machine’s open ports — useful for checking your own system.
- **Logs Time**: It tracks how long the scan takes, so you can see how fast (or slow) things are going.

## Running the Project

### What You Need

You need:
- Python 3.x installed on your machine. If you don’t have it, grab it [here](https://www.python.org/downloads/).
- A text editor or IDE (VS Code works great for this!).

### How to Use It

1. **Clone the repo** (or just download the file):
   ```bash
   git clone https://github.com/SukanyaGhosh6/port_scanner.git
   ```

2. **Navigate to your project folder**:
   ```bash
   cd port-scanner
   ```

3. **Run the script**:
   - Open the terminal in VS Code or your system terminal.
   - Execute the script:
     ```bash
     python port_scanner.py
     ```

4. **Input when prompted**:
   - Enter the IP address of the machine you want to scan.
   - Provide a range of port numbers (e.g., from 1 to 1023).

### Example Output

```bash
Enter the IP address to scan: 192.168.1.1
Enter the starting port number: 1
Enter the ending port number: 1023
Scanning target: 192.168.1.1
Scanning ports from 1 to 1023
Port 22 is OPEN
Port 80 is OPEN
Port 443 is OPEN
...
Scan completed in: 0:00:03.145000
```

## What’s Going On Behind the Scenes?

So, here’s the deal: This script uses Python’s **socket module** to establish connections to a range of ports on a target machine. Each time it tries to connect, it either gets a response (indicating the port is open) or it times out (meaning the port is closed or unreachable). The process is repeated for each port in the given range, and you get the results after it’s done.

Now, the fun part is that I learned a lot while building this. I had to think about things like:
- **Port Ranges**: There are so many ports (from 1 to 65535!). I’ve limited it to 1 to 1023 for simplicity (these are the "well-known" ports), but you could easily extend this to scan the entire range.
- **Network Timeouts**: A lot of time, if the port is closed, you’ll just get no response. So I had to account for that and make sure the script doesn’t hang forever.
- **Security Stuff**: This isn’t exactly a hacking tool (don’t try scanning random networks you don’t own, please). But understanding how port scanners work is useful in cybersecurity — it’s one of the first steps in figuring out where vulnerabilities might exist in a network.

## Things to Explore Further

This project is basic, but there’s so much more you can do with it once you understand the core concept. Here are some things to explore if you’re feeling adventurous:

- **Multi-threading**: The script currently checks each port one by one, but if you want to speed things up, you can use **multi-threading** to check multiple ports at once.
- **Service Detection**: You could extend the script to not only check if a port is open but also identify which service is running on it (e.g., HTTP on port 80, SSH on port 22).
- **OS Fingerprinting**: Advanced scanners (like **Nmap**) can sometimes guess the operating system based on which ports are open. You could add some logic to try to detect what OS might be running.

## Why Port Scanning Matters

When you think about it, a port scanner is like knocking on the doors of a house (the machine) to see which ones are open. Each open port can potentially be a way in. For **cybersecurity professionals**, scanning ports is one of the first things they do when they’re testing a system’s security. For example, an attacker might scan a machine to find an open port running a vulnerable service, which they can exploit.

On the flip side, defenders use port scanning to discover and close unnecessary or insecure open ports.

## Final Thoughts

Building this port scanner was a really fun and educational experience. It gave me a deeper understanding of how computers communicate over networks and how important it is to keep things secure. Now I can’t stop thinking about ways to expand it or make it more robust.

The goal was to build something simple to understand, and I think I’ve done that. But there’s always room for improvement, and that’s what makes this field (and coding in general) so exciting!

