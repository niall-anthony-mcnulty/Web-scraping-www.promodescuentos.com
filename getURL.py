

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re
import requests
import bs4
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import time
import pprint
from datetime import datetime
import urllib
import base64
import os.path
import schedule
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
import pytz
import openpyxl
import os
from github import Github
import lxml


# ---------------------- loop through website for individual URLS ------------------- #
# ----------------------------------------------------------------------------------- #

#url based off page number
pageno = 1

# list of urls
arr_url  = []

# loop through pages until pages run out
while pageno < 61:
    
    

    headers = {
        'authority': 'www.promodescuentos.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'view_layout_horizontal=%221-1%22; show_my_tab=0; f_v=%229f0ea980-3230-11ec-a29c-0242ac110003%22; _ga=GA1.3.1054458069.1634794497; _gid=GA1.3.1552499565.1634794497; ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22browser-1626960373888-6%22%2C%22c%22%3A1634794497594%2C%22l%22%3A1634794497605%7D; ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%2264eea135-5993-3f15-ebc4-09adf427628c%22%2C%22c%22%3A1634794497609%2C%22l%22%3A1634794497609%7D; discussions_widget_selected_option=%22popular%22; _hjid=ae0f1ed2-2d92-4f09-bf43-c7bc66931033; __gads=ID=0ce43e3eff6da5ec:T=1634794499:S=ALNI_Mad7QJuOXppxRjU5egRVkmABAHc-A; stg_returning_visitor=Thu%2C%2021%20Oct%202021%2005:35:35%20GMT; navi=%7B%22homepage%22%3A%22picked%22%7D; _hjIncludedInSessionSample=0; xsrf_t=%22HEKJhu3kbDLqi5JfV1bDT2SpB0casC7t8lYr123B%22; _hjAbsoluteSessionInProgress=0; _pk_ses.12dffd1a-d9f7-4108-953d-b1f490724bce.09fe=*; stg_externalReferrer=; stg_traffic_source_priority=1; browser_push_permission_requested=1634922729; _gat=1; pepper_session=%22O3fygKnag0an5mcXzMUY4Cte4ZhqyaiBdI8DDjVk%22; remember_6fc0f483e7f442dc50848060ae780d66=%22778370%7CXrIutHkF0kW4HvN6kagIuDIqsQmOzP4HwyizQpKc3jl642wfYMc55YZfHmph%7C%242y%2410%24UCA2KfcAHkp28h5luvz69eim1o4ljCHTkbPNiE.Gm%5C%2FdRld.JuV4ei%22; u_l=1; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%226b6610eb-9a5d-5719-499c-6571b7fa98c8%22%2C%22e%22%3A2134922914462%2C%22c%22%3A1634794497601%2C%22l%22%3A1634922914462%7D; stg_last_interaction=Fri%2C%2022%20Oct%202021%2017:15:17%20GMT; _pk_id.12dffd1a-d9f7-4108-953d-b1f490724bce.09fe=6f429fab6ac98163.1634794500.12.1634922917.1634919759.',
    }

   

    baseurl = "https://www.promodescuentos.com/nuevas?page=" + str(pageno)

    # request page and soupify
    r = requests.get(baseurl, headers=headers).text
    soup = BeautifulSoup(r, 'lxml')
    
    # error handling for login required links
    try:
        
        products = soup.find_all('a', {"class": "cept-thread-image-link"},href=True)
    
        #loop through 'a' elements and extract url
        for links in products:
            arr_url.append(links['href'])

        
    except:
        continue
    
    # increment pageno by 1
    pageno += 1


pprint.pprint(arr_url)
print(len(arr_url))
print(pageno)


# store urls
df = pd.DataFrame(arr_url, columns = ['urls'])

# save to csv - Save to your own directory

df.to_csv("/Users/Niall-McNulty/Desktop/Computer Science Projects:Courses/Web Scraping/Web-scraping-www.promodescuentos.com/nuevas_urls-first-60.csv", index = False)


# ----------------------------------------------------------------------------------- #
