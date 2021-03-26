import requests as reqs
from bs4 import BeautifulSoup  

r = reqs.get("http://dns2.asia.edu.tw/~jdwang/PaperList.htm")
r.encoding = "big5"
if r.status_code == 200:
    #print(r.text)
    soup = BeautifulSoup(r.text, "lxml")
    #print(soup)
    result1 = soup.find_all("li")
    #rint(result1)
    fp = open("out2.txt","w",encoding="big5")
    for val in result1:
        text2 = val.text.replace('\n','')
        text3 = text2.replace(' ','')
        print(text3)
        fp.write(text3+"\n")
    fp.close()
    
else:
    print("no page")