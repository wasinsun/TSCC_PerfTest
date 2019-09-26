from config import Config
import json
from Interday_Summaries import InterdaySummariesModel
import logging
import datetime

def runTest():
    config = Config()
    testSuites = config.getTestSuites()
    interdaySummariesTestCase(config)
    
def loadTestData(path):
    testcases = []
    try:
        testcases = open(path, 'r').readlines()
    except:
        pass
    testcases = [x.strip() for x in testcases]
    return testcases[1:]
    
def interdaySummariesTestCase(config):
    testSuite = "Interday_Summaries"
    roundOfTest = config.getRoundOfTest(testSuite)
    testSuiteEndPoint= config.getTestSuiteEndPoint(testSuite)
    endPointData = config.getEndPointsData(testSuiteEndPoint)
    headerData = config.getHeaderData(testSuite)
    testDataFile = config.getTestDataFile(testSuite, 'InterdaySummaries')
    csvData = loadTestData(testDataFile)
    for e in csvData:
        data = e.split(',')
        testCase = data[0]
        ric = data[1]
        interval = data[2]
        start = data[3]
        end = data[4]
        adjustments = data[5].replace('|',',')
        fields = data[6]
        count = data[7]
        interdaySummariesModel = InterdaySummariesModel()
        interdaySummariesModel.setRic(ric)
        interdaySummariesModel.setInterval(interval)
        interdaySummariesModel.setDateByStartEnd(start, end)
        interdaySummariesModel.setAdjustments(adjustments)
        interdaySummariesModel.setCount(count)
        interdaySummariesModel.setFields(fields)
        requestURL = interdaySummariesModel.getURL()

        # print('url: {}'.format(requestURL))
        logging.basicConfig(filename='./log/interdaySummariesTestCase{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%dT%H_%M_%S')), level=logging.DEBUG)
        logging.debug(requestURL)

runTest()