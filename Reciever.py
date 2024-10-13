import socket
import os
from venv import create

recieve_size = 8000

# Server settings
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 5001  # Arbitrary non-privileged port

def create_file(filepath,filename,data_chunk):
    print("Filepath is recieved as ",filepath)
    print("Filename is recieved as ",filename)
    filename_modded = filename + "_modded.txt"
    fp = open(filename_modded, 'w')
    print(f'Receiving file: {filename}')
    fp.write(data_chunk)
    fp.close()
    print(f'File received successfully: {filename}')

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Server listening on {HOST}:{PORT}')
        
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            """
            filename = conn.recv(recieve_size).decode() #Get the filename from client
            print("Filename is recieved as ",filename)
            sep_a = conn.recv(recieve_size).decode()
            print("sep1 received")

            filepath = conn.recv(recieve_size).decode()  # Get the filepath from client
            print("Filepath is recieved as ", filepath)
            sep_b = conn.recv(recieve_size).decode()
            print("Sep2 received")

            data_chunk = conn.recv(recieve_size).decode()
            print("Data_chunk is recieved as ",data_chunk)

            create_file(filepath,filename,data_chunk)
            """
            recieve_object_var = conn.recv(recieve_size).decode()
            print("Recieved Object")
            process_obj(recieve_object_var)

def process_obj(recv_obj):
    obj_split_first = recv_obj.split("&")
    #print(obj_split_first)
    obj_split_second = [obj_split_first[0],"filepath","data_chunk"]
    """
    for obj_i in obj_split_first:
        if "|-|" in obj_i:
            obj_split = obj_i.split("|-|")
            obj_i_splitted_first = obj_split[0]
            print("objifirst ", obj_i_splitted_first)
            obj_i_splitted_second = obj_split[1]
            print("objisecond ",obj_i_splitted_second)
            obj_split_second[1] = obj_i_splitted_first
            obj_i_splitted_second[2] = obj_i_splitted_second
        else:
            continue
        filepath = obj_split_second[1]
        filename = obj_split_second[0]
        data_chunk = obj_split_second[2]
        print("final List is ",obj_split_second)
        create_file(filepath, filename, data_chunk)
    """
    obj_i = obj_split_first[1]

    obj_split = obj_i.split("|-|")
    obj_i_splitted_first = obj_split[0]
    #print("objifirst ", obj_i_splitted_first)

    obj_i_splitted_second = obj_split[1]
    #print("objisecond ", obj_i_splitted_second)

    obj_split_second[1] = obj_i_splitted_first
    obj_split_second[2] = obj_i_splitted_second
    filepath = obj_split_second[1]
    filename = obj_split_second[0]
    data_chunk = obj_split_second[2]
    print("final List is ", obj_split_second)
    create_file(filepath, filename, data_chunk)

if __name__ == "__main__":
    start_server()
    
        
