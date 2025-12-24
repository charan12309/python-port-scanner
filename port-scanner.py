import socket
from concurrent.futures import ThreadPoolExecutor

TARGET = "127.0.0.1"
START_PORT = 1
END_PORT = 1024
TIMEOUT = 1.0
THREADS = 100

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(TIMEOUT)
        if sock.connect_ex((TARGET, port)) == 0:
            return port
    return None

def main():
    print(f"Scanning {TARGET} (ports {START_PORT}-{END_PORT})...\n")
    open_ports = []

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for port in executor.map(scan_port, range(START_PORT, END_PORT + 1)):
            if port:
                open_ports.append(port)
                print(f"[OPEN] Port {port}")

    print("\nScan complete.")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
