# -*- coding: utf-8 -*-
#Vipro_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

acil = LINETCR.LINE() 
acil.login(token="ExgaaSxL4WKUZQSlUL9a.FrRaFsa2S2DfEdOkgzkYUG.bvup/S9DGazFODrHY+6QRnh0I2vWvgR2qKKmWFQhBNs=")
acil.loginResult()

pb1 = LINETCR.LINE() 
pb1.login(token="Excm8z4UxfLhbmkKtKR5.VxTn0rMR1ZQZ31qVTyQkzq.hrGmmcoLW1+H/EAtcoFPQdPLVT4LA6ZHF0ou+g9sFmg=")
pb1.loginResult()

pb2 = LINETCR.LINE() 
pb2.login(token="Ex09yBlEHiyffrhsUSj7.oISUxqs9khqTd3kgBWDsDW.j7jkXcF3yyTWl7Pv3/WJLuoJIW5Wzk0+DoGhoMk4an4=")
pb2.loginResult()
print "Avrilia-Login Success\n\n=====[Sukses Login]====="


reload(sys)
sys.setdefaultencoding('utf-8')

pisMessage ="""
╔═──────┅═ই۝ई═┅──────
║꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂
║           ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ
╠═──────┅═ই۝ई═┅──────
╠ ͜͡✪͜͡✪➢Me
╠ ͜͡✪͜͡✪➢Add
╠ ͜͡✪͜͡✪➢Cn "text"
╠ ͜͡✪͜͡✪➢Clockname "text"
╠ ͜͡✪͜͡✪➢TL:"text"
╠ ͜͡✪͜͡✪➢Ban:"mid"
╠ ͜͡✪͜͡✪➢Unban:"mid"
╠ ͜͡✪͜͡✪➢Bl:on
╠ ͜͡✪͜͡✪➢Unbl:on
╠ ͜͡✪͜͡✪➢Mcheck
╠ ͜͡✪͜͡✪➢Mybio:
╠ ͜͡✪͜͡✪➢Mybots
╠ ͜͡✪͜͡✪➢Mymid
╠ ͜͡✪͜͡✪➢Mygroups
╠ ͜͡✪͜͡✪➢Message set:"text"
╠ ͜͡✪͜͡✪➢Message confirm
╠ ͜͡✪͜͡✪➢Msg add-"text"
╠ ͜͡✪͜͡✪➢Com set:"text"
╠ ͜͡✪͜͡✪➢Comment
╠ ͜͡✪͜͡✪➢Comban/del/cek
╠ ͜͡✪͜͡✪➢Help set:"text"
╠ ͜͡✪͜͡✪➢Change
╠ ͜͡✪͜͡✪➢Gn "text"
╠ ͜͡✪͜͡✪➢Clink/Curl
╠ ͜͡✪͜͡✪➢Kick:"mid"
╠ ͜͡✪͜͡✪➢Invite:"mid"
╠ ͜͡✪͜͡✪➢Creator
╠ ͜͡✪͜͡✪➢Contact
╠ ͜͡✪͜͡✪➢Cancel/Bcancel
╠ ͜͡✪͜͡✪➢Gcancel:"jumlah"
╠ ͜͡✪͜͡✪➢Gcancelall
╠ ͜͡✪͜͡✪➢Ginfo
╠ ͜͡✪͜͡✪➢Prank in (Masukin bot)
╠ ͜͡✪͜͡✪➢Prank out (Keluarin bot)
╠ ͜͡✪͜͡✪➢Setlastpoint
╠ ͜͡✪͜͡✪➢Cctv
╠ ͜͡✪͜͡✪➢Glink
╠ ͜͡✪͜͡✪➢Spam on/of "jumlah/text"
╠ ͜͡✪͜͡✪➢Gurl
╠ ͜͡✪͜͡✪➢Sc:"mid"
╠ ͜͡✪͜͡✪➢Blocklist
╠ ͜͡✪͜͡✪➢Banlist
╠ ͜͡✪͜͡✪➢Update
╠ ͜͡✪͜͡✪➢Creator
╠ ͜͡✪͜͡✪➢Sc "@"
╠ ͜͡✪͜͡✪➢Fuck "@"
╠ ͜͡✪͜͡✪➢Sikat "@"
╠ ͜͡✪͜͡✪➢Spam "@"
╠ ͜͡✪͜͡✪➢Ban "@" 
╠ ͜͡✪͜͡✪➢Unban "@"
╠ ͜͡✪͜͡✪➢Copy "@"
╠ ͜͡✪͜͡✪➢Nuke
╠ ͜͡✪͜͡✪➢Backup
╠ ͜͡✪͜͡✪➢Tag
╠ ͜͡✪͜͡✪➢Bc "text"
╠ ͜͡✪͜͡✪➢Say "text"
╠ ͜͡✪͜͡✪➢Kick@mbl "kick blacklist"
╠ ͜͡✪͜͡✪➢Ping
╠ ͜͡✪͜͡✪➢Sett
╚═──────┅═ই۝ई═┅──────
                         ASSISTAN
╔═──────┅═ই۝ई═┅──────
╠ ͜͡✪͜͡✪➢All:
╠ ͜͡✪͜͡✪➢Allbio:
╠ ͜͡✪͜͡✪➢All mid
╠ ͜͡✪͜͡✪➢Respon
╠ ͜͡✪͜͡✪➢B:out
╠ ͜͡✪͜͡✪➢B1-2 mid
╠ ͜͡✪͜͡✪➢B1-2name "text"
╠ ͜͡✪͜͡✪➢B1-2
╠ ͜͡✪͜͡✪➢B1-2 gift
╠ ͜͡✪͜͡✪➢B come
╠ ͜͡✪͜͡✪➢B1-2 in
╠ ͜͡✪͜͡✪➢B1-2 bye
╚═──────┅═ই۝ई═┅──────
                         SETTINGS
╔═──────┅═ই۝ई═┅──────
╠ ͜͡✪͜͡✪➢Contact:on/off
╠ ͜͡✪͜͡✪➢Add:on/off
╠ ͜͡✪͜͡✪➢Join:on/off
╠ ͜͡✪͜͡✪➢Leave:on/off
╠ ͜͡✪͜͡✪➢Share:on/off
╠ ͜͡✪͜͡✪➢Com:on/off
╠ ͜͡✪͜͡✪➢Clock:on/off
╚═──────┅═ই۝ई═┅──────
                          PROTECT
╔═──────┅═ই۝ई═┅──────
╠ ͜͡✪͜͡✪➢Pro:on/off
╠ ͜͡✪͜͡✪➢Prolink:on/off
╠ ͜͡✪͜͡✪➢Proinvite:on/off
╠ ͜͡✪͜͡✪➢Procancel:on/off
╠═──────┅═ই۝ई═┅──────
║             ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ
║http://line.me/ti/p/~avrilia_ganteng
╚═──────┅═ই۝ई═┅──────

"""
helo="====I AM SELF Avrilia"

