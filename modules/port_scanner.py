import socket

def run(target_ip):
    """Scans common ports on a target IP address."""
    print(f"\n[+] Starting Port Scan on: {target_ip}")
    
    # List of common ports to test (HTTP, HTTPS, SSH, FTP)
    common_ports = [21, 22, 80, 443]
    
    for port in common_ports:
        # Create a network socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # Wait 1 second max per port
        
        # Try connecting to the port
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"  --> Port {port}: OPEN")
        s.close()
    print("[+] Port scan complete.")
