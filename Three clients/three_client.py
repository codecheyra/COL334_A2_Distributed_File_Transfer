
import socket
import json
import time
start = time.time()
ajay = socket.socket()
hitesh  = socket.socket()
# chaitu = socket.socket()
#there is no need to create a port number for client but it is required for a server because we shoul dknow where to send.
tot = 1000

    
ajay.connect(('10.194.28.229',8048))
hitesh.connect(('10.194.6.169', 8015))
# chaitu.connect(('10.194.16.77', 8014))


print("connected to 3 sercers")

all_lines = set()
ajay_set = set()
hitesh_set = set()
# chaitu_set = set()
my_set = set()

vayu = socket.socket()

hash = {}
hash["-1"] = "minus1"
all_lines.add("-1")
vayu.connect(('10.17.51.115',9801))
x = 8192
a = set()

while len(all_lines) < tot+1:
    if len(hash) %50 == 0:
        if len(hash) not in a:
            a.add(len(hash))
            print("time taken for ", len(hash),"lines is ", time.time()-start)
    # print("inside loop")
    for z in range (0, 1):
        vayu.send("SENDLINE\n".encode("utf-8"))
        data = ""
        while True:
            data += vayu.recv(8192).decode()
            if data[-1] == "\n":
                break
        s = data
        i = 0
        line_number = ""
        digits = 0
        while i < len(s) and s[i].isnumeric():
                line_number += s[i]
                digits += 1
                i += 1
        
        if line_number !="":  # Check if line_number is not empty before converting to int ((if it s -1 it wont append anything))
            num = int(line_number)
            hash[line_number] = s
    temp_set = str(num)    
    
    if len(all_lines) == tot+1:
        break
    ajay.send(bytes("Welcome", "utf-8"))
    # chaitu.send(bytes("Welcome", "utf-8"))
    hitesh.send(bytes("Welcome", "utf-8"))

    # print('send and running')
    data = ajay.recv(x)
    data1 = hitesh.recv(x)
    # data2 = chaitu.recv(x)

    ajay_string = data.decode()    # akash line number
    hitesh_string = data1.decode() 
    # chaitu_string = data2.decode()

    # print("ajay ", ajay_string)
    # print("hitesh ", hitesh_string)
    # print("chaitu ", chaitu_string)

    ajay_set.add(ajay_string)
    hitesh_set.add(hitesh_string)
    # chaitu_set.add(chaitu_string)
    my_set.add(temp_set)

    all_lines.add(ajay_string)
    all_lines.add(hitesh_string)
    # all_lines.add(chaitu_string)
    all_lines.add(temp_set)
    # print("total lines = ", len(all_lines))
ajay.send(bytes("done", "utf-8"))
hitesh.send(bytes("done", "utf-8"))
# chaitu.send(bytes("done", "utf-8"))

print("loop1 over")



if "-1" in hash:
    del hash["-1"]
if "" in hash:
    del hash[""]




print("receiving ajay")


start1 = time.time()

new_set = ajay_set-my_set
# print(new_set)

for i in new_set:
    if len(hash) %50 == 0:
        if len(hash) not in a:
            a.add(len(hash))
            print("time taken for ", len(hash),"lines is ", time.time()-start)
    ajay.send(str(i).encode())
    data  = ""
    # print(i, "ajay")
    while True:
        data += ajay.recv(4096).decode()
        # print(data, "data")
        if data[-1] == "\n":
            break
    hash[i] = data
    my_set.add(i)
ajay.send("done".encode())


new_set2 = hitesh_set - my_set

for i in new_set2:
    if len(hash) %50 == 0:
        if len(hash) not in a:
            a.add(len(hash))
            print("time taken for ", len(hash),"lines is ", time.time()-start)
    hitesh.send(str(i).encode())
    data  =""
    while True:
        data += hitesh.recv(4096).decode()
        if data[-1] == "\n":
            break
    hash[i] = data
    my_set.add(i)
hitesh.send("done".encode())


# new_set3 = chaitu_set - my_set

# for i in new_set3:
#     if len(hash) %50 == 0:
#         if len(hash) not in a:
#             a.add(len(hash))
#             print("time taken for ", len(hash),"lines is ", time.time()-start)
#     chaitu.send(str(i).encode())
#     data  =""
#     while True:
#         data += chaitu.recv(4096).decode()
#         if data[-1] == "\n":
#             break
#     hash[i] = data
#     my_set.add(i)
# chaitu.send("done".encode())

end1 = time.time()

# print("loop2 over")
# print("receiving hitesh")
# k = 0
# while k < len(hitesh_set):
#     if len(hash) %50 == 0:
#         print("time taken for ", len(hash),"lines is ", time.time()-start)
#     k += 1
#     data_line = ""
#     while True:
#         data_line += hitesh.recv(x).decode()
#         if data_line[-1] == "\n":
#             break
#     hitesh.send("ok".encode())
#     line_number = ""
#     s = data_line
#     i = 0
#     while i < len(s) and s[i].isnumeric():
#             line_number += s[i]
#             i += 1
#     if line_number != "":
#         hash[line_number] = data_line

# print("loop3 over")
# print("receiving chaitraja")
# k = 0
# while k < len(chaitu_set):
#     if len(hash) %50 == 0:
#         print("time taken for ", len(hash),"lines is ", time.time()-start)
#     k += 1
#     data_line = ""
#     while True:
#         data_line += chaitu.recv(x).decode()
#         if data_line[-1] == "\n":
#             break
#     chaitu.send("ok".encode())
#     line_number = ""
#     s = data_line
#     i = 0
#     while i < len(s) and s[i].isnumeric():
#             line_number += s[i]
#             i += 1
#     if line_number != "":
#         hash[line_number] = data_line

print("loop4 over")
if "" in hash:
    del hash[""]

vayu.send("SUBMIT\n".encode())
vayu.send("cs1210568@hackers alert\n".encode())
vayu.send((str(len(hash))+"\n").encode())
count = 0
for i in hash:
    if i != "-1":
        vayu.send((hash[i]).encode())
        count += 1
sub_data = vayu.recv(1024).decode()
done = ajay.recv(6).decode()

print("submitted to vayu")
time2 = time.time()-start

all_lines.remove("-1")
ajay_set = all_lines - ajay_set

print()

for i in ajay_set:
    ajay.send(hash[i].encode())
    zz = ajay.recv(6).decode() 
    # print(zz)
ajay.send("done\n".encode())
# print(1)

# chaitu_set = all_lines-chaitu_set


# for i in chaitu_set:
#     # print("sending ", hash[i])
#     chaitu.send(hash[i].encode())
#     zz = chaitu.recv(6).decode() 
# chaitu.send("done\n".encode())

# print(2)

hitesh_set = all_lines-hitesh_set
for i in hitesh_set:
    hitesh.send(hash[i].encode())
    zz = hitesh.recv(6).decode() 
hitesh.send("done\n".encode())
# print(3)

end = time.time()
print("master submit time = ", time2)
print("time taken to receive from remaining lines ", end1-start1)
print("total time taken = ", end-start)
print(sub_data)