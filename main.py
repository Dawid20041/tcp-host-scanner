import socket

def check_hosts(host, port):
    try:
        sock = socket.create_connection((host, port), timeout=3)
        sock.close()
        return True
    except:
        return False
    
with open('data.txt', 'r') as file:
    data = []
    seen = set()

    for line in file:
        clean_line = line.strip()
        
        if not clean_line:
            continue
        if clean_line.count(':') != 1:
            print(f"Invalid line skipped: {clean_line}")
            continue
        
        host, str_port = clean_line.split(':')

        if not host:
            print(f"Empty host skipped: {clean_line}")

        try:
            port = int(str_port)

        except ValueError:
            print(f"Invalid line skipped: {clean_line}")
            continue
        if not (1 <= port <= 65535):
            print(f"Port out of range: {port}")
            continue
        key = (host, port)

        if key not in seen:
            data.append(key)
            seen.add(key)

    for host, port in data:
        if check_hosts(host, port):
            print(f"{host}:{port} is reachable.")
        else:
            print(f"{host}:{port} is not reachable.")



