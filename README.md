# 🔗 P2P File Sharing System

A simple and beginner-friendly **Peer-to-Peer File Sharing System** built using **Python Socket Programming**.

This project allows two peers to connect with each other, view shared files, and download files directly from one peer to another without using a centralized server.

---

## 📌 Project Overview

The **P2P File Sharing System** demonstrates how peer-to-peer communication works using TCP sockets.

Each peer works as both:

- A **server** that shares files
- A **client** that connects to another peer and downloads files

This project is useful for understanding:

- Computer networks
- Socket programming
- TCP communication
- Peer-to-peer architecture
- File transfer using Python

---

## 🚀 Features

- Peer-to-peer file sharing
- TCP socket-based communication
- Each peer works as both client and server
- List files from another peer
- Download files from another peer
- Separate shared folder for each peer
- Menu-driven interface
- Beginner-friendly Python implementation
- No external libraries required

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Socket Programming | Network communication |
| Threading | Handling peer connections |
| OS Module | File handling |
| TCP Protocol | Reliable file transfer |

---

## 📂 Project Structure

```text
P2P_Project/
│
├── Peer1/
│   ├── peer.py
│   └── shared_files/
│
├── Peer2/
│   ├── peer.py
│   └── shared_files/
│
└── README.md
```

---

## ✅ Requirements

Before running this project, make sure Python is installed on your system.

### Check Python Version

For Windows:

```bash
python --version
```

For Linux/macOS:

```bash
python3 --version
```

Recommended version:

```text
Python 3.x
```

This project uses only Python built-in libraries, so no extra installation is required.

Built-in modules used:

```text
socket
threading
os
```

---

## 📥 Clone the Repository

Copy and paste this command:

```bash
git clone https://github.com/glenjr009/P2P_Project.git
```

Now go inside the project folder:

```bash
cd P2P_Project
```

---

# ▶️ How to Run the Project

To test the project properly, open **two separate terminals**.

- Terminal 1 will run **Peer 1**
- Terminal 2 will run **Peer 2**

Each peer must run on a different port number.

Example:

```text
Peer 1 Port: 5001
Peer 2 Port: 5002
```

---

## 🖥️ Terminal 1: Run Peer 1

Open the first terminal.

### Windows

```bash
cd P2P_Project\Peer1
python peer.py
```

### Linux/macOS

```bash
cd P2P_Project/Peer1
python3 peer.py
```

When asked for a port number, enter:

```text
5001
```

Example:

```text
Enter port number for this peer: 5001
```

---

## 🖥️ Terminal 2: Run Peer 2

Open the second terminal.

### Windows

```bash
cd P2P_Project\Peer2
python peer.py
```

### Linux/macOS

```bash
cd P2P_Project/Peer2
python3 peer.py
```

When asked for a port number, enter:

```text
5002
```

Example:

```text
Enter port number for this peer: 5002
```

---

# 📤 How to Share Files

To share a file, place it inside the `shared_files` folder of any peer.

Example:

```text
Peer1/shared_files/sample.txt
```

or

```text
Peer2/shared_files/demo.txt
```

---

## 📝 Create Sample Files for Testing

You can quickly create test files using the commands below.

---

### Windows PowerShell

Run these commands from inside the `P2P_Project` folder:

```powershell
echo "Hello from Peer 1" > Peer1\shared_files\peer1_file.txt
echo "Hello from Peer 2" > Peer2\shared_files\peer2_file.txt
```

---

### Linux/macOS Terminal

Run these commands from inside the `P2P_Project` folder:

```bash
echo "Hello from Peer 1" > Peer1/shared_files/peer1_file.txt
echo "Hello from Peer 2" > Peer2/shared_files/peer2_file.txt
```

---

# 🔍 List Files from Another Peer

After both peers are running, choose option:

```text
1. List files from another peer
```

---

## Example: Peer 1 Listing Files from Peer 2

In Peer 1 terminal, enter:

```text
Enter your choice: 1
Enter peer IP address: 127.0.0.1
Enter peer port number: 5002
```

This will display files available in:

```text
Peer2/shared_files/
```

---

## Example: Peer 2 Listing Files from Peer 1

In Peer 2 terminal, enter:

```text
Enter your choice: 1
Enter peer IP address: 127.0.0.1
Enter peer port number: 5001
```

This will display files available in:

```text
Peer1/shared_files/
```

---

# 📥 Download File from Another Peer

Choose option:

```text
2. Download file from another peer
```

---

## Example: Peer 1 Downloading File from Peer 2

In Peer 1 terminal, enter:

```text
Enter your choice: 2
Enter peer IP address: 127.0.0.1
Enter peer port number: 5002
Enter file name to download: peer2_file.txt
```

The file will be downloaded into:

```text
Peer1/shared_files/
```

---

## Example: Peer 2 Downloading File from Peer 1

In Peer 2 terminal, enter:

```text
Enter your choice: 2
Enter peer IP address: 127.0.0.1
Enter peer port number: 5001
Enter file name to download: peer1_file.txt
```

The file will be downloaded into:

```text
Peer2/shared_files/
```

---

# 📁 Show My Shared Files

Choose option:

```text
3. Show my shared files
```

This displays all files available in your own `shared_files` folder.

---

# ❌ Exit the Program

Choose option:

```text
4. Exit
```

---

# 🧪 Full Copy-Paste Testing Guide

Follow these steps to test the project from the beginning.

---

## Step 1: Clone the Project

