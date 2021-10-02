from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome( "C:/Users/mylap/Downloads/chromedriver.exe" )
url = 'https://collegedunia.com/engineering-colleges'
driver.get(url)

colleges = driver.find_elements_by_class_name('jsx-765939686 listing-block text-uppercase bg-white position-relative')
colleges_result=[]
for college in colleges:
    name = college.find_element_by_xpath('.//*[@id="__next"]/div[3]/section/div/div[2]/div[2]/div[4]/div[5]/div/div[1]/div/div[3]/a/h3').text
    address = college.find_element_by_xpath('.//*[@id="__next"]/div[3]/section/div/div[2]/div[2]/div[4]/div[5]/div/div[2]/div/span/span[1]').text
    fees = college.find_element_by_xpath('.//*[@id="__next"]/div[3]/section/div/div[2]/div[2]/div[4]/div[5]/div/div[2]/ul/li[1]/a/span[1]').text
    list={
        'name':name,
        'address':address,
        'Fee':fees
    }
    colleges_result.append(list)
data=pd.DataFrame(colleges_result)
print(data)