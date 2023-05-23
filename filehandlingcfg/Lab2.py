import configparser


config_file=configparser.ConfigParser()
config_file.add_section("FTPSettingsDetails")


config_file.set("FTPSettingsDetails","FTP_URL","demoftp.simplilearn.com")
config_file.set("FTPSettingsDetails","FTP_USER","user")
config_file.set("FTPSettingsDetails","FTP_PASSWORD","kvbjvbfbvkbdf")

with open('ciscoconfiguration.ini','w') as file:
    config_file.write(file)
    file.flush() # Clear the Object
    file.close()

print("CISCO Configuration File Created ")

readfile=open('ciscoconfiguration.ini','r')
content=readfile.read()
print(content)
readfile.flush()
readfile.close()