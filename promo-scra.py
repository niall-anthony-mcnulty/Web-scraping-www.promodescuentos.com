## imports

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import time
import pprint
from datetime import datetime
import urllib
import base64
import os.path
import schedule
# from apikey import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
import pytz
import openpyxl
import os

# ---------------------- loop through website for individual URLS ------------------- #
# ----------------------------------------------------------------------------------- #

# #url based off page number
# pageno = 1

# # list of urls
# arr_url  = []

# # loop through pages until pages run out
# while pageno < 2000:
    
    

#     headers = {
#         'authority': 'www.promodescuentos.com',
#         'cache-control': 'max-age=0',
#         'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"macOS"',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-fetch-site': 'none',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-user': '?1',
#         'sec-fetch-dest': 'document',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#         'cookie': 'view_layout_horizontal=%221-1%22; show_my_tab=0; f_v=%229f0ea980-3230-11ec-a29c-0242ac110003%22; _ga=GA1.3.1054458069.1634794497; _gid=GA1.3.1552499565.1634794497; ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22browser-1626960373888-6%22%2C%22c%22%3A1634794497594%2C%22l%22%3A1634794497605%7D; ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%2264eea135-5993-3f15-ebc4-09adf427628c%22%2C%22c%22%3A1634794497609%2C%22l%22%3A1634794497609%7D; discussions_widget_selected_option=%22popular%22; _hjid=ae0f1ed2-2d92-4f09-bf43-c7bc66931033; __gads=ID=0ce43e3eff6da5ec:T=1634794499:S=ALNI_Mad7QJuOXppxRjU5egRVkmABAHc-A; stg_returning_visitor=Thu%2C%2021%20Oct%202021%2005:35:35%20GMT; navi=%7B%22homepage%22%3A%22picked%22%7D; _hjIncludedInSessionSample=0; xsrf_t=%22HEKJhu3kbDLqi5JfV1bDT2SpB0casC7t8lYr123B%22; _hjAbsoluteSessionInProgress=0; _pk_ses.12dffd1a-d9f7-4108-953d-b1f490724bce.09fe=*; stg_externalReferrer=; stg_traffic_source_priority=1; browser_push_permission_requested=1634922729; _gat=1; pepper_session=%22O3fygKnag0an5mcXzMUY4Cte4ZhqyaiBdI8DDjVk%22; remember_6fc0f483e7f442dc50848060ae780d66=%22778370%7CXrIutHkF0kW4HvN6kagIuDIqsQmOzP4HwyizQpKc3jl642wfYMc55YZfHmph%7C%242y%2410%24UCA2KfcAHkp28h5luvz69eim1o4ljCHTkbPNiE.Gm%5C%2FdRld.JuV4ei%22; u_l=1; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%226b6610eb-9a5d-5719-499c-6571b7fa98c8%22%2C%22e%22%3A2134922914462%2C%22c%22%3A1634794497601%2C%22l%22%3A1634922914462%7D; stg_last_interaction=Fri%2C%2022%20Oct%202021%2017:15:17%20GMT; _pk_id.12dffd1a-d9f7-4108-953d-b1f490724bce.09fe=6f429fab6ac98163.1634794500.12.1634922917.1634919759.',
#     }

   

#     baseurl = "https://www.promodescuentos.com/nuevas?page=" + str(pageno)

#     # request page and soupify
#     r = requests.get(baseurl, headers=headers).text
#     soup = BeautifulSoup(r, 'html.parser')
    
#     # error handling for login required links
#     try:
        
#         products = soup.find_all('a', {"class": "cept-thread-image-link"},href=True)
    
#         #loop through 'a' elements and extract url
#         for links in products:
#             arr_url.append(links['href'])

        
#     except:
#         continue
    
#     # increment pageno by 1
#     pageno += 1


# pprint.pprint(arr_url)
# print(len(arr_url))
# print(pageno)


# # store urls
# df = pd.DataFrame(arr_url, columns = ['urls'])

