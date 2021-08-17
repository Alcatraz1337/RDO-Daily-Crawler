import requests
from bs4 import BeautifulSoup
import re

def GenerateURL(date):
    url = "https://rdodailies.com/?date="+date+"&lang=zh"
    return url

def ReadHTML(url):
    print("Requesting...")
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def GetAllChallenges(soup, file):
    print("Getting all challenges...")
    allChallenges = soup.find_all('span', class_='challenge-input-container-label')
    allChallengeGoals = soup.find_all('span', class_='challenge-goal')

    with open(file, "w", encoding="utf-8") as f:
        for i in range(len(allChallenges)):
            if len(re.split(r'[\n]', allChallenges[i].label.get_text())) > 1:
                txtToWrite = str(re.split(r'[\n]', allChallenges[i].label.get_text())[1]+'：'+re.split(r'[\n]',allChallengeGoals[i].get_text())[1]+'\n')
                f.write(txtToWrite)
            else:
                txtToWrite = str(re.split(r'[\n]', allChallenges[i].label.get_text())[0]+'：'+re.split(r'[\n]',allChallengeGoals[i].get_text())[1]+'\n')
                f.write(txtToWrite)

    print("Done!")

def FormatFile(date, file):
    print("Formating...")

    # 常规
    with open(file, "r+", encoding="utf-8") as f:
        tmpData = f.read()
        f.seek(0)
        f.write("\n常规\n" + tmpData)
        print("Format complete!")

def main():
    date = input("Enter date (YYYY-MM-DD): ")
    file = "D:\Documents\我的坚果云\RDO 每日挑战\Archive\daily"+date+".txt"
    url = GenerateURL(date)
    soup = ReadHTML(url)
    GetAllChallenges(soup, file)
    FormatFile(date, file)

if __name__ == "__main__":
    main()