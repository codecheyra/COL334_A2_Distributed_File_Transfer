import json
import socket
import time

vayu = socket.socket()

hash = {}
hash['-1'] = 'minus1'
vayu.connect(('10.17.51.115',9801))
s = socket.socket()     
print("Socket Created")
s.bind(('10.194.6.169', 8015))
s.listen(5)
final_akash_set = {}
c, addr  = s.accept()
start=time.time()

while True:
    data = c.recv(8192) 
    if data.decode()== "done":
        break
    for z in range (0, 1):
        num = "-1"
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
        if line_number!= "":  
            num = int(line_number)
            hash[line_number] = s
    temporary_result = str(num)        
    c.send(bytes(temporary_result, "utf-8"))


if "-1" in hash:
    del hash["-1"]

# for num in hash:
#     q = hash[num]
#     c.send(bytes(q, 'utf-8'))
#     done = c.recv(2).decode()

while True:
    num1 = c.recv(5).decode()
    if num1 == "done":
        break
    c.send(hash[num1].encode())


# check_set = set()
# ajay_set = set()
# for i in range (0, 1000):
#     if str(i) not in hash:
#         check_set.add(str(i))


extra_lines = set()
c.send("sendme".encode())
while True:
    line = ""
    while True:
        line += c.recv(8192).decode()
        # print(line)
        if line[-1] == "\n":
            break
    # print(line)
    if line=="done\n":
        break
    extra_lines.add(line)
    c.send("thanks".encode())


k = 0

if "-1" in hash:
    del hash["-1"]
if "" in hash:
    del hash[""]

vayu.send("SUBMIT\n".encode())
vayu.send("2021CS10568@hackers alert\n".encode())
vayu.send((str(len(hash)+len(extra_lines))+"\n").encode())
count = 0
for i in hash:
    if i != "-1":
        vayu.send((hash[i]).encode())
        count += 1

for ele in extra_lines:
    vayu.send(ele.encode())

final = vayu.recv(1024).decode()
print(final)

vayu.close()
c.close()
end=time.time()
print(end-start)