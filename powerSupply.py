from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import JavascriptException

def getStatus():
    s=Service('./chromedriver')
    options = Options()
    options.headless = True
    options.page_load_strategy = 'normal'

    # Get power status
    driver = webdriver.Chrome(service=s, options=options)
    url='http://169.254.95.52/web.exe?file=N57xxFrontPanel.html'
    driver.get(url)

    button = driver.find_element(By.XPATH, '//img[@alt="On Off Button"]')
    #By.CSS, img[@alt='On Off Button']
    usemap = button.get_attribute('usemap')

    if(usemap == "#turnon1"):
        power = "Off"
    elif (usemap == "#turnoff1"):
        power = "On"
    else:
        power = "Unknown"

    driver.quit()

    # Get Voltage and Current Settings
    driver = webdriver.Chrome(service=s, options=options)
    url='http://169.254.95.52/web.exe?file=N57xxmodifySettings.html'
    driver.get(url)

    voltage = driver.find_element(By.NAME, "voltage").get_attribute('value')
    current = driver.find_element(By.NAME, "current").get_attribute('value')
    
    retString = "\nPower Status: " + power + "\nVoltage: " + voltage + "\nCurrent: " + current

    return retString


def setPower(status):
    s=Service('./chromedriver')
    options = Options()
    options.headless = True
    options.page_load_strategy = 'normal'

    driver = webdriver.Chrome(service=s, options=options)
    url='http://169.254.95.52/web.exe?file=N57xxFrontPanel.html'
    driver.get(url)

    if(status == 0):
        powerStatus = "turnoff1"
    else:
        powerStatus = "turnon1"
    
    mapElement = driver.find_element(By.NAME, powerStatus)
    area = mapElement.find_element(By.XPATH, "./area")

    try:
        area.click()
    except JavascriptException:
        driver.quit()
        
    driver.quit()

def setOutput(v=-1, c=-1):
    s=Service('./chromedriver')
    options = Options()
    options.headless = True
    options.page_load_strategy = 'normal'

    driver = webdriver.Chrome(service=s, options=options)
    url='http://169.254.95.52/web.exe?file=N57xxmodifySettings.html'
    driver.get(url)
    
    voltageInput = driver.find_element(By.NAME, "voltage")
    currentInput = driver.find_element(By.NAME, "current")
    saveButton   = driver.find_element(By.NAME, "outputvalues")

    voltage = v if (v != -1) else voltageInput.get_attribute('value')
    current = c if (c != -1) else currentInput.get_attribute('value')

    voltageInput.clear()
    currentInput.clear()

    voltageInput.send_keys(voltage)
    currentInput.send_keys(current)

    saveButton.click()

    driver.quit()