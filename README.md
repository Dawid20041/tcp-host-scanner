# 🔎 TCP Host Scanner (CLI Tool)

A multithreaded TCP host scanner written in Python.  
This tool reads a list of `host:port` entries from a file and checks whether a TCP connection can be established.

Designed as a practical networking and automation project with a focus on:

- input validation
- concurrency (threading)
- CLI argument parsing
- defensive programming
- clean data structures

---

## 🚀 Features

- ✅ Multithreaded scanning using `ThreadPoolExecutor`
- ✅ Configurable timeout
- ✅ Configurable number of threads
- ✅ Input validation (format, port range, empty values)
- ✅ Duplicate removal
- ✅ Graceful handling of invalid lines
- ✅ Simple CLI interface using `argparse`

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Dawid20041/tcp-host-scanner.git
cd tcp-host-scanner
```

Python 3.8+ recommended.

No external dependencies required.

---

## 🧠 Usage

Basic usage:

```bash
python scanner.py data.txt
```

With custom settings:

```bash
python scanner.py data.txt --threads 20 --timeout 2
```

### Arguments

| Argument | Description | Default |
|----------|------------|----------|
| `file` | Path to file containing hosts (`host:port`) | required |
| `--threads` | Number of worker threads | 10 |
| `--timeout` | Connection timeout in seconds | 3 |

---

## 📄 Input File Format

The input file must contain one `host:port` entry per line:

```
8.8.8.8:53
google.com:80
localhost:22
```

### Validation Rules

- Empty lines are skipped
- Lines without exactly one `:` are skipped
- Ports must be integers
- Ports must be in range `1-65535`
- Duplicate entries are removed
- Invalid lines are reported but do not stop execution

---

## 🛠 Example Output

```
8.8.8.8:53 is reachable.
google.com:80 is reachable.
localhost:22 is not reachable.
```

Invalid lines:

```
Invalid line skipped: example.com:abc
Port out of range: 70000
```

---

## ⚙️ How It Works

1. Parses CLI arguments via `argparse`
2. Validates and processes input file
3. Removes duplicates using a `set`
4. Uses `socket.create_connection()` to test TCP reachability
5. Runs checks concurrently using `ThreadPoolExecutor`

---

## 📈 Performance

Sequential version worst-case:

```
hosts × timeout
```

With threading:

```
(hosts / threads) × timeout
```

This significantly reduces execution time for large host lists.

---

## 🎯 Educational Purpose

This project was built as part of hands-on practice in:

- Python networking
- Concurrency
- CLI tooling
- Writing production-style defensive code
- Preparing for cloud / infrastructure automation roles

---

## 🔮 Future Improvements

- Colored terminal output
- CSV export of results
- Logging support
- Progress bar
- Async version (asyncio)
- Packaging as installable CLI tool

---



## 📜 License


MIT License
