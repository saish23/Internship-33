#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')
get_ipython().system('pip install html5lib')


# In[2]:


import requests
from bs4 import BeautifulSoup


# In[50]:


# 1) Write a python program to display all the header tags from wikipedia.org.

url1 = 'https://en.wikipedia.org/wiki/Main_Page'
response1 = requests.get(url1)
htmlresponse1 = response1.content
soup1 = BeautifulSoup(htmlresponse1,'html.parser')
title1 = soup1.find_all(['h1','h2','h3','h4','h5','h6'])
print('List of all header tags: ',*title1,sep='\n\n')


# In[3]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[51]:


# 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
#    and make data frame.

url2 = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&view=simple'
url3 = 'https://www.imdb.com/search/title/?groups=top_100&view=simple&sort=user_rating,desc&start=51&ref_=adv_nxt'
page2 = requests.get(url2)
page3 = requests.get(url3)
# print(page2,'\n\n\n')

# Getting page contents:
soup2 = BeautifulSoup(page2.content)
soup3 = BeautifulSoup(page3.content)
# print(soup2,'\n\n\n') # This is page source code

# scrapping all names:

titles1 = []
titles2 = []

for i in soup2.find_all('span',class_="lister-item-header"):
    movie1 = i.text.replace('\n','')
    titles1.append(movie1)

for p in soup3.find_all('span',class_="lister-item-header"):
    movie2 = p.text.replace('\n','')
    titles2.append(movie2)

# scrapping year of release:

years1 = []
years2 = []

for j in soup2.find_all('span',class_="lister-item-year text-muted unbold"):
    years1.append(j.text.replace('(','').replace(')',''))
    
for q in soup3.find_all('span',class_="lister-item-year text-muted unbold"):
    years2.append(q.text.replace('(','').replace(')',''))

# scrapping rating:

ratings1 = []
ratings2 = []


for k in soup2.find_all('div',class_="col-imdb-rating"):
    ratings1.append(k.text.replace('\n','').replace(' ',''))

for r in soup3.find_all('div',class_="col-imdb-rating"):
    ratings2.append(r.text.replace('\n','').replace(' ',''))

data1 = pd.DataFrame()
data1['Movie Names'] = titles1
data1['Year of release'] = years1
data1['Ratings'] = ratings1

data2 = pd.DataFrame()
data2['Movie Names'] = titles2
data2['Year of release'] = years2
data2['Ratings'] = ratings2

frames = [data1,data2]
result = pd.concat(frames)

result


# In[58]:


# 3) Write a python program to display IMDB’s Top rated 100  Indian movies’ data (i.e. name, rating, year of release)
#    and make data frame.

url4 = 'https://www.imdb.com/india/top-rated-indian-movies/'

page4 = requests.get(url4)

# Getting page contents:
soup4 = BeautifulSoup(page4.content)

# scrapping all names:

ind_titles = []

for i in soup4.find_all('td',class_="titleColumn"):
    movie4 = i.text.replace('\n','')
    ind_titles.append(movie4)
    
mov = []

for i in range(0,100):
    mov.append(ind_titles[i])
    

# scrapping year of release:

years4 = []

for j in soup4.find_all('span',class_="secondaryInfo"):
    years4.append(j.text.replace('(','').replace(')',''))
    
yrs = []

for i in range(0,100):
    yrs.append(years4[i])


# scrapping rating:

ratings4 = []

for k in soup4.find_all('td',class_="ratingColumn imdbRating"):
    ratings4.append(k.text.replace('\n','').replace(' ',''))
    
rat4 = []

for i in range(0,100):
    rat4.append(ratings4[i])

data4 = pd.DataFrame()
data4['Movie Names'] = mov
data4['Year of release'] = yrs
data4['Ratings'] = rat4

data4 


# In[59]:


# 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) 
#    from https://presidentofindia.nic.in/former-presidents.htm

