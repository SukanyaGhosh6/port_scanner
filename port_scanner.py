import socket
from datetime import datetime

# Function to scan a range of ports
def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning target: {target_ip}")
    print(f"Scanning ports from {start_port} to {end_port}")
    
    # Recording the start time of the scan
    start_time = datetime.now()
    
    # Iterating over the specified range of ports
    for port in range(start_port, end_port + 1):
        # Try to connect to each port
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1 second timeout
            result = sock.connect_ex((target_ip, port))
            
            # If the result is 0, the port is open
            if result == 0:
                print(f"Port {port} is OPEN")
            sock.close()
        except socket.error:
            pass
    
    # Recording the end time of the scan and print the duration
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Scan completed in: {total_time}")

# Input target IP and port range
target_ip = input("Enter the IP address to scan: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

# Calling the port scanning function
scan_ports(target_ip, start_port, end_port)
