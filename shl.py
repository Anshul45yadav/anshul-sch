import schedule
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from tbselenium.tbdriver import TorBrowserDriver
Links=[]
satatus=[1,1]
urgent=[0,0]
def job():
   with TorBrowserDriver("/home/codebin/Downloads/tor-browser") as driver:
      driver.get('https://duckduckgo.com/?q=bianlianlbc5an4kgnay3opdemgcryg2kpfcbgczopmm3dnbz3uaunad.onion&ia=onionaddress')
      data=driver.page_source   
      alldata="".join(data)
      soup=BeautifulSoup(alldata,'html.parser')
      Title=[]
      Ara=[]
      link=driver.find_elements(By.XPATH,"/html/body/div/div/div/div/div/div/div/article/div/div/a")
      for l in range(4):
         Links.append(link[l].get_attribute('href')) 
      for o in Links:
        driver.get(o)
        time.sleep(1)
        ta=driver.page_source
        aldata=''.join(ta)
        soup=BeautifulSoup(aldata,'html.parser')
        ara= soup.find_all("p")
        ra=soup.find_all('h2')
        a=soup.find_all("h3")
        tem=""
        cem=""
        for t in ra:
           cem+=t.text
        for t in a: 
            cem+=t.text 
        Title.append(cem)  

        for t in ra:
           tem+=t.text
        for t in a: 
            tem+=t.text  
        for t in ara:
          tem+=t.text

        Ara.append(tem)
        createdBy=[]
        createdaAt=[]
        for i in range(len(Ara)):
            createdBy.append("anshul")
            createdaAt.append("28/12/2022") 

        
      print(Ara)
      l=pd.DataFrame({'title':Title,'body':Ara,'url':Links,'createdBy':createdBy,'createdaAt':createdaAt})
      l.to_csv('/home/codebin/Documents/ MYdata00.csv',index=False)
      print(l)
   Links.clear()
def scrap1():
   with TorBrowserDriver("/home/codebin/Downloads/tor-browser") as driver:
      driver.get('http://lockbitapt2yfbt7lchxejug47kmqvqqxvvjpqkmevv4l3azl3gy6pyd.onion')
      y=3000
      for i in range(10):
         driver.execute_script(f"window.scrollTo(0,{y})")
         y+=2000
         time.sleep(3)
      data=driver.page_source   
      alldata="".join(data)
      soup=BeautifulSoup(alldata,'html.parser') 
     
      Para=[]
      Date=[]
    #Link=[]
    #Ara=[]
    
      head=driver.find_elements(By.XPATH,"/html/body/div/div/div/div/div/div/div/div[1]")
      para=driver.find_elements(By.XPATH,"/html/body/div/div/div/div/div[2]/div")
    #para=soup.find_all('div',class_="post-block-text")
      date=driver.find_elements(By.XPATH,"/html/body/div/div/div/div/div/div[1]/span")
      for u in head:
         Links.append(u.text)
      for p in para:
         Para.append(p.text)
      for d in date:
         Date.append(d.text)   
      createdBy=[]
      createdaAt=[]
      url=[]
      for i in range(len(Links)):
         createdBy.append("anshul")
         createdaAt.append("28/12/2022")
         url.append("http://lockbitapt2yfbt7lchxejug47kmqvqqxvvjpqkmevv4l3azl3gy6pyd.onion")             
   #print(Para)
   #print(Date) 
   l=pd.DataFrame({'title':Links,'body':Para,'Date':Date,'url':url,'createdBy':createdBy,'createdaAt':createdaAt})
   l.to_csv('/home/codebin/Documents/ MYdata99.csv',index=False)
   print(l)
   print(l)
  
   
   





       

if len(Links)==0:
   for i in range(2):
      if urgent[i]==1:
         if i==0:
            schedule.every(5).seconds.do(job)

         else:
             schedule.every(5).seconds.do(scrap1)

   for i in range(2):
      if satatus[i]==1:
         if i==0:
            schedule.every(5).seconds.do(job)

         
         else:   
            schedule.every(5).seconds.do(scrap1)






while True:
   schedule.run_pending()
   time.sleep(1)