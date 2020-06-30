from datetime import datetime
from hashlib import sha224
from ..models import CrawlerStats
from dateparser import parse



def checkDescription(description):
    if description == "":
        return True
    return False

def getPublishedAt(date):
    try:
        now = datetime.now()
        date = parse(date)
        diff = now - date
        hours = diff.seconds / 3600
        if 24 >= hours >= -24:
            date = str(date)
        else:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return date

def getCrawlerStats(resource, session):
    hash = sha224(resource + str(datetime.now().date())).hexdigest()
    crawlerStats = session.query(CrawlerStats).filter(CrawlerStats.hash == hash).first()
    if crawlerStats is None:
        crawlerStats = CrawlerStats(time=datetime.now(), resource=resource, count=0, operation_time=0, hash=hash)
        session.save(crawlerStats)
    else:
        crawlerStats.time = datetime.now()
        session.update(crawlerStats)
    return crawlerStats

def updateCrawlerStats(crawlerStats, session, n=1):
    crawlerStats.operation_time = (datetime.now() - crawlerStats.time).total_seconds()
    crawlerStats.count += n
    session.update(crawlerStats)
