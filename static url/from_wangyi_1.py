from selenium import webdriver
import csv

url = "http://music.163.com/#/discover/playlist/\
    ?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"

driver = webdriver.PhantomJS()
with open("playlist.cvs","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['标题','播放量','链接'])
    while url != 'javascript:void(0)':
        driver.get(url)
        driver.switch_to.frame("contentFrame")
        data = driver.find_element_by_id("m-pl-container").\
            find_elements_by_tag_name("li")
        # print(data.size)
        # print(dir(data))
        for i in range(0,len(data)):
            nb = data[i].find_element_by_class_name("nb").text
            if "万" in nb and int(nb.split("万")[0])>500:
                msk = data[i].find_element_by_css_selector("a.msk")
                writer.writerow([msk.get_attribute('title').encode('GBK', 'ignore'),
                                nb,
                                msk.get_attribute('href').encode('GBK', 'ignore')])
        url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
