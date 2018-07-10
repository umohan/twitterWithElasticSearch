from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search, DateRange
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import datetime
connections.create_connection()
#For Deleting the data of all the index
# curl -XDELETE localhost:9200/shop
def getNoOfData(self,request,format=None):
    # Requirements:
    # model
    try:
        sendData=[]
        es = Elasticsearch()
        es.indices.refresh(index=request['model'])
        res = es.search(index="twitter-index", body={"query": {"match_all": {}}})
        sendData.append({ "Totaltweets": res['hits']['total']})
        return sendData
    except Exception as e:
        return "Bad_Request"

def addTweet(self,request,format=None):
    # Requirements:
    # noOfData
    try:
        es = Elasticsearch()
        ACCESS_TOKEN = ''
        ACCESS_SECRET = ''
        CONSUMER_KEY = ''
        CONSUMER_SECRET = ''
        oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        twitter_stream = TwitterStream(auth=oauth)
        iterator = twitter_stream.statuses.sample()
        tweet_count = int(request["noOfData"])
        for tweet in iterator:
            if 'text' in tweet:
                print tweet['id']
                hashtags = []
                for hashtag in tweet['entities']['hashtags']:
                    hashtags.append(hashtag['text'])
                source= {
                    "created_at": tweet['created_at'],
                    "text": tweet['text'],
                    "userId": tweet['user']['id'],
                    "userName": tweet['user']['name'],
                    "hashTags":hashtags
                    }
                es.index(index="twitter-index", doc_type='tweets', id=tweet['id'], body=source)
                tweet_count -= 1
                if (tweet_count == 0):
                    break
        return "DoneAdding"
    except:
        return "Bad_request"

def searchUser(self, request, format=None):
    # Requirements:
    # model
    # userName
    try:
        sendData = []
        es = Elasticsearch()
        es.indices.refresh(index=request['model'])
        res = es.search(index="twitter-index", body={"query": {"match": {"userName":request["userName"]}}})
        sendData.append({"Totaltweets": res['hits']['total']})
        return sendData
    except Exception as e:
        return "Bad_Request"

def searchText(self,request,format=None):
    try:
        sendData = []
        searchValue='.*'+str(request["search"])+'.*'
        print searchValue
        es = Elasticsearch()
        es.indices.refresh(index=request['model'])
        res = es.search(index=request['model'], body={"query":
                                                          {"bool":
                                                               {"should":
                                                                    [
                                                                        {"regexp": {"text": searchValue}},
                                                                         {"regexp": {"hashTags": searchValue}}
                                                                     ]
                                                                }
                                                           }
                                                      }
                        )
        print (res['hits']['total'])

        sendData.append({"TotalMatches": res['hits']['total']})
        totalCount=int(res['hits']['total'])
        # for i in range(0,totalCount):
        #     source = {
        #         "id":res['hits']['hits'][i]['_id'],
        #         "text": res['hits']['hits'][i]['_source']['text'],
        #         "hashTags": res['hits']['hits'][1]['_source']['hashTags']
        #     }
        #     sendData.append(source)
        return sendData
    except Exception as e:
        return "Bad_Request"


def searchWithTime(self,request,format=None):
    # Requirements:
    # model
    # maxTime upto which userwant to search
    es = Elasticsearch()
    res = es.search(index=request['model'], body={
        "query": {
            "range": {
                "time": {
                    "gte": request["maxTime"],
                    "lte": datetime.datetime.now()-datetime.timedelta(seconds=90),
                }
            }
        }
    })
    # "range":{
    #     "doc.timestamp_utc": {
    #         "gte": 1451606400000,
    #         "lt": 1483228800000,
    #         "format": "epoch_millis"
    #     }
    # }
    print res