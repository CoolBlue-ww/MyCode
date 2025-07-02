# def main(input_num):
#     print(input_num, end='=')
#     for num in range(2, input_num):
#         while input_num % num == 0:
#             input_num /= num
#             if input_num == 1:
#                 print(num, end='*')
#                 break
#     return 0

# if __name__ == '__main__':
#     num = int(input('Enter a number: '))
#     main(num)
    

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/home/SayMyName/下载/chromedriver-linux64 (1)/chromedriver-linux64/chromedriver')

driver = webdriver.Chrome(service=service)
driver.get("https://www.baidu.com")


# import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# import time
# import random
# from lxml import etree
# from bs4 import BeautifulSoup
# import numpy
# import pandas
# import matplotlib.pyplot as plt
# import re
# import urllib.request
# import socket
# from fake_useragent import UserAgent
# import os
# from concurrent.futures import ThreadPoolExecutor as TPE
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from datetime import datetime
# import math
# import json
# import ijson
# from tqdm import tqdm
# import asyncio
# import io
# import pathlib
# from PIL import Image
# import warnings
# import subprocess
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import hashlib
# import platform
# import sys
# import types
# from webdriver_manager.chrome import ChromeDriverManager
# import filemagic


# 等待时间
# WAIT_TIME = 10
# 请求头
# ua = UserAgent()
# HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-encoding': 'gzip, deflate, br, zstd',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'cache-control': 'max-age=0',
#     'cookie': 'is_human=1; anonymous_user_id=c19cb89f9645441d86b19243eb45551f; csrftoken=PfwHaQhkgrZ3xcVdTs6LgqZWp7edcduU; _cfuvid=Yy00pIYPTH.PxmD7f8k0I0El6pe30KYFTrWXzRl1kEc-1749348120437-0.0.1.1-604800000; _sp_ses.aded=*; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Jun+08+2025+10%3A16%3A14+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=eff2dce2-44f3-4419-bd71-d5347d68dd6d&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _sp_id.aded=e51bd3a3-517c-428f-9cbf-efe0c4a50f59.1749346210.2.1749348976.1749346270.2bd9f518-6232-4e5e-ae4f-84a94b6f7f46.392fc768-349f-4553-b236-f7d4e6d2c96d.18b9ddd1-67ee-42da-870f-e14fc396f601.1749348135643.9; __cf_bm=3UVkG7CnIWtELNGhYrGJJK7nMeCZ4Jg13IdMQyrY94Y-1749349477-1.0.1.1-.cMD7ZuVcJg_uixqk.bti__vh_5MMrYPqLmTIlevHMBihKAQCFiBRng8QFq2CUW4mT_HMb2JPTUxgLVCVFmfGtazOkf1bTXkTyqarcSKg1A',
#     'priority': 'u=0, i',
#     'referer': 'https://pixabay.com/',
#     'sec-ch-ua': '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': "Linux",
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': 1,
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
# }
# 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:139.0) Gecko/20100101 Firefox/139.0'
# 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
# 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
# # 浏览器的Options对象
# OPTIONS = Options()
# OPTIONS.add_argument('--headless')  # 开启无头浏览器模式
# OPTIONS.add_argument('--disable-gpu')  # 禁用gpu加速
# OPTIONS.add_argument('--disable-popup-blocking')  # 禁用浏览器弹窗
# OPTIONS.add_argument('--disable-notifications')  # 禁用浏览器通知
# OPTIONS.add_argument('--disable-extensions')  # 禁用所有扩展程序
# OPTIONS.add_argument('--disable-infobars')  # 禁用自动化测试软件控制提示
# 创建Service对象
# log = 'ss'  # 浏览器日志的输出路径
# browser_driver = 'cc'  # 浏览器驱动的路径
# SERVICE = Service(executable_path=browser_driver, log_output=log)

service = Service(executable_path='/home/SayMyName/桌面/GitHub/MyCode/DeepLearn/PyTorch/A/browser/chromedriver')
b = webdriver.Chrome(service=service)
b.get('https://www.baidu.com')

# print(ua.random)
# print(os.environ)
# print(platform.system())
# class Driver(object):
#     __slots__ = ['driver', 'service', 'options']
#     def __init__(self):
#         self.service = Service(executable_path='./browser/chromedriver', log_output=None)
#         self.options = Options()
#         self.options.binary_location = './browser/chrome'
#         self.driver = webdriver.Chrome(service=self.service, options=self.options)
#
#     # def by(self):
#
#
# a = Driver()
# a.get('https://www.baidu.com')



























