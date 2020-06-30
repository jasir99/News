from flask import Flask, request, jsonify
from flask_mongoalchemy import MongoAlchemy
from datetime import datetime, timedelta
from pymongo import MongoClient


API_KEY = "4ab0aeff-4eb5-4d96-a2b8-f40ecf0412a3"

app = Flask(__name__)

app.config['MONGOALCHEMY_SERVER'] = 'localhost'
client = MongoClient('mongodb://localhost:27017')
app.config['MONGOALCHEMY_DATABASE'] = 'news'

db = MongoAlchemy(app)

from modules.models import *

def toInt(tmpVal, default=0):
    if tmpVal is None or not tmpVal.isdigit:
        return default
    else:
        return int(tmpVal)

#Get all news articles
@app.route("/")
def news_all():
    #Parse Arguments
    api_key = request.args.get('api_key')
    limit = toInt(request.args.get('limit'), 10)
    offset = toInt(request.args.get('offset'), 0)
    since = request.args.get('since')

    #Check API Key
    if api_key != API_KEY:
        return jsonify({"message": "Bad API Key!"})

    if since is not None:
        news = News.query.filter(News.crawled_time > datetime.fromtimestamp(float(since), None)).descending(News.crawled_time).limit(limit).skip(offset)
        total = news.count()
    else:
        news = News.query.descending(News.crawled_time).limit(limit).skip(offset)
        total = news.count()

    return jsonify(total=total, news=[n.serialize() for n in news])

#Filter news articles by league code
@app.route("/league/<league>")
def news_league(league):
    # Parse Arguments
    api_key = request.args.get('api_key')
    limit = toInt(request.args.get('limit'), 10)
    offset = toInt(request.args.get('offset'), 0)
    since = request.args.get('since')

    # Check API Key
    if api_key != API_KEY:
        return jsonify({"message": "Bad API Key!"})

    if since is not None:
        news = News.query.filter(News.crawled_time > datetime.fromtimestamp(float(since), None)).filter(News.league == league).descending(News.crawled_time).limit(limit).skip(offset)
        total = news.count()
    else:
        news = News.query.filter(News.league == league).descending(News.crawled_time).limit(limit).skip(offset)
        total = news.count()

    return jsonify(total=total, news=[n.serialize() for n in news])

#Filter news articles by league code v2
@app.route("/v2/league/<league>")
def news_league_v2(league):
    # Parse Arguments
    api_key = request.args.get('api_key')
    limit = toInt(request.args.get('limit'), 10)
    offset = toInt(request.args.get('offset'), 0)
    since = request.args.get('since')

    # Check API Key
    if api_key != API_KEY:
        return jsonify({"message": "Bad API Key!"})

    if since is not None:
        news = News.query.filter(News.crawled_time > datetime.fromtimestamp(float(since), None)).filter(News.league == league).limit(limit).skip(offset)
        total = news.count()
    else:
        news = News.query.filter(News.league == league).descending(News.crawled_time).limit(limit).skip(offset)
        total = news.count()

    return jsonify(total=total, news=[n.serialize() for n in news])

#Filter news articles by team name
@app.route("/team/<team>")
def news_team(team):
    # Parse Arguments
    api_key = request.args.get('api_key')
    limit = toInt(request.args.get('limit'), 10)
    offset = toInt(request.args.get('offset'), 0)

    # Check API Key
    if api_key != API_KEY:
        return jsonify({"message": "Bad API Key!"})

    news = News.query.filter(News.team == team).descending(News.crawled_time).limit(limit).skip(offset)
    return jsonify(news=[n.serialize() for n in news])


#Filter news articles by Team Code
@app.route("/team_code/<team_code>")
def news_team_code(team_code):
    # Parse Arguments
    api_key = request.args.get('api_key')
    limit = toInt(request.args.get('limit'), 10)
    offset = toInt(request.args.get('offset'), 0)

    # Check API Key
    if api_key != API_KEY:
        return jsonify({"message": "Bad API Key!"})

    news = News.query.filter(News.team_code == team_code).descending(News.crawled_time).limit(limit).skip(offset)
    return jsonify(news=[n.serialize() for n in news])