KAC=[acil,pb1,pb2]
mid = acil.getProfile().mid
pb1mid = pb1.getProfile().mid
pb2mid = pb2.getProfile().mid
Bots=[mid,pb1mid,pb2mid]
admsa = "u7d1ac07d2036b36745783a0a1992b2ba"

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"тнαикѕ fσя α∂∂ мє...\nBY:\n──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/~avrilia_quester\n──────┅═ই۝ई═┅──────""",
    "lang":"JP",
    "comment1":"BY:\n──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/~avrilia_quester\n──────┅═ই۝ई═┅──────",
    "comment":"Thanks For Add Me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"──┅═͜͡✥A⃟⃟V⃟⃟R⃟⃟ I⃟⃟L⃟⃟❂➤",
    "cNames":"──┅═͜͡✥A⃟⃟V⃟⃟R⃟⃟ I⃟⃟L⃟⃟❂➤",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "copy":True,
    "copy2":"target",
    "target":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


contact = acil.getProfile()
backup = acil.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

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
                    acil.cancelGroupInvitation(op.param1, matched_list)
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
                if msg.from_ == "u7d1ac07d2036b36745783a0a1992b2ba":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            acil.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = acil.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            acil.updateGroup(G)
                        except:
                            acil.sendText(msg.to,"Suksess")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    acil.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                acil.like(url[25:58], url[66:], likeType=1001)
                pb1.like(url[25:58], url[66:], likeType=1001)
                pb2.like(url[25:58], url[66:], likeType=1001)
                acil.comment(url[25:58], url[66:], wait["comment1"])
                pb1.comment(url[25:58], url[66:], wait["comment1"])
                pb2.comment(url[25:58], url[66:], wait["comment1"])
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
                        acil.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
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
            elif msg.text.lower() == 'Pis':
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,pisMessage)
                else:
                    acil.sendText(msg.to,helpMessage)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    pb1.updateGroup(group)
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
                msg.contentMetadata = {'mid': mid}
                acil.sendText(msg.to,"─────┅═•••͜͡❍ই۝ई❍͜͡•••═┅─────")
                acil.sendMessage(msg)
                acil.sendText(msg.to,"─────┅═•••͜͡❍ই۝ई❍͜͡•••═┅─────")
            elif "Mybots" == msg.text:
            	msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                msg.contentType = 13
                acil.sendText(msg.to,"─────┅═•••͜͡❍ই۝ई❍͜͡•••═┅─────")
                acil.sendMessage(msg) 
                msg.contentMetadata = {'mid': pb1mid}
                acil.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': pb2mid}
                acil.sendMessage(msg) 
                acil.sendText(msg.to,"─────┅═•••͜͡❍ই۝ई❍͜͡•••═┅─────")
                msg.contentType = 13
            elif "B1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': pb1mid}
                pb1.sendMessage(msg)
            elif "B2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': pb2mid}
                pb2.sendMessage(msg)
            elif "Creator" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u7d1ac07d2036b36745783a0a1992b2ba'}
                acil.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                pb1.sendMessage(msg)
            elif msg.text in ["Gift","i gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                acil.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","B2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                pb2.sendMessage(msg)

            elif msg.text in ["B Cancel","Cancel dong","Bcancel"]:
                if msg.toType == 2:
                    group = pb1.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        pb1.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            acil.sendText(msg.to,"No invites👈")
                        else:
                            acil.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Tidak ada undangan")
                    else:
                        acil.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        acil.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            acil.sendText(msg.to,"No invites👈")
                        else:
                            acil.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        acil.sendText(msg.to,"invitan tidak ada")
            #elif "gurl" == msg.text:
                #print acil.getGroup(msg.to)
                ##acil.sendMessage(msg)
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
                        acil.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        acil.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Curl"]:
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    acil.updateGroup(group)
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"URL close ô€¨👈")
                    else:
                        acil.sendText(msg.to,"URL close ô€¨👈")
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        acil.sendText(msg.to,"Can not be used for groups other than ô€œ")
            elif "Ginfo" == msg.text:
              if msg.toType == 2:
#                if msg.from_ in admin:
                  ginfo = acil.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
#                else:
                  if wait["lang"] == "JP":
                    acil.sendText(msg.to,"Can not be used outside the group")
                  else:
                    acil.sendText(msg.to,"Not for use less than group")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                acil.sendMessage(msg)
            elif "Mymid" == msg.text:
                acil.sendText(msg.to,mid)
            elif "B1 mid" == msg.text:
                pb1.sendText(msg.to,pb1mid)
            elif "B2 mid" == msg.text:
                pb2.sendText(msg.to,pb2mid)
            elif "All mid" == msg.text:
                pb1.sendText(msg.to,pb1mid)
                pb2.sendText(msg.to,pb2mid)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                acil.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+acil.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = pb1.getProfile()
                    profile.displayName = string
                    pb1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = pb2.getProfile()
                    profile.displayName = string
                    pb2.updateProfile(profile)
                    acil.sendText(msg.to,"􀜁􀇔􏿿semua nama telah di update menjadi\n👉 " + string + "👈")
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = pb1.getProfile()
                    profile.statusMessage = string
                    pb1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = pb2.getProfile()
                    profile.statusMessage = string
                    pb2.updateProfile(profile)
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
                    profile = pb1.getProfile()
                    profile.displayName = string
                    pb1.updateProfile(profile)
                    pb1.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B2name " in msg.text:
                string = msg.text.replace("B2name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = pb2.getProfile()
                    profile.displayName = string
                    pb2.updateProfile(profile)
                    pb2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "â‡‡â‡‡👈")
#--------------------------------------------------------
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = acil.getProfile()
                    profile.statusMessage = string
                    acil.updateProfile(profile)
                    acil.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "â‡‡â‡‡👈")
