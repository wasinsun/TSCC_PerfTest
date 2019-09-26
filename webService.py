from config import Config
import json
from Interday_Summaries import InterdaySummariesModel

def runTest():
    config = Config()
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
    testSuite = "TestSuite_1"
    roundOfTest = config.getRoundOfTest(testSuite)
    endPointData = config.getEndPointsData('INTRA_VIP_POD_INT')
    headerData = config.getHeaderData(testSuite)
    testDataFile = config.getTestDataFile(testSuite, 'InterdaySummariesTestCase')
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

        print('url: {}'.format(requestURL))

runTest()