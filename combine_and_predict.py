from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import csv
import pandas as pd


df=pd.read_csv('test.csv')

#change
api_key='your api key'
u='your url'

authenticator = IAMAuthenticator(api_key)
personality_insights = PersonalityInsightsV3(
    version='2017-07-13',
    authenticator=authenticator
)
personality_insights.set_service_url(u)

for i in df.bio:
   if(str(i)!='nan' and len(i)>25000):
        profile = personality_insights.profile(
                i,
                'text/csv',
                content_type='text/html',
                consumption_preferences=True,
                raw_scores=True,
                csv_headers=True
            ).get_result()
        dec_content = profile.content.decode('utf-8')
        cr = csv.reader(dec_content.splitlines(), delimiter=',')
        my_list = list(cr)
        my_list[0].insert(0,'Names')
        data=[]
        data.append(my_list[1])
        data[0].insert(0,df['Names'][l])
        bio.append(data)
                
bio2=[]
for i in bio:
	bio2.append(i[0])

df3=pd.DataFrame(bio2,columns=my_list[0])
df4=df3.iloc[:,:35]
df5=df3.iloc[:,86:120]
df5['Names']=df4['Names'].values
df4.set_index('Names_x')
df.set_index('Names')
df6=pd.merge(df4,df5,how='inner',left_index=True,right_index=True)
df6=df6.drop('Names_y',axis=1)#it contains extra name
df7=pd.merge(df,df6,how='inner',left_index=True,right_index=True)
df7=df7.drop(['Unnamed: 0','Names_x','Personality traits'],axis=1)
df7.to_csv('celebrities_personalityTraits_dataset.csv.csv',index=False)