link = 'https://presidentofindia.nic.in/former-presidents.htm'

page5 = requests.get(link)

# Getting page contents:
soup5 = BeautifulSoup(page5.content)

# scrapping all names of president:

names_terms = []

for i in soup5.find_all('div',class_="presidentListing"):
    names = i.text.replace('\n','')
    names_terms.append(names.split('Term of Office:'))
    
namez = []
for i in range(0,14):
    namez.append(names_terms[i][0])
    
termz = []
for i in range(0,14):
    termz.append(names_terms[i][1])
    
termz[0][1].replace('https://ramnathkovind.nic.in','')
termz[1][1].replace('http://pranabmukherjee.nic.in','')
termz[2][1].replace('http://pratibhapatil.nic.in','')
termz[3][1].replace('http://abdulkalam.nic.in','')

data_prez = pd.DataFrame()
data_prez['Names'] = namez
data_prez['Term'] = termz

data_prez['Term'][0].replace('https://ramnathkovind.nic.in','',)
data_prez['Term'][1].replace('http://pranabmukherjee.nic.in','')
data_prez['Term'][2].replace('http://pratibhapatil.nic.in','')
data_prez['Term'][3].replace('http://abdulkalam.nic.in','')

data_prez


# In[62]:


# 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

link1 = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'

pglink2 = requests.get(link1)

# Getting page contents:
soup_5 = BeautifulSoup(pglink2.content)

# scrapping all names of teams:

team_names = []

for i in soup_5.find_all('span',class_="u-hide-phablet"):
    teams = i.text.replace('\n','')
    team_names.append(teams)

team_names

first_team = team_names[0]
first_matches = soup_5.find('td',class_="rankings-block__banner--matches")
first_points = soup_5.find('td',class_="rankings-block__banner--points")
first_ranking = soup_5.find('td',class_="rankings-block__banner--rating")

# scrapping team matches points and ratings :

matches_points = []

for j in soup_5.find_all('td',class_="table-body__cell u-center-text"):
    matches_points.append(j.text.replace('(','').replace(')',''))
    
matches = []

for m in range(0,38,2):
    matches.append(matches_points[m])
    
matches.insert(0,first_matches.text)

points = []

for p in range(1,38,2):
    points.append(matches_points[p])

points.insert(0,first_points.text)

rating = []

for k in soup_5.find_all('td',class_="table-body__cell u-text-right rating"):
    rating.append(k.text)
    
rating.insert(0,first_ranking.text.strip())

data5 = pd.DataFrame()
data5['Team names'] = team_names
data5['Matches'] = matches
data5['Points'] = points
data5['Ratings'] = rating

data5.head(10)


# In[63]:


# b) Top 10 ODI Batsmen along with the records of their team and rating.

linkb = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi'

pglinkb = requests.get(linkb)

# Getting page contents:
soup_5b = BeautifulSoup(pglinkb.content)

# scrapping all names of teams:

first_rec_b = soup_5b.find('div',class_="rankings-block__banner--name")
first_rec_t = soup_5b.find('div',class_="rankings-block__banner--nationality")
first_rec_r = soup_5b.find('div',class_="rankings-block__banner--rating")

batsmen_names = []

for i in soup_5b.find_all('td',class_="table-body__cell name"):
    bname = i.text.replace('\n','')
    batsmen_names.append(bname)
    
batsmen_names.insert(0,first_rec_b.text)

    
plteams = []

for j in soup_5b.find_all('span',class_="table-body__logo-text"):
    plteams.append(j.text.replace('(','').replace(')',''))
    
plteams.insert(0,first_rec_t.text.strip('890\n '))


bratings = []

for k in soup_5b.find_all('td',class_="table-body__cell u-text-right rating"):
    bratings.append(k.text.replace('(','').replace(')',''))

bratings.insert(0,first_rec_r.text)

