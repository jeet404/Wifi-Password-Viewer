import subprocess
import re

command = "netsh wlan show profile"
ssid = subprocess.check_output(command, shell=True)
ssid = ssid.decode("utf-8")
ssid_list = re.findall('(?:Profile\s*:\s)(.*)', ssid)
result=""
for ssid_name in ssid_list:
    ssid_name=ssid_name.split("/")[0]

    process = subprocess.check_output(["netsh","wlan","show","profile",ssid_name,"key=clear"] ,shell=True,text=True)
    result = result + process

with open("WifiDetails.txt","w+") as file:
    file.write(result)