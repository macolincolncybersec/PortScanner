import socket


def scan_ports(target, start_port, end_port):
    # Iterate over the range of ports to scan
    for port in range(start_port, end_port + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout value for the connection attempt

        # Attempt to connect to the target on the current port
        result = sock.connect_ex((target, port))

        # Check if the connection was successful
        if result == 0:
            print(f"Port {port} is open")

        # Close the socket connection
        sock.close()


# Example usage
target_ip = '127.0.0.1'  # Target IP address to scan
start_port = 1  # Start port
end_port = 100  # End port

scan_ports(target_ip, start_port, end_port)
