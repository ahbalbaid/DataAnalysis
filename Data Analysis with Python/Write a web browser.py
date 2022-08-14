import socket

def webpy():
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org',80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data)<1):
            break
        print(data.decode())
    mysock.close()

import urllib.request,  urllib.parse, urllib.error

def webur():
    try:
        fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1/htm')
        for line in fhand:
            print(line.decode().strip())
    except:
        raise ConnectionError('Connection Failed')

if __name__ == '__main__':
    webur()

