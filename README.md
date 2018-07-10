Django Project for fetching/Counting the tweet among 
10Million of Tweets Using ElasticSearch

APIs 
1.getweetcount/, 
required field:-model return:-No of twitt ass of now in the database 

2.addData 
required field:- noOFData,model 
return:-"Data Added" with 202 status code 


3.searchtext/ 
required field:- model,text 
return:-The no of Tweets Contains "text" in the body or in the HashTags field of tweet

Note:- 
model:-the index name on which data is being searched 
noOFData:-noOfData which we want to add 
text:-text to be seach across all the tweets and the HashTags od all the tweet

Python Library Used: 
certifi==2018.4.16 
chardet==3.0.4 
cookies==2.2.1 
Django==1.11.14 
django-elasticsearch-dsl==0.5.0 
djangorestframework==3.8.2 
elasticsearch==6.3.0 
elasticsearch-dsl==6.2.1 
funcsigs==1.0.2 
idna==2.7 
ipaddress==1.0.22 
mock==2.0.0 
pbr==4.1.0 
pretty==0.1 
python-dateutil==2.7.3 
pytz==2018.5 
requests==2.19.1 
responses==0.9.0 
twitter==1.18.0
