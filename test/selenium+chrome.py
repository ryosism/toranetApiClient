import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from selenium import webdriver

options = webdriver.chrome.options.Options()
options.add_argument("--headless")  # これ消せばブラウザ画面が出ます
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://sukumizu.moe")

# タイトル
print(driver.title)

import pdb; pdb.set_trace()
