import time
import datetime
import json
import requests
import re
import feedparser
import sys
from pprint import pprint
from config import *

#AUTHTOKEN=fb1d3b5e97836bb98c98d24ba1f0138
#print("TITLE","                                                   ","LINK")
#print("------------------------------------------------------------------")
#
#feed = feedparser.parse( rss_url )
#
#y = len(feed[ "items" ])
##
#
#print (y)
#
#tname = {}
#for x in range(0,y):
#    tname[x] = feed["items"][x][ "title" ]
##    print ()
#    if ('down' in tname[x]):
#        print (tname[x])
#        atext = tname[x]
##    if tname[x] == confirmed_alert:
##        print('It is confirmed alert')
#    

##############################################################

purl = 'https://www.site24x7.com/api/current_status'
pheaders = {'Accept': 'application/json; version=2.0', 'Authorization': AUTHTOKEN}
#headers = {'Accept': 'application/json; version=2.0'}

def get_purl(purl, pheaders):
    url = purl
    headers = pheaders
    response = requests.get(url, headers=pheaders)
    pcontent = response.content.decode("utf8")
    jspcontent = json.loads(pcontent)
    d = len(jspcontent["data"][ "monitors" ])
#    print(d)
    return jspcontent, d

jspcontent, d = get_purl(purl, pheaders)
print(d)