data5_b = pd.DataFrame()
data5_b['Player names'] = batsmen_names
data5_b['Team'] = plteams
data5_b['Ratings'] = bratings

data5_b.head(10)


# In[65]:


# c) Top 10 ODI bowlers along with the records of their team and rating.

linkc = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling'

pglinkc = requests.get(linkc)

# Getting page contents:
soup_5c = BeautifulSoup(pglinkc.content)

# scrapping all names of bowlers:

first_rec_bo = soup_5c.find('div',class_="rankings-block__banner--name-large")
first_rec_tbo = soup_5c.find('div',class_="rankings-block__banner--nationality")
first_rec_rbo = soup_5c.find('div',class_="rankings-block__banner--rating")

bowler_names = []

for i in soup_5c.find_all('td',class_="table-body__cell rankings-table__name name"):
    boname = i.text.replace('\n','')
    bowler_names.append(boname)
    
bowler_names.insert(0,first_rec_bo.text)

    
boteams = []

for j in soup_5c.find_all('span',class_="table-body__logo-text"):
    boteams.append(j.text.replace('(','').replace(')',''))
    
boteams.insert(0,first_rec_tbo.text.strip())


boratings = []

for k in soup_5c.find_all('td',class_="table-body__cell rating"):
    boratings.append(k.text.replace('(','').replace(')',''))

boratings.insert(0,first_rec_rbo.text)

data5_c = pd.DataFrame()
data5_c['Bowler names'] = bowler_names
data5_c['Team'] = boteams
data5_c['Ratings'] = boratings

data5_c.head(10)


# In[66]:


# 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

linkw = 'https://www.icc-cricket.com/rankings/womens/team-rankings/odi'

pglinkw = requests.get(linkw)

# Getting page contents:
soup_6a = BeautifulSoup(pglinkw.content)

# scrapping all names of teams:

wteam_names = []

for i in soup_6a.find_all('span',class_="u-hide-phablet"):
    teams = i.text.replace('\n','')
    wteam_names.append(teams)

wfirst_team = wteam_names[0]
wfirst_matches = soup_6a.find('td',class_="rankings-block__banner--matches")
wfirst_points = soup_6a.find('td',class_="rankings-block__banner--points")
wfirst_ranking = soup_6a.find('td',class_="rankings-block__banner--rating")

# scrapping team matches points and ratings :

wmatches_points = []

for j in soup_6a.find_all('td',class_="table-body__cell u-center-text"):
    wmatches_points.append(j.text.replace('(','').replace(')',''))
    

wmatches = []

for m in range(0,20,2):
    wmatches.append(wmatches_points[m])
    
wmatches.insert(0,wfirst_matches.text)

wpoints = []

for n in range(1,20,2):
    wpoints.append(wmatches_points[n])
    
wpoints.insert(0,wfirst_points.text)

wrating = []

for l in soup_6a.find_all('td',class_="table-body__cell u-text-right rating"):
    wrating.append(l.text)
    
wrating.insert(0,wfirst_ranking.text.strip())

data6a = pd.DataFrame()
data6a['Team names Womens'] = wteam_names
data6a['Matches(W)'] = wmatches
data6a['Points(W)'] = wpoints
data6a['Ratings(W)'] = wrating

data6a.head(10)


# In[67]:


# b) Top 10 women’s ODI Batting players along with the records of their team and rating.

linkwb = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi'

pglinkwb = requests.get(linkwb)

# Getting page contents:
soup_6b = BeautifulSoup(pglinkwb.content)

# scrapping all names of teams:

wfirst_rec_b = soup_6b.find('div',class_="rankings-block__banner--name")
wfirst_rec_t = soup_6b.find('div',class_="rankings-block__banner--nationality")
wfirst_rec_r = soup_6b.find('div',class_="rankings-block__banner--rating")

wbatsmen_names = []

for i in soup_6b.find_all('td',class_="table-body__cell name"):
    wbname = i.text.replace('\n','')
    wbatsmen_names.append(wbname)
    
