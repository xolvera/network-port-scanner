import socket
import argparse
import csv

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        sock.close()
        return True
    except:
        return False

def main():
    parser = argparse.ArgumentParser(description="Basic TCP port scanner")
    parser.add_argument("--target", type=str, required=True, help="Target IP or hostname")
    parser.add_argument("--start-port", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end-port", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--verbose", action="store_true", help="Show closed ports as well")
    parser.add_argument("--output", type=str, help="Output CSV filename (optional)")

    args = parser.parse_args()

    results = []

    for port in range(args.start_port, args.end_port + 1):
        is_open = scan_port(args.target, port)
        if is_open:
            print(f"[+] Port {port} is OPEN")
            results.append((port, "OPEN"))
        else:
            if args.verbose:
                print(f"[-] Port {port} is closed")
            results.append((port, "CLOSED"))

    if args.output:
        with open(args.output, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Port", "Status"])
            writer.writerows(results)
        print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()

