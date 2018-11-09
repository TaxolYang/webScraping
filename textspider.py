import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import time
import random
from random import randint
import threading







number = 50
newfile = '旅游吃.txt'
path1 = os.path.join('text', newfile)
path2 = os.path.join('text', '早餐时间.txt')

for year in range(2018, 2016, -1):
    for month in range(10, 1, -1):


        for date in range(28 , 1, -1):
            flag =True
            for page in range(1, int(number)):
                headers = {
                'Host': 's.weibo.com',

                'Upgrade-Insecure-Requests': '1',
                    'X-Forwarded-For': str(randint(1, 255))+'.'+str(randint(1, 255))+'.'+str(randint(1, 255))+'.'+str(randint(1, 255)),
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                'Cookie': 'SINAGLOBAL=2600044568305.1245.1539160824221; wvr=6; login_sid_t=b1b63e219239bb04d97ad717edab9a5a; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; UOR=www.google.com.hk,www.weibo.com,www.baidu.com; Apache=1688769208254.0684.1540131589071; ULV=1540131589076:4:4:1:1688769208254.0684.1540131589071:1540013657357; SCF=Ai0mrAZ6Bw5_8HL3FhzKIPa6Q8DxOuSm4CT5YQECs-uMPciKlAeLXrLtUT__kYg-C1wOWUSMO_sDvxzVTOhOUpc.; SUHB=0S7Db9R6h1S4P6; WBStorage=e8781eb7dee3fd7f|undefined; WBtopGlobal_register_version=a6a3e8a5473574f8'
}
                print(str(year)+'-'+str(month)+'-'+str(date)+'-0:'+str(year)+'-'+str(month)+'-'+str(int(date)+1))
                url ='https://s.weibo.com/weibo?q=旅游%20吃&scope=ori&haspic=1&timescope=custom:'+str(year)+'-'+str(month)+'-'+str(date)+'-0:'+str(year)+'-'+str(month)+'-'+str(int(date)+1)+'-0&Refer=g&sudaref=s.weibo.com&display=0&retcode=6102&page='+str(page)

                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.content, 'html.parser')

                soup.encode('utf-8')
                text_link = soup.select('.txt')
                #time_link = soup.select('.from')
                if flag==True:
                    page1 = soup.select('.s-scroll li')
                    try :
                        number = page1[-1].text.lstrip('第').rstrip('页')


                        print(number)
                        flag =False
                    except:
                        print('IndexError: list index out of range')
                for i in text_link:
                    f =open(path1, 'a', encoding='utf-8')
                    f.write(i.text.strip()+'\n')

                    print('正在存取%s-%s-%s第%s页'%(year, month, date, page)+str(i.text))
                    f.close()
                #for time1 in time_link:
                #   f =open(path2, 'a', encoding='utf-8')
                 #   f.write((time1.text.replace('\n', '')).replace(' ', '')+'\n')
#
 #                   print('正在存取'+(time1.text.replace('\n', '')).replace(' ', '')+'\n')
  #                  f.close()
   #                 # time.sleep(random.random()*2)
#

# res = requests.get(url, headers)
# soup = BeautifulSoup(res.content, 'html.parser')
# soup.encode('utf-8')

# print(text_link[0].text.strip())

# f = open(path1, 'w')

