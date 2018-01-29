import ftplib
import socket

class ftpscanner(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.email = email

    # Bruteforce FTP login using a password file
    def bf_ftp_login(host, passFile):
        pass

    def check_ports(self, host, port, email):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            if (s.connect_ex(host, port) == 0):
                print ("[OPEN]: {}:{}").format(host, port)
                ftp_login(host, email)
            else:
                print("[CLOSED]: {}:{}").format(host, port)

    def ftp_login(self, host, email):
        try:
            ftp = ftplib.FTP(host)
            ftp.login('anonymous', email)
            print ("Succeeded " + str(host))
            ftp.quit()
            return True
        except Exception as e:
            print ("Failed: " + str(host) + " " + e)
            return False
