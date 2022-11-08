import ftplib

FTP_HOST = "ftp.ieltscalculator.net"
FTP_USER = "frontend_monster@ieltscalculator.net"
FTP_PASS = "frontend_monster"

# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"

# the name of file you want to download from the FTP server
filename = "db.sqlite3"
with open(filename, "wb") as file:
    # use FTP's RETR command to download the file
    ftp.retrbinary(f"RETR {filename}", file.write)

# quit and close the connection
ftp.quit()