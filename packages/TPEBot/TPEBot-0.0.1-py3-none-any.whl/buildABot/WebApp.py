import os
directory = os.getcwd()
parent = os.path.dirname(directory).replace('\\','/')

class WebApp:
    def __init__(self):
        import pandas as pd

    def readFiles():
        tempFile = open('./Chatbot/WebApp/public/index_template.html', "r")
        data = tempFile.read()
        return data, tempFile

    def getInfo(df, data):
        subject = df['Subject'][0]
        persona = df['Persona'][0]

        data = data.replace("SUBJECTNAME", subject)
        data = data.replace("BOTNAME", persona)

        return data

    def createHTML(data, tempFile):
        htmlFile = open('./Chatbot/WebApp/public/index.html', 'w')

        htmlFile.write(data)
        tempFile.close()
        htmlFile.close()

        return("WebApp HTML file Succesfully Created!\n")