from bs4 import BeautifulSoup
from selenium import webdriver


import requests




option = webdriver.ChromeOptions()
# I recommend to use the headless option at least
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')

web_driver = webdriver.Chrome(options=option)
 
web_driver.get('https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html') # Getting page HTML through request
soup = BeautifulSoup(web_driver.page_source, 'html.parser') # Parsing content using beautifulsoup.
 
# @param selector: the selector of the html code you want to collect
# collects the html from the selector
def collectData(selector):
    data = soup.select(selector)
    return data

# @param data: the html code gotten from the selector
# removes the html tags from the code
def justText(data):
    newData = []
    for i in data:
        newData.append(i.text)
    return newData

# @param data: the collected data
# creates dictionary to hold province case data
def createDict(data):
    dictData = {}
    counter = 0
    for collectedText in data:
        trimmedText = collectedText
        if counter % 4 == 0:
            tempKey = trimmedText
        else:
            if tempKey in dictData.keys():
                
                dictData[tempKey].append(trimmedText)
            else:
                dictData[tempKey] = [trimmedText]
        counter += 1
    return dictData


def main():
    try:
        f = open("data.txt", "w")
        date = justText(collectData("#newCases > caption > span"))
        covidData = justText(collectData("#newCases > tbody > tr > td"))
        covidDataDict = createDict(covidData)
        # write the data
        f.write("Canadian COVID-19 case data.\n")
        f.write(str(date))
        f.write("\n")
        f.writelines(str(covidDataDict))
        f.close()
        return
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
    except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
    except KeyboardInterrupt:
        print("Someone closed the program")
    

main()

