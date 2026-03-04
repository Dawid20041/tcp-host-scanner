Network Host Reachability Checker
A lightweight Python utility designed to verify the status of multiple network hosts and ports. It reads a list of targets from a file, validates the formatting, removes duplicates, and attempts a socket connection to see if the service is reachable
🚀 Features
Bulk Checking: Processes multiple host:port pairs from an external file.

Data Validation: Automatically skips empty lines, malformed entries, and invalid port numbers (outside the 1-65535 range).

Deduplication: Ensures each unique host/port combination is only checked once.

Timeout Protection: Uses a 3-second timeout per connection to prevent the script from hanging on unresponsive hosts.

🛠️ Requirements
Python 3.x

No external libraries required (uses the built-in socket module).

📋 Configuration
The script looks for a file named data.txt in the same directory. Each line in the file should follow the format host:port.

Example data.txt:

Plaintext
google.com:80
192.168.1.1:443
localhost:8080
example.com:22
💻 Usage
Clone or save the script to your local machine.

Create your data.txt file with the hosts you want to monitor.

Run the script via your terminal:

Bash
python main.py
Example Output:
Plaintext
google.com:80 is reachable.
192.168.1.1:443 is not reachable.
Invalid line skipped: malformed_line_no_port
Port out of range: 99999
⚙️ How it Works
The script follows a simple three-step logic:

Parsing: It reads data.txt, strips whitespace, and splits the host from the port.

Filtering: It validates that the port is an integer and that the pair hasn't been processed yet.

Connection: It uses socket.create_connection to attempt a TCP handshake. If successful, the host is marked as "reachable."

📝 License
This project is open-source and free to use.