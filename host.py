# -*- coding:utf-8 -*-
import urllib2,urllib,os,sys,time,datetime

reload(sys)
sys.setdefaultencoding("utf-8")
print datetime.datetime.now()

if not os.path.exists("e:\etc\hosts"):
	print "there is no file!"
	pass
else:
	print "has a file!"
	file = open("hosts",'w')   
	old = open("e:\\etc\hosts","r")  
	url="https://raw.githubusercontent.com/racaljk/hosts/master/hosts"
	res=urllib.urlopen(url).read()
	old_host=old.read()
	file.write("# update by hehehe at time "+str(datetime.datetime.now()))
	file.write(old_host)    
	file.write(res)            
	time.sleep(2)
	file.close()
	update=open("C:\Windows\System32\drivers\etc\hosts","w")
	new=open("hosts","r").read()
	update.write(new)
	update.close()
	os.system("ipconfig -flushdns")  
	time.sleep(2)
	print "ok"