```bash
git clone https://github.com/glenjr009/P2P_Project.git
cd P2P_Project
```

---

## Step 2: Add Test Files

### Windows PowerShell

```powershell
echo "This file belongs to Peer 1" > Peer1\shared_files\peer1_file.txt
echo "This file belongs to Peer 2" > Peer2\shared_files\peer2_file.txt
```

### Linux/macOS

```bash
echo "This file belongs to Peer 1" > Peer1/shared_files/peer1_file.txt
echo "This file belongs to Peer 2" > Peer2/shared_files/peer2_file.txt
```

---

## Step 3: Run Peer 1

Open Terminal 1.

### Windows

```bash
cd Peer1
python peer.py
```

### Linux/macOS

```bash
cd Peer1
python3 peer.py
```

Enter this port:

```text
5001
```

---

## Step 4: Run Peer 2

Open Terminal 2.

### Windows

```bash
cd Peer2
python peer.py
```

### Linux/macOS

```bash
cd Peer2
python3 peer.py
```

Enter this port:

```text
5002
```

---

## Step 5: Download Peer 2 File from Peer 1

In Peer 1 menu, enter:

```text
Enter your choice: 2
Enter peer IP address: 127.0.0.1
Enter peer port number: 5002
Enter file name to download: peer2_file.txt
```

Now `peer2_file.txt` will be downloaded into:

```text
Peer1/shared_files/
```

---

## Step 6: Download Peer 1 File from Peer 2

In Peer 2 menu, enter:

```text
Enter your choice: 2
Enter peer IP address: 127.0.0.1
Enter peer port number: 5001
Enter file name to download: peer1_file.txt
```

Now `peer1_file.txt` will be downloaded into:

```text
Peer2/shared_files/
```

---

# 🌐 Running on Two Different Systems

You can also run Peer 1 and Peer 2 on two different computers connected to the same Wi-Fi/LAN network.

---

## Find IP Address on Windows

Run:

```bash
ipconfig
```

Look for:

```text
IPv4 Address
```

Example:

```text
192.168.1.10
```

---

## Find IP Address on Linux/macOS

Run:

```bash
ifconfig
```

or:

```bash
ip addr
```

Example:

```text
192.168.1.20
```

---

## Example for LAN Testing

Suppose Peer 1 is running on:

```text
192.168.1.10:5001
```

If Peer 2 wants to connect to Peer 1, enter:

```text
Enter peer IP address: 192.168.1.10
Enter peer port number: 5001
```

Suppose Peer 2 is running on:

```text
192.168.1.20:5002
```

If Peer 1 wants to connect to Peer 2, enter:

```text
Enter peer IP address: 192.168.1.20
Enter peer port number: 5002
```

> Make sure both devices are connected to the same network and the firewall allows the selected ports.

---

# 🧠 How It Works

1. Each peer starts a server socket on a selected port.
2. The peer listens for incoming connections.
3. Another peer connects using the target peer's IP address and port number.
4. The connected peer can request a file list or download a specific file.
5. The requested file is transferred using TCP.
6. The downloaded file is saved in the local `shared_files` folder.

---

# 📌 Menu Options

```text
========== P2P File Sharing System ==========
1. List files from another peer
2. Download file from another peer
3. Show my shared files
4. Exit
```

---

# 🧯 Common Issues and Fixes

## 1. Port Already in Use

If one port does not work, use another port number.

Example:

```text
5003
```

or:

```text
6001
```

---

## 2. File Not Found

Make sure the file exists inside the other peer's `shared_files` folder.

Example:

```text
Peer2/shared_files/peer2_file.txt
```

Also make sure the file name is typed correctly.

---

## 3. Connection Refused

Check these points:

- Both peers are running
- Correct IP address is entered
- Correct port number is entered
- Firewall is not blocking the connection
- Both devices are on the same network if testing on LAN

---

## 4. Python Command Not Working

Try:

```bash
python3 peer.py
```

instead of:

```bash
python peer.py
```

On Windows, you can also try:

```bash
py peer.py
```

---

## 5. Shared Folder Missing

Make sure each peer has a `shared_files` folder.

If missing, create it manually.

### Windows

```powershell
mkdir Peer1\shared_files
mkdir Peer2\shared_files
```

### Linux/macOS

```bash
mkdir -p Peer1/shared_files
mkdir -p Peer2/shared_files
```

---

# ✅ Use Cases

- Computer networking mini project
- Python socket programming practice
- Peer-to-peer architecture demonstration
- File transfer system prototype
- Academic project submission
- Understanding distributed communication basics

---

# 🔐 Limitations

This is a basic academic implementation and does not currently include:

- User authentication
- Encryption
- File integrity checking
- Automatic peer discovery
- GUI interface
- Download progress bar
- Resume support for interrupted downloads

---

# 🚀 Future Enhancements

- Add encrypted file transfer
- Add file integrity verification using SHA-256
- Add GUI using Tkinter
- Add automatic peer discovery
- Add download progress indicator
- Add multiple peer support
- Add logs for upload and download activity
- Add authentication between peers

---

# 👨‍💻 Author

**Glen Fernandes**  
Cybersecurity Enthusiast | Web-Developer | Computer Science Undergraduate

GitHub: [glenjr009](https://github.com/glenjr009)

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📌 Git Commands to Add This README

After creating or editing the `README.md` file, run these commands:

```bash
git add README.md
git commit -m "Add user-friendly README with setup commands"
git push origin main
```
