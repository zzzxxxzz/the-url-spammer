import socket
from tkinter import *
import time
import webbrowser
def user():
    """
    this function communicates with the server and takes the user input
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("10.0.0.14", 100)
    connected = False
    while not connected:
        try:
            sock.connect(server_address)
            connected = True
        except Exception:
            print("...")

    while True:
        try:
            opt = sock.recv(1024).decode()
        except Exception:
            exit()
        try:
            if opt == "1":
                sock.sendall("accepted_opt".encode())
                massage = sock.recv(1024).decode()

                root = Tk()
                w = Label(root, text=massage)
                w.pack()
                root.mainloop()
                sock.sendall("task_completed".encode())
                continue
        except Exception:
            exit()
        try:
            if opt == "2":

                sock.sendall("accepted_opt".encode())
                url = sock.recv(1024).decode()
                webbrowser.open_new(url)
                sock.sendall("task_completed".encode())
                continue
        except Exception:
            exit()
        try:
            if opt == "3":

                sock.sendall("accepted_opt".encode())
                url = sock.recv(1024).decode()
                i = 0
                while i <= 200:
                    webbrowser.open_new_tab(url)
                    i = i+1

                sock.sendall("task_completed".encode())
                exit()
        except Exception:
            exit()
        if opt == "9":
            sock.sendall("exit_opt".encode())
            exit()
        sock.sendall("error_opt".encode())


def main():
    user()


if __name__ == '__main__':
    main()
