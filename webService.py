from config import Config
import json
import csv
import logging
import datetime
import urllib.parse
import requests
import time 
import pprint
import uuid
import pandas
import os

from Summaries import SummariesModel, InterdaySummariesModel

def runTest():
    config = Config()
    interdaySummaries(config)
    summaries(config)

def sendRequest(interface, config, requestURL, businessID, guid, permission):
    headers = {'Accept-Encoding': 'gzip, deflate',
               'Content-Type': 'application/json',
               'E2EBusinessProcessID': businessID,
               'E2ETraceBC': 'True',
               'E2ETraceRequestID': guid,
               'x-ts-applicationID': 'SingleResponseTime',
               'x-ts-uuid': permission,
               'x-ts-requestID': guid,
               'x-ts-productID': 'SingleResponseTime'
               }

    start_time = time.time() * 1000
    response = requests.get(requestURL, headers=headers)
    end_time = time.time() * 1000  # millisec
    content = response.json()

    diffTime = round(((end_time - start_time) / 1000), 3)
    count = None
    if interface == 'Interday_Summaries':
        Source = response.headers['Source']
    else:
        Source = None
    
    try:
        for TS in content['timeseriesData']:
            count=len(TS['dataPoints'])
        print('Data point is ' + str(count))
        return diffTime, count, int(start_time), int(end_time), Source
    except:
        try:
            for TS in content:
                count=len(TS['data'])
            print('Historical Data point is ' + str(count))
            return diffTime, count, int(start_time), int(end_time), Source
        except KeyError as e:
            pprint.pprint(content)
            return 'KeyError',str(e),int(start_time), ''
        except TypeError as e:
            pprint.pprint(content)
            return 'TypeError', str(e), int(start_time), ''
        except Exception as e:
            return 'OtherException', str(e), int(start_time), ''

        pass
      
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
    rounds = 1
    permission = 'PATSFCP-REALTIME'
    testSuites = config.getTestSuites(interface)
    for e in testSuites:
        testSuite = e
        roundOfTest = config.getRoundOfTest(interface, testSuite)
        testSuiteEndPoint= config.getTestSuiteEndPoint(interface, testSuite)
        endPointData = config.getEndPointsData(testSuiteEndPoint)
        testDataFile = config.getTestDataFile(interface, testSuite)
        testSuiteColumnName = getColumnName(testDataFile)
        configRequestParams = config.getRequestParams(interface)
        result = []
        if testSuiteColumnName == configRequestParams:
            while(rounds <= roundOfTest):
                print('rounds: {}'.format(rounds))
                csvData = loadTestData(testDataFile)
                for e in csvData:
                    data = e.split(',')
                    businessID = data[0]
                    ric = data[1]
                    interval = data[2]
                    start = data[3]
                    end = data[4]
                    adjustments = data[5].replace('|',',')
                    fields = data[6].replace('|',',')
                    count = data[7]
                    guid = str(uuid.uuid1()).upper()
                    interdaySummariesModel = InterdaySummariesModel()
                    interdaySummariesModel.setRic(ric)
                    interdaySummariesModel.setInterval(interval)
                    interdaySummariesModel.setDateByStartEnd(start, end)
                    interdaySummariesModel.setAdjustments(adjustments)
                    interdaySummariesModel.setCount(count)
                    interdaySummariesModel.setFields(fields)
                    requestURL = interdaySummariesModel.getURL()
                    requestURLStr = urllib.parse.unquote(requestURL)
                    
                    ####Response####
                    time, count, start_time, end_time, Source = sendRequest(interface, config, requestURL, businessID, guid, permission)
                    line = [rounds, data[0], guid, str(time), str(count), str(start_time), str(end_time), Source, requestURLStr]
                    result.append(line)
                    columnName = ["Rounds","TestCaseName", "RequestID","TestResponseTime(sec)","Count","TestStartTime(ms)","TestEndTime(ms)", "Source", "RequestURL"]
                                      
                rounds += 1

            result_df = pandas.DataFrame(result, columns=columnName)
            logPath = './log/InterdaySummaries'
            if not os.path.exists(logPath):
                os.makedirs(logPath)
            result_df.to_csv(os.path.join(logPath, testSuite + '_' + datetime.datetime.now().strftime('%Y-%m-%dT%H_%M_%S') + '.csv'),index=False)  

        else:
            print("Please Check column's name of {}.csv !".format(testSuite))

def summaries(config):
    interface = "Summaries"
    rounds = 1
    permission = 'PATSFCP-REALTIME'
    testSuites = config.getTestSuites(interface)
    for e in testSuites:
        testSuite = e
        roundOfTest = config.getRoundOfTest(interface, testSuite)
        testSuiteEndPoint= config.getTestSuiteEndPoint(interface, testSuite)
        endPointData = config.getEndPointsData(testSuiteEndPoint)
        testDataFile = config.getTestDataFile(interface, testSuite)
        testSuiteColumnName = getColumnName(testDataFile)
        configRequestParams = config.getRequestParams(interface)
        result = []
        if testSuiteColumnName == configRequestParams:
            while(rounds <= roundOfTest):
                print('rounds: {}'.format(rounds))
                csvData = loadTestData(testDataFile)
                for e in csvData:
                    data = e.split(',')
                    businessID = data[0]
                    ric = data[1]
                    interval = data[2]
                    start = data[3]
                    end = data[4]
                    adjustments = data[5].replace('|',',')
                    fields = data[6].replace('|',',')
                    count = data[7]
                    guid = str(uuid.uuid1()).upper()
                    summariesModel = SummariesModel()
                    summariesModel.setRic(ric)
                    summariesModel.setInterval(interval)
                    summariesModel.setDateByStartEnd(start, end)
                    summariesModel.setAdjustments(adjustments)
                    summariesModel.setCount(count)
                    summariesModel.setFields(fields)
                    requestURL = summariesModel.getURL()
                    requestURLStr = urllib.parse.unquote(requestURL)
                    
                    ####Response####
                    time, count, start_time, end_time, Source = sendRequest(interface, config, requestURL, businessID, guid, permission)
                    line = [rounds, data[0], guid, str(time), str(count), str(start_time), str(end_time), requestURLStr]
                    result.append(line)
                    columnName = ["Rounds","TestCaseName", "RequestID","TestResponseTime(sec)","Count","TestStartTime(ms)","TestEndTime(ms)", "RequestURL"]
                                        
                rounds += 1

            result_df = pandas.DataFrame(result, columns=columnName)
            logPath = './log/Summaries'
            if not os.path.exists(logPath):
                os.makedirs(logPath)
            result_df.to_csv(os.path.join(logPath, testSuite + '_' + datetime.datetime.now().strftime('%Y-%m-%dT%H_%M_%S') + '.csv'),index=False)  

        else:
            print("Please Check column's name of {}.csv !".format(testSuite))
            
        
runTest()