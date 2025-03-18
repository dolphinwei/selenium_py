from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 用来购买12306的python自动化脚本，不支持选座
# 需要安装selenium库
# 需要安装对应浏览器的驱动，这里用的是Edge浏览器


# 填写12306的用户名，密码，和身份证后4位
username = ''
password = ''
id_4 = ''

driver = webdriver.Edge()

# 访问12306网站
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc/")

# 登录
def login():
    # 输入用户名密码
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'J-userName'))
    ).send_keys(username)
    driver.find_element(By.ID, 'J-password').send_keys(password)
    driver.find_element(By.ID, 'J-login').click()

    time.sleep(2)

    # 身份证后4位
    driver.find_element("id", "id_card").send_keys(id_4)

    # 验证码
    vf_code_btn = driver.find_element("id", "verification_code")
    vf_code_btn.click()

    # 输入验证码后点击确定
    input("请手动完成验证后按回车继续...")


# 设置起始站
from_input_box = driver.find_element("id", "fromStationText")
from_input_box.click()
from_input_box.send_keys("南宁")
from_city = driver.find_element(By.XPATH, './/span[@class="ralign" and contains(text(), "南宁东")]')
from_city.click()

# 设置终点站
to_input_box = driver.find_element("id", "toStationText")
to_input_box.click()
to_input_box.send_keys("广州南")
to_city = driver.find_element(By.XPATH, './/span[@class="ralign" and contains(text(), "广州南")]')
to_city.click()

# 设置出发时间
train_date = driver.find_element("id", "train_date")
train_date.clear()
train_date.click()
train_date.send_keys("2025-03-28")

# 点击查询
query_ticket_btn = driver.find_element("id", "query_ticket")
query_ticket_btn.click()

time.sleep(2)

# 余票监控与选择
while True:
    query_ticket_btn.click()
    try:
        ticket = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//tr[td[1]/div/div[1]/div/a[contains(text(),'D3629')]]/td[13]/a"))
        )
        ticket.click()
        break
    except:
        driver.refresh()

# 身份验证与订单提交（需人工介入验证码）
# 登录
login()

time.sleep(2)

# 选择乘车人，选择乘车列表的第一个
passenger = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//ul/li[1]/input"))
        )
passenger.click()

# 提交订单
sumit_btn = driver.find_element("id", "submitOrder_id")
sumit_btn.click()

time.sleep(2)

# 选位置 D座，还不支持，被12306反制了
# seat_btn = driver.find_element("id", "1D")
# # seat_btn.click()
# ActionChains(driver) \
#         .click(seat_btn) \
#         .perform()


# 确认提交
qr_submit_btn = driver.find_element("id", "qr_submit_id")
qr_submit_btn.click()




