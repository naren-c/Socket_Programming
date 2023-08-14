import socket
  
import math
  
def encypt_func(txt, s):  
    result = ""  
  
#caeser encryption
# transverse the plain txt  
    for i in range(len(txt)):  
        char = txt[i]  
        # encypt_func uppercase characters in plain txt  
  
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)  
        # encypt_func lowercase characters in plain txt  
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result  
  
#caeser decryption
def decypt_func(msg):
    key = 5
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LETTERS = LETTERS.lower()
    message = str(msg)
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    return translated

# take the server name and port name
host = 'localhost'
port = 5000
  
# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
  
# bind the socket with server
# and port number
s.bind(('', port))
  
# allow maximum 1 connection to
# the socket
s.listen(1)
c, addr = s.accept()
      
# display client address
print("CONNECTION FROM:", str(addr))
while True: 
    # wait till a client accept
    # connection
   
    # send message to the client after
    # encoding into binary string
    c.send(b"enter e to encrypt and d to decrypt and f to disconnect")
    while True:
        msg1 = c.recv(1024)
        print(msg1)
        msg_str = msg1.decode()
        if(msg_str == "f"):
            print("disconnecting ",str(addr))
            c.send(b"ack")
            c.close()
            exit(0)
            
        if(msg_str == "e"):
            c.send(b"enter message to encrypt")
            
            msg2 = c.recv(1024)
            msg2_str = msg2.decode()
            print(msg2_str)
            print(encypt_func(msg2_str,4)) #s=4,shift =s+1 =5
            answer =encypt_func(msg2_str,4)
            c.send(answer.encode())
            break
            
        if(msg_str == "d"):
            c.send(b"enter message to decrypt")
            msg2 = c.recv(1024)
            msg2_str = msg2.decode()
            print(msg2_str)
            print(decypt_func(msg2_str))
            answer = decypt_func(msg2_str)
            
            c.send(answer.encode())
            break
        
        #c.send(b"connection end")
        #c.close() #added this line and below
        #break
#        if int(msg) == 3+4:
 #           c.send("Correct answer".encode())
#            c.close()
#            break 
        
#        else:
#            c.send("Wrong answer try again.".encode())
    
    
# disconnect the server
c.close()
exit(0)
