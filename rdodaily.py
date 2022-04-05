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
        f.write("\n最近传送点：\n#荒野大镖客：救赎2# #荒野大镖客线上#")

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

def Insert(str, txt, idx):
    #找到匹配的任务于txt[idx]，拷贝之后的任务
    after = txt[idx+1:] 
    txt[idx+1] = str #插入攻略
    txt[idx + 2:] = after #将之后的任务添加回去
    return idx + 2, txt


def ReFill(file): # Auto fill some challenges here, using re
    print("Auto filling...")
    with open(file,"r+", encoding="utf-8") as f:
        text = f.readlines()
        i = 0
        while i < len(text):
            #常规任务
            if text[i].find("决战")>=0 or text[i].find("系列赛")>=0 or text[i].find("竞速系列赛")>=0:
                i, text = Insert("在线菜单（L）-快速加入-满足要求的系列赛，中途加入不算\n", text, i)
            elif text[i].find("待命状态")>=0:
                i, text = Insert("在线菜单（L）-快速加入-待命故事任务\b", text, i)
            elif text[i].find("火车")>=0:
                i, text = Insert("麦克法兰牧场常刷火车\n", text, i)
            elif text[i].find("烟")>=0:
                i, text = Insert("吸烟有害健康！\n", text, i)
            elif text[i].find("乘坐马车旅行")>=0:
                i, text = Insert("赏金马车，狩猎马车和私酒马车都算\n", text, i)
            elif text[i].find("调味")>=0:
                i, text = Insert("和野薄荷、牛至、百里香一起烹饪\n", text, i)
            elif text[i].find("抓倒在地")>=0:
                i, text = Insert("冲刺后扑倒敌对NPC\n", text, i)
            elif text[i].find("自定义的武器")>=0:
                i, text = Insert("在武器店更新武器\n", text, i)
            elif text[i].find("出售的动物牙齿")>=0:
                i, text = Insert("猎杀鳄鱼、河狸等动物可以获得\n", text, i)
            elif text[i].find("匕首")>=0:
                i, text = Insert("用绳索套住后捅死，或者麻醉后捅死（掉荣誉）\n", text, i)
            elif text[i].find("电报")>=0:
                i, text = Insert("背包（B）-文件-电报任务\n", text, i)
            elif text[i].find("牵马")>=0:
                i, text = Insert("在马附近，右键-牵引\n", text, i)
            elif text[i].find("已踩踏的")>=0:
                i, text = Insert("骑马踩过去\n", text, i)
            elif text[i].find("团队暗斗")>=0 or text[i].find("采药")>=0 or text[i].find("大鱼")>=0 or text[i].find("团队竞速")>=0 or text[i].find("猎鸟")>=0 or text[i].find("团队对抗")>=0 or text[i].find("斩首行动")>=0:
                i, text = Insert("在线菜单（L）-团队-团队对抗，需要固定团队才能开始\n", text, i)
            elif text[i].find("腰带扣")>=0:
                i, text = Insert("在衣柜处更新\n", text, i)
            elif text[i].find("服装风格")>=0:
                i, text = Insert("在衣柜里换衣服，或者直接在马背上更换套装即可\n", text, i)
            elif text[i].find("营地主题")>=0:
                i, text = Insert("在营地野外供应商处购买更换\n", text, i)
            elif text[i].find("高敌意等级")>=0:
                i, text = Insert("一个游戏日内不主动击杀其他玩家\n", text, i)
            elif text[i].find("面具")>=0:
                i, text = Insert("戴上面具，或者在衣柜给一个套装选中一个蒙面巾也行\n", text, i)
            elif text[i].find("出售的草药")>=0:
                i, text = Insert("在瓦伦丁、圣丹尼斯的药店出售\n", text, i)
            elif text[i].find("食用的草药")>=0:
                i, text = Insert("在背包（B）中原材料里找到草药食用，或者直接采摘食用\n", text, i)
            elif text[i].find("饮用的咖啡")>=0:
                i, text = Insert("在篝火处煮咖啡，或者在私酒酒吧喝\n", text, i)
            elif text[i].find("分解的小型动物")>=0:
                i, text = Insert("在背包（B）中分解\n", text, i)
            elif text[i].find("更新面部外观")>=0 or text[i].find("更新的发型")>=0:
                i, text = Insert("在黑水镇、瓦伦丁、圣丹尼斯的发廊更新\n", text, i)
            elif text[i].find("免费零食")>=0:
                i, text = Insert("在酒吧里找提供的小零食，或者在私酒棚屋酒吧找\n", text, i)
            elif text[i].find("喝醉")>=0:
                i, text = Insert("不断喝酒，直到画面开始扭曲为止\n", text, i)
            elif text[i].find("进行自拍")>=0 or text[i].find("马拍照")>=0:
                i, text = Insert("在物品栏中找到相机，按对应按键进行拍照\n", text, i)
            elif text[i].find("黑市出售")>=0:
                i, text = Insert("在盗贼领地、翡翠车站、罗兹的黑市出售物品\n", text, i)
            elif text[i].find("加入的团队")>=0:
                i, text = Insert("加入一支固定队伍即可\n", text, i)
            elif text[i].find("掩护时杀死")>=0:
                i, text = Insert("在掩体后击杀敌人即可\n", text, i)
            elif text[i].find("取得资本券")>=0:
                i, text = Insert("通过游玩血染之财任务，搜刮可能获得\n", text, i)
            elif text[i].find("动物放上马背")>=0:
                i, text = Insert("同一只动物不算\n", text, i)
            elif text[i].find("更新马具")>=0:
                i, text = Insert("在马厩更新一个马具\n", text, i)
            elif text[i].find("杀死的狼")>=0:
                i, text = Insert("找不到狼可以通过完成：传说悬赏-狼人 来完成\n", text, i)

            #赏金猎人
            elif text[i].find("马背上")>=0:
                i, text = Insert("骑马时，在马背上套住目标\n", text, i)
            elif text[i].find("困兽")>=0:
                i, text = Insert("使用困兽索套住目标\n", text, i)
            elif text[i].find("新奥斯汀")>=0:
                i, text = Insert("在风滚草镇、本尼迪克特车站、犰狳镇接受任务\n", text, i)
            elif text[i].find("西伊丽莎白")>=0:
                i, text = Insert("在华莱士车站、草莓镇、里格斯车站、黑水镇接受任务\n", text, i)
            elif text[i].find("新汉诺威")>=0:
                i, text = Insert("在瓦伦丁、翡翠车站、范霍恩、安尼斯堡接受任务\n", text , i)
            elif text[i].find("莱莫恩")>=0:
                i, text = Insert("在罗兹、圣丹尼斯接受任务\n", text, i)
            elif text[i].find("拍到活捉")>=0:
                i, text = Insert("用绳索套住后，用相机拍摄\n", text, i)
            elif text[i].find("加强型")>=0:
                i, text = Insert("需要在职业用品中购买加强型绳索后，在马背上选中使用\n", text, i)

            #商贩
            elif text[i].find("小型动物")>=0:
                i, text = Insert("参考：兔子、鼠、青蛙\n", text, i)
            elif text[i].find("中型动物")>=0:
                i, text = Insert("参考：郊狼、狐狸\n", text, i)
            elif text[i].find("大型动物")>=0:
                i, text = Insert("参考：鹿、羊、狼、狮\n", text, i)
            elif text[i].find("食肉动物")>=0:
                i, text = Insert("参考：狼、狮、鳄鱼、灰熊\n", text, i)
            elif text[i].find("完美尸体")>=0:
                i, text = Insert("干净猎杀即可，无需三星\n", text, i)
            elif text[i].find("特制营地炖汤")>=0:
                i, text = Insert("更换战局可以刷新配方\n", text, i)

            #收藏家
            elif text[i].find("饮用的古董酒")>=0:
                i, text = Insert("背包（B）-收藏品-古董酒饮用\n", text, i)
            
            #私酒贩
            elif text[i].find("普通或以上")>=0:
                i, text = Insert("1星配方以上，生产完成后结算\n", text, i)
            elif text[i].find("改良或以上")>=0:
                i, text = Insert("2星配方以上，生产完成后结算\n", text, i)
            elif text[i].find("特殊私酒配方")>=0:
                i, text = Insert("3星配方，生产完成后结算\n", text, i)
            elif text[i].find("剧毒私酒")>=0:
                i, text = Insert("购买手册学习后，在篝火处制作\n", text, i)
            elif text[i].find("变更装饰")>=0:
                i, text = Insert("在玛姬处变更\n", text, i)
            elif text[i].find("走私者")>=0:
                i, text = Insert("在玛姬处接受，以及自由模式下刷新的动态任务也算\n", text, i)
            elif text[i].find("私酒故事任务")>=0:
                i, text = Insert("在玛姬处重新接受任务\n", text, i)
            elif text[i].find("醉酒玩家互动")>=0:
                i, text = Insert("提示：按E进入棚屋之后瞬间，连续快速按F可以完成，无需别的玩家\n", text, i)
            else:
                i += 1
               
        result = "".join(text)
        f.seek(0)
        f.write(result)
        print("Auto fill complete!")

def main():
    date = input("Enter date (YYYY-MM-DD): ")
    if not os.path.exists("Archive"):
        os.mkdir("Archive")
    dateOfFile = "/Archive/daily-"+date+".txt"
    file = os.path.dirname(os.path.abspath(__file__)) + dateOfFile
    print("Saving file to: " + file)
    url = GenerateURL(date)
    soup = ReadHTML(url)
    GetAllChallenges(soup, file)
    GetNazarLocation(soup, file)
    FormatFile(file)
    ReFill(file)
    print("已完成，将在3秒后退出！")
    time.sleep(3)

if __name__ == "__main__":
    main()