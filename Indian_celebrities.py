from urllib.request import urlopen
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np


def getHtmlCode(link):
    code=urlopen(link)
    soup=BeautifulSoup(code,'html.parser')
    return soup
    
#getting actresses list
content=getHtmlCode('https://en.wikipedia.org/wiki/List_of_Indian_film_actresses')
names=[]
navg_link=[]
for i in content.findAll('li'):
    name=i.find('a',href=True)
    if(name!=None):
        navg_link.append('https://en.wikipedia.org'+name.get('href'))
        names.append(name.text)
        if(name.text=='Zaheeda'):
            break;
names=names[2:]
navg_link=navg_link[2:]


#getting all actors name
content2=getHtmlCode('https://en.wikipedia.org/wiki/List_of_Indian_film_actors')
names2=[]
navg_link2=[]
for i in content2.findAll('li'):
    name=i.find('a',href=True)
    if(name!=None):
        navg_link2.append('https://en.wikipedia.org'+name.get('href'))
        names2.append(name.text)
        if(name.text=='Zulfi Syed'):
            break;          
names2=names2[1:]
navg_link2=navg_link2[1:]


#to get images
image_link=[]
for  i in navg_link:
    if ('title' in i) or ('action' in i) or  ('redlink' in i):
        image_link.append(None)
        continue
    content3=getHtmlCode(i)
    tbody_data=content3.findAll('tbody')[0]
    name=tbody_data.find('img')
    if(name!=None):
        image_link.append(name.get('src'))
    else:
        image_link.append(None)



image_link2=[]
for  i in navg_link2:
    if ('title' in i) or ('action' in i) or  ('redlink' in i):
        image_link2.append(None)
        continue
    content3=getHtmlCode(i)
    tbody_data=content3.findAll('tbody')[0]

    name=tbody_data.find('img')
    if(name!=None):
        image_link2.append(name.get('src'))
    else:
        image_link2.append(None)
            

def url_to_array(url):
    image=urlopen(url)
    image_array=np.asarray(bytearray(image.read()), dtype="uint8")
    return image_array


images_array=[]
for i in image_link:
    if i==None:
        images_array.append(None)
        continue
    image=url_to_array('https:'+i)
    images_array.append(image)

images_array2=[]
for i in image_link2:
    if i==None:
        images_array2.append(None)
        continue
    image=url_to_array('https:'+i)
    images_array2.append(image)

Names=names+names2
p=profiles_text1+profiles_text2
Images=images_array+images_array2
df=pd.DataFrame({'Images':Images,'Names':Names,'Personality traits':p})
df.to_csv('G:/Explore ML (amrita)/assignment_bipolar/celebrities_dataset.csv',index=False)
