from config import Config
import json
import csv
import logging
import datetime
import urllib.parse

from Interday_Summaries import InterdaySummariesModel

def runTest():
    config = Config()
    interdaySummaries(config)
      
def loadTestData(path):
    testcases = []
    try:
        testcases = open(path, 'r').readlines()
    except:
        pass
    testcases = [x.strip() for x in testcases]
    return testcases[1:]

def getColumnName(path):
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        columnName = reader.fieldnames
    return columnName
    
def interdaySummaries(config):
    interface = "Interday_Summaries"
    testSuites = config.getTestSuites(interface)
    for e in testSuites:
        testSuite = e
        roundOfTest = config.getRoundOfTest(interface, testSuite)
        testSuiteEndPoint= config.getTestSuiteEndPoint(interface, testSuite)
        endPointData = config.getEndPointsData(testSuiteEndPoint)
        headerData = config.getHeaderData()
        testDataFile = config.getTestDataFile(interface, testSuite)
        csvColumnName = getColumnName(testDataFile)
        configRequestParams = config.getRequestParams(interface)
        if csvColumnName == configRequestParams:
            csvData = loadTestData(testDataFile)
            for e in csvData:
                data = e.split(',')
                testCase = data[0]
                ric = data[1]
                interval = data[2]
                start = data[3]
                end = data[4]
                adjustments = data[5].replace('|',',')
                fields = data[6].replace('|',',')
                count = data[7]
                interdaySummariesModel = InterdaySummariesModel()
                interdaySummariesModel.setRic(ric)
                interdaySummariesModel.setInterval(interval)
                interdaySummariesModel.setDateByStartEnd(start, end)
                interdaySummariesModel.setAdjustments(adjustments)
                interdaySummariesModel.setCount(count)
                interdaySummariesModel.setFields(fields)
                requestURL = interdaySummariesModel.getURL()

                print('url: {}'.format(urllib.parse.unquote(requestURL)))
                logging.basicConfig(filename='./log/interdaySummaries{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%dT%H_%M_%S')), level=logging.DEBUG)
                logging.debug(urllib.parse.unquote(requestURL))
        else:
            print("Please Check column's name of {}.csv !".format(testSuite))
            
        

runTest()