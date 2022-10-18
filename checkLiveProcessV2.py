import pprint
# from googleapiclient.discovery import build
import optparse
import time
import sys
import os
import sqlite3
from sqlite3 import Error
import re
import threading
import datetime
import random
import json
import psutil
import psycopg2
import string
import subprocess
import urllib.parse
from bs4 import BeautifulSoup
from datetime import timezone
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
try:
    import requests
except ImportError:
    if sys.platform.startswith('linux'):
        print(" please install requests  module in Debian")
        sys.exit(" sudo apt-get install python-requests ")
    else:
        print(" install requets module for python here : https://pypi.python.org/pypi/requests/2.9.1 or try: pip install requests")
        sys.exit()


software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value,
                     OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=100)


name = sys.argv[0].split('/')[-1]
com = 'pgrep -f ' + name

totalQueries = 0

p = subprocess.Popen([com], stdout=subprocess.PIPE, shell=True)
res = p.communicate()[0]

if isinstance(res, bytes):
    res = res.decode("utf-8")
res = [str(x) for x in res.split('\n') if len(x) > 0]


# if len(res) > 0:
#     print('Already running!')
#     print('Exit!')
#     exit()
#     exit()
#     exit()


proxies = {
    'http': 'socks5h://10.72.1.117:9050',
    'https': 'socks5h://10.72.1.117:9050',
}

proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050',
}

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
}

class Response1:
    def __init__(self, code1, text1):
        self.status_code = code1
        self.text = text1


num11 = 10
relsite = 1
safe11 = 'off'
counttreads = 0
lastcomment = 0
prev_numpost = 0
lastip = 0
restTorStart = 0
nowH = 0
relsite = 0
safe11 = 'active'
datelist = ['d', 'w', 'm', 'y']
targetlist = []
visitedUrl = []
alreadyAdded = []

blockThread = False
emptylist = []


targetlist3 = ['xamarin', 'ксамарин', 'ксомарин', 'AppGyver', 'App Gyver', 'Аппгайвер', ' Ionic ', 'PhoneGap', 'Phone Gap', 'Sencha Touch', 'SenchaTouch', 'CodeName One', 'CodeNameOne', 'React Native', 'ReactNative', 'Appcelerator', ' PWA ', ' PWA,', ' PWA.', ' pwa ', ' pwa,', ' pwa.', 'GoodBarber', 'Good Barber', 'Shoutem', 'Swiftic', 'AppInstitute', 'App Institute', 'Appy Pie', 'AppyPie', 'Bizness Apps', 'BiznessApps', 'AppYourself', 'App Yourself', 'Mobile Roadie', 'MobileRoadie', 'AppMachine', 'App Machine', 'Mobincube', 'AppsBuilder', 'Apps Builder', 'MobAppCreator', 'Mob App Creator', 'MobApp Creator',
               'AppMakr', 'App Makr', 'IBuild App', 'IBuildApp', 'BuildFire', 'Build Fire', 'Appery.io', 'Gamesalad', 'Zoho Creator', 'ZohoCreator', 'Zengine', 'Зенджин', 'Taplytics', 'Тэплитикс', 'Salesforce', 'Salesforce1', 'Mobile Roadie', 'MobileRoadie', 'Мобайл Роуди', 'Мобикарт', 'MobiCart', 'Гудбарбер', 'GoodBarber', 'Good Barber', 'GameSalad', 'Game Salad', 'Геймсэлэд', 'EachScape', 'Each Scape', ' Ичскейп ', 'BuildFire', 'Bizness Apps', 'BiznessApps', 'AppNotch', 'App Notch', 'AppMakr', 'App Makr', 'App Machine', 'AppMachine', 'Appery.io', 'AppBuilder', 'App Builder', 'App Factory', 'AppFactory', 'app.cat']


def find_phrases2(filename, phrases):
    with open(filename) as file:
        str1 = file.read()
        if len(str1) == 0:
            return False
        text = '\n'.join(str1.split())
    start = text.find(phrases)
    if start == -1:
        return False
    else:
        return True


def find_phrases(filename, phrases):
    with open(filename) as file:
        str1 = file.read()
        if len(str1) == 0:
            return False
        text = ' '.join(str1.split())
    start = text.find(phrases)
    if start == -1:
        return False
    else:
        return True



