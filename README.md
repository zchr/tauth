# Authenticate with a Tweet#
------
I created this as an experiment in passwordless authentication. Instead of getting an email or a text, users instead sign in by sending a tweet.

The app uses Flask and their SQLAlchemy library, and I deployed and tested the app on Heroku, using the add-on Postgresql. https://addons.heroku.com/heroku-postgresql

The app reads and saves all of the tweets that contain '#post' by connecting to a public stream. I tried to add a healthy number of comments to make the code clear and show where values need to be replaced. These two tutorials were incredibly helpful in deploying
- Heroku's Python walkthrough: https://devcenter.heroku.com/articles/python
- More Flask oriented, this one really helped me understand database configuration and the like: http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku/

