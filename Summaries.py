import urllib.parse 
from config import Config
import datetime,calendar

config = Config()
class SummariesModel:
    def __init__(self):
        self.url = self.setUrl(endpoint=config.getTestSuiteEndPointURL('Summaries', 'InterdaySummaries'))
        self.ric = ''
        self.queryString = {
            "interval":"",
            "start":"",
            "end":"",
            "adjustments":"",
            "fields":"",
            "count":""
        }
        self.path = "data/historical-pricing/v1/views/summaries"
        
    def setUrl(self,protocol='http',endpoint=None,port=8080):
        return "{protocol}://{endpoint}:{port}".format(protocol=protocol,endpoint=endpoint,port=port)

    def getURL(self):
        path = self.path
        keys = self.queryString.keys()
        for k in list(keys):
            if self.queryString[k]=="":
                self.queryString.pop(k)     
        URL = "{url}/{path}/{ric}?{query}".format(url=self.url,path=path,ric=self.ric,query=urllib.parse.urlencode(self.queryString))
        return URL
    
    def setRic(self, ric):
        self.ric = ric
        
    def setInterval(self, interval):
        self.queryString['interval'] = interval

    def setStartDate(self, startdate):
        self.queryString['start'] = startdate
    
    def setEndDate(self, enddate):
        self.queryString['end'] = enddate

    def setAdjustments(self, adjustment):
        self.queryString['adjustment'] = adjustment

    def setFields(self, fields):
        self.queryString['fields'] = fields
    
    def setCount(self,count):
        self.queryString['count'] = count
    
    def setDateByStartEnd(self,start,end):
        startDate = start
        endDate = end
        if start != "":
            if start != "now":
                start = start.split('-')[1]
                if start[-1] == "M":
                    monthToDayCount = 0
                    now  = datetime.datetime.now()
                    for i in range(int(start[:-1]), 0, -1):
                        monthRange = calendar.monthrange(now.year-(i//now.month), now.month - (i%now.month))[1]
                        monthToDayCount += monthRange
                    startDate = datetime.datetime.now() - datetime.timedelta(days=monthToDayCount)
                elif start[-1] == "W":
                    startDate = datetime.datetime.now() - datetime.timedelta(weeks=int(start[:-1]))
                elif start[-1] == "D":
                    startDate = datetime.datetime.now() - datetime.timedelta(days=int(start[:-1]))
                elif start[-1] == "h":
                    startDate = datetime.datetime.now() - datetime.timedelta(hours=int(start[:-1]))
                elif start[-1] == "m":
                    startDate = datetime.datetime.now() - datetime.timedelta(minutes=int(start[:-1]))
                elif start[-1] == 's':
                    startDate = datetime.datetime.now() - datetime.timedelta(seconds=int(start[:-1]))
                else:
                    startDate = datetime.datetime.now()
            elif start == "now":
                startDate = datetime.datetime.now()

            try:
                startDate = startDate.strftime('%Y-%m-%dT%H:%M:%SZ')
            except Exception as e:
                print(e)

        if end != "":
            if end != "now":
                end = end.split('-')[1]
                if end[-1] == "M":
                    monthToDayCount = 0
                    now = datetime.datetime.now()
                    for i in range(int(end[:-1]), 0, -1):
                        monthRange = calendar.monthrange(now.year - (i / now.month), now.month - (i % now.month))[1]
                        monthToDayCount += monthRange
                    endDate = datetime.datetime.now() - datetime.timedelta(days=monthToDayCount)
                elif end[-1] == "W":
                    endDate = datetime.datetime.now() - datetime.timedelta(weeks=int(end[:-1]))
                elif end[-1] == "D":
                    endDate = datetime.datetime.now() - datetime.timedelta(days=int(end[:-1]))
                elif end[-1] == "h":
                    endDate = datetime.datetime.now() - datetime.timedelta(hours=int(end[:-1]))
                elif end[-1] == "m":
                    endDate = datetime.datetime.now() - datetime.timedelta(minutes=int(end[:-1]))
                elif end[-1] == "s":
                    endDate = datetime.datetime.now() - datetime.timedelta(seconds=int(end[:-1]))
                else:
                    endDate = datetime.datetime.now()
            elif end == "now":
                endDate = datetime.datetime.now()

            try:
                endDate = endDate.strftime('%Y-%m-%dT%H:%M:%SZ')
            except Exception as e:
                print(e)
                pass

        self.setStartDate(startDate)
        self.setEndDate(endDate)
    
class InterdaySummariesModel(SummariesModel):
    def __init__(self):
        self.url = self.setUrl(endpoint=config.getTestSuiteEndPointURL('Interday_Summaries', 'InterdaySummaries'))
        self.ric = ''
        self.queryString = {
            "interval":"",
            "start":"",
            "end":"",
            "adjustments":"",
            "fields":"",
            "count":""
        }
        self.path = "data/historical-pricing/v1/views/interday-summaries"