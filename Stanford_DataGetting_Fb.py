# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:16:47 2020

@author: MARYAM
"""

#Getting the data

#Importing libraries

import requests
import time 
import random
import pandas as pd

token = "your token"

def req_facebook(req):
    r = requests.get("https://graph.facebook.com/v5.0/"+ req , {'access_token': token})
    
    return r

#the below one is having all comments,replies+likes thing
req= "mentalhealthawarenesspk/feed?fields=comments{comments{message},message},message,reactions.type(LIKE).limit(0).summary(total_count).as(reactions_like),reactions.type(LOVE).limit(0).summary(total_count).as(reactions_love),reactions.type(SAD).limit(0).summary(total_count).as(reactions_sad),reactions.type(WOW).limit(0).summary(total_count).as(reactions_wow),reactions.type(HAHA).limit(0).summary(total_count).as(reactions_haha),reactions.type(ANGRY).limit(0).summary(total_count).as(reactions_angry)"
results = req_facebook(req).json()


data = []
m=results
i=0
while True:
    
    try:
        time.sleep(random.randint(2,5))
        data.extend(m['data'])
        r=requests.get(m['paging']['next'])
        print(r)
        m = r.json()
        i+=1
        print(i)
        if i > 20:
            break
        
    except:
        print ('done')
        break
    
data1= data
        
from flatten_json import flatten   

dic_flattened = (flatten(d) for d in data1)   
dff = pd.DataFrame(dic_flattened) 
dff.to_csv('Stanford_Project_Sentiment.csv')
#checking all those columns that have message name in the header
a = dff.columns
a.tolist()
#for i in range(len(a)):
#    matching = [s for s in a if "message" in s]
matching1 = [q for q in a if "message" in q]


g = dff[matching1]
g3= g.stack()
g5 = pd.DataFrame(g3)
g5 = g5.reset_index(drop = True)
g5.to_csv('Stanford_only_comments_.csv', index=False)

