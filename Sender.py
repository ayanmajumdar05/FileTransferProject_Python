import socket
import os
import pickle

send_size = 8000

# Server settings
HOST = 'localhost'  # Change to server IP if remote
PORT = 5001

def send_file(filename,filepath, conn):
    if os.path.isfile(filepath):
        sep1 = "&"
        sep2 = "|-|"
        filename_send = filename
        filepath_send = filepath
        #conn.send(filename_send.encode())
        #print("---------Filename sent----------")
        #conn.send(sep1.encode())
        #print("-------Sep1 sent--------")

        #conn.send(filepath_send.encode())  # Send filename first
        #print("---------Filepath sent----------")
        #conn.send(sep2.encode())
        #print("------sep2 send-------")


        fr = open(filepath, 'r')
        fb = open("Temp_binary_file.bin",'wb')
        chunk = fr.read(send_size)
        pickle.dump(chunk, fb)
        fb.close()
        fr.close()
        fbr = open("Temp_binary_file.bin",'rb')
        data_chunk = pickle.load(fbr)
        #conn.send(data_chunk.encode())
        #print("---------Data_Chunk sent----------")
        fbr.close()

        send_obj = filename + sep1 + filepath + sep2 + data_chunk
        conn.send(send_obj.encode())
        print("Send_Obj sent")
        #print(f'File sent successfully: {filename_ext}')
    else:
        print(f'File {filename} does not exist.')

def connect_to_server(filename,filepath):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        send_file(filename,filepath,s)

if __name__ == "__main__":
    filepath = input("Enter the Filepath = ")
    filename_ext = os.path.basename(filepath)
    filename_ext_split = filename_ext.split(".")
    filename = filename_ext_split[0]
    print("Filepath is - ", filepath)
    print("Filename_ext is - ",filename_ext)
    print("Filename is - ",filename)
    connect_to_server(filename,filepath)