#--------------------------------------------------------
            elif "Sc:" in msg.text:
                mmid = msg.text.replace("Sc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                acil.sendMessage(msg)
            elif msg.text.lower() == 'contact:on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Sudah On")
                    else:
                        acil.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already open 👈")
                    else:
                        acil.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact:off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        acil.sendText(msg.to,"It is already off ô€œô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        acil.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text in ["Pro:on"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Protection Enable 􀜁􀇔􏿿👈")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Protection Enable􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Prolink:on']:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿👈")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Link Protect Enable􀜁��􏿿")
                    else:
                        acil.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Proinvite:on']:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿👈")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Procancel:on']:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿👈")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'join:on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'blocklist':
                blockedlist = acil.getBlockedContactIds()
                acil.sendText(msg.to, "Please wait...")
                kontak = acil.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                acil.sendText(msg.to, msgs)
            elif msg.text.lower() == 'join:off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Auto Join Already Off")
                    else:
                        acil.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close")
                    else:
                        acil.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Pro:off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Protection Disable ô€œ👈")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close")
                    else:
                        acil.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Prolink:off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Link Protection Disable ô€œ👈")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close")
                    else:
                        acil.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Proinvite:off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Invite Protection Disable ô€œ👈")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close")
                    else:
                        acil.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Procancel:off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Cancel Protection Disable ô€œ👈")
                    else:
                        acil.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already close")
                    else:
                        acil.sendText(msg.to,"It is already open ô€œ👈")
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            acil.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            acil.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            acil.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            acil.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        acil.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on👈")
                    else:
                        acil.sendText(msg.to,"on👈")
            elif msg.text in ["Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        acil.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Off👈")
                    else:
                        acil.sendText(msg.to,"Off👈")
            elif msg.text.lower() == 'set':
                md = ""
                if wait["contact"] == True: md+="􀜁􀇔􏿿 Contact:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Contact:off􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀜁􀇔􏿿 Auto Join:on 􀜁􀄯􏿿\n"
                else: md +="􀜁􀇔􏿿 Auto Join:off􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀜁􀇔􏿿 Auto cancel:" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+= "􀜁􀇔􏿿 Group cancel:off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀜁􀇔􏿿 Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Auto leave:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀜁􀇔􏿿 Share:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀜁􀇔􏿿 Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto add:off 􀜁��􏿿\n"
                if wait["commentOn"] == True: md+="􀜁􀇔􏿿 Auto komentar:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto komentar:off 􀜁􀄰􏿿\n"
                if wait["protect"] == True: md+="􀜁􀇔􏿿 Protect:on 🔓\n"
                else:md+="􀜁􀇔􏿿 Protect:off 🔒\n"
                if wait["linkprotect"] == True: md+="􀜁􀇔􏿿Link Protect:on 🔓\n"
                else:md+="􀜁􀇔􏿿 Link Protect:off🔒\n"
                if wait["inviteprotect"] == True: md+="􀜁􀇔􏿿Invitation Protect:on🔓\n"
                else:md+="􀜁􀇔􏿿 Invitation Protect:off🔒\n"
                if wait["cancelprotect"] == True: md+"􀜁􀇔􏿿 CancelProtect:on 🔓\n"
                else:md+="􀜁􀇔􏿿 Cancel Protect:off 🔒\n"
                acil.sendText(msg.to,md)
                acil.sendText(msg.to,"──────┅═ই۝ई═┅──────")
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ubd7b4dd119abd73ab3df542fb58a8a65'}
                acil.sendMessage(msg)
                acil.sendText(msg.to,"──────┅═ই۝ई═┅──────")
            elif "Gowner" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                acil.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                acil.sendMessage(msg)
            elif cms(msg.text,["Add"]):
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u978f7e8d02351b3d1d4a3973000c2080"}
                  acil.sendText(msg.to,"─────┅═•••͜͡❍ই۝ई❍͜͡•••═┅─────")
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u5818cb4404411c2e2e6e6937d172cca8"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u17a086ccff618e754588a1108335867f"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua028b2a4f96dff4b4a52ae25223e5073"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "udfaf52176415b46cb445ae2757ec85f3"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u29ad304bbe5e9025b8431e65832a4cfa"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u565281632a958bb2795f6434f6872e3b"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u30ceda3992172f0861558a2b7a6ef5ab"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u224e7f2fd36e3565b0756319936450c5"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u604ca77dec7ab8d450ae762d5d08cd93"}
                  acil.sendMessage(msg)
                    #msg.contentType = 13
                    #msg.contentMetadata = {'mid': "u2ca90ea24d7ba639272925d715d8a99c"}
                    #acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u2552e86aab1b1426749dd0439b0f8c7f"}
                  acil.sendMessage(msg)
                    #msg.contentType = 13
                    #msg.contentMetadata = {'mid': "uc67a847198ce188b412a058d86f10367"}
                    #acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u190afbb99dd1c28cc57642627f2aa1a2"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u12322ff2ca2b48474389f3d91b9ff385"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u2beb70887d61c0e3abf3ac327b7b21d9"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ub08e59948aaf244041d99091254e743c"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u2c83fe9f836a2f74f7f9316e0c184f9d"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u02c62ba90a4f9ff95950d1a5ee9f2154"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u47b8e60143e0e1c6fdebe67e6a355ad2"}
                  acil.sendMessage(msg)
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "u70489ca3e0d013e866a556665ee9d99b"}
                  acil.sendMessage(msg)
                  acil.sendText(msg.to,"─────┅═•••͜͡❍ই۝ई❍͜͡•••═┅─────")
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = acil.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Tidak ada album👈")
                    else:
                        acil.sendText(msg.to,"Dalam album tidak👈")
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
                    acil.sendText(msg.to,mg)
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = acil.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Tidak ada album")
                    else:
                        acil.sendText(msg.to,"Dalam album tidak")
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
                albums = acil.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        acil.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    acil.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = acil.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (acil.getGroup(i).name,i)
                acil.sendText(msg.to,h)
            elif msg.text.lower() == '@out':
                gid = pb1.getGroupIdsJoined()
                gid = pb2.getGroupIdsJoined()
                #gid = acil.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                for i in gid:
                    pb1.leaveGroup(i)
                    pb2.leaveGroup(i)
                    #acil.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,"꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂ Sudah Keluar Di semua grup")
                else:
                    acil.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Gcancelall"]:
                gid = acil.getGroupIdsInvited()
                for i in gid:
                    acil.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    acil.sendText(msg.to,"He declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = acil.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        acil.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    acil.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["Add:on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already On")
                    else:
                        acil.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already On👈")
                    else:
                        acil.sendText(msg.to,"Already On👈")
            elif msg.text in ["Add:off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Already Off👈")
                    else:
                        acil.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                acil.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                acil.sendText(msg.to,"We changed the Help👈")
            elif "Msg add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,"Kami mengubah pesan🛡")
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
                    acil.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    acil.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    acil.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    acil.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Com set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    acil.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    acil.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Comment:on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Aku berada di👈")
                    else:
                        acil.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        acil.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Com:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Hal ini sudah off")
                    else:
                        acil.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Off👈")
                    else:
                        acil.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                acil.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
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
                    turl = pb1.getUserTicket(tid)
                    pb1.sendText(msg.to,"line://ti/p" + turl)
                else:
                    pb1.sendText(msg.to,"error")

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
                acil.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Comban del"]:
                wait["dblack"] = True
                acil.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Comban cek"]:
                if wait["commentBlack"] == {}:
                    acil.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    acil.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +acil.getContact(mi_d).displayName + "\n"
                    acil.sendText(msg.to,mc)
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
                    acil.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'Clock:off':
                if wait["clock"] == False:
                    acil.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    acil.sendText(msg.to,"Adalah Off")
            elif "Clockname " in msg.text:
                n = msg.text.replace("Jam say ","")
                if len(n.decode("utf-8")) > 30:
                    acil.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    acil.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = acil.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    acil.updateProfile(profile)
                    acil.sendText(msg.to,"Diperbarui👈")
                else:
                    acil.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "Fuck: " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = acil.getGroup(msg.to)
                       ginfo = acil.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       acil.updateGroup(gs)
                       invsend = 0
                       Ticket = acil.reissueGroupTicket(msg.to)
                       acil.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"Fuck You")
                           pass
                       else:
                           for target in targets:
                                try:
                                    acil.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    acil.leaveGroup(msg.to)
                                    gs = acil.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    acil.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    acil.updateGroup(gs)
