import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup
import json

sixDays = ["月", "火", "水", "木", "金", "土"]
jigen = ["1~2限", "3~4限", "5~6限", "7~8限", "9~10限", "11~12限", "13~14限", "15~16限"]

def indexToDay(index):
    return sixDays[index%6]

def indexToJigen(index):
    return jigen[int(index/6)]

def loadPrivateData():
    with open("privateData.json", "r") as f:
        import pdb; pdb.set_trace()
        JSON = json.load(f)
        userId = JSON["userId"]
        password = JSON["password"]

        return userId, password

def getTimeTable():

    options = webdriver.chrome.options.Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    # ブラウザ起動
    driver = webdriver.Chrome(chrome_options=options, service_log_path="./chromedriver.log")
    driver.implicitly_wait(1)

    # ログイン
    userId, password = loadPrivateData()
    driver.get("https://tora-net.sti.chubu.ac.jp/portal/top.do")
    driver.find_element_by_id("userId").send_keys("tp00000")
    driver.find_element_by_id("password").send_keys("xxxxxxxx")
    driver.find_element_by_xpath("//*[@id='loginButton']").click()

    # 時間割ページへ直接移動
    driver.get("https://tora-net.sti.chubu.ac.jp/portal/prtlmjkr.do?clearAccessData=true&amp;contenam=prtlmjkr&amp;kjnmnNo=18&#10;")
    try:
        driver.find_element_by_xpath('//*[@id="nav"]/li[4]/a').is_displayed()
    except:
        dict401 = {"status" : 401}

        driver.quit()
        JSON = json.dumps([dict401, {"response" : []}], ensure_ascii=False, indent=2)
        return JSON

    # htmlを取得
    soup = BeautifulSoup(driver.page_source, "lxml")



    if len(soup.find_all(class_="jikanwariKoma")) == 0:
        dict404 = {"status" : 404}

        driver.quit()
        JSON = json.dumps([dict404, {"response" : []}], ensure_ascii=False, indent=2)
        return JSON

    # ここまで来ればちゃんと認証通ってる
    timeTable = []
    dict200 = {"status" : 200}
    timeTable.append(dict200)
    response = []

    # 各コマに対してaタグがあるか精査、あったらtimeTableに各情報を追加
    for index, koma in enumerate(soup.find_all(class_="jikanwariKoma")):
        if len(koma.find_all("a")) != 0: # aタグがあったら(講義リンクがあったら)
            komaTitle, komaRoom, komaTeature, _ = koma.text.replace("\n\n\n", "").split("\n")
            komaRoom = komaRoom.strip()
            komaTeature = komaTeature.strip()
            komaTeature = komaTeature.replace("\u3000", " ")
            dict = {
                "day" : indexToDay(index),
                "jigen" : indexToJigen(index),
                "komaTitle" : komaTitle,
                "komaRoom" : komaRoom,
                "komaTeature" : komaTeature
            }
            response.append(dict)

    driver.quit()
    timeTable.append({"response" : response})

    return json.dumps(timeTable, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print(getTimeTable())
