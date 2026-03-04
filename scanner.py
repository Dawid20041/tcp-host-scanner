import socket
from concurrent.futures import ThreadPoolExecutor
import argparse


def check_hosts(host, port, timeout):
    try:
        sock = socket.create_connection((host, port), timeout=timeout)
        sock.close()
        return True
    except:
        return False

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple TCP Host Scanner")

    parser.add_argument("file", help="Path to file with hosts (host:port)")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads to use (default: 10)")
    parser.add_argument("--timeout", type=int, default=3, help="Connection timeout in seconds (default: 3)")

    return parser.parse_args()

args = parse_arguments()

file_path = args.file
thread_count = args.threads
timeout_value = args.timeout

with open(file_path, 'r') as file:
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
            continue
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
def check_and_print(host_port):
    host, port = host_port
    if check_hosts(host, port, timeout_value):
        print(f"{host}:{port} is reachable.")
    else:
        print(f"{host}:{port} is not reachable.")
  
    
with ThreadPoolExecutor(max_workers=thread_count) as executor:
    executor.map(check_and_print, data)


