
import urllib.request
import json

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent} 
address="http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page="

i=1
true_count=0
false_count=0
has_more=True
#iterate over each page
while has_more==True:
	url=address+str(i)
	print(url)
	i=i+1
	request=urllib.request.Request(url,None,headers)
	response=urllib.request.urlopen(request)
	json_parsed=json.loads(response.read())
	#iterate over array
	for index in range(len(json_parsed['response'])):
		if json_parsed['response'][index]['flags']['hd']==True:
			true_count=true_count+1
		else:
			false_count=false_count+1
	has_more=json_parsed['more']
	print(has_more)

print("true flags:hd count:" + str(true_count))
print("false flags:hd count:" + str(false_count))
