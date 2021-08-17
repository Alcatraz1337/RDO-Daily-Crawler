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
        f.write("\n赏金猎人\n")
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
            if i < 27:
                prevData += d
            elif i >= 27 and i < 30:
                easyChallenge += d
            elif i >= 30 and i < 33:
                normalChallenge += d
            elif i >= 33 and i < 36:
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
            if i < 44:
                prevData += d
            elif i >= 44 and i < 47:
                easyChallenge += d
            elif i >= 47 and i < 50:
                normalChallenge += d
            elif i >= 50 and i < 53:
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
            if i < 61:
                prevData += d
            elif i >= 61 and i < 64:
                easyChallenge += d
            elif i >= 64 and i < 67:
                normalChallenge += d
            elif i >= 67 and i < 70:
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
            if i < 78:
                prevData += d
            elif i >= 78 and i < 81:
                easyChallenge += d
            elif i >= 81 and i < 84:
                normalChallenge += d
            elif i >= 84 and i < 87:
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
    file = "D:\Documents\我的坚果云\RDO 每日挑战\Archive\daily"+date+".txt"
    url = GenerateURL(date)
    soup = ReadHTML(url)
    GetAllChallenges(soup, file)
    GetNazarLocation(soup, file)
    FormatFile(file)

if __name__ == "__main__":
    main()