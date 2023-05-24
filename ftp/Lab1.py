import ftplib


# https://dlptest.com/ftp-test/

HOSTNAME='ftp.dlptest.com'
USERNAME='dlpuser'
PASSWORD='rNrKYTX9g7z3RgJRmxWuGHbeu'

print("Connection Start")
ftp_server=ftplib.FTP(HOSTNAME,USERNAME,PASSWORD)
print("Connection End")

ftp_server.encoding="utf-8"

filename="sb015.txt"

with open(filename,"rb") as file:
    ftp_server.storbinary(f"STOR {filename}",file)


ftp_server.dir()
ftp_server.quit()
