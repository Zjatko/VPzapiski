import socket

def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('ctf.t3st.si', 5010))
    
    data = s.recv(1024)  # Prejmi uvodni pozdrav
    print(data.decode())
    
    
    
    response = s.recv(1024)
    print(response.decode())  # To bo vsebovalo šifriran "flag" in Feistel izhod
    

    # Pošljite ukaz za pridobitev "flag"
    s.sendall(b"1")


    response = s.recv(1024)
    print(response.decode())  # To bo vsebovalo šifriran "flag" in Feistel izhod



    s.close()

connect_to_server()

