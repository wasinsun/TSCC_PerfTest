import json
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    def __init__(self):
        self.fileConfig = os.path.join(ROOT_DIR,"Config.json")
        self.config = self.loadFileConfig(self.fileConfig)

    def loadFileConfig(self,file):
        return json.loads(open(file).read())

    def getEndPointsData(self,EndPoint):
        return self.config['EndPoints'][EndPoint]

    def getEndPointsUsername(self,EndPoint):
        return self.config['EndPoints'][EndPoint]['User']

    def getEndPointsPassword(self, EndPoint):
        return self.config['EndPoints'][EndPoint]['Password']

    def getEndPointsHostname(self,EndPoint):
        return self.config['EndPoints'][EndPoint]['Hostname']
    
    def getEndPointsBC_Path(self,EndPoint):
        return self.config['EndPoints'][EndPoint]['Path_BC']

    def getHeaderData(self, TestSuite):
        return self.config['TestSuites'][TestSuite]['Header']

    def getTestSuites(self):
        return self.config['TestSuites']

    def getTestCasesEndPoint(self,TestSuite):
        return self.config['TestSuites'][TestSuite]['EndPoint']

    def getTestCasesEndPointURL(self,TestSuite):
        endPointTestCase = self.getTestCasesEndPoint(TestSuite)
        return self.getEndPointsHostname(endPointTestCase)

    def getRoundOfTest(self, TestSuite):
        return self.config['TestSuites'][TestSuite]['RoundOfTest']

    def getTestDataFile(self, TestSuite, TestCase):
        return os.path.abspath(self.config['TestSuites'][TestSuite]['TestDataFile'][TestCase])