import time
import json
import requests
import re
import feedparser
import sys
from pprint import pprint
from config import *

print("TITLE","                                                   ","LINK")
print("------------------------------------------------------------------")

feed = feedparser.parse( rss_url )

y = len(feed[ "items" ])
#

print (y)

tname = {}
for x in range(0,y):
    tname[x] = feed["items"][x][ "title" ]
#    print ()
    if ('down' in tname[x]):
        print (tname[x])
        atext = tname[x]
#    if tname[x] == confirmed_alert:
#        print('It is confirmed alert')
    

#############################################################


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


def get_last_from_user(updates, user):
    y = len(updates["result"])
#    print (y)
#    print('after number')
    for x in range(0,y):
#        pprint(updates.get('result'))
        sender = updates['result'][x]['message']['from']['first_name']
#        sender = updates['result'][x]['message']['from']['first_name']
#        print("----------------------") 
#        print('the sender is', sender)
#        print('####afetrsender#####')
#        print('the user is', user)        
#        print('#### Loop end #####')
#        sender.get('first_name')
#        if re.search(r'sender', "{}".format(user)):
#        if re.search(r'"{}".format(user)', sender):
        if (user == sender):
#            print('inside if')
            #pprint (updates.get('result').get('message').get('text'))
            last_message = updates['result'][x]['message']['text']
#            pprint(last_message)
#            print('-------------')
#        else:
#            print(last_message)
    return last_message

#get_last_from_user(get_updates(), "O")


user_message = get_last_from_user(get_updates(), "john")

print(user_message)




def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


####

def get_records():
    feed = feedparser.parse( rss_url )
    num_records = len(feed[ "items" ])
    return (num_records)

def get_alert():
    feed = feedparser.parse( rss_url )
    num_records = len(feed[ "items" ])
    for x in range(0,num_records):
        reply = feed["items"][x]["title"]
        if re.search(r'.*down.*', reply):
            alert = feed["items"][x][ "title" ]
    return alert







def main_vars():
    mytext = 'Prosypaisia'
    grchat = '-206368020'
    mychat = '384016403'
    newchat = '543548589'

#mytext = 'Prosypaisia'
#grchat = '-206368020'
#mychat = '384016403'
#newchat = '543548589'

############################################################################



# 1. Start listen - get update from 24x7
def main():
    print ('STARTING ...')
    status = 'not confirmed'
    print ('Status', status)
    while status != 'confirmed':
        num_records = get_records()
        print (num_records,'haha')
        mytext = 'Prosypaisia'
        grchat = '-206368020'
        mychat = '384016403'
        newchat = '543548589'
        print(get_alert())

#    If no down, sleep X minutes, go to start
        if ('down' not in get_alert()):
            time.sleep(10)
            main()
        if ('down' in get_alert()): #confirm or not confirmed
            print ('upalo')
            send_message(atext, grchat)
            print ('poslal v gruppu')
            print ('zhdu 20 sec')
            time.sleep(20)
            last_message = get_last_from_user(get_updates(), "O")
            print(get_last_from_user(get_updates(), "O"))
#           text, chat, sender = get_last_chat_id_and_text(get_updates())
            if ( (last_message) == 'on call'):
                send_message(mytext, newchat)
                print ('poslal v lichnyi naparniku')
                time.sleep(20)
                last_message = get_last_from_user(get_updates(), "john")
                print(get_last_from_user(get_updates(), "john"))
                #print()
                #last_message = get_last_from_user(get_updates(), "mymy")
#                text, chat, sender = get_last_chat_id_and_text(get_updates())
                print (last_message, "Otvet G2" )
                if ( (last_message) == 'na podhvate'):
                    send_message('kaput', grchat)
                    #time.sleep(20)
                    main()
                else:
                    acktext = "{} said {} - ok".format(sender, text)
                    send_message(acktext, grchat)
                    print ('poslal podtver v grup')
                    status = 'confirmed'
                    main()
                
            else:
                acktext = "{} said {} - ok".format(sender, text)
                send_message(acktext, grchat)
                print ('poslal podtver v grup')
                status = 'confirmed'
                main()
#                confirmed_alert = tname
#            else:
    #            last_textchat = (text, chat)
#                time.sleep(1.5)
#                count = count + 1







#    If YES down, 
#            wright it to variable
#            if variable confirmed
#            exit
#        else
#            post to group
#            sleep X to check reply
#            get update from guard1
#
#            If reply is "under control"
#               post to group "Guard1 said "undercontrol""
#               mark variable as confirmed
#               exit
#            else
#               post to GUARD2 "variable is down"
#               sleep for X min
#               get update from Guard2
#               If reply is "under control"
#               post to group "Guard2 said "undercontrol""
#               mark variable as confirmed
#               GO to beginning - exit
#               else
#               post to group "NOBODY THERE"
#               GO to beginning - exit
#               exit
#            
#




#def main():
##    last_textchat = (None, None)
#    print ('kuku2')
#    count = 1
#    status = 'not confirmed'
#    #while (count < 5):
#    while status != 'confirmed':
#        num_records = get_records()
#        print (num_records,'haha')
#
#        mytext = 'Prosypaisia'
##        acktext = "{} said {} - ok".format(sender, text)
#        grchat = '-206368020'
#        mychat = '384016403'
#        newchat = '543548589'
#        tname = {}
#        for x in range(0,num_records):
#            tname[x] = feed["items"][x][ "title" ]
#            atext = tname[x]
#            #print(atext)
#
#
#            if ('down' in atext):
#                print ('upalo')
#                send_message(atext, grchat)
#                print ('poslal v gruppu')
#                print ('zhdu 10 sec')
#                time.sleep(20)
#                text, chat, sender = get_last_chat_id_and_text(get_updates())
#                if ( (text) == 'on call'):
##and (chat) == mychat ):
#                    send_message(mytext, newchat)
#                    print ('poslal v lichnyi naparniku')
#                    print (text)
#                    time.sleep(20)
#                    text, chat, sender = get_last_chat_id_and_text(get_updates())
#                    print (text)
#                    if ( (text) == 'on call'):
#                        send_message('kaput', grchat)
#                        break
#                else:
#                    acktext = "{} said {} - ok".format(sender, text)
#                    send_message(acktext, grchat)
#                    print ('poslal podtver v grup')
#                    status = 'confirmed'
##                    confirmed_alert = tname
##                else:
#    #                last_textchat = (text, chat)
##                    time.sleep(1.5)
##                    count = count + 1


if __name__ == '__main__':
    main()




#text, chat = get_last_chat_id_and_text(get_updates())
#send_message(text, chat)

#def myget_last_chat_id_and_text(updates):
#    mynum_updates = len(updates["result"])
#    mylast_update = mynum_updates - 1
#    mytext = updates["result"][mylast_update]["message"]["text"]
#    mytext = 'Prosypaisia'
#    mychat_id = updates["result"][mylast_update]["message"]["chat"]["id"]
#    return (mytext, mychat_id)



