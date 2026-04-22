import sys


def main():
    host = sys.argv[1]
    port = int(sys.argv[2])
    filepath = sys.argv[3]

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(' ', 2)
            cmd = parts[0]
            k = parts[1]
            v = parts[2] if len(parts) > 2 else ""

if __name__ == "__main__":
    main()