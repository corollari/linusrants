import requests
import json
import pickle

api_endpoint="http://text-processing.com/api/sentiment/" #API Documentation: http://text-processing.com/docs/sentiment.html
analyzed=[]

def hateIndex(o):
    return o["hate"]

for line in open("original/rants.txt", 'r'):
    line=line[:-1] #Remove line break
    result=requests.post(api_endpoint, data={"text":line})
    negativity=json.loads(result.text)["probability"]["neg"]
    analyzed.append({"text":line, "hate":negativity})
analyzed.sort(key=hateIndex)
open("data.json", 'w').write(json.dumps(analyzed))
open("data.pkl", 'w').write(pickle.dumps(analyzed))

