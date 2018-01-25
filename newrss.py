import time
import json
import requests

import feedparser
import sys

#if len(sys.argv) < 2:
#    print("USAGE: python feedparse.py <rss feed link>")
#    exit()

#rss_url = sys.argv[1]
rss_url = 'https://www.site24x7.com/sv.do?id=TomG9XHaG6PCbxrHL55MhmA5a8ufEbLgD8vvWmukU2LpnofnY%2B9ibvRH9c1%2BorSW4EftR5DVZx7s%0AWMXEoqXfP%2F6PgJrnHQiJ&rss=true'
print("TITLE","                                                   ","LINK")
print("------------------------------------------------------------------")

feed = feedparser.parse( rss_url )

y = len(feed[ "items" ])



print (y)

#print (feed["items"][1][ "title" ])


for x in range(0,y):
    "tname{}".format(x) = feed["items"][x][ "title" ]
    if ('down' in tname):
        print (tname(x))
#        atext = (tname)
    if tname == confirmed_alert:
        print('It is confirmed alert')
    

#############################################################

TOKEN = "306317133:AAELUg13H13lSOmFiHc_UUmRueJgzy_z8DI"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)



def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    sender = updates["result"][last_update]["message"]["from"]["first_name"]
    return (text, chat_id, sender)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)









def main():
#    last_textchat = (None, None)
    count = 1
    status = 'not confirmed'
    #while (count < 5):
    while status != 'confirmed':
        #text, chat = get_last_chat_id_and_text(get_updates())
        mytext = 'Prosypaisia'
#        acktext = "{} said {} - ok".format(sender, text)
        grchat = '-206368020'
        mychat = '384016403'
        #if (text, chat) != last_textchat:
        for x in range(0,y):
            tname = feed["items"][x][ "title" ]
            if ('down' in tname):
                print ('upalo')
                atext = (tname)
                send_message(atext, grchat)
                print ('poslal v gruppu')
                time.sleep(10)
                text, chat, sender = get_last_chat_id_and_text(get_updates())
                if (text) == 'on call':
                    send_message(mytext, mychat)
                    print ('poslal v lichnyi')
                else:
                    acktext = "{} said {} - ok".format(sender, text)
                    send_message(acktext, grchat)
                    print ('poslal podtver v grup')
                    status = 'confirmed'
                    confirmed_alert = tname
#            else:
    #            last_textchat = (text, chat)
#                time.sleep(1.5)
#                count = count + 1


if __name__ == '__main__':
    main()




#text, chat = get_last_chat_id_and_text(get_updates())
#send_message(text, chat)
#MYTOKEN = "457575840:AAEW_ypqiVRmdEWow05Dqp5Plu27FwWGOEc"
#MYURL = "https://api.telegram.org/bot{}/".format(MYTOKEN)

#def myget_last_chat_id_and_text(updates):
#    mynum_updates = len(updates["result"])
#    mylast_update = mynum_updates - 1
#    mytext = updates["result"][mylast_update]["message"]["text"]
#    mytext = 'Prosypaisia'
#    mychat_id = updates["result"][mylast_update]["message"]["chat"]["id"]
#    return (mytext, mychat_id)



