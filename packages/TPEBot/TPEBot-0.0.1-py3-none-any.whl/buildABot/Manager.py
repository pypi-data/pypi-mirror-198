import pandas as pd
import os

from buildABot.Database import Database
from buildABot.Entities import Entities
from buildABot.HotTopics import HotTopics
from buildABot.Intents import Intents
from buildABot.WebApp import WebApp
from buildABot.Webhook import Webhook
from buildABot.Menu import Menu
from buildABot.Paraphraser import Paraphraser

directory = os.getcwd()
parent = os.path.dirname(directory).replace('\\','/')

class Manager(Intents, Database, Entities, HotTopics, WebApp, Webhook, Menu, Paraphraser):

    def __init__(self, qaFile, slFile, studentFile, keyFile):
        self.qaFile = qaFile
        self.slFile = slFile
        self.studentFile = studentFile
        self.keyFile = keyFile

    def getData(file):
        """
        Read QAfile and clean the file before using
        :param file: QA_data.xlsx, SL Inputs.xlsx
        :return: [Dataframe] Cleaned file as dataframe
        """
        # Get QAfile and read as dataframe
        df = pd.read_excel(file, dtype=str)
        df.fillna(value='', inplace=True)
        return df
    
    def createParaphrases(self):
        Paraphraser.random_state(1234)
        qaData = Manager.getData(self.qaFile)
        df, df_qn, dfString = Paraphraser.extractData(df=qaData)
        numTrainPara, paraphrases = Paraphraser.paraphrase(dfString=dfString)
        Paraphraser.createNewQAFile(numTrainPara=numTrainPara, paraphrases=paraphrases, df=df, df_qn=df_qn)
        
        return print("Paraphrased QA Data Succcessfully Created!\n")
    
    def createIntents(self):
        """
        Executing the different functions to obtain JSON files of all intents
        :return: Display message after successful excution
        """
        data = Manager.getData("./Tutor/QA_Data.xlsx")
        data_with_labels = Intents.getLabels(df=data)
        data_with_labels.to_excel('./Tutor/QA_Paraphrased.xlsx', index=False)  # Update
        result = Intents.getIntents(df=data_with_labels)

        return result

    def createHotTopics(self):
        """
        Executing the different functions to obtain JSON files of hot topics intents
        :param SLfile: SL inputs.xslx
        :return: Display message after creating hot topics successfully
        """
        data = Manager.getData(self.slFile)
        hotTopics = HotTopics.createHotTopicsIntents(data)

        return hotTopics

    def createEntities(self):
        studentData = Manager.getData(file=self.studentFile)
        slData = Manager.getData(file=self.slFile)

        cleanedStudentData = Entities.cleanStudentID(studentData)
        studentEntity = Entities.createEntity(cleanedStudentData)
        dummyEntity = Entities.createEntity(slData)

        return print(dummyEntity)

    def createFulfillment(self):
        slData = Manager.getData(file=self.slFile)
        accKeyFile, tempFile = Webhook.readFiles(keyFile=self.keyFile)
        template, tempFile = Webhook.getInfo(slData=slData, accKeyFile=accKeyFile, tempFile=tempFile)
        fulfillment = Webhook.createFulfillment(template=template, tempFile=tempFile)

        return print(fulfillment)
    
    def createFirebase(self):
        studentData = Manager.getData(file=self.studentFile)
        slData = Manager.getData(file=self.slFile)

        data, slLogins = Database.getID(data=studentData, slData=slData)
        strings = Database.dataEncryption(data=data, slLogins=slLogins)
        names = Database.sanitiseName(data=studentData)
        firebaseDB = Database.createDBData(strings=strings, names=names)

        return print(firebaseDB)

    def createWebApp(self):
        df = Manager.getData(file=self.slFile)
        data, tempFile = WebApp.readFiles()
        template = WebApp.getInfo(df=df, data=data)
        webApp = WebApp.createHTML(data=data, tempFile=tempFile)

        return print(webApp)

    def createMenu(self):
        df = Manager.getData("./Tutor/QA_Paraphrased.xlsx")
        Menu.createLearnMenu(df=df)
        Menu.createMainTopicMenu3(df=df)
        Menu.createMainTopicMenu2(df=df)

        return print("Learn Menu Successfully Created!\n")