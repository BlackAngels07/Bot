# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile


acil = LINETCR.LINE()
acil.login(token="ExwxR6OYNxWPaILRS6Ga.FrRaFsa2S2DfEdOkgzkYUG.sUV2MX76CGMR1L25itnWq1yaZeUKdV6tNTxzZwIbrX8=")
acil.loginResult()
ki = LINETCR.LINE()
ki.login(token="Ex2ATUwiY1KiindBtdj5.VxTn0rMR1ZQZ31qVTyQkzq.OCpCNK+PN8Em8TUBS+4mz8Uk6NhwpKnpOPhH7Fs+6ew=")
ki.loginResult()
ki2= LINETCR.LINE()
ki2.login(token="ExFDaktPpA63s65Hbnm7.oISUxqs9khqTd3kgBWDsDW.rt9sZ9i/Cdou1dt6DZTlgkd5PTH2RSlDGey89OoWu40=")
ki2.loginResult()
ki3 = LINETCR.LINE()
ki3.login(token="Ex6yaYYsQN9hyEwtZDMb.1ukj8Siz/gtoFdNrOJRlAW.Oy05gRgkCUVj3fapFE8it+JP0KIAgi32l8XT0uZjUmo=")
ki3.loginResult()
ki4 = LINETCR.LINE()
ki4.login(token="ExGXT1DdiJRKR769c4De.GKij/8O+6pnVT3oKPvap7G.TMwsadVJcKShG0Ra8kay1thXRlI3mi+xcbC6T4E/ZXI=")
ki4.loginResult()
ki5 = LINETCR.LINE()
ki5.login(token="ExhrQAN6xkEZ51NpIcLf.kIk3M0DLMRUyv22aWQdj7W.1PGHUqtw7Vy5W/asO9wt8hCuLVrAnznPhEg2RZBTJfo=")
ki5.loginResult()
ki6 = LINETCR.LINE()
ki6.login(token="ExH1bU9VtFnuxpybADe4.OE0oAskQDWeU8YTg5zp4La.8U9rQsUR/1ZkAgTLPKuF2SH9lY2udX1vRLtL9ErZsAM=")
ki6.loginResult()
ki7 = LINETCR.LINE()
ki7.login(token="Exe8TcBtmIUuLcKwUzC9.6I4D+Keff6FXvjs++YJD/q.wWta6X5MBFXX4u46KbuXzjtjAS9goX+pG43ar7w0fpU=")
ki7.loginResult()
ki8 = LINETCR.LINE()
ki8.login(token="Ex2KQRtIys1KzpTSeUj2.1v9/yQDHECuVVcxT7egdmG.WHUpnK93MJq5heMEbtmZ5xnPnpJsyB0EicXDT/+mLQo=")
ki8.loginResult()
ki9 = LINETCR.LINE()
ki9.login(token="ExO3E8IYoy91iAPVKflc.vTKNHqTqtEpwe1grUOEb+a.CTMcQnVn+lwqAdCSMZ+RHutCm2C98y75m/9xJO0HrJc=")
ki9.loginResult()
ki10 = LINETCR.LINE()
ki10.login(token="ExdDbBcxS3M9prkDIoEf.i27A4rVcSmzCc9ssw/8BFW.CXiYdPaEaVFsqzyZ9/q4Nr2iL6hRI7BA1aQRSIgnwy4=")
ki10.loginResult()
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage="""
TEAM ELITE......
༺࿇˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏𖤓˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋࿇༻
༺࿇      ཫ ⃕ᙩℒᴀⳟᴋ_Ꭿⴄℊℯℒʂ⃕ ཀ      ࿇༻
༺࿇˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏𖤓˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋࿇༻
༺Me
༺Add
༺Gift
༺Spam gift️
༺Cn "text"
༺Clockname "text"
༺TL:"text"
༺Ban:"mid"
༺Unban:"mid"
༺Bl:on
༺Unbl:on
༺Mcheck
༺Mybio:
༺Mybots
༺Mymid
༺Mygroups
༺Group id
༺Message set:"text"
༺Message confirm
༺Msg add-"text"
༺Com set:"text"
༺Comment
༺Comban/del/cek
༺Help set:"text"
༺Change
༺Gn "text"
༺Clink/Curl
༺Kick:"mid"
༺Invite:"mid"
༺Creator
༺Gcancel:"jumlah"
༺Gcancelall
༺Ginfo
༺Check
༺Cctv
༺Glink
༺Spam on/off
༺Gurl
༺Clink
༺Blocklist
༺Banlist
༺Update
༺Creator
༺Sc:"mid"
༺Ban "@"
༺Unban "@"
༺Sc @
༺Nuke
༺Backup
༺Tagall
༺Kick@mbl 
༺Reinvite
༺Conban
༺Clearban
༺Gid
༺Grupname
༺ Lurk:on/off
༺Lurkers
༺Wc️
༺Sp
༺Stafflist
༺Reboot
༺Leaveallgroup
༺Pmfavorite
༺Broken
༺Youtube *text*
༺Youtubesearch *user*
༺Audio "text"
༺Lirik "text"
༺Ig "name"
༺Tts "judul/nama band"
༺Gimage 
༺Image *text*
༺Google *text*
༺Micadd @
༺Micdel @
༺Miclist
༺Picturl @
༺Coverurl @
༺Copy @
༺Getname @
༺Getinfo @
༺pict @️
༺Getcontact @
༺Getvid @
༺Getmid @
༺Copy @     
༺Recopy
༺Getcover @    
༺Getbio @
༺Getinfo @
༺youinfo @
༺info "mid"
༺Contact "mid"
༺Id "idline"
༺Memlist
༺Setimage:
༺Papimage
༺Setvideo:
༺Papvideo
༺Checkdate
༺Myname
༺Mybio
༺Mypict
༺Myvid
༺Urlpict
༺Mycover
༺Urlcover
༺༺Hay "text"
༺Record "text"
༺Xvideo "text"
༺Smule "id smule"
༺Time
༺Imagetxt "text"
༺Cuaca*txt
༺Lokasi*txt
༺Shalat*txt
༺Anime"text"
༺Cekmovie"text"
༺Video"text"
༺Playstore"txt"
༺Twitter*txt
༺Klip"text"
༺༺Github*txt
༺Facebook*txt
༺Wikipedia*txt
༺Checkdate*ttl
༺Virus
༺sendpm "text"
༺sendgrup "text"
༺sider:*txt*
༺tagme:*txt
༺welcome:*txt
༺left:*txt
༺message set:*txt*
༺STKID:*sticker id
༺STKPKGID:*stkr gid
༺STKVER:*version
༺cekresponse
༺Fuck1/10 "@"
༺Kick1/10 "@"
༺All mid
༺Reinvite
༺B1-10 mid
༺༺B1-10name "text"
༺B1-10
༺B1-10 gift
༺B1-10 in
༺B1-10 bye
༺Bc "text"
༺Say "text"
༺Bom "text"
༺Allgift
༺Spam gift️
༺Botcopy
༺Botbackup
༺Botpict
༺Botcover
༺Botak
༺Allname "nama"
༺Allbio "status"
༺Sendcontact "text"
༺Botbyeall  
༺Ban:on/Unbl:on
༺Contact:on/off
༺Add:on/off
༺Join:on/off
༺Leave:on/off
༺Share:on/off
༺Com:on/off
༺Clock:on/off
༺Respon:on/off
༺Stickertag:on/off
༺Welcome:on/off
༺Left:on/off
༺Sider:on/off
༺Notag:on/off
༺Mimic on/off
༺Simsimi:on/off
༺Read:0n/off
༺Like:on/off
༺Runtime
༺Pro:on/off
༺༺Prolink:on/off
༺Proinvite:on/off
༺Procancel:on/off
༺Namelock:on/off
༺Projoin:on/off
༺Protect:on/off
༺࿇˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏𖤓˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋࿇༻
༺{  Media  }
༺{Translate}
༺{    Set   }
༺{Helpbots}
༺{Settings}
༺{Setauto}
༺࿇˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏˶̏𖤓˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋˵̋࿇༻
"""
translateMessage ="""
╔══════════
║(╣℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́ ̰в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╣)
║╔═════════
║══════════
║✰║ Afrika/
║✰║ Albanian/
║✰║ Arab/
║✰║ Armenian/
║✰║ Bengali/
║✰║ Catalan/
║✰║ Chinese/
║✰║ Croatian/
║✰║ Czech/
║✰║ Danish/
║✰║ Dutch/
║✰║ English/
║✰║ Australia/
║✰║ Uk/
║✰║ Us/
║✰║ Esperanto/
║✰║ Finnish/
║✰║ French/
║✰║ German/
║✰║ Greek/
║✰║ Hindi/
║✰║ Hungarian/
║✰║ Icelandic/
║✰║ Indonesia/
║✰║ Italia/
║✰║ Japanese/
║✰║ Khmer/
║✰║ Korean/
║✰║ Latin/
║✰║ Latvian/
║✰║ Macedonian/
║✰║ Malaysia/
║✰║ Norwegian/
║✰║ Polish/
║✰║ Portuguese/
║✰║ Romanian/
║✰║ Russian/
║✰║ Sarbian/
║✰║ Sinhala/
║✰║ Slovak/
║✰║ Spanish/
║✰║ Spain/
║✰║ Swadhili/
║✰║ Swedish/
║✰║ Tamil/
║✰║ Thai/
║✰║ Turki/
║✰║ Ukrainian/
║✰║ Vietnam/
║✰║  Welsh/
║╩═══NEXT PAGE═╦
║🃏║ ✰ {  Media  }
║🇲🇨║ ✰ {Translate}
║⚙️║ ✰ {    Set   }
║🏴║ ✰ {Helpbots}
║🔧║ ✰ {Settings}
║🔛║ ✰ {Setauto}
╚══╩══════╝
"""
KAC=[acil,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
mid = acil.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid]
admsa = "u7d1ac07d2036b36745783a0a1992b2ba"
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'tagme':"message tag belum di set",
    'sider1':"message sider belum di set",
    'joingc':"message member join belum di set",
    'leftgc':"Papaii...",
    "stickerMention":False,
    'message':"""Auto Like By:\n【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n  http://line.me/ti/p/~avrilia_ganteng\n\n. . . . . . . . . . .*. . . . . . . ** *\n. . . . .. . . . . .*** . . * . . *****\n. . . . . . . . . . .** . . **. . . . .*\n. . . . . . . . . . ***.*. . *. . . . .*\n. . . . . . . . . .****. . . .** . . . ******\n. . . . . . . . . ***** . . . .**.*. . . . . **\n. . . . . . . . .*****. . . . . **. . . . . . *.**\n. . . . . . . .*****. . . . . .*. . . . . . *\n. . . . . . . .******. . . . .*. . . . . *\n. . . . . . . .******* . . .*. . . . .*\n. . . . . . . . .*********. . . . . *\n. . . . . . . . . .******* . ***\n*******. . . . . . . . .**\n.*******. . . . . . . . *\n. ******. . . . . . . . * *\n. .***. . *. . . . . . .**\n. . . . . . .*. . . . . *\n. . . . .****.*. . . .*\n. . . *******. .*. .*\n. . .*******. . . *.\n. . .*****. . . . *\n. . .**. . . . . .*\n. . .*. . . . . . **.*\n. . . . . . . . . **\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . *\n. . . . . . . . *\n▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄""",
    "lang":"JP",
    "comment":"Thx For Add Me (^_^)\nInvite Me To Your Group...!!!\n\n╔═──────┅═ই۝ई═┅──────\n_░▒███████\n░██▓▒░░▒▓██\n██▓▒░__░▒▓██___██████\n██▓▒░____░▓███▓__░▒▓██\n██▓▒░___░▓██▓_____░▒▓██\n██▓▒░_______________░▒▓██\n_██▓▒░______________░▒▓██\n__██▓▒░____________░▒▓██\n___██▓▒░__________░▒▓██\n____██▓▒░________░▒▓██\n_____██▓▒░_____░▒▓██\n______██▓▒░__░▒▓██\n_______█▓▒░░▒▓██\n_________░▒▓██\n_______░▒▓██\n_____░▒▓██\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n  http://line.me/ti/p/~avrilia_ganteng\n\n. . . . . . . . . . .*. . . . . . . ** *\n. . . . .. . . . . .*** . . * . . *****\n. . . . . . . . . . .** . . **. . . . .*\n. . . . . . . . . . ***.*. . *. . . . .*\n. . . . . . . . . .****. . . .** . . . ******\n. . . . . . . . . ***** . . . .**.*. . . . . **\n. . . . . . . . .*****. . . . . **. . . . . . *.**\n. . . . . . . .*****. . . . . .*. . . . . . *\n. . . . . . . .******. . . . .*. . . . . *\n. . . . . . . .******* . . .*. . . . .*\n. . . . . . . . .*********. . . . . *\n. . . . . . . . . .******* . ***\n*******. . . . . . . . .**\n.*******. . . . . . . . *\n. ******. . . . . . . . * *\n. .***. . *. . . . . . .**\n. . . . . . .*. . . . . *\n. . . . .****.*. . . .*\n. . . *******. .*. .*\n. . .*******. . . *.\n. . .*****. . . . *\n. . .**. . . . . .*\n. . .*. . . . . . **.*\n. . . . . . . . . **\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . *\n. . . . . . . . *\n▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█\n╚═────────┅═ই۝ई═┅─────────",
    "comment1":"",
    "commentOn":True,
    "likeOn":True,
    "wcOn":False,
    "leftOn":False,
    "alwayRead":False,
    "Removechat":False,
    "detectMention":False,    
    "kickMention":False,
    "cpp":True,
    "steal":False,
    'pap':{},
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":True,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "atjointicket":True,
    "potoMention":{},
    "prankName":False,
    "Sider":{},
    "cyduk":{},
    "pname":{},
    "pro_name":{},
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
settings = {
    "simiSimi":{}
    }
