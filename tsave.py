import requests, json
from tinit import tweets, db

print "working"
r = requests.post('https://stream.twitter.com/1/statuses/filter.json', data={'track': 'post'}, auth=('<TWITTER-USERNAME>', '<TWITTER-PASSWORD>'), stream=True)
print "connected to stream"

for line in r.iter_lines():
	try:	
		m = json.loads(line)
		if '#post' in m['text']: #if it's really something from me, or close to it
			newtweet = tweets(tweetscreen=m['user']['screen_name'], tweettext=m['text'])
			print "added", m['user']['screen_name']
			db.session.add(newtweet)
			db.session.commit()
	except Exception as e:
		print e		