# # save to csv - Save to your own directory

# df.to_csv("/Users/Niall-McNulty/Desktop/Computer Science Projects:Courses/Web Scraping/Web-scraping-www.promodescuentos.com/nuevas_urls.csv", index = False)


# ----------------------------------------------------------------------------------- #



# ------------------------------ Open URL csv --------------------------------------- #
# ----------------------------------------------------------------------------------- #


def job():
    #read in URL csv - Load in from your own directory

    directory = os.path.dirname(__file__)
    filename = "csv/nuevas_urls.csv"
    file_path = os.path.join(directory, filename)
    df_url = pd.read_csv(file_path, index_col=False)


    # create a list of URLS to iterate over
    arr_url = [ x for x in df_url['urls']]

    # ------------------------------ Run Scraper ---------------------------------------- #
    # ----------------------------------------------------------------------------------- #


    #lists will become columns in dataframe

    # each_url_degrees = []
    # each_url_product = []
    # each_url_final_price = []
    # each_url_original_price = []
    # each_url_free_shipping = []
    # each_url_merchant = []
    # each_url_username = []
    # each_url_date = []
    # each_url_origin = []
    # url = []
    # each_url_category_1 = []
    # each_url_category_2 = []
    # each_url_category_3 = []
    # each_url_category_4 = []
    # each_url_category_5 = []
    # each_url_category_6 = []
    # each_url_category_7 = []
    # each_url_category_8 = []
    # each_url_category_9 = []
    # top_comment_user = []
    # top_comment = []
    # thumbs_up = []

    # count = 0
    for urls in arr_url[0:10]:
        print(urls)
        
        

        ## ------- Remote Driver --------###
        # add headless mode
        options = Options()
        options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        # # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--no-sandbox") # Bypass OS security model
        s=Service(str(os.environ.get("CHROMEDRIVER_PATH")))
        driver = webdriver.Chrome(service=s, options=options)
        driver.get(urls)

        # ## ------- Local Driver --------###
        # DRIVER_PATH = '/Users/Niall-McNulty/Desktop/Computer Science Projects:Courses/Web Scraping/Web-scraping-www.promodescuentos.com/chromedriver'
        # # add headless mode
        # options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        # options.add_argument('--no-sandbox') # Bypass OS security model
        # driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        # driver.get(urls)

        r = driver.page_source
        print(r)
        #soup = BeautifulSoup(r, 'html.parser')

        #--------------------------------------------------------------------------------------------------------------------#   
        # append URL to list

            
    


    # ----------------------------------------------------------------------------------- #
    # ------------------------ Encode & Email with Scheduler ---------------------------- # 


    # with open('nuevas_data.xlsx', 'rb') as f:
    #     data = f.read()
    #     f.close()

    # encoded = base64.b64encode(data).decode()
    # message = Mail(
    # from_email=FROM_EMAIL,
    # to_emails=TO_EMAIL,
    # subject='Your File is Ready',
    # html_content='<strong>Attached is Your Scraped File</strong>')
    # attachment = Attachment()
    # attachment.file_content = FileContent(encoded)
    # attachment.file_type = FileType('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    # attachment.file_name = FileName('nuevas_data.xlsx')
    # attachment.disposition = Disposition('attachment')
    # attachment.content_id = ContentId('Example Content ID')
    # message.attachment = attachment

    # try:
    #     sg = SendGridAPIClient(SENDGRID_API_KEY)
    #     response = sg.send(message)
    #     print(response.status_code)
    #     print(response.body)
    #     print(response.headers)
    # except Exception as e:
    #         print(e)


schedule.every(5).minutes.do(job)
# # # # schedule.every().hour.do(job)
# # # # schedule.every().day.at('13:58').do(job)
# # # # schedule.every(5).to(10).minutes.do(job)
# # # # schedule.every().monday.do(job)
# # # # schedule.every().thursday.at("17:24").do(job)
# # # # schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute



