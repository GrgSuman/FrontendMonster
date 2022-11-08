import ftplib

FTP_HOST = "ftp.ieltscalculator.net"
FTP_USER = "frontend_monster@ieltscalculator.net"
FTP_PASS = "frontend_monster"

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"

# # local file name you want to upload and replace if exists
filename = "db.sqlite3"
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    ftp.storbinary(f"STOR {filename}", file)

ftp.quit()