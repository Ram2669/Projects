import socket
import threading
import json
from search import Search
import logging as log

log.basicConfig(level=log.DEBUG,filename="error.log")

def customer(cust_soc):
    try:
            cust_data = cust_soc.recv(4096).decode() 
            cust_req = json.loads(cust_data)
            cust_filename = cust_req.get("filename")
            fetch_word = cust_req.get("word")
            search_file = Search(cust_filename)
            search_file.clean() 
            res = search_file.getLines(fetch_word)
            cust_response = json.dumps(res)
            cust_soc.send(cust_response.encode())
            log.info("server succesfully handle client")
    except Exception as e1:
            error_message = {"error":str(e1)}
            cust_soc.send(json.dumps(error_message).encode())
            log.error("server cannot handle request by client")
    finally:
        cust_soc.close()
def st_server():
       try:
                server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                host = '127.0.0.1'
                port = 5000
                server.bind((host,port))
                server.listen(5)
                print(f"server is listening on port {port}")
                log.info("server successfully connected to client")
                while True:
                        cust_soc , addr = server.accept()
                        print(f'connection received from {addr}')
                        cust_handler = threading.Thread(target=customer,args=(cust_soc,))
                        cust_handler.start()
       except Exception as e1:
             error_message = {"error":str(e1)}
             log.error("server cannot connected to the client")
if __name__ == "__main__":
        st_server()



    
