import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#######################################################
#    (not so) STEP by STEP GUIDE
#######################################################
# STEP 1. Download and install python
# STEP 2. Download and install firefox (Yes, Doris wants firefox!!!!)
# STEP 3. Put the geckodriver.exe file on your environment PATH
# STEP 3.1 If you don't know what is PATH, then put the geckodriver.exe into C:\Windows\System32
# STEP 4. Install python package "Selenium". Minimise any window, Press down WIN+R to call up RUN Window.
# STEP 5. Enter "CMD" then type "python -m pip install selenium" to install selenium
# STEP 6. Try to get an IDE, for example, download Pycharm here: 
# https://www.jetbrains.com/pycharm/download/#section=windows
# STEP 7. Change the ID and Password below to your own, keep the "" marks.
# STEP 7.1 RUN this file in PyCharm. 
# STEP 8. If anything is not working, kindly ask the person who gave you this file to show you how it works.
#
#########################################################
# Change the ID and Password to log-on
#########################################################

#UserID
UserID = "*****"

#CompanyID
CompanyID = "MTR"

#Password
Pass = "*****"

##########################################################
# Modify the code at your own risk.....ahahahahhahahah ###
##########################################################

give_me_a_number = input('Type the transmittals number, type end to end the program: ')
browser = webdriver.Firefox()
url = "https://www.tfnswteambinder.com/TeamBinder2202/Logon/default.aspx"

url2 = 'https://au2.doc.ineight.com/TeamBinder2206/Logon/default.aspx'
browser.get(url2)
browser.implicitly_wait(0.5)
print(browser.title)


browser.find_element(by=By.NAME,value="txtUserId").send_keys(UserID)
browser.find_element(by=By.NAME,value="txtCompanyId").send_keys(CompanyID)
browser.find_element(by=By.NAME,value="txtPassword").send_keys(Pass)

browser.find_element(by=By.ID, value="lnkLogon").click()
browser.implicitly_wait(5)

original_window = browser.current_window_handle

for window_handle in browser.window_handles:
    if window_handle != original_window:
        browser.switch_to.window(window_handle)
        break

print(browser.current_url)

actions = ActionChains(browser)
'''
################           SMCSW3             ###################

actions = ActionChains(browser)
smcsw = browser.find_element(by=By.ID, value='GridViewProjList_ctl00')
#browser.find_element(by=By.CSS_SELECTOR,value="#GridViewProjList_ctl00__0")
#SMCSW1 = browser.find_element(by=By.CSS_SELECTOR,value="#GridViewProjList_ctl00__0")

actions = ActionChains(browser)
actions.move_to_element(smcsw)

actions.perform()
actions.click()
actions.perform()
'''

############################################
#Document
#WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.ID,"divDocuments"))).click()

#toDocument = browser.find_element(by=By.ID, value="divDocuments")
#toDocument.click()
#actions.move_to_element(toDocument)
#actions.perform()
#actions.click()
#actions.perform()

#Transmittal
#WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.ID,"divTransmittals"))).click()

#############################################
#Search
WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.ID,"btnSearch"))).click()

'''
#select "All Project"
time.sleep(3)
WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.ID,'RadComboBoxProjects_Arrow'))).click()
WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[1]/div/div/ul/li[1]'))).click()
'''


#All, Transmittals
time.sleep(1)
All = browser.find_element(By.XPATH,"/html/body/form/div[4]/div/table/tbody/tr[4]/td/div/div/div/table/tbody/tr/td[4]/div/div[4]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[3]/td/div/table/tbody/tr[6]/td[3]/input[2]")
actions.move_to_element(All)
actions.click()
actions.perform()


Trans = browser.find_element(By.ID,"chkDocTrn")
Trans.click()

####################################################
#####          Start to search!!!          #########
####################################################
SearchText = browser.find_element(By.ID, "txtSearchtext")


while str(give_me_a_number)!='end':
    SearchText.clear()
    SearchText.send_keys(str(give_me_a_number))

    browser.find_element(By.ID, "cmdSearch").click()
    print('Searching results of: ', str(give_me_a_number))

    WebDriverWait(browser, 200).until(EC.visibility_of_element_located((By.ID,"ctl00_cntPhMain_GridViewResults_ctl00")))
    #browser.find_element(By.ID,"ctl00_cntPhMain_GridViewResults_ctl00")
    first_result = browser.find_element(By.ID,"ctl00_cntPhMain_GridViewResults_ctl00")
    actions.move_to_element(first_result)
    #actions.perform()
    time.sleep(1.5)
    actions.double_click()
    actions.perform()


    print('You can now enter another transmittal number')
    give_me_a_number = input('(type "end" to exit) Transmittal number: ')

print('Well done! Now it is time to buy Doris a coffee')

######################
# 
#
#
#
#