wbatsmen_names.insert(0,wfirst_rec_b.text)

tenwb = []

for i in range(0,10):
    tenwb.append([wbatsmen_names[i].strip('[]')])
    
wplteams = []

for j in soup_6b.find_all('span',class_="table-body__logo-text"):
    wplteams.append(j.text.replace('(','').replace(')',''))
    
wplteams.insert(0,wfirst_rec_t.text.strip('785\n '))

tenteams = []

for i in range(0,10):
    tenteams.append([wplteams[i].strip('[]')])
    
wbratings = []

for k in soup_6b.find_all('td',class_="table-body__cell u-text-right rating"):
    wbratings.append(k.text.replace('(','').replace(')',''))

wbratings.insert(0,wfirst_rec_r.text)

tenratings = []

for i in range(0,10):
    tenratings.append([wbratings[i].strip('[]')])

data6_b = pd.DataFrame()
data6_b['Player names'] = tenwb
data6_b['Team'] = tenteams
data6_b['Ratings'] = tenratings

data6_b.head(10)
    


# In[68]:


# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

alinkwb = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder'

apglinkwb = requests.get(alinkwb)

# Getting page contents:
soup_6c = BeautifulSoup(apglinkwb.content)

# scrapping all names of teams:

awfirst_rec_b = soup_6c.find('div',class_="rankings-block__banner--name-large")
awfirst_rec_t = soup_6c.find('div',class_="rankings-block__banner--nationality")
awfirst_rec_r = soup_6c.find('div',class_="rankings-block__banner--rating")

allrounder_names = []

for i in soup_6c.find_all('td',class_="table-body__cell rankings-table__name name"):
    wallname = i.text.replace('\n','')
    allrounder_names.append(wallname)
    
allrounder_names.insert(0,awfirst_rec_b.text)

tenpl = []

for i in range(0,10):
    tenpl.append([allrounder_names[i].strip('[]')])

tenwall = []

for i in range(0,10):
    tenwall.append([allrounder_names[i].strip('[]')])
    
wallwteams = []

for j in soup_6c.find_all('span',class_="table-body__logo-text"):
    wallwteams.append(j.text.replace('(','').replace(')',''))
    
wallwteams.insert(0,awfirst_rec_t.text.strip('785\n '))

tencount = []

for i in range(0,10):
    tencount.append([wallwteams[i].strip('[]')])
    
allwbratings = []

for k in soup_6c.find_all('td',class_="table-body__cell rating"):
    allwbratings.append(k.text.replace('(','').replace(')',''))

allwbratings.insert(0,awfirst_rec_r.text)

alltenratings = []

for i in range(0,10):
    alltenratings.append([allwbratings[i].strip('[]')])

data6_c = pd.DataFrame()
data6_c['Player names'] = tenpl
data6_c['Team'] = tencount
data6_c['Ratings'] = alltenratings

data6_c.head(10)


# In[69]:


"""7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
i) Headline
ii) Time
iii) News Link"""

cnbclink = 'https://www.cnbc.com/world/?region=world'

pagecnbc = requests.get(cnbclink)

# Getting page contents:
soup_7 = BeautifulSoup(pagecnbc.content)

headlines = []

for i in soup_7.find_all('a',class_="LatestNews-headline"):
    hd = i.text.replace('\n','')
    headlines.append(hd)
    
time = []

for i in soup_7.find_all('time',class_="LatestNews-timestamp"):
    tm = i.text.replace('\n','')
    time.append(tm)
    
link = []

for i in soup_7.find_all('a',class_="LatestNews-headline"):
    link.append(i.get('href'))
        
data7 = pd.DataFrame()
data7['Headlines'] = headlines
data7['Time'] = time
data7['Link'] = link

data7.head(10)


# In[70]:


