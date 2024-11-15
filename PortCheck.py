import socket

def port_scan(host, start_port=1, end_port=1024):
    print(f'Scanning {host} from port {start_port} to {end_port}')
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Timeout for socket connection
        try:
            s.connect((host, port))
            open_ports.append(port)
        except (socket.timeout, socket.error):
            pass
        finally:
            s.close()
    if open_ports:
        print(f'Open ports on {host}:')
        for port in open_ports:
            print(f'Port {port} is open')
    else:
        print(f'No open ports found on {host} in the specified range.')

if __name__ == '__main__':
    host = input('Enter the host to scan: ')
    start_port = int(input('Enter the starting port number (default 1): ') or 1)
    end_port = int(input('Enter the ending port number (default 1024): ') or 1024)
    port_scan(host, start_port, end_port)
