#Christopher Greer
#Covid Notifier
#26/6/20


from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
import lxml
import pandas as pd

def notify_user(title, message):
    notification.notify(
    title = title,
    message = message,
    app_icon = "./Covid-19_Real-time_Notification/Notify_icon.ico" ,
    timeout = 5)
    
def getInfo(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
        #t = int(input("Enter interval in secs: "))
        country = input("Enter name of country/countries: ")
        #li = list(map(str, input("Enter name of country/countries: ").split(",")))
        countries = []
        pageData = getInfo('https://www.worldometers.info/coronavirus/')
        soup = BeautifulSoup(pageData, 'lxml')
        
        #Get information from webpage were table tag is used
        countriesTable = soup.find("table", id="main_table_countries_today")
        
        #Get title of every columns using th tag
        headers = []
        for i in countriesTable.find_all("th"):
            title = i.text
            #title = title.split("\n\n")
            headers.append(title)
            
        #Create Dataframe
        mydata = pd.DataFrame(columns = headers)
        
        while True:
            soup = BeautifulSoup(pageData, 'lxml')
            
            #Get information from webpage were table tag is used
            update = soup.find("table", id="main_table_countries_today")
        
            #Loop to fill data frame
            for j in update.find_all("tr")[1:]:
                data = j.find_all("td")
                row = [i.text for i in data]
                length = len(mydata)
                mydata.loc[length] = row
            
            #Loop to find country
            for row in mydata["Country,Other"]:
                print(mydata["Country,Other"[row]])
                #if country==i["Country,Other"]:
                 #   print(country,": Total Cases:", mydata["TotalCases"[i]],", New Cases:", mydata["NewCases"[i]])

                    
            #time.sleep(t)
            time.sleep(2)
            
            