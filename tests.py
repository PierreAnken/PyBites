from collections import namedtuple
import feedparser

if __name__ == '__main__':
    FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"
    Game = namedtuple('Game', 'title link')
    fp = feedparser.parse(FEED_URL)
    print(fp.entries[0].link)
