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

    def getInterfaces(self):
        return self.config['Interfaces']

    def getTestSuites(self, Interface):
        return self.config['Interfaces'][Interface]['TestSuites']

    def getTestSuiteEndPoint(self, Interface, TestSuite):
        return self.config['Interfaces'][Interface]['TestSuites'][TestSuite]['EndPoint']

    def getTestSuiteEndPointURL(self, Interface, TestSuite):
        endPoint = self.getTestSuiteEndPoint(Interface, TestSuite)
        return self.getEndPointsHostname(endPoint)

    def getRoundOfTest(self, Interface, TestSuite):
        return self.config['Interfaces'][Interface]['TestSuites'][TestSuite]['RoundOfTest']

    def getTestDataFile(self, Interface, TestSuite):
        return os.path.abspath(self.config['Interfaces'][Interface]['TestSuites'][TestSuite]['DataFile'])

    def getRequestParams(self, Interface):
        return self.config['Interfaces'][Interface]['RequestParams']
