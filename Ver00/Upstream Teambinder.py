from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time


##########################################################
### Change the information, replace the ID and Password  #
##########################################################
#UserID
UserID = "*****"

#CompanyID
CompanyID = "MTR"

#Password
Pass = "*****"

#########################################################
#########################################################
# Change the code at your own need(risk)
#########################################################
#########################################################

browser = webdriver.Firefox()
url = "https://www.tfnswteambinder.com/TeamBinder2202/Logon/default.aspx"

url2 = 'https://au2.doc.ineight.com/TeamBinder2206/Logon/default.aspx'
browser.get(url)
browser.implicitly_wait(0.5)

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

#################    Transmittal number Enter here              ############################

print("HELLO!! \n Please check the browser and close ALLLLL pop up notifications!!!!! \n The code would not work otherwise..")

give_me_a_number = input('Type the transmittals number, type end to end the program: ')
# testing TX number: SMCSWLWC-SYC-TX-008571
#Search
WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.ID,"btnSearch"))).click()

#select "All Project"
time.sleep(2)
WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.ID,'RadComboBoxProjects_Arrow'))).click()
WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[1]/div/div/ul/li[1]'))).click()

#All button
time.sleep(1)
All = browser.find_element(By.XPATH,"/html/body/form/div[5]/div/table/tbody/tr[4]/td/div/div/div/table/tbody/tr/td[4]/div/div[4]/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr[3]/td/div/table/tbody/tr[6]/td[3]/input[2]")
actions.move_to_element(All)
actions.perform()
time.sleep(1)
actions.click()
actions.perform()

# Transmittals checkbox
Trans = browser.find_element(By.ID,"chkDocTrn")
Trans.click()

#####          Start to search!!!          #########
SearchText = browser.find_element(By.ID, "txtSearchtext")


######################
while give_me_a_number != "end":


    # give_me_a_number = "SMCSWSWM-MTR-TX-000206"
    SearchText.clear()
    SearchText.send_keys(str(give_me_a_number))

    browser.find_element(By.ID, "cmdSearch").click()
    print('Searching results of: ', str(give_me_a_number))
    WebDriverWait(browser, 200).until(EC.visibility_of_element_located((By.ID,"ctl00_cntPhMain_GridViewResults_ctl00")))
    #browser.find_element(By.ID,"ctl00_cntPhMain_GridViewResults_ctl00")
    time.sleep(1)
    first_result = browser.find_element(By.ID,"ctl00_cntPhMain_GridViewResults_ctl00")

    time.sleep(5)
    print("found it or gave up...")
    actions.move_to_element(first_result)
    #actions.perform()
    time.sleep(0.5)
    actions.double_click()
    actions.perform()
    give_me_a_number = input('Type the transmittals number, type end to end the program: ')


print("program has ended. \n Don't forget to rate Doris 10/10 ")
