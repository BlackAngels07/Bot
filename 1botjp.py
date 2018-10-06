# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

cl = LINETCR.LINE() #Selfmu
cl.login(token="ExdyIgxc6xu75wDhnXx5.l+YDu0nPM1WEapmG1C74fq.xtDC+oTuqB09Ix19E+ZUwH/AQVAMEy1ATebAyqzKnbM=")
cl.loginResult()

print u"Keren vril dah login"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""  
꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂
           ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ
╠═════════════════
╠☣☣General Command☣☣
╠═════════════════
╠ ͜͡✪͜͡✪➢ Id
╠ ͜͡✪͜͡✪➢ Me
╠ ͜͡✪͜͡✪➢ Help
╠ ͜͡✪͜͡✪➢ Copy
╠ ͜͡✪͜͡✪➢ Gift
╠ ͜͡✪͜͡✪➢ Pic
╠ ͜͡✪͜͡✪➢ Mid
╠ ͜͡✪͜͡✪➢ Nk
╠ ͜͡✪͜͡✪➢ Cover
╠ ͜͡✪͜͡✪➢ Myname
╠ ͜͡✪͜͡✪➢ Creator
╠ ͜͡✪͜͡✪➢ Blocklist
╠ ͜͡✪͜͡✪➢ Clearban
╠ ͜͡✪͜͡✪➢ Friendlists
╠══════════════════
╠☣☣Chat Related☣☣
╠══════════════════
╠ ͜͡✪͜͡✪➢ Pp
╠ ͜͡✪͜͡✪➢ Cover
╠ ͜͡✪͜͡✪➢ Music
╠ ͜͡✪͜͡✪➢ Image
╠ ͜͡✪͜͡✪➢ Myvid
╠ ͜͡✪͜͡✪➢ Mybio
╠ ͜͡✪͜͡✪➢ Pp group
╠ ͜͡✪͜͡✪➢ Groupname
╠ ͜͡✪͜͡✪➢ Group id
╠ ͜͡✪͜͡✪➢ Get vid
╠ ͜͡✪͜͡✪➢ Gbroadcast
╠ ͜͡✪͜͡✪➢ Cbroadcast
╠ ͜͡✪͜͡✪➢ Respon on/off
╠ ͜͡✪͜͡✪➢ Sider on/off
╠══════════════════
╠☣☣Command Mimic ☣☣
╠══════════════════
╠ ͜͡✪͜͡✪➢ Mimic add
╠ ͜͡✪͜͡✪➢ Mimic del
╠ ͜͡✪͜͡✪➢ Mimic list
╠ ͜͡✪͜͡✪➢ Mimic on
╠ ͜͡✪͜͡✪➢ Mimic off
╠══════════════════
╠☣☣ Command group ☣☣
╠══════════════════
╠ ͜͡✪͜͡✪➢ Gurl
╠ ͜͡✪͜͡✪➢ Cek
╠ ͜͡✪͜͡✪➢ Read
╠ ͜͡✪͜͡✪➢ Gpict
╠ ͜͡✪͜͡✪➢ Minfo
╠ ͜͡✪͜͡✪➢ Info
╠ ͜͡✪͜͡✪➢ Vkick
╠ ͜͡✪͜͡✪➢ Ourl
╠ ͜͡✪͜͡✪➢ Kill
╠ ͜͡✪͜͡✪➢ Fuck
╠ ͜͡✪͜͡✪➢ Nuke
╠ ͜͡✪͜͡✪➢ Curl
╠ ͜͡✪͜͡✪➢ Reboot
╠ ͜͡✪͜͡✪➢ Runtime
╠ ͜͡✪͜͡✪➢ Set
╠ ͜͡✪͜͡✪➢ Banlist
╠ ͜͡✪͜͡✪➢ Blocklist
╠ ͜͡✪͜͡✪➢ Clearban
╠ ͜͡✪͜͡✪➢ Ginfo
╠ ͜͡✪͜͡✪➢ Creator
╠ ͜͡✪͜͡✪➢ Invite:on
╠ ͜͡✪͜͡✪➢ Groups
╠ ͜͡✪͜͡✪➢ Sp/speed
╠ ͜͡✪͜͡✪➢ Tag / Ats
╠ ͜͡✪͜͡✪➢ Cancel
╠ ͜͡✪͜͡✪➢ Link on / off
╠ ͜͡✪͜͡✪➢ Sider on / off
╠ ͜͡✪͜͡✪➢ Respon on /off
╠ ͜͡✪͜͡✪➢ Welcome on /off
╠ ͜͡✪͜͡✪➢ Protect on / off
╠ ͜͡✪͜͡✪➢ Share on / off
╠ ͜͡✪͜͡✪➢ Autoadd on / off
╠ ͜͡✪͜͡✪➢ Contact on / off
╠ ͜͡✪͜͡✪➢ Autojoin on / off
╠ ͜͡✪͜͡✪➢ Autocancel on /off
╠ ͜͡✪͜͡✪➢ Autoleave on /off
╠ ͜͡✪͜͡✪➢ Autocomment on /off
╠ ͜͡✪͜͡✪➢ Linkprotect on /off
╠ ͜͡✪͜͡✪➢ Inviteprotect on /off
╠ ͜͡✪͜͡✪➢ Cancelprotect on /off
╠═════════════════════
line.me/ti/p/~avrilia_ganteng
"""""
#TEAM BOT PROTECTION
#DKZ TEAM
#OPEN ORDER
#BOT PROTECTION
#SELFBOT PROTECT
#SIRI LEGEND
#OWNERS BOTS
#ADMIN BOTS
#STAFF BOTS
#PROTECT GROUP/EVENT

#Scrif yg gk sYa taro di help bnyak
#cari ndri bljar creatif
#def dan remote khusus only sdah ada semua
#silahkan di kreasi

line.me/ti/p/~avrilia_ganteng
hem=""

KAC=[cl]
mid = cl.getProfile().mid
Bots = [mid]
admsa = "u2ffc9d5343699b5c1e00f320d5cef815"
admin = "u2ffc9d5343699b5c1e00f320d5cef815"

mulai = time.time()

wait = {
    "likeOn":True,
    "alwaysRead":False,
    "detectMention":False,    
    "kickMention":False,
    "steal":True,
    'pap':{},
    'invite':{},
    "spam":{},
    "sider":{},
    "members":1,
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":50},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'alwasyRead':False,
    "detectMention":False,
    'point':False,
    'sidermem':False,
    'message':"Thanks For Add Me\nJangan Lupa Add My Creator Kak.....\n\n╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n Creator By:\n   http://line.me/ti/p/~avrilia_ganteng\n╚═────────┅═ই۝ई═┅─────────",
    "lang":"JP",
    "comment":"Auto Like By:\n╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_ganteng\n╚═────────┅═ই۝ई═┅─────────",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "winvite":False,
    "cyduk":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "displayname":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "mid":{},
    "protect":False,
    "sendMessage":True,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "welcome":False,
    "re":False
    
    
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
    "target":{},
    }
    
settings = {
    "simiSimi":{}
    }
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

res = {
    'num':{},
    'us':{},
    'au':{},
    }
 
setTime = {}
setTime = wait2['setTime']


contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

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
        bb += "➢ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
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

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"    
            
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
      
def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': objectId,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudio(self, to_, path):
        M = Message(to=to_,contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
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
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True
        
def sendAudioWithURL(self, to_, url):
        path = 'pythonLiness.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e

def waktu(secs):
      mins, secs = divmod(secs,60)
      hours, mins = divmod(mins,60)
      return '[ %02d : Jam  %02d : Menit  %02d : Detik ]' % (hours, mins, secs)
       

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

def sendMessage(to, text, contentMetadata={}, contentType=0):
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
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e    
  
            if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\☠ " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Nahhhh " + "❂•••{ " + Name + " }•••❂" + "\nSinih Kuy")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        cl.sendText(op.param1, "Nahhhh " + "❂•••{ " + Name + " }•••❂" + "\nNgapain")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    cl.sendText(op.param1, "Nahhhh " + "❂•••{ " + Name + " }•••❂" + "\nCctv...")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass   
            
                    
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
                                cl.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))     
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + " Ada Apa??,Kangen Yehkan Ma Gw ", cName + " Kenapa si??...Kalo Kangen Pc Aja!!!"]
                     balas1 = "Cieee Ppnya Ahahahaha"
                     ret_ = "'"+ random.choice(balas)
                     image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                           'STKPKGID': '1066653',
                                                           'STKTXT': '[]',
                                                           'STKVER': '1',
                                                           'STKID':'2754655'
                                                         }
                                  cl.sendMessage(msg)                                
                                  break            
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + " Ngapain Ngetag?, ", cName + " Kenapa Tag saya?,  " + cName + "?", "Ada Perlu apa, " + cName + "?","Tag doang tidak perlu., ", "Tersummon -_-, "]
                     ret_ = "**Auto Respond** " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break                 
            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)   
            if msg.contentType == 13:
                  if msg.from_ in admin:
                    if wait["wblacklist"] == True:
                       if msg.contentMetadata["mid"] in wait["blacklist"]:
                         cl.sendText(msg.to,"Is already banned")
                       wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"has been banned by :")

            elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                       del wait["blacklist"][msg.contentMetadata["mid"]]
                       cl.sendText(msg.to,"Has been Unbanned deleted by :")
                       wait["dblacklist"] = False

                    else:
                       wait["dblacklist"] = False
                       kk.sendText(msg.to,"is not in banned!")
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)        
        if op.type == 17:
          if wait["welcome"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            cl.sendText(op.param1, "╠══════════════════\n╠ ͜͡✪͜͡✪➢ Nahh Haloo Kakak\n╠ ͜͡✪͜͡✪➢ 🅆🄴🄻🄲🄾🄼🄴 🅃🄾\n_______________________________ \n╠ ͜͡✪͜͡✪➢ Group " + str(ginfo.name) + "\n╠══════════════════")
            cl.sendText(op.param1, "╠══════════════════\n╠ ͜͡✪͜͡✪➢ Owner Grup " + str(ginfo.name) + " :\n╠ ͜͡✪͜͡✪➢" + ginfo.creator.displayName)
            print "MEMBER HAS LEFT THE GROUP"
        if op.type == 15:
            if op.param2 in admin:
                return
            cl.sendText(op.param1, "╠══════════════════\n╠ ͜͡✪͜͡✪➢ Nah Lohhhhhh Napa Tuh\n╠ ͜͡✪͜͡✪➢ Baper Kali Tuh Orang\n╠══════════════════")
            print "MEMBER HAS LEFT THE GROUP" 
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u7d1ac07d2036b36745783a0a1992b2ba":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"success")
                           
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to," ͜͡✪͜͡✪➢" + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         cl.findAndAddContactsByMid(invite)
                                         cl.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
                
       
#--------------------------------------------------------------------     
            elif msg.text in ["Key","Crot","Help"]:
                cl.sendText(msg.to,helpMessage)
 #---------------------------------------------------------
            elif msg.text in ["Pp","pp"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
         
            elif msg.text in ["Cover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
                    
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Invite"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"Send contact")
#---------------------------------------------------------
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Di Groups")
 #---------------------------------------------------------
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")

            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
                
            elif "Pp group" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            
#---------------------------------------------------------
            
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                
          
#-------------elif msg.text in ["Alwaysread on"]:
	
	       

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Menolak Undangan")
                        else:
                            cl.sendText(msg.to,"Saya Menolak Semua Undangan")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
    #---------------------------------------------------------            
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
 #---------------------------------------------------------
 
            elif "Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
               
 #---------------------------------------------------------        
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)

 #---------------------------------------------------------
 
            elif "Reboot" in msg.text:
                print "[Command]Reboot"
                try:
                 cl.sendText(msg.to,"Bot Restarted...")
                 cl.sendText(msg.to,"Success Restart")
                 restart_program()
                except:
                 cl.sendText(msg.to,"Please wait")
                restart_program()
                pass
            
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])

             #---------------------------------------------------------       
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to," Done update names " + string + " ☠")

#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag","Cuy","Hem","Crit"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                  if jml <= 100:
                      tagall(msg.to, nama)
                  if jml > 100 and jml < 500:
                      for i in range(0,99):
                          nm1 += [nama[i]]
                      tagall(msg.to, nm1)
                      for j in range(100, len(nama)-1):
                          nm2 += [nama[j]]
                      tagall(msg.to, nm2)
                      for k in range(200, len(nama)-1):
                          nm3 += [nama[k]]
                      tagall(msg.to, nm3)
                      for l in range(300, len(nama)-1):
                          nm4 += [nama[l]]
                      tagall(msg.to, nm4)
                      for m in range(400, len(nama)-1):
                          nm5 += [nama[m]]
                      tagall(msg.to, nm5)
                  cnt = Message()
                  cnt.text = "❂••••••{Mention By:BLACK ANGELS}••••••❂"
                  cnt.to = msg.to
                  cl.sendMessage(cnt)
                  if jml > 500:
                      cnt = Message()
                      cnt.text = "❂•••{BLACK ANGELS}•••❂\n\n"+ datetime.now().strftime('%H:%M:%S')
                      cnt.to = msg.to
                      cl.sendMessage(cnt)
#-------------Fungsi Tag All Finish--------------#

            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
#---------------------------------------------------------
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           

            elif "Gbroadcast: " in msg.text:
                bc = msg.text.replace("Gbroadcast: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.sendText(i, bc)
                    
            elif "Cbroadcast: " in msg.text:
                bc = msg.text.replace("Cbroadcast: ","")
                gid = cl.getAllContactIds()
                for i in gid:
                    cl.sendText(i, bc)
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
#---------------------------------------------------------
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[Already on] ")
                    else:
                        cl.sendText(msg.to,"[Already on] ")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"[Already on] ")
                    else:
                        cl.sendText(msg.to,"[Already off] ")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off ")
                    else:
                        cl.sendText(msg.to,"Already off ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off ")
                    else:
                        cl.sendText(msg.to,"Already off ")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
            elif msg.text.lower() == 'linkprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on  ")
                    else:
                        cl.sendText(msg.to,"Already on ")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
            elif msg.text.lower() == 'autojoin on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")

 #---------------------------------------------------------
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait ")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text in ["Allprotect on","Mode on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")      
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Allprotect on done")
            elif msg.text in ["Allprotect off","Mode Off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                    else:
                        cl.sendText(msg.to,"Invite OFF")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")      
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text.lower() == 'autojoin off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set off ")
                    else:
                        cl.sendText(msg.to,"Autojoin set off ")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set off ")
                    else:
                        cl.sendText(msg.to,"Autojoin set off ")
                        
            
                   
            elif msg.text in ["Respontag on","Autorespon:on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                cl.sendText(msg.to,"Auto respon tag On")
              
            elif msg.text in ["Respontag off","Autorespon:off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"Auto respon tag Off")
 
            elif msg.text in ["Autoread off","Read:off"]:
               if wait["cyduk"] ==False:
               	if wait["lang"] == "JP":
                      cl.sendText(msg.to,"Auto read Off")
               else:
                 if wait["cyduk"] == False:
                	if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Auto read Off")
                       
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set off ")
                    else:
                        cl.sendText(msg.to,"Protect set off ")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set off ")
                    else:
                        cl.sendText(msg.to,"It is already open ")
            elif msg.text in ["Linkprotect off","linkprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Linkprotect set off ")
                    else:
                        cl.sendText(msg.to,"Linkprotect set off ")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Linkprotect set off ")
                    else:
                        cl.sendText(msg.to,"Linkprotect set off ")
                        
            elif msg.text in ["Wc on","Welcome on"]:
                if wait["welcome"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                else:
                    wait["welcome"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Wc off","Welcome off"]:
                if wait["welcome"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off ")
                else:
                    wait["welcome"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off ")         
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Inviteprotect set off ")
                    else:
                        cl.sendText(msg.to,"Inviteprotect set off ")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Inviteprotect set off ")
                    else:
                        cl.sendText(msg.to,"It is already open ")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancelprotect set off ")
                    else:
                        cl.sendText(msg.to,"Cancelprotect set off ")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancelprotect set off ")
                    else:
                        cl.sendText(msg.to,"Cancelprotect set off ")
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave on","Autoleave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
            elif msg.text in ["Autoleave off","Autoleave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoleave set off ")
                    else:
                        cl.sendText(msg.to,"Autoleave set off ")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoleave set off ")
                    else:
                        cl.sendText(msg.to,"Autoleave set off ")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set off ")
                    else:
                        cl.sendText(msg.to,"Share set off ")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set off ")
                    else:
                        cl.sendText(msg.to,"Share set off ")

            elif msg.text.lower() == 'set':
                md ="╔═────────┅═ই{ [ $3TINGS] }ई═┅────────\n"                                                                                      
                if wait["contact"] == True: md+="╠ ͜͡✪͜͡✪➢Contact on  \n"
                else: md+="╠ ͜͡✪͜͡✪➢Contact off  \n"
                if wait["autoJoin"] == True: md+="╠ ͜͡✪͜͡✪➢Autojoin on \n"
                else: md +="╠ ͜͡✪͜͡✪➢Autojoin off \n"
                if wait["autoCancel"]["on"] == True:md+="╠ ͜͡✪͜͡✪➢Autocancel:" + str(wait["autoCancel"]["members"]) + " 🎵\n"
                else: md+= "╠ ͜͡✪͜͡✪➢Autocancel off \n"
                if wait["leaveRoom"] == True: md+="╠ ͜͡✪͜͡✪➢Autoleave on \n"
                else: md+="╠ ͜͡✪͜͡✪➢Autoleave off \n"
                if wait["timeline"] == True: md+="╠ ͜͡✪͜͡✪➢Share on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Share off \n"
                if wait["autoAdd"] == True: md+="╠ ͜͡✪͜͡✪➢Autoadd on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Autoadd off \n"
                if wait["commentOn"] == True: md+="╠ ͜͡✪͜͡✪➢Autocomment on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Autocomment off \n"
                if wait["protect"] == True: md+="╠ ͜͡✪͜͡✪➢Protect on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Protect off\n"
                if wait["linkprotect"] == True: md+="╠ ͜͡✪͜͡✪➢Linkprotect on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Linkprotect off \n"
                if wait["inviteprotect"] == True: md+="╠ ͜͡✪͜͡✪➢Inviteprotect on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Inviteprotect off \n"
                if wait["welcome"] == True: md+=" ╠ ͜͡✪͜͡✪➢Welcome on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Welcome off \n" 
                if wait["detectMention"] == True: md+=" ╠ ͜͡✪͜͡✪➢Respon on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Respon off \n" 
                if wait["sider"] == True: md+=" ╠ ͜͡✪͜͡✪➢Sider on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Sider off \n" 
                if wait["cancelprotect"] == True: md+="╠ ͜͡✪͜͡✪➢Cancel Protect on \n"
                else:md+="╠ ͜͡✪͜͡✪➢Cancel Protect off \n╚═────────┅═ই✪͜͡✪۝✪͜͡✪ई═┅─────────"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {}
                cl.sendMessage(msg)
 
            elif msg.text.lower() == 'runtime':
             eltime = time.time() -mulai
             van = "[[[Bot Bergerak Dalam Waktu]]]\n" +waktu(eltime)
             cl.sendText(msg.to,van)

                
#---------------------------------------------------------
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                #cl.sendText(msg.to,"❂•••••••••••✧•••••••••••❂")
                #cl.sendText(msg.to,"▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█")
                cl.sendText(msg.to,"──────┅═ই۝ई═┅──────")
                cl.sendMessage(msg)
                #h = cl.getContact(mid)
                #cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                cl.sendText(msg.to,"──────┅═ই۝ई═┅──────")
                #cl.sendText(msg.to,"▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█")
                #cl.sendText(msg.to,"❂•••••••••••✧•••••••••••❂")
                cl.sendText(msg.to,"[Gue Ini Mahh...!!!]")
                
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid':"u7d1ac07d2036b36745783a0a1992b2ba"}
                cl.sendText(msg.to,"────────┅═ই✪͜͡ ۝ ͜͡✪ई═┅─────────")
                cl.sendText(msg.to,"❂•••••••••••✧✧✧••••••••••❂")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"❂•••••••••[ CREATOR ]••••••••❂")
                cl.sendText(msg.to,"────────┅═ই✪͜͡ ۝ ͜͡✪ई═┅─────────")
                cl.sendText(msg.to,"[Add Aja All,Creator Tamvan Itu...!!!]")
      #---------------------------------------------------------          
      


      
            elif msg.text in ["Cancelall"]:
                if msg.from_ in admin:
                  gid = cl.getGroupIdsInvited()
                  for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"Ok...")	
                    
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album??")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Sider on" in msg.text:
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
                cl.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off")
                else:
                    cl.sendText(msg.to, "Cek dulu kak set nya 😇")    
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)

                    
            elif msg.text in ["Clear ban","Clearban"]:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Removed banlist user target succes.")       
                    
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
                    
            elif msg.text in ["Autoadd on","Autoadd:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on ")
                    else:
                        cl.sendText(msg.to,"Already on ")
            elif msg.text in ["Autoadd off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoadd set off ")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autoadd set off ")
                    else:
                        cl.sendText(msg.to,"Autoadd set off ")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like By:\n╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_ganteng\n╚═────────┅═ই۝ई═┅─────────")
                    else:
                        cl.sendText(msg.to,"Auto Like By:\n╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_ganteng\n╚═────────┅═ই۝ई═┅─────────")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")           
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
          
          

            elif "Gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Already off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
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
                                    cl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.eaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)


            elif msg.text == "Lurk":
                    cl.sendText(msg.to, "Yang suka ngintip")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text in ["Glist","Groups","Group"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠ ͜͡✪͜͡✪➢ %s\n" % (cl.getGroup(i).name +"➡["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"╠══════════════════\n╠ ☣☣☣ My Group ☣☣☣\n╠══════════════════\n"+ h +"\n☣ Total Group ☣ = " +""+str(len(gid))+"")

            elif msg.text == "Lurkers":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "╠ ͜͡✪͜͡✪➢\n"

                        cl.sendText(msg.to, "╔══════════════════════\n║         {YANG SUKA NGINTIP}\n╠══════════════════════\n╠ ͜͡✪͜͡✪➢"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Nahhhhhhhhhhh")
                        
                        
				
#-----------------------------------------------------------
        

            elif ("Fuck " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
                           
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Vk " in msg.text:                  
                       nk0 = msg.text.replace("Beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
                                    cl.sendText(msg.to,"Good Bye")

#-------------------------------------------------
#-----------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")


#-----------------------------------------------------------)
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
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
                      cl.sendText(msg.to,"Succes Bosque")
                   except:
                      pass
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    kk.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
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
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    kk.sendText(msg.to,"Error")
#-----------------------------------------------------------

            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Ok...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes")
                                except Exception as e:
                                    print e
                                    

            elif msg.text in ["Mybackup","backup"]:
                    try:
                        client.updateDisplayPicture(backup.pictureStatus)
                        client.updateProfile(backup)
                        sendMessage(msg.to, "Backup done")
                    except Exception as e:
                        sendMessage(msg.to, str(e))
                    

#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------<------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------

            
                
            elif msg.text in ["Sp","Speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress Speeds ...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time)) 

#----------------------------------------------------------

#------------------------------------------------------------------	
            elif "Cover @" in msg.text:            
                print "[Command]cover executing"
                _name = msg.text.replace("Cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Ok")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]Cover executed"			
#------------------------------------------------------------------
            elif "Pp @" in msg.text:            
                print "[Command]pic executing"
                _name = msg.text.replace("Pp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]Pic executed"			
 #------------------------------------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif msg.text in ["Bans:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbans:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "➡" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "➡" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "Daftar Hitam")

            elif "Nuke" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuke","")
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    h = cl.getProfile()
                    cl.sendText(msg.to,"────────┅═ই✪͜͡ ۝ ͜͡✪ई═┅───────── ")
                    cl.sendText(msg.to,"▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█ ")
                    cl.sendText(msg.to,"🅆🄴🄻🄲🄾🄼🄴 🅃🄾\n🄺🄸🄲🄺🄴🅁 🄰🅁🄴🄽🄰\n_______________________________ ")
                    #cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/0he9EBKW8QOhZ4Oxb3ih5FQUR-NHsPFTxeAF9zI1xpNyEFDy5IQll0Il9rZiBSX3VDFFR1clw9MSVQ")
                    cl.sendText(msg.to,"⚠️⚠️__AWAS!!! __⚠️⚠️\n___TANPA PERMISI GW___\n🔥 BAKAR GRUP LO NYET!!🔥\n___JANGAN TANYA KENAPA___\n😎KARNA KAMI PUNYA PRINSIF 😎\n  KALO GAK RATA ZOOM MUKA KANG KIBAR\n\n\n──────┅═ই۝ई═┅──────\n【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n       ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n      line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────\n\n\nKAMI TAU APA!!?? KAMI HANYA NUMPANG KIBAR&PLAY\n\n\nDAH GITU AJA TQ\n\n\n(itu)JADI TANGKIS AJE BOSS (itu)\n\n\nGO!!  GO!!  GO!!  GO!!  GO!!\n\n\n________ (go)________ ")
                    cl.sendText(msg.to,"❂•••••••••••✧•••••••••••❂ ")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)   
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u37b0cb6a5b9750c3a376e92a81307d24"}
                    cl.sendMessage(msg)
                    cl.sendText(msg.to,"❂•••••••••••✧•••••••••••❂ ")
                    cl.sendText(msg.to,"★_____TANGKIS NYETT_____★\n\nUDAH GITU  AJA YANG PENTING KIBAR\n\n🔥RATA KAMI SENANG GAK RATA BULY AJE KAMI  DISINI🔥\n\n\n__JADI TANGKIS AJA GO_GO_GO_!!!!!__\n\n______【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】______ ")
                    cl.sendText(msg.to,"▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█ ")
                    cl.sendText(msg.to,"────────┅═ই✪͜͡ ۝ ͜͡✪ई═┅───────── ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg,to,"Group cleanse")


            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
    
            elif msg.text in ["Mangat","Absen"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"kadir")
                    cl.sendText(msg.to,"kadir")
                    cl.sendText(msg.to,"kadir")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
                    
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
            elif 'Say' in msg.text:
                 psn = msg.text.replace("record ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')          
            elif ("Mimic add " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Mimic del " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Mimic list"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Already on ")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                cl.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                cl.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                cl.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                cl.sendVideoWithURL(msg.to,wait["pap"])
            elif "TL:" in msg.text:
              if msg.toType == 2:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])

            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )

#----------------------------------------------- 

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
			cl.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
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
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n▶ " + Nama
                        wait2['ROM'][op.param1][op.param2] = "▶ " + Nama
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    cl.sendText
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
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
            
