from urllib.request import urlopen
from bs4 import BeautifulSoup



def getHtmlCode(link):
    code=urlopen(link)
    soup=BeautifulSoup(code,'html.parser')
    return soup

#getting celebrities total=200
#page1
link1='https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=1'
content=getHtmlCode(link1)
names=[]
navg_link=[]
for i in content.findAll('h3',attrs={'class':'lister-item-header'}):
    name=i.find('a',href=True)
    if(name!=None):
        navg_link.append('https://www.imdb.com'+name.get('href'))
        names.append(name.text[1:-1])


bio_link=[]
for i in navg_link:
    content=getHtmlCode(i)
    l=content.findAll('div',attrs={'class':'inline'})[0]
    name=l.find('a',href=True,string='See full bio')
    if name!=None:
        bio_link.append('https://www.imdb.com'+name.get('href'))
    
bio=[]
for i in bio_link:
    content=getHtmlCode(i)
    l=content.findAll('div',attrs={'id':'bio_content'})[0]
    if l!=None:
        bio.append(l)    


#page2
link2=link1[:-1]+'2'
content=getHtmlCode(link2)
names2=[]
navg_link2=[]
for i in content.findAll('h3',attrs={'class':'lister-item-header'}):
    name=i.find('a',href=True)
    if(name!=None):
        navg_link2.append('https://www.imdb.com'+name.get('href'))
        names2.append(name.text[1:-1])

bio_link2=[]
for i in navg_link2:
    content=getHtmlCode(i)
    l=content.findAll('div',attrs={'class':'inline'})[0]
    name=l.find('a',href=True,string='See full bio')
    if name!=None:
        bio_link2.append('https://www.imdb.com'+name.get('href'))
    
bio2=[]
for i in bio_link:
    content=getHtmlCode(i)
    l=content.findAll('div',attrs={'id':'bio_content'})[0]
    if l!=None:
        bio2.append(l)        

Names=names+names2
b=bio+bio2
df1=pd.DataFrame({'Names':Names,'bio':b})
df2=pd.read_csv('celebrities_dataset.csv')
df1.set_index('Names',inplace=True)
df2.set_index('Names',inplace=True)
final=pd.merge(df1,df2,how='left',left_index=True,right_index=True)
final2=pd.merge(df2,df1,how='left',left_index=True,right_index=True)
final=final.append(final2,sort=False)
final.reset_index(inplace=True)
final.drop_duplicates(subset='Names',keep='first',inplace=True)
final.reset_index(inplace=True)
final.loc[203:,'bio']=final.loc[203:,'Personality traits']
final.to_csv('test.csv',index=False)
