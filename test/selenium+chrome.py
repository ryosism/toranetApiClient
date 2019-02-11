import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from selenium import webdriver
import chromedriver_binary

options = webdriver.chrome.options.Options()
# options.add_argument("--headless")  # これ消せばブラウザ画面が出ます
options.add_argument("--no-sandbox")
options.add_argument("--always-authorize-plugins")
options.add_argument("--javascript-harmony")
options.add_argument("--user-agent='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Version/3.1 Safari/525.19'")


driver = webdriver.Chrome(chrome_options=options, service_log_path="./chromedriver.log")
driver.implicitly_wait(3)

driver.get("https://tora-net.sti.chubu.ac.jp/portal/top.do")

# タイトル
print(driver.title)
print(driver.page_source)
