

from bs4 import BeautifulSoup
import urllib

word = raw_input("Enter the word you want to search\n") 
get = urllib.urlopen("http://www.thefreedictionary.com/"+word)
rd = get.read()
#print rd[2]
fp1 = open("test", "w")

soup1 = BeautifulSoup(rd) 

li = soup1.find_all("table")
#print li
#rd2 = ''
rd2 = li[5]
rd3 = str( rd2 )
print rd3
#fp1.write(rd3)
#print rd3[2]
#print rd2
soup2 = BeautifulSoup(rd3) 
flag = 0
li2 = soup2.find_all('div')
li5 = []
#string = ''
for w1 in li2:
   w2 = str(w1)
   for ch in w2:
     if ch == '<':
       flag = 1
     elif ch == '>':
       flag = 0
     elif flag == 1:
       continue
     else:
        li5.append(ch)
   str1 = ''.join(li5)
   print str1
   li5 = []
   str1 = ''
   #soup3 = BeautifulSoup(w2)
   #print soup3.span.string
   print '\n\n'

#print tag['class']