def getip():

    try:
        r45 = requests.get('https://ident.me', proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return Response1("201", '')

    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return Response1("201", '')
    except requests.ConnectionError:
        print("Can't connect to the site, sorry")
        return Response1("201", '')

    print(r45.text)

    return r45



global time1lastrestart1
time1lastrestart1 = datetime.datetime.now()



def restartTor(sec=0,torWath=3, forc1=False):
    #return False# comment it later
    
    if not forc1:
        global time1lastrestart1
        diff1 = (datetime.datetime.now()-time1lastrestart1).seconds
        if diff1 < 120: #torWath:
            return 0

    #subprocess.run(["brew", "services", "restart", "tor"])
    #subprocess.run(["brew", "services", "reload", "tor"])
    subprocess.run(["pkill", "-HUP", "tor"])
    time1lastrestart1 = datetime.datetime.now()

    if sec == 0:
        sec = 0.001
    time.sleep(sec)


def getCountryCode(ip=''):

    try:
        r45 = requests.get('https://freegeoip.app/json/' +
                           str(ip), proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return 0

    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return 0
    except requests.ConnectionError:
        print("Can't connect to the site, sorry")
        return 0

    print(r45.text)
    d = json.JSONDecoder()
    rval = d.decode(r45.text)
    countryCode = rval['country_code']

    return countryCode


def switchProxyIfNeedForCountry():
    while getCountryCode(getip().text) != 'RU':
        restartTor()


def switchProxyIfNeedForGoogle():
    while google() != '200':
        restartTor()


def switchProxyIfNeed(target, targetlist3):
    if target not in targetlist3:
        while getCountryCode(getip().text) != 'RU' and google() != '200' and random.randint(1, 10) > 1:
            restartTor()
    getCountryCode(getip().text)


def google():
    q = 'mobsted'
    randUa = user_agent_rotator.get_random_user_agent()
    headersget = {

        'User-Agent': randUa,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    try:
        r = requests.get(url, headers=headersget,
                         proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return '201'

    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return '201'


    print('google target :'+str(r.status_code))
    return str(r.status_code)










def find_all(a_str, sub):
    a_str = a_str.lower()
    sub = sub.lower()
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)








def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn




    

        


   



def updateProtocol(site0,site16,protocol,siteData1):
    print('protocol "',protocol,'"; tryes "',site16,'"; ',siteData1)
    
    try:
        for x in range(0, 999):
            try:
                    conpg = psycopg2.connect(database=pgdb, user=pguser, password=pgpswd,
                            host=pghost, port=pgport) # , options=f'-c search_path={pgschema}'
            except:
                time.sleep(0.2)
                pass
            finally:
                break

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                sql = " Set search_path =%(pgdb)s "
                params={"pgdb":pgdb}
                curpg.execute(sql,params)
                # conpg.commit()

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
              if len(protocol)>0:
                sql = " Update projects set protocol=%(protocol)s where id=%(id)s and protocol='' "
                params={"protocol":protocol,"id":site0}
                curpg.execute(sql,params)
                # conpg.commit()

            #   for x in range(0, 99):
            #     try:
            #         curpg.execute(sql,params)
            #         conpg.commit()
            #     except:
            #         time.sleep(1)
            #         pass
            #     finally:
            #         break
              if protocol!='https://' and protocol!='http://':
                if site16=='None':
                  site16='0'
                sql = " Update projects set tryesnotproxy=%(tryesnotproxy)s where id=%(id)s"
                params={"tryesnotproxy":int(str(site16 or 0))+1,"id":site0}
                curpg.execute(sql,params)
                print('protocol update - ',int(str(site16 or 0)),'  ',siteData1)
                # conpg.commit()

                # for x in range(0, 99):
                #     try:
                #         curpg.execute(sql,params)
                #         conpg.commit()
                #     except:
                #         time.sleep(1)
                #         pass
                #     finally:
                #       break

                if False and int(str(site16 or 0))>1777:#10
                    sql = " Update projects set statussite=%(statussite)s where id=%(id)s"
                    params={"statussite":'not work',"id":site0}
                    curpg.execute(sql,params)
                    # # 

                    # for x in range(0, 99):
                    #     try:
                    #         curpg.execute(sql,params)
                    #         conpg.commit()
                    #     except:
                    #         time.sleep(1)
                    #         pass
                    #     finally:
                    #         break
                conpg.commit()
    except psycopg2.DatabaseError as e:
        print('Error %s' % e)

        


    



 

def fromBase():
    try:
        conpg = psycopg2.connect(database=pgdb, user=pguser, password=pgpswd,
                                host=pghost, port=pgport) # , options=f'-c search_path={pgschema}'
        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                sql = " Set search_path =%(pgdb)s "
                params={"pgdb":pgdb}
                curpg.execute(sql,params)
                # conpg.commit()

        curpg = conpg.cursor(name='foo145live')
        
        #      with conpg.cursor(name='foo') as curpg:
        curpg.itersize = 100000
        print('request')
        sql = "SELECT * FROM projects where statussite is null and protocol='' and tryesnotproxy is null order by id desc limit 100000 " #  where not inprogress or inprogress is null
        curpg.execute(sql)

        # print('return')
        # return curpg

        print('fetchall')
        res1 = curpg.fetchall()
        print('end fetchall')
        curpg.close()
        conpg.close()
        return res1
    except psycopg2.DatabaseError as e:
        print('Error %s' % e)

def check_lives(siteData0,siteData1,siteData16):
        # print(siteData0)
        # print(siteData1)
        # print(siteData16)
        # exit()
        #datetime.datetime.now()
        # time.sleep(1/random.randint(1,1000000))
        # time.sleep(random.uniform(0, 1))
        p = psutil.Process(os.getpid())
        p.nice(4)

        rtext = makeGetRequest('https://'+str(siteData1), 'https://'+str(siteData1))
        if rtext is None:
            rtext = makeGetRequest('http://'+str(siteData1), 'http://'+str(siteData1))
            if rtext is None:
                # print('die site - ',siteData)
                updateProtocol(siteData0,siteData16,'',siteData1)
            else:
                updateProtocol(siteData0,siteData16,'http://',siteData1)
        else:
            updateProtocol(siteData0,siteData16,'https://',siteData1)

        
           

def makeGetRequest(url, main, nproxy=False):

    rtext = None
    # str1, str2, *_ = main.split('//')
    useTor = True
    # else:
    #  str2=main
    # if url.find(str2) == -1:
    #     return None
    # global visitedUrl
    # if str(url) in visitedUrl:
    #     return None
    # visitedUrl.append(url)
    # print(url)
    counttryes = 0
    while True:
        useTor = True
        r = Response1("0", '')
        counttryes = counttryes+1
        if counttryes > 2:
            return None
        if counttryes > 1:
            nproxy = not nproxy
        try:
            randUa = user_agent_rotator.get_random_user_agent()

            if not nproxy:
             useTor = False
            #  print('useTor',useTor)
             r = requests.get(url, headers={
                'origin': url,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cache-control': 'no-cache',
                'user-agent': randUa
             }, timeout=10, allow_redirects=True)
            else:
            #  print('useTor',useTor)
             r = requests.get(url, headers={
                'origin': url,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cache-control': 'no-cache',
                'user-agent': randUa
             }, proxies=proxies, timeout=10, allow_redirects=True)


            # r = requests.get(url, headers={
            # 'origin': url,
            # 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'user-agent': randUa
            # }, timeout=1, allow_redirects=True)

            if r.history:
                # print("Request was redirected")
                # for resp in r.history:
                #     print(resp.status_code, resp.url)
                # print("Final destination:")
                # print(r.status_code, r.url)
                return makeGetRequest(r.url,main, nproxy)
            # else:
            #     print("Request was not redirected")
            
            rtext = r.text
            r.close()
        except requests.ConnectionError as e:
            # print("[-] host die  ConnectionError: "+str(e))
            if useTor:
             restartTor()

            continue
        except requests.HTTPError as e:
            print("[-] host die  HTTPError: "+str(e))
            if useTor:
             restartTor()

            continue
        except requests.exceptions.ConnectTimeout as e:
            print("[-] host die  ConnectTimeout: "+str(e))
            if useTor:
             restartTor()

            continue
        except requests.exceptions.ReadTimeout as e:
            # print("[-] host die  ReadTimeout: "+str(e))
            if useTor:
             restartTor()

            continue
        except requests.exceptions.Timeout as e:
            print("[-] host die  Timeout: "+str(e))
            if useTor:
             restartTor()

            continue
        except requests.exceptions.TooManyRedirects as e:
            print("[-] host die TooManyRedirects: "+str(e))
            if useTor:
             restartTor()

            continue
        except requests.exceptions.RequestException as e:
            if (str(str(e))).find('Failed to parse:') != -1:
                continue
        except:
            if useTor:
             restartTor()
            continue


        if int(r.status_code) != 200:
            if useTor:
             restartTor()
            continue
     
        return rtext



pgdb = 'great_paraser'
pguser = 'postgres'
pgpswd = 'blabla'
pghost = '0.1.1.1'
pgport = '6432'
pgschema = 'great_paraser'
max_process_count = 399
if True:
    # rtext = makeGetRequest('http://ident.me', 'http://ident.me', False)
    # print(rtext)
    # if rtext:
    #     print('!!!!!!!!!')
    # rtext = makeGetRequest('https://ident.me', 'https://ident.me', False)
    # print(rtext)
    # if rtext:
    #     print('!!!!!!!!!')
    # rtext = makeGetRequest('http://ident.me', 'http://ident.me', True)
    # print(rtext)
    # if rtext:
    #     print('!!!!!!!!!')
    # rtext = makeGetRequest('https://ident.me', 'https://ident.me', True)
    # print(rtext)
    # if rtext:
    #     print('!!!!!!!!!')

    
    # exit()

    p = psutil.Process(os.getpid())
    p.nice(4)
    # siteData = sys.argv[1]
    # siteData2 = sys.argv[2]
    # siteData3 = sys.argv[3]
    # # restartTor(0,3,True)
    # # print(sys.argv)
    # # time.sleep(10)
    # check_lives(siteData, siteData2, siteData3, datetime.datetime.now())

    siteGen = sys.argv
    siteGen.pop(0)
    # print(siteGen)
    # print(siteGen[0])
    # print(siteGen[1])
    # siteGen1 = eval(siteGen[0])
    # print(siteGen1[0])
    # print(siteGen1[1])
    
    # exit()



    restartTor(0,3,True)
    if True:
        # threading.stack_size(64*1024)
        # siteGen = fromBase()
        # print(len(siteGen))
        for siteData in siteGen:
            # if(random.randint(1, 99) == 1):
            #   psLoad = psutil.cpu_percent()
            #   while int(psLoad)>85 and psLoad!='0.0':
            #     print(' - psutil.cpu_percent() ',int(psLoad))
            #     print(' - psutil.cpu_percent() ',str(psLoad))
            #     time.sleep(60)
            #     psLoad = psutil.cpu_percent()
            # continue
            # (id,          site,            protocol,   torWath,  diffTimeProcess,  depthSite,  enddate,  hasSW,  hasMan,  resText,  resJson,  resOver,  inprogress,  fixed,  tryesproxy,  statussite,  tryesnotproxy,  startdate)
            # (209029934, 'thecurlyfugu.com', 'http://',    2,       8,                 1,         None,   None,   None,     None,     None,     None,       None,      None,    None,          None,         None,        None)
            # (0,                 1,              2,        3,       4,                 5,           6,      7,      8,       9,        10,       11,        12,        13,       14,            15,           16,         17)
            if True:

                if(random.randint(1, 399) == 1):
                    print(str(threading.active_count())+' - threading.active_count()')
                    # print(getip())

                while threading.active_count() > max_process_count:
                    if(random.randint(1, 99) == 1):
                     print(' - timewait')
                    time.sleep(0.2)

         
                    
                siteData1 = eval(siteData)
                thread = threading.Thread(
                    target=check_lives, args=(siteData1[0], siteData1[1], siteData1[2]))
                thread.daemon = True
                thread.start()
        print('end of for')
        time.sleep(120)

# while threading.active_count() > 1:
#     print('--')
#     time.sleep(10)
# print('exit')

                