"""8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days. 
https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
Scrape below mentioned details :
i) Paper Title 
ii) Authors
iii) Published Date 
iv) Paper URL"""

artlink = 'https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles'

pageart = requests.get(artlink)

# Getting page contents:
soup_8 = BeautifulSoup(pageart.content)

pap_title = []

for i in soup_8.find_all('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    ti = i.text.replace('\n','')
    pap_title.append(ti)
    
authors = []

for i in soup_8.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
    au = i.text.replace('\n','')
    authors.append(au)
    
date = []

for i in soup_8.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
    dt = i.text.replace('\n','')
    date.append(dt)

links = []

for i in soup_8.find_all('a',class_="sc-5smygv-0 nrDZj"):
    links.append(i.get('href'))
    
data8 = pd.DataFrame()
data8['Titile'] = pap_title
data8['Author'] = authors
data8['Date'] = date
data8['URL'] = links

data8


# In[71]:


"""9) Write a python program to scrape mentioned details from dineout.co.in :
i) Restaurant name
ii) Cuisine
iii) Location 
iv) Ratings
v) Image URL

"""

Dineoutlink = 'https://www.dineout.co.in/delhi-restaurants/value-for-money'

pagedin = requests.get(Dineoutlink)

# Getting page contents:
soup_9 = BeautifulSoup(pagedin.content)

rec_name = []

for i in soup_9.find_all('a',class_="restnt-name ellipsis"):
    nam = i.text.replace('\n','')
    rec_name.append(nam)
    
prices_cuisine = []

for i in soup_9.find_all('span',class_="double-line-ellipsis"):
    cu = i.text.replace('\n','')
    prices_cuisine.append(cu.split('|'))
    
cuisine = []

for i in range(0,21):
    cuisine.append(prices_cuisine[i][1])
    
locat = []

for i in soup_9.find_all('div',class_="restnt-loc ellipsis"):
    lo = i.text.replace('\n','')
    locat.append(lo)
    
ratn = []

for i in soup_9.find_all('div',class_="restnt-rating rating-4"):
    rat = i.text
    ratn.append(rat)
    
ratn.insert(10,soup_9.find_all('div',class_="restnt-rating rating-3"))
ratn.insert(11,soup_9.find_all('div',class_="restnt-rating rating-5"))


imgurl = []

for i in soup_9.find_all('img',class_="no-img"):
    imgurl.append(i.get('href'))
    
data9 = pd.DataFrame()
data9['Restaurant name'] = rec_name
data9['Cuisine'] = cuisine
data9['Location'] = locat
data9['Ratings'] = ratn
data9['Image URL'] = imgurl

data9


# In[72]:


"""
10) Write a python program to scrape the details of top publications from Google Scholar from 
https://scholar.google.com/citations?view_op=top_venues&hl=en
i) Rank 
ii) Publication
iii) h5-index
iv) h5-media"""

publink = 'https://scholar.google.com/citations?view_op=top_venues&hl=en'

pagepub = requests.get(publink)

# Getting page contents:
soup_10 = BeautifulSoup(pagepub.content)

rank = []

for i in soup_10.find_all('td',class_="gsc_mvt_p"):
    rnk = i.text.replace('\n','')
    rank.append(rnk)
    
publication = []

for i in soup_10.find_all('td',class_="gsc_mvt_t"):
    pub = i.text.replace('\n','')
    publication.append(pub)
    
h5ind = []

for i in soup_10.find_all('a',class_="gs_ibl gsc_mp_anchor"):
    ind = i.text.replace('\n','')
    h5ind.append(ind)
    
h5media = []

for i in soup_10.find_all('span',class_="gs_ibl gsc_mp_anchor"):
    h5m = i.text.replace('\n','')
    h5media.append(h5m)
    
data10 = pd.DataFrame()
data10['rank'] = rank
data10['publication'] = publication
data10['h5index'] = h5ind
data10['h5media'] = h5media

data10


# In[ ]:




