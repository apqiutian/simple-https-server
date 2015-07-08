import ssl, socket, time
buf='''
HTTP/1.x 200 OK   
Content-Type: text/html 

<head> 
<title>MY HTTPS</title> 
</head> 
<html> 
<p>This is my https server.</p> 
<IMG src="test.jpg"/> 
</html> 
'''
if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    bindsocket = socket.socket()
    bindsocket.bind(('127.0.0.1', 8888))
    while True:
        bindsocket.listen(5)
        newsocket, fromaddr = bindsocket.accept()
        connstream = context.wrap_socket(newsocket, server_side=True)
        data = connstream.recv(1024)
        print(data)
        buf = buf.encode()
        connstream.send(buf)
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
        newsocket.close()
