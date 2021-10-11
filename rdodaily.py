import requests
from bs4 import BeautifulSoup
import re
import time
import os

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

    if not os.path.exists("Archive"):
        os.mkdir("Archive")

    with open(file, "w+", encoding="utf-8") as f:
        for i in range(len(allChallenges)):
            if len(re.split(r'[\n]', allChallenges[i].label.get_text())) > 1:
                count = str(i + 1)
                txtToWrite = str(count+'. '+re.split(r'[\n]', allChallenges[i].label.get_text())[1]+'：'+re.split(r'[\n]',allChallengeGoals[i].get_text())[1]+'\n')
                f.write(txtToWrite)
            else:
                txtToWrite = str(re.split(r'[\n]', allChallenges[i].label.get_text())[0]+'：'+re.split(r'[\n]',allChallengeGoals[i].get_text())[1]+'\n')
                f.write(txtToWrite)

def GetNazarLocation(soup, file):
    nazar = soup.select("#nazar-location-container")[0].img.get('src')
    with open(file, "a", encoding="utf-8") as f:
        f.write('\n夫人位置\n')
        f.write(nazar)

    print("Done!")

def FormatFile(file):
    print("Formating...")

    # 常规
    with open(file, "r+", encoding="utf-8") as f:
        tmpData = f.read()
        f.seek(0)
        f.write("常规\n\n" + tmpData)

    # 赏金猎人
    with open(file, "r+", encoding="utf-8") as f:
        prevData = ""
        afterData = ""
        easyChallenge = ""
        normalChallenge = ""
        hardChallenge = ""
        for i, d in enumerate(f.readlines(), start = 1):
            if i < 10:
                prevData += d
            elif i >= 10 and i < 13:
                easyChallenge += d
            elif i >= 13 and i < 16:
                normalChallenge += d
            elif i >= 16 and i < 19:
                hardChallenge += d
            else:
                afterData += d
        
        
        f.seek(0)
        f.write(prevData)
        f.write("\n职业任务（不同等级任务不同，具体请按照自己当前等级参考\n赏金猎人\n")
        f.write("\n1-4级\n")
        f.write(easyChallenge)
        f.write("\n5-14级\n")
        f.write(normalChallenge)
        f.write("\n15级以上\n")
        f.write(hardChallenge)
        f.write(afterData)

    # 商贩
    with open(file, "r+", encoding="utf-8") as f:
        prevData = ""
        afterData = ""
        easyChallenge = ""
        normalChallenge = ""
        hardChallenge = ""
        for i, d in enumerate(f.readlines(), start = 1):
            if i < 28:
                prevData += d
            elif i >= 28 and i < 31:
                easyChallenge += d
            elif i >= 31 and i < 34:
                normalChallenge += d
            elif i >= 34 and i < 37:
                hardChallenge += d
            else:
                afterData += d
        
        
        f.seek(0)
        f.write(prevData)
        f.write("\n商贩\n")
        f.write("\n1-4级\n")
        f.write(easyChallenge)
        f.write("\n5-14级\n")
        f.write(normalChallenge)
        f.write("\n15级以上\n")
        f.write(hardChallenge)
        f.write(afterData)

    # 收藏家
    with open(file, "r+", encoding="utf-8") as f:
        prevData = ""
        afterData = ""
        easyChallenge = ""
        normalChallenge = ""
        hardChallenge = ""
        for i, d in enumerate(f.readlines(), start = 1):
            if i < 45:
                prevData += d
            elif i >= 45 and i < 48:
                easyChallenge += d
            elif i >= 48 and i < 51:
                normalChallenge += d
            elif i >= 53 and i < 54:
                hardChallenge += d
            else:
                afterData += d
        
        
        f.seek(0)
        f.write(prevData)
        f.write("\n收藏家\n")
        f.write("\n1-4级\n")
        f.write(easyChallenge)
        f.write("\n5-14级\n")
        f.write(normalChallenge)
        f.write("\n15级以上\n")
        f.write(hardChallenge)
        f.write(afterData)

    # 私酒贩
    with open(file, "r+", encoding="utf-8") as f:
        prevData = ""
        afterData = ""
        easyChallenge = ""
        normalChallenge = ""
        hardChallenge = ""
        for i, d in enumerate(f.readlines(), start = 1):
            if i < 62:
                prevData += d
            elif i >= 62 and i < 65:
                easyChallenge += d
            elif i >= 65 and i < 68:
                normalChallenge += d
            elif i >= 68 and i < 71:
                hardChallenge += d
            else:
                afterData += d
        
        
        f.seek(0)
        f.write(prevData)
        f.write("\n私酒贩\n")
        f.write("\n1-4级\n")
        f.write(easyChallenge)
        f.write("\n5-14级\n")
        f.write(normalChallenge)
        f.write("\n15级以上\n")
        f.write(hardChallenge)
        f.write(afterData)

    # 博物学家
    with open(file, "r+", encoding="utf-8") as f:
        prevData = ""
        afterData = ""
        easyChallenge = ""
        normalChallenge = ""
        hardChallenge = ""
        for i, d in enumerate(f.readlines(), start = 1):
            if i < 79:
                prevData += d
            elif i >= 79 and i < 82:
                easyChallenge += d
            elif i >= 82 and i < 85:
                normalChallenge += d
            elif i >= 85 and i < 88:
                hardChallenge += d
            else:
                afterData += d
        
        
        f.seek(0)
        f.write(prevData)
        f.write("\n博物学家\n")
        f.write("\n1-4级\n")
        f.write(easyChallenge)
        f.write("\n5-14级\n")
        f.write(normalChallenge)
        f.write("\n15级以上\n")
        f.write(hardChallenge)
        f.write(afterData)

    print("Format complete!")

def main():
    date = input("Enter date (YYYY-MM-DD): ")
    dateOfFile = "\Archive\daily"+date+".txt"
    file = os.path.join(os.path.dirname(__file__) + dateOfFile)
    url = GenerateURL(date)
    soup = ReadHTML(url)
    GetAllChallenges(soup, file)
    GetNazarLocation(soup, file)
    FormatFile(file)
    print("已完成，将在3秒后退出！")
    time.sleep(3)

if __name__ == "__main__":
    main()