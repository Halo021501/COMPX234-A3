import sys
import socket

def main():
    port = int(sys.argv[1])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        while True:
            conn, addr = s.accept()
            conn.close()

if __name__ == "__main__":
    main()