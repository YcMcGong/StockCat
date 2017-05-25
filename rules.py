"""
This files is to defind stock checking rules
"""

class Rules():
    
    # Init function related variables
    def init__function_related(self):
    
        # __rule__detect_big_loser
        self.loser_threshold = -0.5*0.01
        self.warning_sent = False

        # __rule__rapid_losing_detection
        self.rapid_lose_threshold = 0.3*0.01

        # __rule_detect_news
        self.number_of_article = 3
        pass

    def rule__detect_big_loser(self):
        if (not self.warning_sent): 
            if (float(self.percent) <= self.loser_threshold):
                    message = 'Big Loser Info:\t' + self.name + '\t' + self.percent
                    self.warning_sent = True
                    self.send(message)
        pass

    def rule__rapid_losing_detection(self):
        percent_change = float(self.last_percent)-float(self.percent)
        if float(percent_change)>=self.rapid_lose_threshold:
            message = 'Rapid Losing Info:\t' + self.name + '\tPercent_change:\t' + str(percent_change) + '\tCurrent_change\t' + self.percent
        pass

    # def __rule_detect_news(self):
    #     if (self.news_titles[0]!=self.last_title):
    #         message = 'New news detected\t'+self.name
    #         for i in range(self.number_of_article):
    #             message = message + '\t' + self.news_titles[i] + '\t' + self.news_links[i]
    #     pass

