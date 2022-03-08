import time
from datetime import datetime as dt

ip_localmachine="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
hosts_path="C:\Windows\System32\drivers\etc\hosts"
start_time="09:0:0"
end_time="16:0:0"
    
now=dt.now()
current_time=now.strftime("%H:%M:%S")
print(current_time)

while True:
    if start_time<=current_time and current_time<=end_time:
        print("Working hours")
        with open(hosts_path,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                
                else:
                    file.write(ip_localmachine+" "+website+"\n")
            
    else:
        print("Non working hours")
        with open(hosts_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                
            file.truncate(0)    
    
    time.sleep(10)