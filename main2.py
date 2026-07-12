import socket

print("=" * 45)
print("NETWORK PORT SCANNER")
print("=" * 45)

host = input("Enter IP Address or Hostname: ")

try:
    target = socket.gethostbyname(host)
    print("\nScanning:", target)
except:
    print("Invalid Host!")
    exit()
    print("\nScanning Common Ports...\n")

ports = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

for port, service in ports.items():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} ({service}) : OPEN")
    else:
        print(f"Port {port} ({service}) : CLOSED")

    s.close()