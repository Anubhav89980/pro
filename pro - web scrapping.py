#!/usr/bin/env python
# coding: utf-8

# In[65]:


import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging


# In[66]:


flipcart_url = "https://www.flipkart.com/search?q=" + "iphone12pro"


# In[67]:


flipcart_url


# In[68]:


urlclient = urlopen(flipcart_url)


# In[69]:


urlclient


# In[70]:


flipcart_page = urlclient.read()


# In[71]:


flipcart_html = bs(flipcart_page,'html.parser')


# In[99]:


"https://www.flipkart.com/"+"apple-iphone-12-pro-max-pacific-blue-128-gb/p/itmd89812b558a03?pid=MOBFWBYZZABKHZQA&lid=LSTMOBFWBYZZABKHZQACQ9MLL&marketplace=FLIPKART&q=iphone12pro&store=tyy%2F4io&srno=s_1_2&otracker=search&iid=e633c664-795d-437d-9c98-cf74b54b9e13.MOBFWBYZZABKHZQA.SEARCH&ssid=mu9oenbu0w0000001707653580688&qH=712933e6bd68e7b9"


# In[100]:


bigbox = flipcart_html.findAll("div", {"class":"_1AtVbE col-12-12"})


# In[101]:


len(bigbox)
del bigbox[0:3]


# In[102]:


productlink = "https://www.flipkart.com" +bigbox[3].div.div.div.a['href']


# In[110]:


product_req = requests.get(productlink)


# In[111]:


productlink


# In[112]:


product_html = bs(product_req.text,'html.parser')


# In[114]:


comment_box = product_html.find_all("div" ,{"class" : "_16PBlm"})


# In[115]:


comment_box[0]


# In[116]:


comment_box[0].div.div.find_all('p',{"class":"_2sc7ZR _2V5EHH"})[0].text


# In[117]:


for i in comment_box:
    print(i.div.div.find_all('p',{"class":"_2sc7ZR _2V5EHH"})[0].text)


# In[118]:


comment_box[0].div.div.div.div.text


# In[119]:


for i in comment_box:
    print(i.div.div.div.div.text)


# In[121]:


for i in comment_box:
    print(i.div.div.div.p.text)


# In[122]:


comment_box[0].div.div.find_all('div',{"class":''})[0].text


# In[123]:


for i in comment_box:
    print(i.div.div.find_all('div',{"class":''})[0].text)


# In[58]:


for i in bigbox:
    print("https://www.flipkart.com" +i.div.div.div.a['href'])


# In[ ]:





# In[ ]:




