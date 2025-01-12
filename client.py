import socket
import json
import logging as log

log.basicConfig(level=log.DEBUG,filename="error.log")
def st_client():
    try:
        customer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address='127.0.0.1'
        port = 5000
        customer.connect((server_address,port))
        print(f"connected to server at {server_address}")
        filename = input("Enter the filename : ")
        word = input("Enter the word to search for: ")
        request = {"filename":filename,"word":word}
        # print("Client ",request)
        customer.send(json.dumps(request).encode())
        response = customer.recv(4096).decode()
        result = json.loads(response)
        # print("Client2 = ",result)
        if "error" in result:
            print(f"Error : {result["error"]}")
        else:
            print("Search Results : ")
            for elem in result[1:]:
                print(f"Line {elem[0]}:{elem[1]}")
        log.info("client successfully connected to server")
    except Exception as e1:
        error_message = {"error":str(e1)}
        log.error("Failed to connect to server : {e1}")
    finally:
        customer.close()
if __name__ == "__main__":
    st_client()
