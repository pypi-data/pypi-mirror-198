import os
import pandas as pd

directory = os.getcwd()
parent = os.path.dirname(directory).replace('\\','/')

class Webhook:
    def __init__(self):
        pass

    def readFiles(keyFile):
        '''
        Read csv and template files
        :param slFile
        :return:
        '''
        #slData = Manager.getData(file=slFile)
        accKeyFile = open(keyFile)
        tempFile = open("./Chatbot/Dialogflow Fulfillment/index_template.js", "r", encoding='utf8')

        return accKeyFile, tempFile

    def getInfo(slData, accKeyFile, tempFile):
        '''
        Get necessary data from csv files (service account key, firebase url, email)
        '''
        template = tempFile.read()
        accKey = accKeyFile.read()
        dbURL = slData['Firebase URL'][0]
        slEmail = slData['Email'][0]

        '''
        Replace keywords with extracted values
        '''
        template = template.replace("SERVICEACCOUNTKEYHERE", accKey)
        template = template.replace("DBURLHERE", dbURL)
        template = template.replace("TUTOREMAILHERE", slEmail)

        return template, tempFile

    def createFulfillment(template, tempFile):
        '''
        Write updated fulfillment code into destinated files and close files
        '''
        finalFile = open('./Chatbot/Dialogflow Fulfillment/index.js', 'w', encoding='utf8')
        tutorFile = open("./Tutor/For Deployment/index.js", 'w', encoding="utf-8")

        finalFile.write(template)
        tutorFile.write(template)

        tempFile.close()
        finalFile.close()
        tutorFile.close()

        return("Fulfillment Successfully Created!\n")