res = {
    'num':{},
    'us':{},
    'au':{},
    }
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
setTime = {}
setTime = wait2['setTime']
 
contact = acil.getProfile()
mybackup = acil.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup = ki2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki3.getProfile()
backup = ki3.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki4.getProfile()
backup = ki4.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki5.getProfile()
backup = ki5.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def tagall(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "⚚ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "⛥Mention⛦\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
      cl.sendMessage(msg)
    except Exception as error:
      print error
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error 
#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=1):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('http://obs-jp.line-apps.com/oa/album/a/object_info.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Success')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Success')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('http://obs-jp.line-apps.com/oa/album/a/object_info.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Success')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Success')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Success')
       

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=1):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = acil.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            acil.rejectGroupInvitation(op.param1)
                        else:
                            acil.acceptGroupInvitation(op.param1)
			    G.preventJoinByTicket = False
			    acil.updateGroup(G)
			    Ticket = acil.reissueGroupTicket(op.param1)
			    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			    G.preventJoinByTicket = True
			    acil.updateGroup(G)
                    else:
                        acil.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        acil.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace(" ",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                acil.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                acil.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            acil.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = acil.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            acil.updateGroup(G)
                        except:
                            acil.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    acil.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                acil.like(url[25:58], url[66:], likeType=1001)
                ki.like(url[25:58], url[66:], likeType=1001)
                ki2.like(url[25:58], url[66:], likeType=1001)
                ki3.like(url[25:58], url[66:], likeType=1001)
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki5.like(url[25:58], url[66:], likeType=1001)
                ki6.like(url[25:58], url[66:], likeType=1001)
                ki7.like(url[25:58], url[66:], likeType=1001)
                ki8.like(url[25:58], url[66:], likeType=1001)
                ki9.like(url[25:58], url[66:], likeType=1001)
                ki10.like(url[25:58], url[66:], likeType=1001)
                acil.comment(url[25:58], url[66:], wait["comment1"])
                ki.comment(url[25:58], url[66:], wait["comment1"])
                ki2.comment(url[25:58], url[66:], wait["comment1"])
                ki3.comment(url[25:58], url[66:], wait["comment1"])
                ki4.comment(url[25:58], url[66:], wait["comment1"])
                ki5.comment(url[25:58], url[66:], wait["comment1"])
                ki6.comment(url[25:58], url[66:], wait["comment1"])
                ki7.comment(url[25:58], url[66:], wait["comment1"])
                ki8.comment(url[25:58], url[66:], wait["comment1"])
                ki9.comment(url[25:58], url[66:], wait["comment1"])
                ki10.comment(url[25:58], url[66:], wait["comment1"])
#-----------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = acil.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = ki2.getGroup(op.param1)
                            except:
                                try:
                                    G = ki3.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki4.getGroup(op.param1)
				    except:
					try:
                                            G = ki5.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        acil.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                ki2.updateGroup(G)
                            except:
                                try:
                                    ki3.updateGroup(G)
                                except:
                                    try:
                                        ki4.updateGroup(G)
                                    except:
                                        try:
                                            ki5.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ki.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                acil.sendText(msg.to, "🤠" + data['result']['response'].encode('utf-8'))
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['detectMention'] == True:
                     contact = acil.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  acil.sendImageWithURL(msg.to,ret_)
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': msg.from_}
                                  acil.sendMessage(msg)
                                  acil.sendText(msg.to, wait["tagme"])
                                  break
            if "MENTION" in msg.contentMetadata.keys() != None:
            	if wait['stickerMention'] == True:
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                           	msg.contentType = 7
                           	msg.text = ''
                           	msg.contentMetadata = {
                                                  	   'STKPKGID': 1,
                                                  	   'STKTXT': '[]',
                                                  	   'STKVER': 100,
                                                  	   'STKID':110 
                                              		 }
                           	acil.sendText(msg.to, wait["tagme"])
                           	acil.sendMessage(msg)
                           	break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = acil.getContact(msg.from_)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in mid:
                                  acil.sendText(msg.to,"don't tag me")
                                  acil.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = acil.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             acil.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 acil.findAndAddContactsByMid(target)
                                 acil.inviteIntoGroup(msg.to,[target])
                                 acil.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      acil.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    acil.sendChatChecked(msg.from_,msg.id)
                else:
                    acil.sendChatChecked(msg.to,msg.id)
            if wait["Removechat"] == True:
                if msg.toType == 0:
                    acil.removeAllMessages(op.param2)
                else:
                    acil.removeAllMessages(op.param2)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        acil.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        acil.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        acil.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        acil.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        acil.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        acil.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        acil.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        acil.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    acil.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = acil.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = acil.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        acil.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = acil.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = acil.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        try:
                            acil.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        except:
                            cu = ""
                        acil.sendText(msg.to,"🎀═displayName═🎀\n✤[" + contact.displayName + "]✤\n🎀═MIDs═🎀\n✤[" + msg.contentMetadata["mid"] + "]✤\n🎀═StatusContact═🎀\n✤" + contact.statusMessage + "✤")
                        acil.sendText(msg.to,"LINKPROFILE\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nLINKBERANDA\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    acil.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Botallbye"]: 
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = ki10.getGroupIdsJoined()
                for i in gid:
                  ki.leaveGroup(i)
                  ki2.leaveGroup(i)
                  ki3.leaveGroup(i)
                  ki4.leaveGroup(i)
                  ki5.leaveGroup(i)
                  ki6.leaveGroup(i)
                  ki7.leaveGroup(i)
                  ki8.leaveGroup(i)
                  ki9.leaveGroup(i)
                  ki10.leaveGroup(i)
                if wait["lang"] == "JP":
                  random.choice(KAC).sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh selfbot...!!!\nMakasih...!!!")
                else:
                  acil.sendText(msg.to,"He declined all invitations")
#--------------------------
            elif msg.text in ["Leaveallgroup"]: 
                gid = acil.getGroupIdsJoined()
                for i in gid:
                  acil.leaveGroup(i)
                if wait["lang"] == "JP":
                  acil.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh selfbot...!!!\nMakasih...!!!")
                else:
                  acil.sendText(msg.to,"He declined all invitations")
#----------------------------------------------
            elif "Sendgrup " in msg.text:
                    bctxt = msg.text.replace("Sendgrup ", "")
                    n = acil.getGroupIdsJoined()
                    for manusia in n:
                        acil.sendText(manusia, (bctxt))
            elif "Sendcontact " in msg.text:
					bctxt = msg.text.replace("Sendcontact ", "")
					t = ki.getAllContactIds()
					t = ki2.getAllContactIds()
					t = ki3.getAllContactIds()
					t = ki4.getAllContactIds()
					t = ki5.getAllContactIds()
					t = ki6.getAllContactIds()
					t = ki7.getAllContactIds()
					t = ki8.getAllContactIds()
					t = ki9.getAllContactIds()
					t = ki10.getAllContactIds()
					for manusia in t:
						ki.sendText(manusia,(bctxt))
						ki2.sendText(manusia,(bctxt))
						ki3.sendText(manusia,(bctxt))
						ki4.sendText(manusia,(bctxt))
						ki5.sendText(manusia,(bctxt))
						ki6.sendText(manusia,(bctxt))
						ki7.sendText(manusia,(bctxt))
						ki8.sendText(manusia,(bctxt))
						ki9.sendText(manusia,(bctxt))
						ki10.sendText(manusia,(bctxt))
            elif "Sendpm " in msg.text:
                    bctxt = msg.text.replace("Sendpm ", "")
                    t = acil.getAllContactIds()
                    for manusia in t:
                        acil.sendText(manusia, (bctxt))
            elif "Code #13" in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "BEBAS,'"}
                acil.sendMessage(msg)
            elif msg.text in ["Stafflist"]:
              if Bots == []:
                  acil.sendText(msg.to,"The Friends is empty")
              else:
                  acil.sendText(msg.to,"Tunggu...")
                  mc = "||===FRIENDLIST===||\n=====================\n"
                  for mi_d in Bots:
                      mc += "★" +acil.getContact(mi_d).displayName + "\n"
                  acil.sendText(msg.to,mc)
                  print "[Command]Friendlist executed"                    
            elif "Youinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = acil.getContact(key1)
                cu = acil.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    acil.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    acil.sendText(msg.to,"Profile Picture " + contact.displayName)
                    acil.sendImageWithURL(msg.to,image)
                    acil.sendText(msg.to,"Cover " + contact.displayName)
                    acil.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Cuy" in msg.text:
                group = acil.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*200 : (j+1)*200]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki.sendMessage(msg) 
                    

            elif "Github " in msg.text:
                    a = msg.text.replace("Github ","")
                    b = urllib.quote(a)
                    acil.sendText(msg.to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Processing...")
                    acil.sendText(msg.to, "Title: " + a + "\nLink: https://github.com/search?utf8=✓&q="+b)
            elif 'playstore ' in msg.text.lower():
                    tob = msg.text.lower().replace('playstore ',"")
                    acil.sendText(msg.to,"Please wait...")
                    acil.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    acil.sendText(msg.to,"This is link aplication")     
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      acil.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              acil.sendText(msg.to, pesan)
                          except Exception as e:
                              acil.sendText(msg.to, str(e))
            elif "Twitter " in msg.text:
                    a = msg.text.replace("Twitter ","")
                    b = urllib.quote(a)
                    acil.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    acil.sendText(msg.to, "https://www.twitter.com" + b)
                    acil.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success") 
            elif "Smule " in msg.text:
                    a = msg.text.replace("Smule ","")
                    b = urllib.quote(a)
                    acil.sendText(msg.to,"Searching to id smule..")
                    acil.sendText(msg.to, "Nama: "+b+"\nId smule: http://smule.com/" +b)
            elif "Google " in msg.text:
                    a = msg.text.replace("Google ","")
                    b = urllib.quote(a)
                    acil.sendText(msg.to,"Searching google..")
                    acil.sendText(msg.to, "Search: "+b+"\nsuccess: http://google.com/" +b)
	    elif "Xvideos " in msg.text:
		    a = msg.text.replace("Xvideos ","")
                    b = urllib.quote(a)
                    acil.sendText(msg.to,"Searching ....\n" "Type:Search Xvideos\nStatus: Processing")
                    acil.sendText(msg.to, "{ Xvideos search page }\n\nTitle: "+b+"\nSource : Xvideos\nhttp://xvideos.com/?k=" +b)
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip(' ')
                gs = acil.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    acil.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            acil.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")
                _nametarget = _name.rstrip(' ')
                gs = acil.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    acil.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            cu = acil.channel.getCover(target)
                            path = str(cu)
                            acil.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"         
            elif msg.text in ["Pmfavorite"]:
                dj = acil.getFavoriteMids()
                kontak = acil.getContacts(dj)
                num = 1
                family = str(len(dj))
                msgs = "[List Favorite Friends Guys]"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\nTotal Friend : %i" % len(kontak)
                acil.sendText(msg.to, msgs)
            elif msg.text.lower()  == 'setauto':
                   acil.sendText(msg.to,helpFun)
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,helpMessage)
                else:
                    acil.sendText(msg.to,helpMessage)
            elif msg.text.lower() == 'media':
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,helpMedia)
                else:
                    acil.sendText(msg.to,helpMedia)
            elif msg.text.lower() == 'helpbots':
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,helpself)
                else:
                    acil.sendText(msg.to,helpself)
            elif msg.text.lower() == 'settings':
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,helpset)
                else:
                    acil.sendText(msg.to,helpset)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    acil.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    acil.updateGroup(group)
                else:
                    acil.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                acil.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                acil.findAndAddContactsByMid(midd)
                acil.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                       msg.contentType = 13
                       acil.sendText(msg.to,"──────┅═ ͜͡✪ই۝ई✪͜͡═┅──────")
                       msg.contentMetadata = {'mid': mid}
                       acil.sendMessage(msg)
                       acil.sendText(msg.to,"──────┅═ ͜͡✪ই۝ई✪͜͡═┅──────")
                       eltime = time.time() - mulai
                       van = "[Avrilia Ini Mahh...!!!]\nDah Gitu Aja\n[TQ]\n " +waktu(eltime)
                       acil.sendText(msg.to,van)
            elif "Mybot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                acil.sendMessage(msg)
            elif "Respon" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                ki10.sendMessage(msg)
                ki.sendText(msg.to,"SEMUA SUDAH DI DALAM GROUP(｀・ω・´)")
            elif msg.text in ["Absen"]:
		        acil.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki2.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki3.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki4.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki5.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki6.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki7.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki8.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki9.sendText(msg.to,"HADIR...(｀・ω・´)")
		        ki10.sendText(msg.to,"HADIR...(｀・ω・´)")
            elif "B1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "B2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "B3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "B4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "B5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "B6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif "B7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
            elif "B8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
            elif "B9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
            elif "B10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                ki10.sendMessage(msg)
            elif "Creator" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u7d1ac07d2036b36745783a0a1992b2ba'}
                acil.sendMessage(msg)
            elif msg.text in ["Allgift","B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","i gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                acil.sendMessage(msg)

            elif msg.text in ["Allgift","B2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Allgift","B3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Allgift","B4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)
            elif msg.text in ["Allgift","B5 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki5.sendMessage(msg)
            elif msg.text in ["Allgift","B6 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                ki6.sendMessage(msg)
            elif msg.text in ["Allgift","B7 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ki7.sendMessage(msg)
            elif msg.text in ["Allgift","B8 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '13'}
                msg.text = None
                ki8.sendMessage(msg)
            elif msg.text in ["Allgift","B9 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '11'}
                msg.text = None
                ki9.sendMessage(msg)
            elif msg.text in ["Allgift","B10 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki10.sendMessage(msg)
            elif msg.text in ["Spam gift"]:
				#if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					ki2.sendMessage(msg)
					ki3.sendMessage(msg)
					ki4.sendMessage(msg)
					ki5.sendMessage(msg)
					ki6.sendMessage(msg)
					ki7.sendMessage(msg)
					ki8.sendMessage(msg)
					ki9.sendMessage(msg)
					ki10.sendMessage(msg)
            elif msg.text in ["Clink"]:
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    acil.updateGroup(group)
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"URL open ô€¨ô€„Œ")
                    else:
                        acil.sendText(msg.to,"URL open ô€¨ô€„Œ")
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"It can not be used outside the group👈")
                    else:
                        acil.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text in ["Curl"]:
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    acil.updateGroup(group)
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"URL close 👈")
                    else:
                        acil.sendText(msg.to,"URL close 👈")
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        acil.sendText(msg.to,"Can not be used for groups other than ")
            elif msg.text.lower() == 'ginfo':        
                    group = acil.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md ="✥GROUP NAME✥\n" + group.name + "\n\n✥GROUP ID✥\n✿" + group.id +"✿" "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\n✥TOTAL MEMBER✥\n" + str(len(group.members)) + " Orang" + "\n✥PENDINGAN✥\n" + str(len(group.invitee)) + " Orang"
                    acil.sendText(msg.to,md)
            elif "Mymid" == msg.text:
                acil.sendText(msg.to,mid)
            elif "B1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "B2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "B3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "B4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "B5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "B6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "B7 mid" == msg.text:
                ki7.sendText(msg.to,ki7mid)
            elif "B8 mid" == msg.text:
                ki8.sendText(msg.to,ki8mid)
            elif "B9 mid" == msg.text:
                ki9.sendText(msg.to,ki9mid)
            elif "B10 mid" == msg.text:
                ki10.sendText(msg.to,ki10mid)
            elif "All mid" == msg.text:
                acil.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                ki10.sendText(msg.to,ki10mid)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                acil.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+acil.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname " in msg.text:
                string = msg.text.replace("Allname ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    acil.sendText(msg.to,"􀜁􀇔􏿿NAMA BOT BERHASIL DI TERAPKAN MENJADI\n👉" + string + "👈")
            elif "Allbio " in msg.text:
                string = msg.text.replace("Allbio ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                    acil.sendText(msg.to,"􀜁􀇔􏿿SEMUA TELAH DI UPDATE BIO PROFILE\n👉" + string + "👈")
            elif "Mybio " in msg.text:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = acil.getProfile()
                    profile.statusMessage = string
                    acil.updateProfile(profile)
                    acil.sendText(msg.to,"􀜁􀇔􏿿Update Bio\n👉" + string + "👈")
#------------------------------------------------------------------------------------------#
            elif "Cn " in msg.text:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = acil.getProfile()
                    profile.displayName = string
                    acil.updateProfile(profile)
                    acil.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
#---------------------------------------------------------
            elif "B1name " in msg.text:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B2name " in msg.text:
                string = msg.text.replace("B2name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B3name " in msg.text:
                string = msg.text.replace("B3name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B4name " in msg.text:
                string = msg.text.replace("B4name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
#--------------------------------------------------------
            elif "B5name " in msg.text:
                string = msg.text.replace("B5name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀇔 􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B6name " in msg.text:
                string = msg.text.replace("B6name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names��" + string + "👈")
#---------------------------------------------------------
            elif "B7name " in msg.text:
                string = msg.text.replace("B7name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B8name " in msg.text:
                string = msg.text.replace("B8name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B9name " in msg.text:
                string = msg.text.replace("B9name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B10name " in msg.text:
                string = msg.text.replace("B10name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")

#--------------------------------------------------------
            elif "You " in msg.text:
                mmid = msg.text.replace("You ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                acil.sendMessage(msg)
            elif msg.text in ["Protect:on"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Protection Enable 􀜁􀇔􏿿􀜁􀇔􏿿✔")
                        ki.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki2.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki3.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki4.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki5.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki6.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki7.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki8.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki9.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki10.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Protection Enable􀜁 􀜁􀇔􏿿✔􀇔􏿿")
                        ki.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki2.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki3.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki4.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki5.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki6.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki7.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki8.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki9.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                        ki10.sendText(msg.to,"Protection Enable 􀜁􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"It is already On 􀜁􀇔􏿿✔")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Link Protect Enable􀜁􏿿")
                    else:
                        acil.sendText(msg.to,"It is already On ô€¨")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"It is already On ¨")
                    if msg.to in wait['pname']:
                        acil.sendText(msg.to,"TURN ON")
                    else:
                        acil.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = acil.getGroup(msg.to).name
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"It is already On ✔")
#=====================================================================================
            elif msg.text in ["Protect:off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki2.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki3.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki4.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki5.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki6.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki7.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki8.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki9.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki10.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ✔")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close")
                        ki.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki2.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki3.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki4.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki5.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki6.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki7.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki8.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki9.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                        ki10.sendText(msg.to,"Protection Disable ✔􀐂􀆭􏿿‮")
                    else:
                        acil.sendText(msg.to,"It is already open ✔")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Link Protection Disable ✖")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close✖")
                    else:
                        acil.sendText(msg.to,"It is already open ✔")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Invite Protection Disable ✖")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close✖")
                    else:
                        acil.sendText(msg.to,"It is already open ✔")
                    if msg.to in wait['pname']:
                        acil.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        acil.sendText(msg.to,"ALREADY OFF")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Cancel Protection Disable ✖")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close✖")
                    else:
                        acil.sendText(msg.to,"It is already open ✔")  

#=====================================================================================   
            elif msg.text.lower() == 'contact:on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Sudah On")
                    else:
                        acil.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already open ✔")
                    else:
                        acil.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact:off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"sudah off ✖")
                    else:
                        acil.sendText(msg.to,"It is already off ✖")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off already")
                    else:
                        acil.sendText(msg.to,"already Close ✔")
            elif msg.text in ["Pro:on"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki2.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki3.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki4.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki5.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki6.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki7.sendText(msg.to,"Protection Enable ??????✔")
                        ki8.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki9.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki10.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Protection Enable􀜁✔􀇔􏿿")
                        ki.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki2.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki3.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki4.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki5.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki6.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki7.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki8.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki9.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                        ki10.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                    else:
                        acil.sendText(msg.to,"It is already On ✔")
            elif msg.text in ['Prolink:on']:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Link Protect Enable􀜁􏿿")
                    else:
                        acil.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Proinvite:on']:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"It is already On ¨")
            elif msg.text in ['Procancel:on']:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"It is already On ✔")
            elif msg.text.lower() == 'join:on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Ini sudah on􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"It is already On ✔")
            elif msg.text.lower() == 'blocklist':
                blockedlist = acil.getBlockedContactIds()
                acil.sendText(msg.to, "Please wait...")
                kontak = acil.getContacts(blockedlist)
                num=1
                msgs="✖User Blocked List✖\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                acil.sendText(msg.to, msgs)
            elif msg.text.lower() == 'join:off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Auto Join Already Off✔")
                    else:
                        acil.sendText(msg.to,"Auto Join set off✔")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close✔")
                    else:
                        acil.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Pro:off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Protection Disable ✔")
                        ki.sendText(msg.to,"Protection Disable ✔")
                        ki2.sendText(msg.to,"Protection Disable ✔")
                        ki3.sendText(msg.to,"Protection Disable ✔")
                        ki4.sendText(msg.to,"Protection Disable ✔")
                        ki5.sendText(msg.to,"Protection Disable ✔")
                        ki6.sendText(msg.to,"Protection Disable ✔")
                        ki7.sendText(msg.to,"Protection Disable ✔")
                        ki8.sendText(msg.to,"Protection Disable ✔")
                        ki9.sendText(msg.to,"Protection Disable ✔")
                        ki10.sendText(msg.to,"Protection Disable ✔")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ✔")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close")
                        ki.sendText(msg.to,"Protection Disable ✔")
                        ki2.sendText(msg.to,"Protection Disable ✔")
                        ki3.sendText(msg.to,"Protection Disable ✔")
                        ki4.sendText(msg.to,"Protection Disable ✔")
                        ki5.sendText(msg.to,"Protection Disable ✔")
                        ki6.sendText(msg.to,"Protection Disable ✔")
                        ki7.sendText(msg.to,"Protection Disable ✔")
                        ki8.sendText(msg.to,"Protection Disable ✔")
                        ki9.sendText(msg.to,"Protection Disable ✔")
                        ki10.sendText(msg.to,"Protection Disable ✔")
                    else:
                        acil.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Prolink:off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Link Protection Disable ✖")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close✖")
                    else:
                        acil.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Proinvite:off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Invite Protection Disable ✖")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close✖")
                    else:
                        acil.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Procancel:off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Cancel Protection Disable ✖")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close✖")
                    else:
                        acil.sendText(msg.to,"It is already open ✔")
            elif "Join:" in msg.text:
                try:
                    strnum = msg.text.replace("Join:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            acil.sendText(msg.to,"Itu off undangan ditolak✖\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan✖")
                        else:
                            acil.sendText(msg.to,"Off undangan ditolak✖Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            acil.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis✔")
                        else:
                            acil.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"")
                    else:
                        acil.sendText(msg.to,"Weird value✖")
            elif msg.text in ["Leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Sudah terbuka 􀜁􀇔✔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Is already open􀇔􏿿✔")
            elif msg.text in ["Leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off􀜁􀇔􏿿✖")
                    else:
                        acil.sendText(msg.to,"Sudah off􀜁􀇔􏿿✖")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Is already close􀇔􏿿✔")
            elif msg.text in ["Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done 􀜁􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ✖")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on ✔")
                    else:
                        acil.sendText(msg.to,"on ✔")
            elif msg.text in ["Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done􀇔􏿿✔")
                    else:
                        acil.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿✔")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Off ✖")
                    else:
                        acil.sendText(msg.to,"Off ✖")
            elif msg.text.lower() == 'set':
                md = "╔▬▬TEAM ELITE▬▬╗\n║▬▬▬T▬▬M▬▬▬║\n"
                if wait["likeOn"] == True: md+="║☆║Like:ON➡️📱\n"
                else: md+="║☆║Like:OFF➡️📴\n"
                if wait["wcOn"] == True: md+="║☆║Welcome:ON➡️📱\n"
                else: md+="║☆║Welcome:OFF➡️📴\n"
                if wait["leftOn"] == True: md+="║☆║Left:ON➡️📱\n"
                else: md+="║☆║Left:OFF➡️📴\n"
                if wait["detectMention"] == True: md+="║☆║Respon:ON➡️📱\n"
                else: md +="║☆║Respon:OFF➡️📴\n"
                if wait["stickerMention"] == True: md+="║☆║Stickertag:ON➡️📱\n"
                else: md +="║☆║Stickertag:OFF➡️📴\n"
                if settings["simiSimi"] == True: md+="║☆║Simisimi:ON➡️📱\n"
                else: md+="║☆║Simisimi:OFF➡️📴\n"
                if wait["alwayRead"] == True: md+="║☆║Auto read:ON➡️📱\n"
                else: md+="║☆║Auto read:OFF➡️📴\n"
                if wait["Sider"] == True: md+="║☆║Sider:ON➡️📱\n"
                else: md+="║☆║Sider:OFF➡️📴\n"
                if wait["kickMention"] == True: md+="║☆║Notag:ON➡️📱\n"
                else:md+="║☆║Notag:OFF➡️📴\n"
                if wait["contact"] == True: md+="║☆║Contact:ON➡️📱\n"
                else: md+="║☆║Contact:OFF➡️📴\n"
                if wait["autoJoin"] == True: md+="║☆║Join:ON➡️📱\n"
                else: md +="║☆║Join:OFF➡️📴\n"
                if wait["autoCancel"]["on"] == True:md+="║☆║Cancel:" + str(wait["autoCancel"]["members"]) + "➡️📱\n"
                else: md+= "║☆║Cancel:OFF➡️📴\n"
                if wait["leaveRoom"] == True: md+="║☆║Leave:ON➡️📱\n"
                else: md+="║☆║Leave:OFF➡️📴\n"
                if wait["timeline"] == True: md+="║☆║Share:ON➡️📱\n"
                else:md+="║☆║Share:OFF➡️📴\n"
                if wait["autoAdd"] == True: md+="║☆║Add:ON➡️📱\n"
                else:md+="║☆║Add:OFF➡️??\n"
                if wait["commentOn"] == True: md+="║☆║Com:ON➡️📱\n"
                else:md+="║☆║Com:OFF➡️📴\n║▬║❨◄▬▬▬►❩\n║☆║◄═PROTECTION═►\n║▬║▬TEAM ELITE▬╣\n"
                if wait["protect"] == True: md+="║☆║Pro:ON➡️📱\n"
                else:md+="║☆║Pro:OFF➡️📴\n"
                if wait["linkprotect"] == True: md+="║☆║ProtectQr:ON➡️📱\n"
                else:md+="║☆║ProtectQr:OFF➡️📴\n"
                if wait["inviteprotect"] == True: md+="║☆║Proinvite:ON➡️📱\n"
                else:md+="║☆║Proinvite:OFF➡️📴\n"
                if wait["cancelprotect"] == True: md+"║☆║Procancel:ON➡️📱\n"
                else:md+="║☆║Procancel:OFF➡️📴\n"
                if wait["pname"] == True: md+="║☆║Namelock:ON➡️📱\n"
                else: md+="║☆║Namelock:OFF➡️📴\n"   
                acil.sendText(msg.to,md + "║▬▬▬T▬▬M▬▬▬║\n╚▬▬TEAM ELITE▬▬╝")
            elif "Creatorgrup" == msg.text:
                try:
                    group = acil.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    GS = acil.getContact(msg.to)
                    acil.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    acil.sendMessage(M)
                    W = acil.getContact(msg.to)
                    acil.sendText(msg.to,"old user")
            elif cms(msg.text,["Add"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u7d1ac07d2036b36745783a0a1992b2ba'}
                acil.sendText(msg.to,"❂•••••••••✧••••••••••❂")
                acil.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u2ffc9d5343699b5c1e00f320d5cef815'}
                acil.sendMessage(msg)
                acil.sendText(msg.to,"❂••••••••✰•✰••••••••❂")
            elif "Tagme: " in msg.text:
                c = msg.text.replace("Tagme: ","")
                if c in [""," ","\n",None]:
                    acil.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["tagme"] = c
                    acil.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Welcome: " in msg.text:
                c = msg.text.replace("Welcome: ","")
                if c in [""," ","\n",None]:
                    acil.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["joingc"] = c
                    acil.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Left: " in msg.text:
                c = msg.text.replace("Left: ","")
                if c in [""," ","\n",None]:
                    acil.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["leftgc"] = c
                    acil.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Sider: " in msg.text:
                c = msg.text.replace("Sider: ","")
                if c in [""," ","\n",None]:
                    acil.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["sider1"] = c
                    acil.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Setrespon: " in msg.text:
                c = msg.text.replace("Setrespon: ","")
                if c in [""," ","\n",None]:
                    acil.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["responName"] = c
                    acil.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki2.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki3.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki4.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki5.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki6.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki7.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki8.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki9.sendText(msg.to,"✨This has been changed✨\n\n" + c)
                    ki10.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Cekresponse" in msg.text:
            	acil.sendText(msg.to,"👇Respon saat di tag👇\n" + wait["tagme"])
            	acil.sendText(msg.to,"👇Respon saat di add👇\n" + wait["comment"])
            	acil.sendText(msg.to,"👇Respon saat member join👇\n" + wait["joingc"])
            	acil.sendText(msg.to,"👇Respon saat member left👇\n" + wait["leftgc"])
            	acil.sendText(msg.to,"👇Respon saat member readchat👇\n" + wait["sider1"])
            	acil.sendText(msg.to,"👇Respon saat member memanggil👇\n" + wait["responName"])
            	acil.sendText(msg.to,"👇Respon di autolike👇\n" + wait["comment1"] + "\n\nHAL INI TIDAK DAPAT DI UBAH SESUAI HAK CIPTA\nCREATOR::TEAM ELITE")
            elif msg.text in ["Left:on"]:
                if wait["leftOn"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done")
                else:
                    wait["leftOn"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already")
            elif msg.text in ["Left:off"]:
                if wait["leftOn"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done")
                else:
                    wait["leftOn"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already") 
            elif msg.text in ["Welcome:on"]:
                if wait['wcOn'] == True:
                    if wait["lang"] == "JP": 
                        acil.sendText(msg.to,"sudah ON")
                else:
                    wait["wcOn"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON")
            elif msg.text in ["Welcome:off"]:
                if wait['wcOn'] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Sudah off")
                else:
                    wait['wcOn'] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already OFF")
            elif msg.text.lower() == 'group id':
                gid = acil.getGroupIdsJoined()
                h = "❂•••••••••L I S T  I D  G R O U P•••••••••❂\n "
                for i in gid:
                    h += "[%s]:%s\n" % (acil.getGroup(i).name,i)
                acil.sendText(msg.to,h)
            elif msg.text in ["Gcancelall"]:
                gid = acil.getGroupIdsInvited()
                for i in gid:
                    acil.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,"Success menolak semua undangan")
                else:
                    acil.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Add:on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already On✔")
                    else:
                        acil.sendText(msg.to,"Already On✔")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already On✔")
                    else:
                        acil.sendText(msg.to,"Already On✔")
            elif msg.text in ["Add:off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Hal ini sudah off✖")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah dimatikan✖")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already Off✖")
                    else:
                        acil.sendText(msg.to,"Untuk mengaktifkan-off✖")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                acil.sendText(msg.to,"✨We changed the message✨")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                acil.sendText(msg.to,"✨We changed the Help✨")
            elif "Msg add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,"✨Kami mengubah pesan✨")
                else:
                    acil.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message confirm"]:
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    acil.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    acil.sendText(msg.to,"I changed the language to engglis✔")
                else:
                    wait["lang"] = "JP"
                    acil.sendText(msg.to,"I changed the language to indonesia✔")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    acil.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["comment"] = c
                    acil.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif msg.text in ["Comment:on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Aku berada di✔")
                    else:
                        acil.sendText(msg.to,"To open✔")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"✔")
                    else:
                        acil.sendText(msg.to,"✔")
            elif msg.text in ["Com:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Hal ini sudah off ✖")
                    else:
                        acil.sendText(msg.to,"It is already turned off ✖")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Off✖")
                    else:
                        acil.sendText(msg.to,"To turn off✖")
            elif msg.text in ["Com","Comment"]:
                acil.sendText(msg.to,"✨Auto komentar saat ini telah ditetapkan sebagai berikut✨\n\n" + str(wait["comment"]))
            elif msg.text in ["Glink","Url"]:
                if msg.toType == 2:
                    g = acil.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        acil.updateGroup(g)
                    gurl = acil.reissueGroupTicket(msg.to)
                    acil.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        acil.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = acil.reissueGroupTicket(gid)
                    acil.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    acil.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“👈")

            elif "gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = acil.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        acil.updateGroup(x)
                    gurl = acil.reissueGroupTicket(msg.to)
                    acil.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Can't be used outside the group")
                    else:
                        acil.sendText(msg.to,"Not for use less than group")
#                else:
#                    acil.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Comban"]:
                wait["wblack"] = True
                acil.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist…”✚")
            elif msg.text in ["Comban del"]:
                wait["dblack"] = True
                acil.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist…”✚")
            elif msg.text in ["Comban cek"]:
                if wait["commentBlack"] == {}:
                    acil.sendText(msg.to,"Nothing in the blacklist✖")
                else:
                    acil.sendText(msg.to,"The following is a blacklist✔")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +acil.getContact(mi_d).displayName + "\n"
                    acil.sendText(msg.to,mc)
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already")
            elif "Namelock:on" in msg.text:
               # if msg.from_ in admin or owner:
                    if msg.to in wait['pname']:
                        acil.sendText(msg.to,"TURN ON")
                    else:
                        acil.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = acil.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
               # if msg.from_ in admin or owner:
                    if msg.to in wait['pname']:
                        acil.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        acil.sendText(msg.to,"ALREADY OFF")                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                acil.sendText(msg.to,"BOT API SIMISIMI TURN ON")
                ki.sendText(msg.to,"already turn active")
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                acil.sendText(msg.to,"BOT API SIMISIMI TURN OFF")
                ki.sendText(msg.to,"already non active")
            elif msg.text in ["Read on","Read:on"]:
                if wait['alwayRead'] == True:
                    if wait["alwayRead"] == "JP": 
                        acil.sendText(msg.to,"Auto Sider ON")
                else:
                    wait["alwayRead"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON")
            elif msg.text in ["Read off","Read:off"]:
                if wait['alwayRead'] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Auto Sider OFF")
                else:
                    wait['alwayRead'] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already OFF auto read")
            elif msg.text in ["Deletechat"]:
                if wait['Removechat'] == True:
                    if wait["Removechat"] == "JP": 
                        acil.sendText(msg.to,"Success!!!")
                if wait['Removechat'] == False:
                    if wait["lang"] == "JP":
                        pass
            elif "Sniper:on" in msg.text:
	#      if msg.toType == 2:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                acil.sendText(msg.to,"Sniper On")
            elif "Sniper:off" in msg.text:
	#      if msg.toType == 2:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    acil.sendText(msg.to, "Sniper Off")
                else:
                    acil.sendText(msg.to, "Heh Belom Di Set")
            elif msg.text in ["Autorespon on","Autorespon:on","Respon on","Respon:on"]:
                if wait["detectMention"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Auto Respon ON")
                else:
                    wait["detectMention"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON")
            elif msg.text in ["Autorespon off","Autorespon:off","Respon off","Respon:off"]:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Auto Respon OFF")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already OFF")
            elif msg.text in ["Notag:on"]:
                if wait["kickMention"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"☠️DANGER TAG KICK ON☠️")
                else:
                    wait["kickMention"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"already ON")
            elif msg.text in ["Notag:off"]:
                if wait["kickMention"] == False:
                   if wait["lang"] == "JP":
                        ki.sendText(msg.to,"SELF PROTECT TAG OFF ✔")
                else:
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"already turn OF")
            elif msg.text.lower() == 'Clock:on':
                if wait["clock"] == True:
                    acil.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = acil.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    acil.updateProfile(profile)
                    acil.sendText(msg.to,"Jam on✔")
            elif msg.text in ["Stickertag:on"]:
                if wait["stickerMention"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"sudah on")
                else:
                    wait["stickerMention"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON")
            elif msg.text in ["Stickertag:off"]:
                if wait["stickerMention"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"sudah off")
                else:
                    wait["stickerMention"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already OFF")
            elif msg.text.lower() == 'Clock:off':
                if wait["clock"] == False:
                    acil.sendText(msg.to,"Hal ini sudah off✖")
                else:
                    wait["clock"] = False
                    acil.sendText(msg.to," Dimatikan ✔")
            elif "Clockname " in msg.text:
                n = msg.text.replace("Jam say ","")
                if len(n.decode("utf-8")) > 30:
                    acil.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    acil.sendText(msg.to,"Ini telah diubah✔\n\n" + n)
            elif msg.text in ["Translate"]:
					if wait["lang"] == "JP":
						acil.sendText(msg.to,translateMessage)
					else:
						acil.sendText(msg.to,helpt)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = acil.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    acil.updateProfile(profile)
                    acil.sendText(msg.to,"Diperbarui✔")
                else:
                    acil.sendText(msg.to,"✨Silahkan Aktifkan Nama✨")
            elif ("Fuck " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           acil.kickoutFromGroup(msg.to,[target])
                       except:
                           acil.sendText(msg.to,"Error")
            elif ("Fuck1 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
            elif ("Fuck2 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif ("Fuck3 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki3.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"Error")
            elif ("Fuck4 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki4.kickoutFromGroup(msg.to,[target])
                       except:
                           ki4.sendText(msg.to,"Error")
            elif ("Fuck5 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki5.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")
            elif ("Fuck6 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki6.kickoutFromGroup(msg.to,[target])
                       except:
                           ki6.sendText(msg.to,"Error")
            elif ("Fuck7 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki7.kickoutFromGroup(msg.to,[target])
                       except:
                           ki7.sendText(msg.to,"Error")
            elif ("Fuck8 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki8.kickoutFromGroup(msg.to,[target])
                       except:
                           ki8.sendText(msg.to,"Error")
            elif ("Fuck9 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki9.kickoutFromGroup(msg.to,[target])
                       except:
                           ki9.sendText(msg.to,"Error")
            elif ("Fuck10 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki10.kickoutFromGroup(msg.to,[target])
                       except:
                           ki10.sendText(msg.to,"Error")
            elif ("Sc " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   key = acil.getContact(key1)
                   acil.sendText(msg.to,"" +  key1)

            elif "Bro " in msg.text:
                       nk0 = msg.text.replace("Bro ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = acil.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    acil.sendText(msg.to,"Good Bye")
#-----------------------------------------------------------
            elif ("Bye " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass


            elif ("Ban " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      acil.sendText(msg.to,"Succes Banned")
                   except:
                      pass

            elif msg.text in ["Mygroups"]:
                 gid = acil.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += "[⛓️] %s \n" % (acil.getGroup(i).name + " | 🗜️Members : " + str(len (acil.getGroup(i).members)))
                 acil.sendText(msg.to, "☆「Group List」☆\n"+ h +"🗜️Total Group : " +str(len(gid)))

#----------------------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = acil.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        acil.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                acil.sendText(msg.to,"Target Unlocked")
                            except:
                                acil.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = acil.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									acil.sendText(msg.to,"Target Locked")
                                except:
                                    acil.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = acil.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									acil.sendText(msg.to,"Target Unlocked")
                                except:
                                    acil.sendText(msg.to,"Error")
            elif "Id " in msg.text:
                msgg = msg.text.replace("Id ",'')
                conn = acil.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    acil.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    acil.sendMessage(msg)
#_________________________________________________________________________
            elif 'ig ' in msg.text.lower():
              #if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    acil.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    acil.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	acil.sendText(msg.to, str(njer))
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    acil.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif msg.text in ["Kalender","Time","Waktu"]:
                       tz = pytz.timezone("Asia/Jakarta")
                       timeNow = datetime.now(tz=tz)
                       day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                       hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                       bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                       hr = timeNow.strftime("%A")
                       bln = timeNow.strftime("%m")
                       for i in range(len(day)):
                           if hr == day[i]: hasil = hari[i]
                       for k in range(0, len(bulan)):
                           if bln == str(k): bln = bulan[k-1]
                       rst = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                       acil.sendText(msg.to, rst)
#==============================================================================#

                
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot has been active "+waktu(eltime)
                acil.sendText(msg.to,van) 
                
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = acil.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    acil.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            acil.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = acil.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                acil.sendMessage(msg)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = acil.getContact(key1)
                cu = acil.channel.getCover(key1)
                try:
                    acil.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    acil.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif msg.text in ["Myname"]:
                    h = acil.getContact(mid)
                    acil.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = acil.getContact(mid)
                    acil.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = acil.getContact(mid)
                    acil.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = acil.getContact(mid)
                    acil.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = acil.getContact(mid)
                    acil.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = acil.getContact(mid)
                    cu = acil.channel.getCover(mid)          
                    path = str(cu)
                    acil.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = acil.getContact(mid)
                    cu = acil.channel.getCover(mid)          
                    path = str(cu)
                    acil.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = acil.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        acil.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                acil.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                acil.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                acil.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                acil.sendVideoWithURL(msg.to,wait["pap"])
#=========================
#-----------------------------------------------------------
            elif msg.text == "Cctv":
                    acil.sendText(msg.to, "Cctv on")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif 'copy ' in msg.text.lower():
                if msg.toType == 2:
                    red = re.compile(re.escape('copy '),re.IGNORECASE)
                    tname = red.sub('',msg.text)
                    tname = tname.lstrip()
                    tname = tname.replace(" @","$spliter$")
                    tname = tname.rstrip()
                    tname = tname.split("$spliter$")
                    tname = tname[0]
                    tname = tname[1:]
                    clist = {
                        "Founded":False,
                        "displayName":"",
                        "statusMessage":"",
                        "pictureStatus":""
                    }
                    mems = acil.getGroup(msg.to).members
                    for targ in mems:
                        if targ.displayName == tname:
                            clist["displayName"] = targ.displayName
                            clist["statusMessage"] = targ.statusMessage
                            clist["pictureStatus"] = targ.pictureStatus
                            clist["Founded"] = True
                    if clist["Founded"]:
                        wait["selfStatus"] = False
                        me = acil.getProfile()
                        me.displayName = clist["displayName"]
                        me.statusMessage = clist["statusMessage"]
                        me.pictureStatus = clist["pictureStatus"]
                        acil.updateDisplayPicture(me.pictureStatus)
                        acil.updateProfile(me)
                        acil.sendText(msg.to,"Done")
                    else:
                        acil.sendText(msg.to,"Done")

            elif "Urlpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Urlpict @","")
                _nametarget = _name.rstrip(' ')
                gs = acil.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    acil.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            acil.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                            print "[Command]dp executed"
            elif "Allcopi @" in msg.text:
                   print "[COPY] OK"
                   _name = msg.text.replace("Allcopi @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki.getGroup(msg.to)
                   gs = ki2.getGroup(msg.to)
                   gs = ki3.getGroup(msg.to)
                   gs = ki4.getGroup(msg.to)
                   gs = ki5.getGroup(msg.to)
                   gs = ki6.getGroup(msg.to)
                   gs = ki7.getGroup(msg.to)
                   gs = ki8.getGroup(msg.to)
                   gs = ki9.getGroup(msg.to)
                   gs = ki10.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       acil.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki.CloneContactProfile(target)
                               ki2.CloneContactProfile(target)
                               ki3.CloneContactProfile(target)
                               ki4.CloneContactProfile(target)
                               ki5.CloneContactProfile(target)
                               ki6.CloneContactProfile(target)
                               ki7.CloneContactProfile(target)
                               ki8.CloneContactProfile(target)
                               ki9.CloneContactProfile(target)
                               ki10.CloneContactProfile(target)
                               acil.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
            elif "Urlcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Urlcover @","")
                _nametarget = _name.rstrip(' ')
                gs = acil.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    acil.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            cu = acil.channel.getCover(target)
                            path = str(cu)
                            acil.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    acil.sendText(msg.to,"Tidak Ada kontak blacklist")
                else:
                    acil.sendText(msg.to,"═════════List Blacklist════════")
                    h = ""
                    for i in wait["blacklist"]:
                        h = acil.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        acil.sendMessage(M)

#-------------------------------------------------
	    elif "Spam " in msg.text:
#	      if msg.from_ in admin:
                _name = msg.text.replace("Spam ","")
                _nametarget = _name.rstrip(' ')
                gs = acil.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
		       acil.sendText(msg.to,"Wating in progres...")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
	  	       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
		       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       acil.sendText(msg.to, "Succes")
                       print " Spammed !"
            elif "Testing" == msg.text:
                       start = time.time()
                       print("Speed")
                       acil.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       acil.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki2.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki3.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki4.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki5.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki6.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki6.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki7.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki7.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki8.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki8.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki9.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki9.sendText(msg.to, "%sseconds" % (elapsed_time))
                       start = time.time()
                       print("Speed")
                       ki10.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                       elapsed_time = time.time() - start
                       ki10.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text in [".sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		acil.sendText(msg.to, "Progress: [100%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
                acil.sendText(msg.to, "%sseconds" % (elapsed_time))
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		#ki.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            start = time.time()
     #           print("Speed")                
       #         elapsed_time = time.time() - start
		#ki2.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            start = time.time()
     #           print("Speed")                
       #         elapsed_time = time.time() - start
		#ki3.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            start = time.time()
     #           print("Speed")                
      #          elapsed_time = time.time() - start
		#ki4.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            start = time.time()
     #           print("Speed")                
      #          elapsed_time = time.time() - start
		#ki5.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            start = time.time()
     #           print("Speed")                
      #          elapsed_time = time.time() - start
		#ki6.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki6.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            start = time.time()
     #           print("Speed")                
      #          elapsed_time = time.time() - start
		#ki7.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki7.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            start = time.time()
     #           print("Speed")                
      #          elapsed_time = time.time() - start
		#ki8.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki8.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            start = time.time()
     #           print("Speed")                
      #          elapsed_time = time.time() - start
		#ki9.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki9.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            start = time.time()
     #           print("Speed")                
      #          elapsed_time = time.time() - start
		#ki10.sendText(msg.to, "Progress: [99%] [⨳⨳⨳⨳⨳⨳⨳⨳⨳⨳.]")
   #             ki10.sendText(msg.to, "%sseconds" % (elapsed_time))
#--------------------------------------------------------------------------
#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		acil.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                text = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (text+"\n")
                if txt[1] == "on":
                    if jmlh <= 10000:
                        for x in range(jmlh):
                            ki.sendText(msg.to, text)
                    else:
                        acil.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 10000:
                        ki.sendText(msg.to, tulisan)
                    else:
                        acil.sendText(msg.to, "Out Of Range!")
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        acil.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        acil.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        acil.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        acil.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            acil.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+acil.getContact(mi_d).displayName + "\n"
                            acil.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                acil.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                acil.sendText(msg.to,"Mimic change to target")
                            else:
                                acil.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        acil.sendText(msg.to,"Reply Message on")
                    else:
                        acil.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        acil.sendText(msg.to,"Reply Message off")
                    else:
                        acil.sendText(msg.to,"Sudah off")
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = acil.getGroup(msg.to)
                acil.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Gid" in msg.text:
                saya = msg.text.replace('Gid','')
                gid = acil.getGroup(msg.to)
                acil.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
            elif msg.text in ["Friendlist"]:    
                contactlist = acil.getAllContactIds()
                kontak = acil.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                acil.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = acil.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                acil.sendText(msg.to, msgs)
               
                
            elif msg.text in ["Friendlistmid"]: 
                gruplist = acil.getAllContactIds()
                kontak = acil.getContacts(gruplist)
                num=1
                msgs="═════════List FriendMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                acil.sendText(msg.to, msgs)
                    
#-----------------------------------------------
            elif "lurk:on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         acil.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     acil.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "lurk:off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    acil.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    acil.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             acil.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = acil.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          acil.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        acil.sendText(msg.to, "Lurking has not been set.")           

            elif msg.text in ["Bl:on"]:
                wait["wblacklist"] = True
                acil.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbl:on"]:
                wait["dblacklist"] = True
                acil.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    acil.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    acil.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "�" +acil.getContact(mi_d).displayName + "\n"
                    acil.sendText(msg.to,mc)
 #---------Fungsi Banlist With Tag--------#
            elif msg.text in ["Banlist","ip banlist"]:
                if wait["blacklist"] == {}:
                    acil.sendText(msg.to,"No user is Blacklisted")
                else:
                    ki.sendText(msg.to,"Blacklisted user")
                    mc = " 🛡️====||B L A C K L I S T||====🛡️\n"
                    for mi_d in wait["blacklist"]:
                        mc += "🗜️" +acil.getContact(mi_d).displayName + "\n"
                    acil.sendText(msg.to,mc)
                    
                    print "[Command]Banlist executed"
            elif msg.text in ["Clearban"]:
                if msg.toType == 2:
                   wait["blacklist"] = {}
                   acil.sendText(msg.to,"clear all blacklist")
                   ki.sendText(msg.to,"done ✔")
                   ki2.sendText(msg.to,"done ✔")
                   ki3.sendText(msg.to,"done ✔")
                   ki4.sendText(msg.to,"done ✔")
                   ki5.sendText(msg.to,"done ✔")
                   ki6.sendText(msg.to,"done ✔")
                   ki7.sendText(msg.to,"done ✔")
                   ki8.sendText(msg.to,"done ✔")
                   ki9.sendText(msg.to,"done ✔")
                   ki10.sendText(msg.to,"done ✔")
                   ki.sendText(msg.to,"blacklist done all removed 👮")
            elif msg.text.lower() == 'kick@mbl':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            acil.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            ki7.kickoutFromGroup(msg.to,[jj])
                            ki8.kickoutFromGroup(msg.to,[jj])
                            ki9.kickoutFromGroup(msg.to,[jj])
                            ki10.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#-----------------------------------------------

#---------------------------------------------------
            elif "Pict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Pict @","")
                _nametarget = _name.rstrip(' ')
                gs = acil.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    acil.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            acil.sendImageWithUrl(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#---------------------------------------------------
#---------------------------------------------------
            elif msg.text in ["Recopy"]:
                try:
                    acil.updateDisplayPicture(mybackup.pictureStatus)
                    acil.updateProfile(mybackup)
                    acil.sendText(msg.to, "Success")
                except Exception as e:
                    acil.sendText(msg.to, str (e))
#-----------------------------------------------------------------------
            elif "Youtube " in msg.text:
                try:
                    textToSearch = (msg.text).replace("Youtube ", "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    acil.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    acil.sendText(msg.to,"Could not find it")
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        acil.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
#------------------------------------------------
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = acil.getContact(key1)
                cu = acil.channel.getCover(key1)
                try:
                    acil.sendText(msg.to,"~Nama\n" + contact.displayName + "\n~Mid\n" + contact.mid + "\n~Bio\n" + contact.statusMessage + "\n~Profile Picture\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n~Header\n" + str(cu))
                except:
                    acil.sendText(msg.to,"~Nama\n" + contact.displayName + "\n~Mid\n" + contact.mid + "\n~Bio\n" + contact.statusMessage + "\n~Profile Picture\n" + str(cu))
            
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = acil.getContact(key1)
                cu = acil.channel.getCover(key1)
                try:
                    acil.sendText(msg.to,contact.statusMessage)
                except:
                    acil.sendText(msg.to,contact.statusMessage)
            elif "Gimage" in msg.text:
					group = acil.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
					acil.sendImageWithURL(msg.to,path)
            
            elif "Getprofile @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getprofile @","")
                _nametarget = _name.rstrip('  ')
                gs = acil.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    acil.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            acil.sendImageWithUrl(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#------------------------------------------------------------
            elif msg.text in ["Invite"]:
                wait["invite"] = True
                acil.sendText(msg.to,"send contact 😉")
#------------------------------------------------------------
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = acil.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    acil.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            cu = acil.channel.getCover(target)          
                            path = str(cu)
                            acil.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif msg.text.lower() == 'reboot':
                    print "[Command]Like executed"
                    try:
                        acil.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        acil.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif "Hay " in msg.text:
                say = msg.text.replace("Hay ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                acil.sendAudio(msg.to,"hasil.mp3")
            elif "Bar" in msg.text:
                if msg.toType == 2:
                    print "Nuke ok"
                    _name = msg.text.replace("Bar","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
                    h = ki.getProfile()
                    h = ki2.getProfile()
                    ki.sendText(msg.to,"█̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳█̳\n█̳░̳░̳╦̳─̳╦̳╔̳╗̳╦̳─̳╔̳╗̳╔̳╗̳╔̳╦̳╗̳╔̳╗̳░̳░̳█̳\n█̳░̳░̳║̳║̳║̳╠̳─̳║̳─̳║̳─̳║̳║̳║̳║̳║̳╠̳─̳░̳░̳█̳\n█̳░̳░̳╚̳╩̳╝̳╚̳╝̳╚̳╝̳╚̳╝̳╚̳╝̳╩̳─̳╩̳╚̳╝̳░̳░̳█̳\n█̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳█̳\n  █̳░̳░̳░̳░░̳░ ╔̳╦̳╗̳ ╔̳╗ ░̳░░̳░̳░̳░̳█̳\n  █̳░̳░░̳░░̳░ ̳─̳║̳─̳ ║̳║ ̳░̳░░̳░░̳░̳█̳\n  █̳░̳░░̳░̳░̳░ ─̳╩̳ ─̳╚̳╝ ░̳░░̳░̳░̳░̳█̳\n  █̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳█̳\n  █̳░̳░̳╦̳╔̳─̳╦̳─̳╔̳╗̳╦̳╔̳─̳╔̳╗̳╔̳╗̳░̳░̳█̳\n  █̳░̳░̳╠̳╣̳─̳║̳─̳║̳─̳╠̳╣̳─̳╠̳─̳╠̳╝̳░̳░̳█̳\n  █̳░̳░̳╩̳╚̳─̳╩̳─̳╚̳╝̳╩̳╚̳─̳╚̳╝̳╩̳╚̳░̳░̳█̳\n  █̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳▀̳█̳\n  █̳░̳░̳╔̳╗̳─̳╔̳╗̳─̳╔̳╗̳╔̳╗̳╦̳─̳╔̳╗̳░̳░̳█̳\n  █̳░̳░̳╠̳╣̳─̳║̳╝̳─̳╠̳─̳║̳║̳║̳─̳╠̳╣̳░̳░̳█̳\n  █̳░̳░̳╝̳╚̳─̳╩̳╚̳─̳╚̳╝̳╩̳╚̳╝̳─̳╝̳╚̳░̳░̳█̳\n  █̳░̳░̳░̳:  B̳L̳A̳C̳K̳ A̳N̳G̳E̳L̳S̳  :░̳░̳░̳█̳\n  █̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳▄̳█̳\n【Ꭺ̶̶̶̶࿆ ̶̶ ̶̶̶̶࿆ ̶̶Ꮩ̶̶̶̶࿆ ̶̶Ꮖ̶̶̶̶࿆ ̶̶Ꮯ̶̶̶̶࿆ ̶̶Ꮖ̶̶̶̶࿆ ̶̶ϴ̶̶̶̶࿆ ̶̶Ⴎ̶̶̶̶࿆ ̶̶Տ̶̶̶̶࿆ ̶̶ ̶̶̶̶࿆ ̶̶Ꮶ̶̶̶̶࿆ ̶̶Ꮖ̶̶̶̶࿆ ̶̶Ꮮ̶̶̶̶࿆ ̶̶Ꮮ̶̶̶̶࿆ ̶̶Ꭼ̶̶̶̶࿆ ̶̶Ꭱ̶̶̶̶࿆ ̶】\n ______________________________")
                    #ki2.sendText(msg.to,"_____Sexy?Sex\n ____?Sexy?Sexy\n ___y?Sexy?Sexy?\n ___?Sexy?Sexy?S\n ___?Sexy?Sexy?S\n __?Sexy?Sexy?Se\n _?Sexy?Sexy?Se\n _?Sexy?Sexy?Se\n _?Sexy?Sexy?Sexy?\n ?Sexy?Sexy?Sexy?Sexy\n ?Sexy?Sexy?Sexy?Sexy?Se\n ?Sexy?Sexy?Sexy?Sexy?Sex\n _?Sexy?__?Sexy?Sexy?Sex\n ___?Sex____?Sexy?Sexy?\n ___?Sex_____?Sexy?Sexy\n ___?Sex_____?Sexy?Sexy\n ____?Sex____?Sexy?Sexy\n _____?Se____?Sexy?Sex\n ______?Se__?Sexy?Sexy\n _______?Sexy?Sexy?Sex\n ________?Sexy?Sexy?sex\n _______?Sexy?Sexy?Sexy?Se\n _______?Sexy?Sexy?Sexy?Sexy?\n _______?Sexy?Sexy?Sexy?Sexy?Sexy\n _______?Sexy?Sexy?Sexy?Sexy?Sexy?S\n ________?Sexy?Sexy____?Sexy?Sexy?se\n _________?Sexy?Se_______?Sexy?Sexy?\n _________?Sexy?Se_____?Sexy?Sexy?\n _________?Sexy?S____?Sexy?Sexy\n _________?Sexy?S_?Sexy?Sexy\n ________?Sexy?Sexy?Sexy\n ________?Sexy?Sexy?S\n ________?Sexy?Sexy\n _______?Sexy?Se\n _______?Sexy?\n ______?Sexy?\n ______?Sexy?\n ______?Sexy?\n ______?Sexy\n ______?Sexy\n _______?Sex\n _______?Sex\n _______?Sex\n ______?Sexy\n ______?Sexy\n _______Sexy\n _______ Sexy?\n ________SexY")
                    #ki.sendImageWithUrl(msg.to,"http://obs-jp.line-apps.com/0he9EB-9d_OhZ4Oxb4VQNFQUR-NHsPFTxeAF9zI1xpNyEFDy5IQll0Il9rZiBSX3VDFFR1clw9MSVQ")                       
                    #ki2.sendImageWithUrl(msg.to,"http://obs-jp.line-apps.com/0h4f8Us-i0a0kFLEezZY8UHjlpZSRyAm0BfU12fXV_PCwtTipPOxghe3IkPHshFS5Pakl0LXcuYi0h")
                    ki3.sendText(msg.to,"⚠️⚠️__AWAS!!! __⚠️⚠️\n___TANPA PERMISI GW___\n🔥 BAKAR GRUP LO NYET!!🔥\n___JANGAN TANYA KENAPA___\n😎KARNA KAMI PUNYA PRINSIF 😎\n  KALO GAK RATA ZOOM MUKA KANG KIBAR\n\n\n──────┅═ই۝ई═┅──────\n【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n       ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n      line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────\n\n\nKAMI TAU APA!!?? KAMI HANYA NUMPANG KIBAR&PLAY\n\n\nDAH GITU AJA TQ\n\n\n(itu)JADI TANGKIS AJE BOSS (itu)\n\n\nGO!!  GO!!  GO!!  GO!!  GO!!\n\n\n________ (go)________ ")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u978f7e8d02351b3d1d4a3973000c2080"}
                    ki4.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u5818cb4404411c2e2e6e6937d172cca8"}
                    ki5.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua028b2a4f96dff4b4a52ae25223e5073"}
                    ki6.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "udfaf52176415b46cb445ae2757ec85f3"}
                    ki7.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u29ad304bbe5e9025b8431e65832a4cfa"}
                    ki8.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u565281632a958bb2795f6434f6872e3b"}
                    ki9.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u30ceda3992172f0861558a2b7a6ef5ab"}
                    ki.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u224e7f2fd36e3565b0756319936450c5"}
                    ki2.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u604ca77dec7ab8d450ae762d5d08cd93"}
                    ki3.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2ca90ea24d7ba639272925d715d8a99c"}
                    ki4.sendMessage(msg)
                    ki5.sendText(msg.to,"★_____TANGKIS NYETT_____★\n\nUDAH GITU  AJA YANG PENTING KIBAR\n\n🔥RATA KAMI SENANG GAK RATA BULY AJE KAMI  DISINI🔥\n\n\n__JADI TANGKIS AJA GO_GO_GO_!!!!!__\n\n______【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】______ ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        acil.sendText(msg.to,"Limit gw njir..")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
            elif msg.text in ["Tag","Tagall","Crot"]:
                group = acil.getGroup(msg.to)
                k = len(group.members)//500
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*500 : (j+1)*500]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    acil.sendMessage(msg) 
            elif msg.text.lower() == 'Inallgrup':
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)

#-----------------------------------------------
            elif msg.text.lower() == 'reinvite':
                if msg.toType == 2:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        acil.sendText(msg.to,"waitting...")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
                        
            elif msg.text in ["@in"]:
              #if msg.from_ in admin:
					G = acil.getGroup(msg.to)
					info = acil.getGroup(msg.to)
					G.preventJoinByTicket = False
					acil.updateGroup(G)
					invsend = 0
					Ticket = acil.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
                                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
                                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
                                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					G = acil.getGroup(msg.to)
					G.preventJoinByTicket = True
                                        acil.updateGroup(G)
                                        print "All_Kickers_Ok!"
                                        G.preventJoinByTicket(G)
                                        acil.updateGroup(G)
#-----------------------------------------------
            elif "B1 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "B2 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "B3 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "B4 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "B5 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "B6 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "B7 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
#-----------------------------------------------
            elif "B8 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
#-----------------------------------------------
            elif "B9 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
#-----------------------------------------------
            elif "B10 in" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
#------------------------------------------------------------------

            elif msg.text.lower() == 'Byeall':
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
#                        acil.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["@out"]:
                    	ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
#-----------------------------------------------
            elif "B1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B8 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B9 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B10 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        ki10.leaveGroup(msg.to)
                    except:
                        pass

            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = acil.getGroup(msg.to)
                acil.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                acil.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
            elif "Bom " in msg.text:
				bctxt = msg.text.replace("Bom ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
#                acil.sendText(msg.to, "Bom chat selesai mbut.😂")
            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki6.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki7.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki8.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki9.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki10.sendText(msg.to,"Ping 􀜁􀇔􏿿")

#-----------------------------------------------
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        acil.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        acil.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        acil.updateGroup(G)
                        ki2.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = acil.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        acil.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = acil.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        acil.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        acil.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        acil.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        acil.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        acil.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        acil.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in ki7mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)
                        ki8.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        acil.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in ki9mid:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                    else:
                        G = ki10.getGroup(op.param1)
                        ki10.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        acil.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki10mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        acil.updateGroup(G)
                        wait["blacklist"][op.param2] = True
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki5.updateGroup(G)
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    acil.sendText(op.param1,"")
	    else:
		acil.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    acil.sendText(op.param1,"")
	    else:
		acil.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    acil.cancelGroupInvitation(op.param1,[contact.mid for contact in acil.getGroup(op.param1).invitee])
		else:
		    acil.sendText(op.param1,"")
	    else:
		acil.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    acil.cancelGroupInvitation(op.param1,[contact.mid for contact in acil.getGroup(op.param1).invitee])
		else:
		    acil.sendText(op.param1,"JANGAN INVITE SEENAKNYA AJA LU...!")
	    else:
		acil.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    acil.sendText(op.param1,"")
	    else:
		acil.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
            	c = Message(to=op.param1, from_=None, text=None, contentType=13)
                #c.contentMetadata={'mid':'u5818cb4404411c2e2e6e6937d172cca8'}
                #acil.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/0hPV_dx45gD3liHSNSj09wLl5YARQVMwkxGntGT0YUVhsdeh8oXnIUGUMYVUBGfUgvX3JCHUMUVk8Y")
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    acil.sendText(op.param1,str(wait["message"]))
                    acil.sendMessage(c)
                    ki.sendText(op.param1,str(wait["message"]))
                    ki.sendMessage(c)
                    ki2.sendText(op.param1,str(wait["message"]))
                    ki2.sendMessage(c)
                    ki3.sendText(op.param1,str(wait["message"]))
                    ki3.sendMessage(c)
                    ki4.sendText(op.param1,str(wait["message"]))
                    ki4.sendMessage(c)
                    ki5.sendText(op.param1,str(wait["message"]))
                    ki5.sendMessage(c)
                    ki6.sendText(op.param1,str(wait["message"]))
                    ki6.sendMessage(c)
                    ki7.sendText(op.param1,str(wait["message"]))
                    ki7.sendMessage(c)
                    ki8.sendText(op.param1,str(wait["message"]))
                    ki8.sendMessage(c)
                    ki9.sendText(op.param1,str(wait["message"]))
                    ki9.sendMessage(c)
                    ki10.sendText(op.param1,str(wait["message"]))
                    ki10.sendMessage(c)
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open Kick finish-----#
#------invite Kick start------#
        if op.type == 13:
            if wait["inviteprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------invite Kick finish-----#
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = acil.getContact(op.param2).displayName
                            Np = acil.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n� " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        acil.sendText(op.param1,"═════════SIDER═════════\n" + nick[0] + "\n" +  wait["sider1"])
                                        acil.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        acil.sendText(op.param1,"═════════SIDER═════════\n" + nick[0] + "\n" +  wait["sider1"])
                                        acil.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    acil.sendText(op.param1,"═════════SIDER═════════\n" + nick[0] + "\n" +  wait["sider1"])
                                    acil.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
        
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = acil.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                acil.sendText
        if op.type == 17:
          if wait["wcOn"] == True:
            	ginfo = acil.getGroup(op.param1)
            	contact = acil.getContact(op.param2)
            	c = Message(to=op.param1, from_=None, text=None, contentType=13)
            	c.contentMetadata={'mid':op.param2}
                acil.sendText(op.param1, "🄷🄰🄻🄻🄾... " + acil.getContact(op.param2).displayName +  "\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n█░░╔╦╗ ╔╗░░█\n█░░─║─ ║║░░█\n█░░─╩ ─╚╝░░█\n\n⛦•••{ " + str(ginfo.name) + " }•••⛦" + "\n\nBudayakan Cek Note\nDan Semoga Betah Disini..\nJangan Lupa Nikung Kak,..Yehkan..\n\nDah Gitu Ajah..\n\n\n===❍•••{☠ʟᴇᴠᴀɴᴀ☠}•••❍===\n\n\n"+"Owner Grup " + str(ginfo.name) +  " :\n "  + ginfo.creator.displayName + "\nWaktu Masuk: " + datetime.now().strftime('%H:%M:%S'))
            	acil.sendMessage(c)
            	acil.sendImageWithUrl(op.param1,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
            	print ("MEMBER JOIN TO GROUP")
        if op.type == 15:
          if wait["leftOn"] == True:
            	c = Message(to=op.param1, from_=None, text=None, contentType=13)
            	c.contentMetadata={'mid':op.param2}
            	acil.sendMessage(c)
            	acil.sendText(op.param1,acil.getContact(op.param2).displayName + "\n" + wait["leftgc"])
            	print ("MEMBER HAS LEFT THE GROUP")
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
        if op.type == 59:
            print op
    except Exception as error:
        print error
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = acil.getProfile()
                profile.displayName = wait["cName"] + nowT
                acil.updateProfile(profile)
            time.sleep(0.30)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
while True:
    try:
        Ops = acil.fetchOps(acil.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(acil.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            acil.Poll.rev = max(acil.Poll.rev, Op.revision)
            bot(Op)