pprint(jspcontent["data"]["monitors"][1][{"name", "status"}]


#atta = {}
#or x in range(0,1):
#   pprint(jspcontent["data"][x]["monitors"])


#print(get_purl(purl, pheaders))

#def get_last_fromsite(updates):
#    num_updates = len(updates["data"]["monitors"])
#    return num_updates

#get_last_fromsite(updates)


#print(num_updates)




##def get_last_fromsite(updates, user):
##    y = len(updates[""])
##    print (y)
##    print('after number')
##    for x in range(0,y):
##        pprint(updates.get('result'))
##        sender = updates['result'][x]['message']['from']['first_name']
##        sender = updates['result'][x]['message']['from']['first_name']
##        print("----------------------") 
##        print('the sender is', sender)
##        print('####afetrsender#####')
##        print('the user is', user)        
##        print('#### Loop end #####')
##        sender.get('first_name')
##        if re.search(r'sender', "{}".format(user)):
##        if re.search(r'"{}".format(user)', sender):
##        if (user == sender):
##            print('inside if')
#            #pprint (updates.get('result').get('message').get('text'))
##            last_message = updates['result'][x]['message']['text']
##            pprint(last_message)
##            print('-------------')
##        else:
##            print(last_message)
##    return last_message
#
#
###############################################################
#
#def get_url(url):
#    response = requests.get(url)
#    content = response.content.decode("utf8")
#    return content
#
#
#def get_json_from_url(url):
#    content = get_url(url)
#    js = json.loads(content)
#    return js
#
#
#def get_updates():
#    url = URL + "getUpdates"
#    js = get_json_from_url(url)
#    return js
#
#
#def get_last_chat_id_and_text(updates):
#    num_updates = len(updates["result"])
#    last_update = num_updates - 1
#    text = updates["result"][last_update]["message"]["text"]
#    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
#    sender = updates["result"][last_update]["message"]["from"]["first_name"]
#    return (text, chat_id, sender)
#
#
#def get_last_from_user(updates, user):
#    y = len(updates["result"])
##    print (y)
##    print('after number')
#    for x in range(0,y):
##        pprint(updates.get('result'))
#        sender = updates['result'][x]['message']['from']['first_name']
##        sender = updates['result'][x]['message']['from']['first_name']
##        print("----------------------") 
##        print('the sender is', sender)
##        print('####afetrsender#####')
##        print('the user is', user)        
##        print('#### Loop end #####')
##        sender.get('first_name')
##        if re.search(r'sender', "{}".format(user)):
##        if re.search(r'"{}".format(user)', sender):
#        if (user == sender):
##            print('inside if')
#            #pprint (updates.get('result').get('message').get('text'))
#            last_message = updates['result'][x]['message']['text']
##            pprint(last_message)
##            print('-------------')
##        else:
##            print(last_message)
#    return last_message
#
##get_last_from_user(get_updates(), "O")
#
#
#user_message = get_last_from_user(get_updates(), "john")
#
#print(user_message)
#
#
#
#
#def send_message(text, chat_id):
#    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
#    get_url(url)
#
#
#####
#
#def get_records():
#    feed = feedparser.parse( rss_url )
#    num_records = len(feed[ "items" ])
#    return (num_records)
#
#def get_alert():
#    feed = feedparser.parse( rss_url )
#    num_records = len(feed[ "items" ])
#    for x in range(0,num_records):
#        reply = feed["items"][x]["title"]
#        if re.search(r'.*down.*', reply):
#            alert = feed["items"][x][ "title" ]
#    return alert
#
#
#def get_watchman():
#    weekNumber = datetime.date.today().isocalendar()[1]
#    print ('Week number:', weekNumber)
#    if ((weekNumber % 2) == 0):
##        print('hello')
#        watchman = "O"
#        watchman_chat = '384016403'
#        reservist = "john"
#        reservist_chat = '543548589'
#    else:
#        watchman = "john"
#        watchman_chat = '543548589'
#        reservist = "O"
#        reservist_chat = '384016403'
#    return (watchman, watchman_chat, reservist, reservist_chat)
#
#    
#
#
#
#
#def main_vars():
#    mytext = 'Prosypaisia'
#    grchat = '-206368020'
#    mychat = '384016403'
#    newchat = '543548589'
#
#mytext = 'Prosypaisia'
#grchat = '-206368020'
#mychat = '384016403'
#newchat = '543548589'
#
#############################################################################
#
#
#
## 1. Start listen - get update from 24x7
#def main():
#    print ('STARTING ...')
#    watchman, watchman_chat, reservist, reservist_chat = (get_watchman())
#    print (watchman, reservist)
#    status = 'not confirmed'
#    print ('Status', status)
#    while status != 'confirmed':
#        num_records = get_records()
#        print (num_records,'haha')
#        print(get_alert())
#
##    If no down, sleep X minutes, go to start
#        if ('down' not in get_alert()):
#            time.sleep(10)
#            main()
#        if ('down' in get_alert()): #confirm or not confirmed
#            print ('upalo')
#            send_message(atext, grchat)
#            print ('poslal v gruppu')
#            print ('zhdu 20 sec')
#            time.sleep(20)
#            last_message = get_last_from_user(get_updates(), watchman)
#            print(get_last_from_user(get_updates(), watchman))
##           text, chat, sender = get_last_chat_id_and_text(get_updates())
#            ##################################################################     
#            if (last_message == 'on call'):
#                send_message(mytext, reservist_chat)
#                print ('poslal v lichnyi naparniku')
#                time.sleep(20)
#                last_message = get_last_from_user(get_updates(), reservist)
#                print(get_last_from_user(get_updates(), reservist))
##                text, chat, sender = get_last_chat_id_and_text(get_updates())
#                print (last_message, "Otvet G2" )
#            ##################################################################
#                if ( (last_message) != 'confirm'):
#                    send_message('kaput', grchat)
#                    #time.sleep(20)
#                    main()
#                else:
#                    acktext = "{} said {} - ok".format(reservist, last_message)
#                    send_message(acktext, grchat)
#                    print ('poslal podtver v grup')
#                    while (last_message != 'on call'):
#                        time.sleep(2)
#                        last_message = get_last_from_user(get_updates(), reservist)
#                    status = 'confirmed'
#                    main()
#            else:
#                acktext = "{} said {} - ok".format(watchman, last_message)
#                send_message(acktext, grchat)
#                print ('poslal podtver v grup')
#                while (last_message != 'on call'):
#                    time.sleep(2)
#                    last_message = get_last_from_user(get_updates(), watchman)
#                status = 'confirmed'
#                main()
#
#
##
#
#
##    If YES down, 
##            wright it to variable
##            if variable confirmed
##            exit
##        else
##            post to group
##            sleep X to check reply
##            get update from guard1
##
##            If reply is "under control"
##               post to group "Guard1 said "undercontrol""
##               mark variable as confirmed
##               exit
##            else
##               post to GUARD2 "variable is down"
##               sleep for X min
##               get update from Guard2
##               If reply is "under control"
##               post to group "Guard2 said "undercontrol""
##               mark variable as confirmed
##               GO to beginning - exit
##               else
##               post to group "NOBODY THERE"
##               GO to beginning - exit
##               exit
##            
##
#
#
#
#
##def main():
###    last_textchat = (None, None)
##    print ('kuku2')
##    count = 1
##    status = 'not confirmed'
##    #while (count < 5):
##    while status != 'confirmed':
##        num_records = get_records()
##        print (num_records,'haha')
##
##        mytext = 'Prosypaisia'
###        acktext = "{} said {} - ok".format(sender, text)
##        grchat = '-206368020'
##        mychat = '384016403'
##        newchat = '543548589'
##        tname = {}
##        for x in range(0,num_records):
##            tname[x] = feed["items"][x][ "title" ]
##            atext = tname[x]
##            #print(atext)
##
##
##            if ('down' in atext):
##                print ('upalo')
##                send_message(atext, grchat)
##                print ('poslal v gruppu')
##                print ('zhdu 10 sec')
##                time.sleep(20)
##                text, chat, sender = get_last_chat_id_and_text(get_updates())
##                if ( (text) == 'on call'):
###and (chat) == mychat ):
##                    send_message(mytext, newchat)
##                    print ('poslal v lichnyi naparniku')
##                    print (text)
##                    time.sleep(20)
##                    text, chat, sender = get_last_chat_id_and_text(get_updates())
##                    print (text)
##                    if ( (text) == 'on call'):
##                        send_message('kaput', grchat)
##                        break
##                else:
##                    acktext = "{} said {} - ok".format(sender, text)
##                    send_message(acktext, grchat)
##                    print ('poslal podtver v grup')
##                    status = 'confirmed'
###                    confirmed_alert = tname
###                else:
##    #                last_textchat = (text, chat)
###                    time.sleep(1.5)
###                    count = count + 1
#
#
#if __name__ == '__main__':
#    main()
#
#
##text, chat = get_last_chat_id_and_text(get_updates())
##send_message(text, chat)
#
##def myget_last_chat_id_and_text(updates):
##    mynum_updates = len(updates["result"])
##    mylast_update = mynum_updates - 1
##    mytext = updates["result"][mylast_update]["message"]["text"]
##    mytext = 'Prosypaisia'
##    mychat_id = updates["result"][mylast_update]["message"]["chat"]["id"]
##    return (mytext, mychat_id)
