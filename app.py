from flask import Flask, session, request, url_for, render_template, redirect
import time, json, requests, string, random, time, os

from tinit import tweets, db

app = Flask(__name__)
app.secret_key = #this is a secret key. there are many like it, but this one is mine.

@app.route('/', methods=['POST', 'GET'])
def home():
	def generate(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
		session['sec']=''.join(random.choice(chars) for x in range (12))
	generate()
	link = 'https://twitter.com/intent/tweet?text=sign%20in%20with%20a%20tweet&hashtags=post%2C'+session['sec']

	return render_template('index.html', ln=link)

@app.route('/auth', methods=['POST', 'GET'])
def auth():
	#make sure they're not signed in
	if 'signed-in-user' in session:
		return redirect(url_for('home'))

	if request.method == 'POST':
		#make sure inputted username doesn't contain '@'
		u = request.form['username-input']
		if '@' in u:
			session['username'] = u[1:]
		else:	
			session['username'] = u
		return redirect(url_for('auth'))
	
	#only for 20ish seconds	
	start=time.time()
	while (time.time()-start) < 20:
		r = tweets.query.filter_by(tweetscreen=session['username']).all()
		for q in r:
			if session['sec'] in q.tweettext:
				session.pop('sec', None) #get rid of sec
				session.pop('username', None) #get rid of username
				session['signed-in-user'] = q.tweetscreen
				
				#delete the tweet from the database
				db.session.delete(q)
				db.session.commit()
				
				print "sign in success"
				return redirect(url_for('home'))	
		time.sleep(.1)
	#else give up
	return redirect(url_for('error'))	

@app.route('/error')
def error():
	return render_template('error.html')

@app.route('/logout')
def logout():
	session.pop('signed-in-user', None) #get rid of user
	return redirect(url_for('home'))

if __name__ == '__main__':
	#configured to run on Heroku
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)	