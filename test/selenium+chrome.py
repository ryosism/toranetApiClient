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


options = webdriver.chrome.options.Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

# ブラウザ起動
driver = webdriver.Chrome(chrome_options=options, service_log_path="./chromedriver.log")
driver.implicitly_wait(1)

print("ログイン中...")

# ログイン
driver.get("https://tora-net.sti.chubu.ac.jp/portal/top.do")
driver.find_element_by_id("userId").send_keys("tp00000")
driver.find_element_by_id("password").send_keys("xxxxxxxxx")
driver.find_element_by_xpath("//*[@id='loginButton']").click()

print("時間割情報を取得中...")

# 時間割ページへ直接移動
driver.get("https://tora-net.sti.chubu.ac.jp/portal/prtlmjkr.do?clearAccessData=true&amp;contenam=prtlmjkr&amp;kjnmnNo=18&#10;")
try:
    print(driver.find_element_by_xpath('//*[@id="nav"]/li[4]/a').is_displayed())
except:
    print("no such element")
    dict401 = {"status" : 401}

# htmlを取得
soup = BeautifulSoup(driver.page_source, "lxml")

# 各コマに対してaタグがあるか精査、あったらtimeTableに各情報を追加
timeTable = []
if len(soup.find_all(class_="jikanwariKoma")) == 0:
    print("ERROR!")

for index, koma in enumerate(soup.find_all(class_="jikanwariKoma")):
    if len(koma.find_all("a")) != 0: # aタグがあったら(講義リンクがあったら)
        komaTitle, komaRoom, komaTeature, _ = koma.text.replace("\n\n\n", "").split("\n")

        # komaTeature = komaTeature.replace(" ", "")
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

        timeTable.append(dict)

JSON = json.dumps(timeTable, ensure_ascii=False, indent=2)
print(JSON)

driver.quit()
