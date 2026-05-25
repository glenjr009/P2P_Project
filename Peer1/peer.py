import socket
import threading
import os

SHARED_FOLDER = "shared_files"


if not os.path.exists(SHARED_FOLDER):
    os.makedirs(SHARED_FOLDER)


def handle_client(conn, addr):
    print(f"\n[+] Connected with {addr}")

    try:
        command = conn.recv(1024).decode()

        if command == "LIST":
            files = os.listdir(SHARED_FOLDER)

            if len(files) == 0:
                conn.send("No files available".encode())
            else:
                file_list = "\n".join(files)
                conn.send(file_list.encode())

        elif command.startswith("GET"):
            filename = command.split(" ", 1)[1]
            filepath = os.path.join(SHARED_FOLDER, filename)

            if os.path.exists(filepath):
                conn.send("FOUND".encode())

                with open(filepath, "rb") as file:
                    data = file.read(1024)

                    while data:
                        conn.send(data)
                        data = file.read(1024)

                print(f"[+] File sent successfully: {filename}")

            else:
                conn.send("NOT_FOUND".encode())

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(5)

    print(f"[+] Peer server started on port {port}")
    print("[+] Waiting for other peers...")

    while True:
        conn, addr = server_socket.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


def list_files_from_peer(peer_ip, peer_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((peer_ip, peer_port))
        client_socket.send("LIST".encode())

        files = client_socket.recv(4096).decode()
        print("\nFiles available on peer:")
        print(files)

    except Exception as e:
        print("Connection failed:", e)

    finally:
        client_socket.close()


def download_file(peer_ip, peer_port, filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((peer_ip, peer_port))
        client_socket.send(f"GET {filename}".encode())

        response = client_socket.recv(1024).decode()

        if response == "FOUND":
            save_path = os.path.join(SHARED_FOLDER, filename)

            with open(save_path, "wb") as file:
                while True:
                    data = client_socket.recv(1024)

                    if not data:
                        break

                    file.write(data)

            print(f"[+] File downloaded successfully: {filename}")

        else:
            print("[-] File not found on peer")

    except Exception as e:
        print("Download failed:", e)

    finally:
        client_socket.close()


def menu():
    print("\n========== P2P File Sharing System ==========")
    print("1. List files from another peer")
    print("2. Download file from another peer")
    print("3. Show my shared files")
    print("4. Exit")


def main():
    port = int(input("Enter port number for this peer: "))

    server_thread = threading.Thread(target=start_server, args=(port,))
    server_thread.daemon = True
    server_thread.start()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            peer_ip = input("Enter peer IP address: ")
            peer_port = int(input("Enter peer port number: "))

            list_files_from_peer(peer_ip, peer_port)

        elif choice == "2":
            peer_ip = input("Enter peer IP address: ")
            peer_port = int(input("Enter peer port number: "))
            filename = input("Enter file name to download: ")

            download_file(peer_ip, peer_port, filename)

        elif choice == "3":
            files = os.listdir(SHARED_FOLDER)

            print("\nYour shared files:")
            if len(files) == 0:
                print("No files available")
            else:
                for file in files:
                    print(file)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()