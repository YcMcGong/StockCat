from datetime import datetime
from datetime import timedelta 
from googlefinance import getQuotes
from googlefinance import getNews
import json
import time
from slacker import Slacker
from rules import Rules

class Stock(Rules):
    
    # Init the stock name
    def __init__(self, name: str, slack):
        self.name = name
        self.init__function_related()
        self.price, self.percent = self.get_price_and_percent()
        # self.news_titles, self.news_links = self.get_news()
        self.slack = slack
        self.last_price = self.price
        self.last_percent = self.percent
        # self.last_title = self.news_titles[0]

    # Method to return price and pecentage
    def get_price_and_percent(self):
        quote = json.dumps(getQuotes(self.name), indent=2)
        quote_list = json.loads(quote)
        price = quote_list[0]['LastTradePrice']
        percent = quote_list[0]['ChangePercent']
        previous_close = quote_list[0]['PreviousClosePrice']
        return price, percent
    
    # Method to return news update about a stock
    def get_news(self):
        number_of_article = self.number_of_article
        quote = json.dumps(getNews(self.name), indent=2)
        quote_list = json.loads(quote)
        quote_list = quote_list[0:number_of_article]
        news_titles = []
        news_links = []
        for i in range(number_of_article):
            news_titles.append(quote_list[i]['t'])
            news_links.append(quote_list[i]['sru'])
        return news_titles, news_links

    # Update prices and news
    def __update__(self):
        self.price, self.percent = self.get_price_and_percent()
        # self.news_titles, self.news_links = self.get_news()

    def send(self, message):
        self.slack.chat.post_message('#general', message)
    
    # The function to check all rules and updates
    def run(self):
        self.__update__()
        self.rule__detect_big_loser()
        self.rule__rapid_losing_detection()
        # self.__rule_detect_news()

class StockPool():
    
    def __init__(self, watch_list, buying_price, init_change):
        self.slack = self.init_slack_bot()
        self.watch_list = watch_list
        self.buying_price = buying_price
        self.number_of_stock = len(watch_list)
        self.stock_price = buying_price
        self.stock_change = init_change
        self.stock_list = []
        for st in watch_list:
            self.stock_list.append(Stock(st, self.slack))

    def init_slack_bot(self):
	# Token and url are hidden for security purpose
	# Once updated and tested admin will add the new code to the server using real token
        slack = Slacker('token',incoming_webhook_url='url') 
        return slack

    def run(self):
        while True:
            for st in self.stock_list:
                st.run()
            time.sleep(30)