#-----------------------------------------------------------

            elif ("Cipok " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           acil.kickoutFromGroup(msg.to,[target])
                       except:
                           acil.sendText(msg.to,"Suksess")
            elif ("Ciduk " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           pb1.kickoutFromGroup(msg.to,[target])
                       except:
                           pb1.sendText(msg.to,"Suksess")
            elif ("Sc " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   key = acil.getContact(key1)
                   acil.sendText(msg.to,"Mid:" +  key1)

            elif "Nk " in msg.text:                  
                       nk0 = msg.text.replace("Beb ","")
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
                           sendMessage(msg.to,"suksess")
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
                  h += "[╠ ͜͡✪͜͡✪➢] %s \n" % (acil.getGroup(i).name + " | Members : " + str(len (acil.getGroup(i).members)))
                 acil.sendText(msg.to, "☆「Group List」☆\n"+ h +"Total Group : " +str(len(gid)))

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
#-----------------------------------------------------------
            elif msg.text == "Mata":
                    acil.sendText(msg.to, "Check Yang Suka Ngintip Orang Mandi")
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

            elif msg.text == "Lihat":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "╠ ͜͡✪͜͡✪➢\n"
                        acil.sendText(msg.to,"======Tercyduck====== %s\n=====Tukang Ngintip======\n%s\nReading point creation date n time:\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                         acil.sendText(msg.to,"An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-------------------------------------------------
	    elif "Spam @" in msg.text:
#	      if msg.from_ in admin:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = acil.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
		       acil.sendText(msg.to,"Wating in progres...\n──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────")
                       acil.sendText(g.mid,"──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────")
                       pb1.sendText(g.mid,"──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────")
                       pb2.sendText(g.mid,"──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────")
                       acil.sendText(g.mid,"──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────")
                       pb1.sendText(g.mid,"──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────")
                       pb2.sendText(g.mid,"──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────")
                       pb1.sendText(g.mid,"──────┅═ই۝ई═┅──────\n꧁􀤁【☆ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☆】􏿿꧂\nᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\nhttp://line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────")
                       acil.sendText(msg.to, "Succes")
                       print " Spammed !"
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
                    if jmlh <= 1000:
                        for x in range(jmlh):
                            acil.sendText(msg.to, text)
                    else:
                        acil.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        acil.sendText(msg.to, tulisan)
                    else:
                        acil.sendText(msg.to, "Out Of Range!")

#-----------------------------------------------------------
            elif msg.text.lower() == 'respon':
                profile = pb1.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿Hadir"
                pb1.sendText(msg.to, text)
                profile = pb2.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿Hadir"
                pb2.sendText(msg.to, text)
#-----------------------------------------------------------speed
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
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "❂••••••BLACKLIST••••••❂" + "\n"
                    for mm in matched_list:
                        cocoa += "😂" +acil.getContact(mm).displayName + "\n"
                    acil.sendText(msg.to,cocoa + "❂••••••••••••••••❂")
            elif msg.text.lower() == 'kick@mbl':
                if msg.toType == 2:
                    group = pb1.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        pb1.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            acil.kickoutFromGroup(msg.to,[jj])
                            pb1.kickoutFromGroup(msg.to,[jj])
                            pb2.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass

#---------------------------------------------------
            elif msg.text in ["backup"]:
                    try:
                       acil.updateDisplayPicture(backup.pictureStatus)
                       acil.updateProfile(backup)
                       acil.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       acil.sendText(msg.to, str(e))
#------------------------------------------------
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    print "[COPY] Ok"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip(' ')
                    gs = acil.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    sendMessage(msg.to, "Ok Vril")
                else:
                     for target in targets:
                         try:
                              acil.cloneContactProfile(target)
                              acil.sendText(msg.to, "success")
                         except Exception as e:
                             print e
#---------------------------------------------- 
#---------------------- = NUKE = ------------------
            elif "KIBAR!!!" in msg.text:
                if msg.toType == 2:
                    print "Kick all member"
                    _name = msg.text.replace("Go","")
                    gs = acil.getGroup(msg.to)
                    gs = pb1.getGroup(msg.to)
                    gs = pb2.getGroup(msg.to)
                    gs = acil.getGroup(msg.to)
                    gs = pb1.getGroup(msg.to)
                    gs = pb2.getGroup(msg.to)
                    gs = acil.getGroup(msg.to)
                    gs = pb1.getGroup(msg.to)
                    h = acil.getContact(mid)
                    start = time.time()
                    pb1.sendText(msg.to, "🅆🄴🄻🄲🄾🄼🄴 🅃🄾\n🄺🄸🄲🄺🄴🅁 🄰🅁🄴🄽🄰\n_______________________________")
                    elapsed_time = time.time() - start
                    pb1.sendText(msg.to, "%sseconds" % (elapsed_time))
                    pb2.sendText(msg.to, "──────┅═ই✪͜͡ ۝ ͜͡✪ई═┅───────")
                    acil.sendText(msg.to, "【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】")
                    pb1.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/0h4f8UopZva0kFLEezRx4UHjlpZSRyAm0BfU12fXV_PCwtTipPOxghe3IkPHshFS5Pakl0LXcuYi0h")
                    pb2.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/0h4f8Us-i0a0kFLEezZY8UHjlpZSRyAm0BfU12fXV_PCwtTipPOxghe3IkPHshFS5Pakl0LXcuYi0h")
                    acil.sendText(msg.to,"⚠️⚠️__AWAS!!! __⚠️⚠️\n___TANPA PERMISI GW___\n🔥 BAKAR GRUP LO NYET!!🔥\n___JANGAN TANYA KENAPA___\n😎KARNA KAMI PUNYA PRINSIF 😎\n  KALO GAK RATA ZOOM MUKA KANG KIBAR\n\n\n──────┅═ই۝ई═┅──────\n【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n       ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n      line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────\n\n\nKAMI TAU APA!!?? KAMI HANYA NUMPANG KIBAR&PLAY\n\n\nDAH GITU AJA TQ\n\n\n(itu)JADI TANGKIS AJE BOSS (itu)\n\n\nGO!!  GO!!  GO!!  GO!!  GO!!\n\n\n________ (go)________ ")
                    pb1.sendText(msg.to,"❂•••••••••••✧•••••••••••❂ ")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u978f7e8d02351b3d1d4a3973000c2080"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u5818cb4404411c2e2e6e6937d172cca8"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua028b2a4f96dff4b4a52ae25223e5073"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "udfaf52176415b46cb445ae2757ec85f3"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u29ad304bbe5e9025b8431e65832a4cfa"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u565281632a958bb2795f6434f6872e3b"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u30ceda3992172f0861558a2b7a6ef5ab"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u224e7f2fd36e3565b0756319936450c5"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u604ca77dec7ab8d450ae762d5d08cd93"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2ca90ea24d7ba639272925d715d8a99c"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2552e86aab1b1426749dd0439b0f8c7f"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "uc67a847198ce188b412a058d86f10367"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u190afbb99dd1c28cc57642627f2aa1a2"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u12322ff2ca2b48474389f3d91b9ff385"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2beb70887d61c0e3abf3ac327b7b21d9"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ub08e59948aaf244041d99091254e743c"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2c83fe9f836a2f74f7f9316e0c184f9d"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u02c62ba90a4f9ff95950d1a5ee9f2154"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u47b8e60143e0e1c6fdebe67e6a355ad2"}
                    acil.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u70489ca3e0d013e866a556665ee9d99b"}
                    acil.sendMessage(msg)
                    pb1.sendText(msg.to, "❂•••••••••••✧•••••••••••❂ ")
                    pb2.sendText(msg.to, "★_____TANGKIS NYETT_____★\n\nUDAH GITU  AJA YANG PENTING KIBAR\n\n🔥RATA KAMI SENANG GAK RATA BULY AJE KAMI  DISINI🔥\n\n\n__JADI TANGKIS AJA GO_GO_GO_!!!!!__\n\n______【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】______ ")
                    acil.sendText(msg.to, "──────┅═ই✪͜͡ ۝ ͜͡✪ई═┅─────── ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        acil.sendText(msg.to,"Success test")
                        ki6.sendText(msg.to,"Success test")
                    else:
                        for target in targets:
                          if target not in Bots or owner:
                            if target in owner:
                              pass
                            elif target in admin:
                              pass
                            elif target in Bots:
                              pass
                            else:
                              try:
                                klist=[cl,ki,ki2]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                              except:
                                acil.sendText(msg,to,"Udah Gitu Aja")
                                pb2.sendText(msg,to,"Rata Yehkan!!!")
#-------------------- = NUKE FINISH = ----------------------------- 
#-------------Fungsi Tagall User Start---------------#
            elif msg.text in ["Dor","Tagall","Sepi","Tag"]:
                group = acil.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                  
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "╠➢@nrik \n"
               
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
               
                try:
                    acil.sendMessage(msg)
                except Exception as error:
                    print error
#-------------------------------------------------------------
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        acil.cancelGroupInvitation(msg.to,[_mid])
                    acil.sendText(msg.to,"I pretended to cancel and canceled👈")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    acil.createAlbum(gid,name)
                    acil.sendText(msg.to,name + "We created an album👈")
                except:
                    acil.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    acil.sendText(msg.to,str(acil.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        acil.sendText(msg.to,str(e))
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                acil.sendText(msg.to, "「Progress Speeds...」")
                pb1.sendText(msg.to, "「Progress Speeds...」")
                pb2.sendText(msg.to, "「Progress Speeds...」")
                elapsed_time = time.time() - start
                acil.sendText(msg.to, "%sseconds" % (elapsed_time))
                pb1.sendText(msg.to, "%sseconds" % (elapsed_time))
                pb2.sendText(msg.to, "%sseconds" % (elapsed_time))
#-----------------------------------------------
            elif msg.text.lower() == '1':
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        pb1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        pb2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text.lower() == '1':
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        pb1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        pb2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        pb1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        pb1.updateGroup(G)
            elif msg.text.lower() == 'In':
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        pb1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        pb2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        pb1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        pb1.updateGroup(G)
#-----------------------------------------------
            elif "1" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        pb1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        pb1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        pb1.updateGroup(G)
#-----------------------------------------------
            elif "2" in msg.text:
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        invsend = 0
                        Ticket = acil.reissueGroupTicket(msg.to)
                        pb2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = acil.getGroup(msg.to)
                        ginfo = acil.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        pb2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        pb2.updateGroup(G)
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text.lower() == '@exit':
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        acil.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 Jangan Lupa Add Yehkan\n"  +  str(ginfo.name)  + "")
                        pb1.leaveGroup(msg.to)
                        pb2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        pb1.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = acil.getGroup(msg.to)
                    try:
                        pb2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = acil.getGroup(msg.to)
                acil.sendText(msg.to,"🅆🄴🄻🄲🄾🄼🄴 🅃🄾\n\n_______________________________ \n\n" + str(ginfo.name))
                acil.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				kisendText(msg.to,(bctxt))
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				pb1.sendText(msg.to,(bctxt))
				pb2.sendText(msg.to,(bctxt))
            elif msg.text.lower() == 'ping':
                pb1.sendText(msg.to,"Pong 􀜁􀇔􏿿")
                pb2.sendText(msg.to,"Pung 􀜁􀇔􏿿")
            
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in pb1mid:
                        G = pb1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        pb1.updateGroup(G)
                        Ticket = pb1.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        acil.updateGroup(G)
                    else:
                        G = pb1.getGroup(op.param1)

                            
                        
                        
                        pb1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        pb1.updateGroup(G)
                        Ticket = pb1.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        acil.updateGroup(G)
                        pb1.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in pb1mid:
                    if op.param2 in pb2mid:
                        G = pb2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        pb2.updateGroup(G)
                        Ticket = pb2.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        pb2.updateGroup(G)
                    else:
                        G = pb2.getGroup(op.param1)

                        pb2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        pb2.updateGroup(G)
                        Ticket = pb2.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        pb1.updateGroup(G)


                elif op.param3 in pb2mid:
                    if op.param2 in mid:
                        G = acil.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        Ticket = acil.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        acil.updateGroup(G)
                    else:
                        G = acil.getGroup(op.param1)

                        
                        acil.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        acil.updateGroup(G)
                        Ticket = acil.reissueGroupTicket(op.param1)
                        acil.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        acil.updateGroup(G)
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
			ks.updateGroup(G)
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
		    acil.sendText(op.param1,"")
	    else:
		acil.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = pb1.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    pb1.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    acil.sendText(op.param1,"")
	    else:
		acil.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    acil.sendText(op.param1,str(wait["message"]))
                    pb1.sendText(op.param1,str(wait["message"]))
                    pb2.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
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


