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
from apikey import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
import pytz
import openpyxl
import os
from github import Github
import lxml


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

    each_url_degrees = []
    each_url_product = []
    each_url_final_price = []
    each_url_original_price = []
    each_url_free_shipping = []
    each_url_merchant = []
    each_url_username = []
    each_url_date = []
    each_url_origin = []
    url = []
    each_url_category_1 = []
    each_url_category_2 = []
    each_url_category_3 = []
    each_url_category_4 = []
    each_url_category_5 = []
    each_url_category_6 = []
    each_url_category_7 = []
    each_url_category_8 = []
    each_url_category_9 = []
    top_comment_user = []
    top_comment = []
    thumbs_up = []

    count_url = 1
    for urls in arr_url:
        print(urls)
        count_url += 1

        
        try:

            # ------- Remote Driver --------###
            # add headless mode
            options = webdriver.ChromeOptions()
            options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
            options.add_argument("--headless") # Runs Chrome in headless mode.
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox") # Bypass OS security model
            s=Service(os.environ.get("CHROMEDRIVER_PATH"))
            driver = webdriver.Chrome(service=s, options=options)
            driver.get(urls)

            # ------- Local Driver --------###
            # DRIVER_PATH = '/Users/Niall-McNulty/Desktop/Computer Science Projects:Courses/Web Scraping/Web-scraping-www.promodescuentos.com/chromedriver'
            # # add headless mode
            # options = webdriver.ChromeOptions()
            # options.add_argument("--headless") # Runs Chrome in headless mode.
            # options.add_argument("--disable-gpu")
            # options.add_argument("--disable-dev-shm-usage")
            # options.add_argument('--no-sandbox') # Bypass OS security model
            # driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
            # driver.get(urls)

            r = driver.page_source
            soup = BeautifulSoup(r, 'lxml')

        #--------------------------------------------------------------------------------------------------------------------#   
        # append URL to list

            try:
                url.append(urls)
            except:
                url.append(None)




        #--------------------------------------------------------------------------------------------------------------------#              
        #loop through URLS and obtain degree integer  
            try:
                degrees = soup.find('div',{'class' : "cept-vote-box"}).text
                degrees = re.sub('[^-?0-9]', '', degrees)
                # return only digits
                each_url_degrees.append(int(degrees))
            except:
                each_url_degrees.append(None)

        #--------------------------------------------------------------------------------------------------------------------#    
        #loop through URLS and obtain product data


            try:
                product = soup.find('span',{'class' : "thread-title--item"}).text
                each_url_product.append(product)
            except:
                each_url_product.append(None)


        #--------------------------------------------------------------------------------------------------------------------#
        # loop through URLS and obtain final price


            try:
                final_price = soup.find('span',{'class' : "cept-tp"}).text
                substring = 'GRATIS'
                # check if final price is GRATIS - return 0 if so
                if substring in final_price:
                    each_url_final_price.append(0)
                else:
                    # return only digits (take out special characters to ensure int datatype)
                    final_price = re.sub('[^0-9]', '', final_price)
                    each_url_final_price.append(int(final_price))
            except:
                each_url_final_price.append(None)


        #--------------------------------------------------------------------------------------------------------------------#

        # loop through URLS and obtain original price


            try:
                original_price = soup.find('span',{'class' : "cept-next-best-price"}).text
                original_price = re.sub('[^0-9]', '', original_price)
                each_url_original_price.append(int(original_price))
            except:
                each_url_original_price.append(None)


        #--------------------------------------------------------------------------------------------------------------------#
        # loop through URLS and obtain free shipping




            try1 = soup.find('span',{'class' : "cept-shipping-price"})
            try2 = soup.find('span',{'class' : "cept-tp"})
            try3 = soup.find('div',{ 'class' : 'threadItem-title'})
            try4 = soup.find('span',{'class' : 'overflow--fade'})
            try5 = soup.find('span',{'class' : 'text--color-greyShade'})

            # check for envio gratis and return true
            substring1 = 'Envio gratis'
            try:

                if (try1 is not None) and (substring1 in try1.text):
                # append to list
                    each_url_free_shipping.append(True)
                elif (try2 is not None) and (substring1 in try2.text):
                    each_url_free_shipping.append(True) 
                elif (try3 is not None) and (substring1 in try3.text):
                    each_url_free_shipping.append(True)
                elif (try4 is not None) and (substring1 in try4.text):
                    each_url_free_shipping.append(True)
                elif (try5 is not None) and (substring1 in try5.text):
                    each_url_free_shipping.append(True)
                else:
                    each_url_free_shipping.append(False)

            except:
                each_url_free_shipping.append(False)

        #--------------------------------------------------------------------------------------------------------------------#
        # loop through URLS and obtain merchant



            try:
                merchant = soup.find('span',{'class' : "cept-merchant-name"}).text
                merchant = re.sub('[\s*$]', '', merchant)


                each_url_merchant.append(merchant)
            except:
                each_url_merchant.append(None)



        #--------------------------------------------------------------------------------------------------------------------#


        # loop through URLS and obtain usernames


            try:
                username = soup.find('span',{'class' : "thread-username"}).text
                username = re.sub('[\s*$]', '', username)
                each_url_username.append(username)
            except:
                each_url_username.append(None)



        #--------------------------------------------------------------------------------------------------------------------#


            # loop through URLS and obtain date

            try:
            
                # check for post date 
                dates = soup.find_all('span',{'class' : "flex--toW3 overflow--wrap-off text--color-greyShade"})
                
                if len(dates) == 0:
                    # check for publication
                    pubs = soup.find('span', {'class' :'flex--toW3 overflow--wrap-off text--color-greyShade text--b'})
                    # if no publication date add None to the dates list/array
                    if len(pubs) == 0:
                        each_url_date.append(None)
                        # if there is a publication date
                    else:
                        # return the date inside the brackets using regex and add to the dates list/array
                        pub_date = pubs.find('span', {'class' :'space--fromW3-ml-1 size--all-s space--t-2 space--fromW3-t-0 overflow--wrap-on space--fromW3-r-2'}).text
                        regex = re.findall('\((.*)\)', pub_date)
                        pub_date = regex[0]
                        pub_date = re.sub('(Publicado)', '', pub_date)

                        # check for string year
                        substring_year = '20'
                        # current year
                        current_year = str(datetime.datetime.now().year)
                        # if it does have the year, don't append 
                        if substring_year in pub_date:
                            pub_date = re.sub('^[ \t]+', '', pub_date)
                            each_url_date.append(pub_date)
                        else:
                            # if it does, concatenate year
                            pub_date = re.sub('^[ \t]+', '', pub_date) + ' ' +  current_year
                            each_url_date.append(pub_date)


                elif soup.find('span', {'class' :'flex--toW3 overflow--wrap-off text--color-greyShade text--b'}):
                    pubs = soup.find('span', {'class' :'flex--toW3 overflow--wrap-off text--color-greyShade text--b'})

                    # if no publication date add None to the dates list/array
                    if len(pubs) == 0:
                        each_url_date.append(None)
                        # if there is a publication date
                    else:
                        # return the date inside the brackets using regex and add to the dates list/array
                        pub_date = pubs.find('span', {'class' :'space--fromW3-ml-1 size--all-s space--t-2 space--fromW3-t-0 overflow--wrap-on space--fromW3-r-2'}).text
                        regex = re.findall('\((.*)\)', pub_date)
                        pub_date = regex[0]
                        pub_date = re.sub('(Publicado)', '', pub_date)

                        # check for string year
                        substring_year = '20'
                        # current year
                        current_year = str(datetime.datetime.now().year)
                        # if it does have the year, don't append 
                        if substring_year in pub_date:
                            pub_date = re.sub('^[ \t]+', '', pub_date)
                            each_url_date.append(pub_date)
                        else:
                            # if it does, concatenate year
                            pub_date = re.sub('^[ \t]+', '', pub_date) + ' ' + current_year
                            each_url_date.append(pub_date)



                else:
                    # loop through the classes
                    for normal_date in dates:
                    # check for clock icon
                        if normal_date.find('svg',{'class':'icon icon--clock text--color-greyShade'}):
                        # return value
                            url_date = normal_date.find('span',{'class':'space--fromW3-ml-1 size--all-s space--t-2 space--fromW3-t-0 overflow--wrap-on space--fromW3-r-2'}).text
                            url_date = re.sub('\((.*)\)', '', url_date)
                            url_date = url_date.rstrip()
                            each_url_date.append(url_date)



            except:
                each_url_date.append(None)



        #--------------------------------------------------------------------------------------------------------------------#    

            #obtain origin 

            
            try:
                elements = soup.find_all('span',{'class' : 'flex--toW3 overflow--wrap-off text--color-greyShade'})
        
                # temporary list
                temp_origin_list = []
                # counter
                count = 0
                while count < len(elements):

                    # loop html elements in elements variable
                    for origins in elements:

                        # check for icon, return text and increment count
                        if origins.find('svg',{'class' : 'icon--world'}):
                            icon_text = origins.find('span',{'class' : 'space--fromW3-ml-1 size--all-s space--t-2 space--fromW3-t-0 overflow--wrap-on space--fromW3-r-2'}).text
                            # return value if it is there and clean string with regex
                            icon_text = re.sub('(Se envía de )', '', icon_text)
                            if len(temp_origin_list) == 0:
                                temp_origin_list.append(icon_text)
                            else:
                                if len(temp_origin_list) == 1:
                                    continue

                            count += 1

                        # check for icon, return text and increment count
                        elif origins.find('svg',{'class' : 'icon--location'}):
                            icon_text = origins.find('span',{'class' : 'space--fromW3-ml-1 size--all-s space--t-2 space--fromW3-t-0 overflow--wrap-on space--fromW3-r-2'}).text
                            # return value if it is there and clean string with regex
                            icon_text = re.sub('(Se envía de )', '', icon_text)
                            if len(temp_origin_list) == 0:
                                temp_origin_list.append(icon_text)
                            else:
                                if len(temp_origin_list) == 1:
                                    continue


                            count += 1

                        else:
                            count += 1
                # if the list is empty, append None to ensure df array lengths match  
                if len(temp_origin_list) == 0:
                    temp_origin_list.append(None)
                # Append temporary list input to 'each_url_origin list' (should be len(1))
                for item in temp_origin_list:
                    each_url_origin.append(item)
            
            except:
                each_url_origin.append(None)


        #--------------------------------------------------------------------------------------------------------------------#   


            # check for categories
            categories = soup.find_all("a",{"class" : "text--b linkPlain cept-thread-group-name thread-link mute--text space--mr-3"})
            try:

                tags = []
                for category in categories:
                    tags.append(category.text)

                if len(tags) == 0:

                    each_url_category_1.append(None)
                    each_url_category_2.append(None)
                    each_url_category_3.append(None)
                    each_url_category_4.append(None)
                    each_url_category_5.append(None)
                    each_url_category_6.append(None)
                    each_url_category_7.append(None)
                    each_url_category_8.append(None)
                    each_url_category_9.append(None)

                if len(tags) == 1:

                    each_url_category_1.append(tags[0])
                    each_url_category_2.append(None)
                    each_url_category_3.append(None)
                    each_url_category_4.append(None)
                    each_url_category_5.append(None)
                    each_url_category_6.append(None)
                    each_url_category_7.append(None)
                    each_url_category_8.append(None)
                    each_url_category_9.append(None)


                if len(tags) == 2:
                    each_url_category_1.append(tags[0])
                    each_url_category_2.append(tags[1])
                    each_url_category_3.append(None)
                    each_url_category_4.append(None)
                    each_url_category_5.append(None)
                    each_url_category_6.append(None)
                    each_url_category_7.append(None)
                    each_url_category_8.append(None)
                    each_url_category_9.append(None)


                if len(tags) == 3:
                    each_url_category_1.append(tags[0])
                    each_url_category_2.append(tags[1])
                    each_url_category_3.append(tags[2])
                    each_url_category_4.append(None)
                    each_url_category_5.append(None)
                    each_url_category_6.append(None)
                    each_url_category_7.append(None)
                    each_url_category_8.append(None)
                    each_url_category_9.append(None)


                if len(tags) == 4:
                    each_url_category_1.append(tags[0])
                    each_url_category_2.append(tags[1])
                    each_url_category_3.append(tags[2])
                    each_url_category_4.append(tags[3])
                    each_url_category_5.append(None)
                    each_url_category_6.append(None)
                    each_url_category_7.append(None)
                    each_url_category_8.append(None)
                    each_url_category_9.append(None)


                if len(tags) == 5:
                    each_url_category_1.append(tags[0])
                    each_url_category_2.append(tags[1])
                    each_url_category_3.append(tags[2])
                    each_url_category_4.append(tags[3])
                    each_url_category_5.append(tags[4])
                    each_url_category_6.append(None)
                    each_url_category_7.append(None)
                    each_url_category_8.append(None)
                    each_url_category_9.append(None)


                if len(tags) == 6:
                    each_url_category_1.append(tags[0])
                    each_url_category_2.append(tags[1])
                    each_url_category_3.append(tags[2])
                    each_url_category_4.append(tags[3])
                    each_url_category_5.append(tags[4])
                    each_url_category_6.append(tags[5])
                    each_url_category_7.append(None)
                    each_url_category_8.append(None)
                    each_url_category_9.append(None)


                if len(tags) == 7:
                    each_url_category_1.append(tags[0])
                    each_url_category_2.append(tags[1])
                    each_url_category_3.append(tags[2])
                    each_url_category_4.append(tags[3])
                    each_url_category_5.append(tags[4])
                    each_url_category_6.append(tags[5])
                    each_url_category_7.append(tags[6])
                    each_url_category_8.append(None)
                    each_url_category_9.append(None)


                if len(tags) == 8:
                    each_url_category_1.append(tags[0])
                    each_url_category_2.append(tags[1])
                    each_url_category_3.append(tags[2])
                    each_url_category_4.append(tags[3])
                    each_url_category_5.append(tags[4])
                    each_url_category_6.append(tags[5])
                    each_url_category_7.append(tags[6])
                    each_url_category_8.append(tags[7])
                    each_url_category_9.append(None)


                # in case any posts have more than 9 tags/categories
                if len(tags) >= 9:
                    each_url_category_1.append(tags[0])
                    each_url_category_2.append(tags[1])
                    each_url_category_3.append(tags[2])
                    each_url_category_4.append(tags[3])
                    each_url_category_5.append(tags[4])
                    each_url_category_6.append(tags[5])
                    each_url_category_7.append(tags[6])
                    each_url_category_8.append(tags[7])
                    each_url_category_9.append(tags[8])

            except:
                each_url_category_1.append(None)
                each_url_category_2.append(None)
                each_url_category_3.append(None)
                each_url_category_4.append(None)
                each_url_category_5.append(None)
                each_url_category_6.append(None)
                each_url_category_7.append(None)
                each_url_category_8.append(None)
                each_url_category_9.append(None)
                
    #--------------------------------------------------------------------------------------------------------------------#   

            # check for top comment, username and thumbs up
            try:
                
                if soup.find_all('span',{'class':'lbox--v-3 space--l-2 size--all-m size--fromW2-l text--b'}):
                    find_comments = soup.find_all('span',{'class':'lbox--v-3 space--l-2 size--all-m size--fromW2-l text--b'})
                    for elements in find_comments:
                        # check for top comments
                        if 'Mejores comentarios' in elements.text:
                            # if there is, find the username (first matching element) and append to list
                            if soup.find('span',{'class': 'userInfo-username'}).text:
                                user_name = soup.find('span',{'class': 'userInfo-username'}).text
                                top_comment_user.append(user_name)
                            else:
                                top_comment_user.appned(None)

                            # check for thumbs up amount and append to list
                            if soup.find('span', {'class': 'comment-like'}).text:
                                thumbs_up_count = soup.find('span', {'class': 'comment-like'}).text
                                thumbs_up.append(thumbs_up_count)
                            else:
                                thumbs_up.append(None)


                            # check for the parent div for comments
                            if soup.find('div',{'class':'commentList-item'}):
                                # assign it to a variable
                                parent = soup.find('div',{'class':'commentList-item'})
                                # check for top comment(first entry)
                                if parent.find('div',{'class':'comment-body'}):
                                    # grab text
                                    comment_text = parent.find('div',{'class':'comment-body'}).text
                                    # if there is no text, it is assumed to be a graphic or image
                                    if comment_text == '':
                                        top_comment.append('Graphic instead of text (image/meme)')
                                        # append text if there is
                                    else:
                                        top_comment.append(comment_text)
                            else:
                                top_comment.append(None)


                        else:
                            top_comment.append(None)

                else:
                    top_comment_user.append(None)
                    top_comment.append(None)
                    thumbs_up.append(None)
                
            except:
                top_comment_user.append(None)
                top_comment.append(None)
                thumbs_up.append(None)
                
                
    #--------------------------------------------------------------------------------------------------------------------#   
                

        except:
            each_url_degrees.append(None)
            each_url_product.append(None)
            each_url_final_price.append(None)
            each_url_original_price.append(None)
            each_url_free_shipping.append(None)
            each_url_merchant.append(None)
            each_url_username.append(None)
            each_url_date.append(None)
            each_url_origin.append(None)
            url.append(None)
            each_url_category_1.append(None)
            each_url_category_2.append(None)
            each_url_category_3.append(None)
            each_url_category_4.append(None)
            each_url_category_5.append(None)
            each_url_category_6.append(None)
            each_url_category_7.append(None)
            each_url_category_8.append(None)
            each_url_category_9.append(None)
            top_comment_user.append(None)
            top_comment.append(None)
            thumbs_up.append(None)

        if (count_url % 500) == 0:

            def date_correction(col):

                substring_double_year = '2020 2021'
                # check for substring
                if substring_double_year in str(col):
                    # split the string
                    split_column_values = str(col).split(" ")
                    # empty string
                    date_1_new = ''
                    
                    # set a counter
                    count = 0
                    # loop through list elements
                    for x in split_column_values:
                        if count == 3:
                            break
                        # concatenate strings together - except for the last element
                        else:
                            date_1_new += (str(x) + ' ')
                            count += 1

                    # split the string to erase weird symbol
                    date_2_new = date_1_new.split("º.")
                    # join them back together
                    date_2_new = ",".join(date_2_new)
                    # return without trailing white space
                    return date_2_new.rstrip()
                    
                else:
                    # split the string to erase weird symbol
                    new_date =  str(col).split("º.")
                    # join them back together
                    new_date_2 = ",".join(new_date)
                    # return without trailing white space
                    return new_date_2.rstrip()
                                                                

                # ----------------------------------------------------------------------------------- #
                # ---------------------------- Translate Month Sring -------------------------------- # 
            def month_translation(col):
                if 'ene' in col:
                    return col.replace('ene','January')
                elif 'feb' in col:
                    return col.replace('feb','February')
                elif 'mar' in col:
                    return col.replace('mar','March')
                elif 'abr' in col:
                    return col.replace('abr','April')
                elif 'may' in col:
                    return col.replace('may', 'May')
                elif 'jun' in col:
                    return col.replace('jun','June')
                elif 'jul' in col:
                    return col.replace('jul','July')
                elif 'ago' in col:
                    return col.replace('ago','August')
                elif 'sep' in col:
                    return col.replace('sep','September')
                elif 'oct' in col:
                    return col.replace('oct', 'October')
                elif 'nov' in col:
                    return col.replace('nov','November')
                elif 'dic' in col:
                    return col.replace('dic','December')
                else:
                    return col


            # ----------------------------------------------------------------------------------- #
            # ------------------------ Change String to Datetime -------------------------------- # 
            def date_time(col):
                try:
                    return datetime.strptime(col, "%B %d, %Y")
                except:
                    return pd.NaT


            data_dict = {'Degrees':each_url_degrees,'Product':each_url_product,'Final_Price':each_url_final_price,'Original_Price':each_url_original_price,'Free_Shipping':each_url_free_shipping,'Merchant':each_url_merchant, 'Username':each_url_username,'Date':each_url_date,'Origin':each_url_origin,'URL':url, 'Category_1':each_url_category_1,'Category_2':each_url_category_2,'Category_3':each_url_category_3,'Category_4':each_url_category_4,'Category_5':each_url_category_5,'Category_6':each_url_category_6,'Category_7':each_url_category_7,'Category_8':each_url_category_8,'Category_9':each_url_category_9,'top_comment_user':top_comment_user,'top_comment':top_comment,'thumbs_up':thumbs_up}
            df_nuevas_data = pd.DataFrame.from_dict(data_dict)

            try:
                df_nuevas_data['Date'] = df_nuevas_data['Date'].apply(date_correction)
            
                # translate month
                df_nuevas_data['Date'] = df_nuevas_data['Date'].apply(month_translation)

                # apply datetime format
                df_nuevas_data['Date'] = df_nuevas_data['Date'].apply(date_time)
            except:
                print('could not convert data')

            df_nuevas_data.index += 1

            # df_nuevas_data.to_csv('promodescuentos-nuevas-sixmonths' + str(count_url) + '.csv')
            # df_nuevas_data.to_excel('promodescuentos-nuevas-sixmonths' + str(count_url) + '.xlsx', encoding='utf-8')

            # directory = os.path.dirname(os.path.realpath(__file__))
            # filename = "nuevas_data.csv"
            # file_path = os.path.join(directory, 'csv/', filename)
            # # # Save to csv format to handle encoding
            # df_nuevas_data.to_csv(file_path)

            
            # save to git using PyGithub
            github = Github(os.environ.get('GIT_KEY'))
            repository = github.get_user().get_repo('Web-scraping-www.promodescuentos.com')
            #path in the repository
            filename = 'promodescuentos-nuevas-sixmonths' + str(count_url) + '.csv'
            # content to write
            df = df_nuevas_data.to_csv(sep=',', index=False)
            content = df
        

            #create a commit message
            f = repository.create_file(filename, "create updated scraper csv", content)
            
            
                    
        

            


    # # Save complete file

    data_dict = {'Degrees':each_url_degrees,'Product':each_url_product,'Final_Price':each_url_final_price,'Original_Price':each_url_original_price,'Free_Shipping':each_url_free_shipping,'Merchant':each_url_merchant, 'Username':each_url_username,'Date':each_url_date,'Origin':each_url_origin,'URL':url, 'Category_1':each_url_category_1,'Category_2':each_url_category_2,'Category_3':each_url_category_3,'Category_4':each_url_category_4,'Category_5':each_url_category_5,'Category_6':each_url_category_6,'Category_7':each_url_category_7,'Category_8':each_url_category_8,'Category_9':each_url_category_9,'top_comment_user':top_comment_user,'top_comment':top_comment,'thumbs_up':thumbs_up}
    df_nuevas_data = pd.DataFrame.from_dict(data_dict)
                                                    
    # ------------------------------- Clean Data ---------------------------------------- #
    # ----------------------------------------------------------------------------------- #
                                                    
    # df_nuevas_data = df_nuevas_data['Date'].astype(str)
    # df_nuevas_data['Free_Shipping'] = df_nuevas_data['Free_Shipping'].astype(bool)                                                
                                                
    # ----------------------------------------------------------------------------------- #
    # ------------------------------- Adjust Date String -------------------------------- #                                                  
    def date_correction(col):

        substring_double_year = '2020 2021'
        # check for substring
        if substring_double_year in str(col):
            # split the string
            split_column_values = str(col).split(" ")
            # empty string
            date_1_new = ''
            
            # set a counter
            count = 0
            # loop through list elements
            for x in split_column_values:
                if count == 3:
                    break
                # concatenate strings together - except for the last element
                else:
                    date_1_new += (str(x) + ' ')
                    count += 1

            # split the string to erase weird symbol
            date_2_new = date_1_new.split("º.")
            # join them back together
            date_2_new = ",".join(date_2_new)
            # return without trailing white space
            return date_2_new.rstrip()
            
        else:
            # split the string to erase weird symbol
            new_date =  str(col).split("º.")
            # join them back together
            new_date_2 = ",".join(new_date)
            # return without trailing white space
            return new_date_2.rstrip()
                                                        

    # ----------------------------------------------------------------------------------- #
    # ---------------------------- Translate Month Sring -------------------------------- # 
    def month_translation(col):
        if 'ene' in col:
            return col.replace('ene','January')
        elif 'feb' in col:
            return col.replace('feb','February')
        elif 'mar' in col:
            return col.replace('mar','March')
        elif 'abr' in col:
            return col.replace('abr','April')
        elif 'may' in col:
            return col.replace('may', 'May')
        elif 'jun' in col:
            return col.replace('jun','June')
        elif 'jul' in col:
            return col.replace('jul','July')
        elif 'ago' in col:
            return col.replace('ago','August')
        elif 'sep' in col:
            return col.replace('sep','September')
        elif 'oct' in col:
            return col.replace('oct', 'October')
        elif 'nov' in col:
            return col.replace('nov','November')
        elif 'dic' in col:
            return col.replace('dic','December')
        else:
            return col


    # ----------------------------------------------------------------------------------- #
    # ------------------------ Change String to Datetime -------------------------------- # 
    def date_time(col):
        try:
            return datetime.strptime(col, "%B %d, %Y")
        except:
            return pd.NaT

    # ----------------------------------------------------------------------------------- #
    # ------------------------ Call Functions & Save to Excel --------------------------- # 


    # fix date
    try:
        df_nuevas_data['Date'] = df_nuevas_data['Date'].apply(date_correction)

    # translate month
        df_nuevas_data['Date'] = df_nuevas_data['Date'].apply(month_translation)

    # apply datetime format
        df_nuevas_data['Date'] = df_nuevas_data['Date'].apply(date_time)
    except:
        print('could not convert data')

    df_nuevas_data.index += 1

    # directory = os.path.dirname(os.path.realpath(__file__))
    # filename = "nuevas_data.csv"
    # file_path = os.path.join(directory, 'csv/', filename)
    # # # Save to csv format to handle encoding
    # df_nuevas_data.to_csv(file_path)


    # save to git using PyGithub
    github = Github(os.environ.get('GIT_KEY'))
    repository = github.get_user().get_repo('Web-scraping-www.promodescuentos.com')
    #path in the repository
    filename = 'promodescuentos-nuevas-'+str(count_url)+'.csv'
    # content to write
    df = df_nuevas_data.to_csv(sep=',', index=False)
    content = df


    #create a commit message
    f = repository.create_file(filename, "create updated scraper csv", content)
    # Print on screen
    # df_nuevas_data.to_csv('promodescuentos-nuevas-sixmonths' + str(count_url) + '.csv')
    # df_nuevas_data.to_excel('promodescuentos-nuevas-sixmonths' + str(count_url) + '.xlsx', encoding='utf-8')



        # ----------------------------------------------------------------------------------- #
        # ------------------------ Encode & Email with Scheduler ---------------------------- # 


        # with open(file_path, 'rb') as f:
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
        # attachment.file_type = FileType('text/csv')
        # attachment.file_name = FileName('nuevas_data.csv')
        # attachment.disposition = Disposition('attachment')
        # attachment.content_id = ContentId('Example Content ID')
        # message.attachment = attachment

        # try:
        #     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        #     response = sg.send(message)
        #     print(response.status_code)
        #     print(response.body)
        #     print(response.headers)
        # except Exception as e:
        #         print(e)


    # # # # # schedule.every(4).minutes.do(job)
    # # # # # schedule.every().hour.do(job)
    # # # # # schedule.every().day.at('01:57').do(job)
    # # # # # schedule.every(5).to(10).minutes.do(job)
schedule.every().thursday.at('15:02').do(job)
# # # # # # schedule.every().thursday.at("17:24").do(job)
# # # # # # schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one second







