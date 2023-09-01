# website blocker using python
# for it we  have to do some changes in your host file for blocking for some time period

#open nnotepad as run as admin-> follow the path to block to do manually rempve https:://
# use cmd also as admin mode only

import datetime 
import time


end_time = datetime.datetime(2022,09,12)
site_block = ["www.wsfjkl.com","www.facebook.com"]
host_path = "c-windows-syst32-drivers-etc-hosts, convert all\ to / "
redirect = "local host server number 127.3.45.5"

while True:
	
	if datetime.datetime.now()<end_time:
		print("website blocking start")
		with open(host_path,"r+") as host-file: #to open the host file in rw mode.
			content = host_file.read()
			for ws in site_block:
				if wb not in content:
					host_file.write(redirect + "+ws"+"\n")
				else:
					pass
	else:
		with open(host_path,"r+") as host-file:
			content = host_file.readlines()
			#to take host file pointer to the start:
			host_file.seek(0)
			for line in content:
				if not any(ws in lines for ws in site_block):
					host_file.write(lines)

			host_file.truncate()
		
		time.sleep(5)




