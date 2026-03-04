Host Connectivity Checker 🛡️A lightweight Python utility designed to verify the availability of hosts on specific ports. The script reads a list of addresses from a file, validates the input, removes duplicates, and performs a TCP connection check.Key FeaturesBulk Processing: Efficiently reads and checks multiple hosts from an external file.Data Validation: Automatically skips malformed lines, empty strings, and out-of-range ports (outside $1-65535$).Deduplication: Identical host/port pairs are processed only once per session.Smart Timeout: Implements a 3-second timeout to ensure the script doesn't hang on unresponsive servers.RequirementsPython 3.xNo external dependencies required (uses the built-in socket library).File Structurescript.py: The main Python logic.data.txt: The input file containing your target list.ConfigurationBefore running the script, create a data.txt file in the same directory. Each entry should follow the host:port format:Plaintextgoogle.com:80
192.168.1.1:443
example.org:22
google.com:80
UsageTo start the connectivity check, run the following command in your terminal:Bashpython script.py
Sample OutputThe program will parse the file and output the status of each unique host:Plaintextgoogle.com:80 is reachable.
192.168.1.1:443 is not reachable.
example.org:22 is not reachable.
[!TIP]This script uses a simple TCP handshake. Ensure your network firewall allows outbound traffic on the ports you are testing.
