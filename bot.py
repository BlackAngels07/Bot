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

nadya = LINETCR.LINE()
#nadya.login(qr=True)
nadya.login(token='ExRTcOu9AzPhd7S39eMa.FrRaFsa2S2DfEdOkgzkYUG.TR5t2XYEDiQbq38z4ztj6kDRkBQxt3EWEBfb7nLgXlY=')
nadya.loginResult()
print "Avrilia-Login Success\n\n=====[Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')


helpMessage ="""
╔o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
║ ❂••••••••••••••••••••❂
║    【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】
║              ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ
║ ❂•••••••••••••••••••❂
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
║ ❂••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}••❂
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
╠ ͜͡✪͜͡✪➢〘sᴇʟғ〙
╠ ͜͡✪͜͡✪➢〘ʜɪ〙
╠ ͜͡✪͜͡✪➢〘ᴍᴇ〙
╠ ͜͡✪͜͡✪➢〘ʏᴏᴜ〙
╠ ͜͡✪͜͡✪➢〘ᴍʏᴍɪᴅ〙
╠ ͜͡✪͜͡✪➢〘ᴍɪᴅ @〙
╠ ͜͡✪͜͡✪➢〘sᴇᴀʀᴄʜɪᴅ (ɪᴅ ʟɪɴᴇ)〙
╠ ͜͡✪͜͡✪➢〘ᴄʜᴇᴄᴋᴅᴀᴛᴇ:ᴅᴅ/ᴍᴍ/ʏʏ〙
╠ ͜͡✪͜͡✪➢〘ᴋᴀʟᴇɴᴅᴇʀ〙
╠ ͜͡✪͜͡✪➢〘sᴛᴇᴀʟ ᴄᴏɴᴛᴀᴄᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴘᴘ @〙
╠ ͜͡✪͜͡✪➢〘ᴄᴏᴠᴇʀ @〙
╠ ͜͡✪͜͡✪➢〘ᴀᴜᴛᴏ ʟɪᴋᴇ〙
╠ ͜͡✪͜͡✪➢〘sᴄʙᴄ ᴛᴇxᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴄʙᴄ ᴛᴇxᴛ〙
╠ ͜͡✪͜͡✪➢〘ɢʙᴄ ᴛᴇxᴛ〙
╠ ͜͡✪͜͡✪➢〘ʙɪᴏ @〙
╠ ͜͡✪͜͡✪➢〘ɪɴғᴏ @〙
╠ ͜͡✪͜͡✪➢〘ɴᴀᴍᴇ @〙
╠ ͜͡✪͜͡✪➢〘ᴘʀᴏғɪʟᴇ @〙
╠ ͜͡✪͜͡✪➢〘ᴄᴏɴᴛᴀᴄᴛ @〙
╠ ͜͡✪͜͡✪➢〘ɢᴇᴛᴠɪᴅ @〙
╠ ͜͡✪͜͡✪➢〘ғʀɪᴇɴᴅʟɪsᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴍɪᴄᴀᴅᴅ @〙
╠ ͜͡✪͜͡✪➢〘ᴍɪᴄᴅᴇʟ @〙
╠ ͜͡✪͜͡✪➢〘ᴍɪᴄʟɪsᴛ〙
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
║            ❂••{☠PART 1☠}••❂
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
╠ ͜͡✪͜͡✪➢〘ᴀʙsᴇɴ〙
╠ ͜͡✪͜͡✪➢〘sᴘ,sᴘᴇᴇᴅ〙
╠ ͜͡✪͜͡✪➢〘ʀᴇsᴘᴏɴ〙
╠ ͜͡✪͜͡✪➢〘ʀᴜɴᴛɪᴍᴇ〙
╠ ͜͡✪͜͡✪➢〘ᴄᴏᴘʏ @〙
╠ ͜͡✪͜͡✪➢〘ᴄᴏᴘʏᴄᴏɴᴛᴀᴄᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴍʏʙᴀᴄᴋᴜᴘ〙
╠ ͜͡✪͜͡✪➢〘ᴍʏʙɪᴏ (ᴛᴇxᴛ)〙
╠ ͜͡✪͜͡✪➢〘ᴍʏɴᴀᴍᴇ (ᴛᴇxᴛ)〙
╠ ͜͡✪͜͡✪➢〘@ʙʏᴇ〙
╠ ͜͡✪͜͡✪➢〘ʙᴏᴛ ᴏɴ/ᴏғғ〙
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
║            ❂••{☠PART 2☠}••❂
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
╠ ͜͡✪͜͡✪➢〘ɢɪғᴛ〙
╠ ͜͡✪͜͡✪➢〘ɢɪғᴛʙʏᴄᴏɴᴛᴀᴄᴛ〙
╠ ͜͡✪͜͡✪➢〘ɢɪғ ɢᴏʀᴇ〙
╠ ͜͡✪͜͡✪➢〘ɢᴏᴏɢʟᴇ (ᴛᴇxᴛ)〙
╠ ͜͡✪͜͡✪➢〘ᴘʟᴀʏsᴛᴏʀᴇ ɴᴀᴍᴀᴀᴘᴘ〙
╠ ͜͡✪͜͡✪➢〘ғᴀɴᴄʏᴛᴇxᴛ ᴛᴇxᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴍᴜsɪᴋ ᴊᴜᴅᴜʟ-ᴘᴇɴʏᴀɴʏɪ〙
╠ ͜͡✪͜͡✪➢〘ʟɪʀɪᴋ ᴊᴜᴅᴜʟ-ᴘᴇɴʏᴀɴʏɪ〙
╠ ͜͡✪͜͡✪➢〘ᴍᴜsʀɪᴋ ᴊᴜᴅᴜʟ-ᴘᴇɴʏᴀɴʏɪ〙
╠ ͜͡✪͜͡✪➢〘ɪɢ ᴜʀsɴᴀᴍᴇɪɴsᴛᴀɢʀᴀᴍ〙
╠ ͜͡✪͜͡✪➢〘ᴄʜᴇᴄᴋɪɢ ɴᴀᴍᴇɪɴsᴛᴀɢʀᴀᴍ〙
╠ ͜͡✪͜͡✪➢〘ᴀᴘᴀᴋᴀʜ ᴛᴇxᴛ:ᴋᴇʀᴀɴɢ ᴀᴊᴀɪʙ〙
╠ ͜͡✪͜͡✪➢〘ᴋᴀᴘᴀɴ ᴛᴇxᴛ:ᴋᴇʀᴀɴɢ ᴀᴊᴀɪʙ〙
╠ ͜͡✪͜͡✪➢〘ʜᴀʀɪ ᴛᴇxᴛ:ᴋᴇʀᴀɴɢ ᴀᴊᴀɪʙ〙
╠ ͜͡✪͜͡✪➢〘ʙᴇʀᴀᴘᴀ ᴛᴇxᴛ:ᴋᴇʀᴀɴɢ ᴀᴊᴀɪʙ〙
╠ ͜͡✪͜͡✪➢〘ʙᴇʀᴀᴘᴀᴋᴀʜ ᴛᴇxᴛ〙
╠ ͜͡✪͜͡✪➢〘ʏᴏᴜᴛᴜʙᴇ ᴊᴜᴅᴜʟ ᴠɪᴅᴇᴏ〙
╠ ͜͡✪͜͡✪➢〘ʏᴏᴜᴛᴜʙᴇᴠɪᴅᴇᴏ :ᴠɪᴅᴇᴏ〙
╠ ͜͡✪͜͡✪➢〘ʏᴏᴜᴛᴜʙᴇsᴇᴀʀᴄʜ:ᴠɪᴅᴇᴏ〙
╠ ͜͡✪͜͡✪➢〘ɪᴍᴀɢᴇ ɴᴀᴍᴀɢᴀᴍʙᴀʀ〙
╠ ͜͡✪͜͡✪➢〘sᴀʏ ᴛᴇxᴛ〙
╠ ͜͡✪͜͡✪➢〘sᴀʏ-ᴇɴ ᴛᴇxᴛ〙
╠ ͜͡✪͜͡✪➢〘sᴀʏ-ᴊᴘ ᴛᴇxᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴛʀ-ɪᴅ ᴛᴇxᴛ( ᴇɴ ᴋᴇ ɪᴅ〙
╠ ͜͡✪͜͡✪➢〘ᴛʀ-ᴇɴ ᴛᴇxᴛ( ɪᴅ ᴋᴇ ᴇɴ〙
╠ ͜͡✪͜͡✪➢〘ᴛʀ-ᴛʜ ᴛᴇxᴛ( ɪᴅ ᴋᴇ ᴛʜ〙
╠ ͜͡✪͜͡✪➢〘ɪᴅ@ᴇɴ ᴛᴇxᴛ( ɪᴅ ᴋᴇ ᴇɴ〙
╠ ͜͡✪͜͡✪➢〘ɪᴅ@ᴛʜ ᴛᴇxᴛ( ɪᴅ ᴋᴇ ᴛʜ〙
╠ ͜͡✪͜͡✪➢〘ᴇɴ@ɪᴅ ᴛᴇxᴛ( ᴇɴ ᴋᴇ ɪᴅ〙
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
║            ❂••{☠PART 3☠}••❂
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
╠ ͜͡✪͜͡✪➢〘ᴡᴇʟᴄᴏᴍᴇ〙
╠ ͜͡✪͜͡✪➢〘sᴀʏ ᴡᴇʟᴄᴏᴍᴇ〙
╠ ͜͡✪͜͡✪➢〘ɪɴᴠɪᴛᴇ ᴄʀᴇᴀᴛᴏʀ〙
╠ ͜͡✪͜͡✪➢〘sᴇᴛᴠɪᴇᴡ/ᴄᴄᴛᴠ〙
╠ ͜͡✪͜͡✪➢〘ᴠɪᴇᴡsᴇᴇɴ/ᴄɪᴅᴜᴋ〙
╠ ͜͡✪͜͡✪➢〘ɢɴ: (ɴᴀᴍᴀɢʀᴏᴜᴘ)〙
╠ ͜͡✪͜͡✪➢〘ᴛᴀɢ ᴀʟʟ〙
╠ ͜͡✪͜͡✪➢〘ʟᴜʀᴋ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ʟᴜʀᴋᴇʀs〙
╠ ͜͡✪͜͡✪➢〘ʀᴇᴄᴏᴠᴇʀ〙
╠ ͜͡✪͜͡✪➢〘ᴄᴀɴᴄᴇʟ〙
╠ ͜͡✪͜͡✪➢〘ᴄᴀɴᴄᴇʟᴀʟʟ〙
╠ ͜͡✪͜͡✪➢〘ɢᴄʀᴇᴀᴛᴏʀ〙
╠ ͜͡✪͜͡✪➢〘ɢɪɴғᴏ〙
╠ ͜͡✪͜͡✪➢〘ɢᴜʀʟ〙
╠ ͜͡✪͜͡✪➢〘ʟɪsᴛ ɢʀᴏᴜᴘ〙
╠ ͜͡✪͜͡✪➢〘ᴘɪᴄᴛ ɢʀᴏᴜᴘ:ɴᴀᴍᴀɢʀᴏᴜᴘ〙
╠ ͜͡✪͜͡✪➢〘sᴘᴀᴍ: (ᴛᴇxᴛ)〙
╠ ͜͡✪͜͡✪➢〘ᴀᴅᴅ ᴀʟʟ〙
╠ ͜͡✪͜͡✪➢〘ᴋɪᴄᴋ: (ᴍɪᴅ)〙
╠ ͜͡✪͜͡✪➢〘ɪɴᴠɪᴛᴇ: (ᴍɪᴅ)〙
╠ ͜͡✪͜͡✪➢〘ɪɴᴠɪᴛᴇ〙
╠ ͜͡✪͜͡✪➢〘ᴍᴇᴍʟɪsᴛ〙
╠ ͜͡✪͜͡✪➢〘ɢᴇᴛɢʀᴏᴜᴘ ɪᴍᴀɢᴇ〙
╠ ͜͡✪͜͡✪➢〘ᴜʀʟɢʀᴏᴜᴘ ɪᴍᴀɢᴇ〙
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
║            ❂••{☠PART 4☠}••❂
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
╠ ͜͡✪͜͡✪➢〘sᴀᴍʙᴜᴛᴀɴ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴍɪᴍɪᴄ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴜʀʟ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴀʟᴡᴀʏsʀᴇᴀᴅ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘sɪᴅᴇʀ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴄᴏɴᴛᴀᴄᴛ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘sᴛɪᴄᴋᴇʀ ᴏɴ〙
╠ ͜͡✪͜͡✪➢〘sɪᴍɪsɪᴍɪ ᴏɴ/ᴏғғ〙
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
║            ❂••{☠PART 5☠}••❂            
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
╠ ͜͡✪͜͡✪➢〘ᴄᴏᴅᴇ #13〙
╠ ͜͡✪͜͡✪➢〘ᴋɪᴄᴋᴀʟʟ〙
╠ ͜͡✪͜͡✪➢〘ʙᴄ: (ᴛᴇxᴛ)〙
╠ ͜͡✪͜͡✪➢〘ᴊᴏɪɴ ɢʀᴏᴜᴘ:ɴᴀᴍᴀɢʀᴏᴜᴘ〙
╠ ͜͡✪͜͡✪➢〘ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ:ɴᴀᴍᴀɢʀᴏᴜᴘ〙
╠ ͜͡✪͜͡✪➢〘ʟᴇᴀᴠᴇ ᴀʟʟ ɢʀᴏᴜᴘ〙
╠ ͜͡✪͜͡✪➢〘ᴛᴀɢ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ʙᴏᴛ ʀᴇsᴛᴀʀᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴛᴜʀɴ ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴀʟʟᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ʙᴀɴ〙
╠ ͜͡✪͜͡✪➢〘ᴜɴʙᴀɴ〙
╠ ͜͡✪͜͡✪➢〘ʙᴀɴ @〙
╠ ͜͡✪͜͡✪➢〘ᴜɴʙᴀɴ @〙
╠ ͜͡✪͜͡✪➢〘ʙᴀɴ ʟɪsᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴄʟᴇᴀʀ ʙᴀɴ〙
╠ ͜͡✪͜͡✪➢〘ᴋɪʟʟ〙
╠ ͜͡✪͜͡✪➢〘ᴋɪᴄᴋ @〙
╠ ͜͡✪͜͡✪➢〘sᴇᴛ ᴍᴇᴍʙᴇʀ: (ᴊᴜᴍʙʟᴀʜ)〙
╠ ͜͡✪͜͡✪➢〘ʙᴀɴ ɢʀᴏᴜᴘ: (ɴᴀᴍᴀɢʀᴏᴜᴘ〙
╠ ͜͡✪͜͡✪➢〘ᴅᴇʟ ʙᴀɴ: (ɴᴀᴍᴀɢʀᴏᴜᴘ〙
╠ ͜͡✪͜͡✪➢〘ʟɪsᴛ ʙᴀɴ〙
╠ ͜͡✪͜͡✪➢〘ᴋɪʟʟ ʙᴀɴ〙
╠ ͜͡✪͜͡✪➢〘ɢʟɪsᴛ〙
╠ ͜͡✪͜͡✪➢〘sᴘ @:sᴘᴀᴍ ᴄᴏɴᴛᴀᴄᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴛᴏ @ᴛᴀʀɢᴇᴛ〙
╠ ͜͡✪͜͡✪➢〘ᴋᴇʟɪɴᴄɪ @ᴛᴀʀɢᴇᴛ〙
╠ ͜͡✪͜͡✪➢〘ɢʟɪsᴛᴍɪᴅ〙
╠ ͜͡✪͜͡✪➢〘ᴅᴇᴛᴀɪʟs ɢʀᴏᴜᴘ: (ɢɪᴅ)〙
╠ ͜͡✪͜͡✪➢〘ᴄᴀɴᴄᴇʟ ɪɴᴠɪᴛᴇ: (ɢɪᴅ)〙
╠ ͜͡✪͜͡✪➢〘ɪɴᴠɪᴛᴇᴍᴇᴛᴏ: (ɢɪᴅ)〙
╠ ͜͡✪͜͡✪➢〘ᴀᴄᴄ ɪɴᴠɪᴛᴇ〙
╠ ͜͡✪͜͡✪➢〘ʀᴇᴍᴏᴠᴇᴄʜᴀᴛ〙
╠ ͜͡✪͜͡✪➢〘ϙʀ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴀᴜᴛᴏᴋɪᴄᴋ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴀᴜᴛᴏᴄᴀɴᴄᴇʟ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ɪɴᴠɪᴛᴇᴘʀᴏ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴊᴏɪɴ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴊᴏɪɴᴄᴀɴᴄᴇʟ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ʀᴇsᴘᴏɴ1 ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ʀᴇsᴘᴏɴ2 ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ʀᴇsᴘᴏɴ3 ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ʀᴇsᴘᴏɴᴋɪᴄᴋ ᴏɴ/ᴏғғ〙
╠ ͜͡✪͜͡✪➢〘ᴠɪʀᴜs ᴏɴ/ᴏғғ〙
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
║ ❂••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}••❂
╠o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
║            ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ
║  http://line.me/ti/p/~avrilia_quester
╚o()xxxx[]{̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶:̶̶̷̶̶➤̶̶
•••͜͡❍☠ B҉ L҉ A҉ C҉ K҉  A҉ N҉ G҉ E҉ L҉ S҉ ☠❍͜͡•••
"""

tjia="u7d1ac07d2036b36745783a0a1992b2ba"

KAC=[nadya]
mid = nadya.getProfile().mid
Bots=[mid]
Creator=["u7d1ac07d2036b36745783a0a1992b2ba"]
admin=["u7d1ac07d2036b36745783a0a1992b2ba"]

contact = nadya.getProfile()
backup1 = nadya.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = nadya.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "Bot":True,
    "AutoJoin":True,
    "AutoJoinCancel":False,
    "memberscancel":30,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    "Add":True,
    'pap':{},
    'invite':{},
    'spammed':{},
    'steal':{},
    'gift':{},
    'copy':{},    
    'likeOn':True,
    'Tagvirus':False,
    'detectMention2':False,
    'detectMention3':True,
    'kickMention':False,  
    'sticker':False,
    'Crash':False,
    'timeline':True,
    "Timeline":True,
    "autoAdd":True,
    "comment":"【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n  http://line.me/ti/p/~avrilia_quester\n\n. . . . . . . . . . .*. . . . . . . ** *\n. . . . .. . . . . .*** . . * . . *****\n. . . . . . . . . . .** . . **. . . . .*\n. . . . . . . . . . ***.*. . *. . . . .*\n. . . . . . . . . .****. . . .** . . . ******\n. . . . . . . . . ***** . . . .**.*. . . . . **\n. . . . . . . . .*****. . . . . **. . . . . . *.**\n. . . . . . . .*****. . . . . .*. . . . . . *\n. . . . . . . .******. . . . .*. . . . . *\n. . . . . . . .******* . . .*. . . . .*\n. . . . . . . . .*********. . . . . *\n. . . . . . . . . .******* . ***\n*******. . . . . . . . .**\n.*******. . . . . . . . *\n. ******. . . . . . . . * *\n. .***. . *. . . . . . .**\n. . . . . . .*. . . . . *\n. . . . .****.*. . . .*\n. . . *******. .*. .*\n. . .*******. . . *.\n. . .*****. . . . *\n. . .**. . . . . .*\n. . .*. . . . . . **.*\n. . . . . . . . . **\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . *\n. . . . . . . . *\n▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄",    
    "commentOn":True,
    "commentBlack":{},
    "message":"╔═──────┅═ই۝ई═┅──────\n_░▒███████\n░██▓▒░░▒▓██\n██▓▒░__░▒▓██___██████\n██▓▒░____░▓███▓__░▒▓██\n██▓▒░___░▓██▓_____░▒▓██\n██▓▒░_______________░▒▓██\n_██▓▒░______________░▒▓██\n__██▓▒░____________░▒▓██\n___██▓▒░__________░▒▓██\n____██▓▒░________░▒▓██\n_____██▓▒░_____░▒▓██\n______██▓▒░__░▒▓██\n_______█▓▒░░▒▓██\n_________░▒▓██\n_______░▒▓██\n_____░▒▓██\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n  http://line.me/ti/p/~avrilia_quester\n\n. . . . . . . . . . .*. . . . . . . ** *\n. . . . .. . . . . .*** . . * . . *****\n. . . . . . . . . . .** . . **. . . . .*\n. . . . . . . . . . ***.*. . *. . . . .*\n. . . . . . . . . .****. . . .** . . . ******\n. . . . . . . . . ***** . . . .**.*. . . . . **\n. . . . . . . . .*****. . . . . **. . . . . . *.**\n. . . . . . . .*****. . . . . .*. . . . . . *\n. . . . . . . .******. . . . .*. . . . . *\n. . . . . . . .******* . . .*. . . . .*\n. . . . . . . . .*********. . . . . *\n. . . . . . . . . .******* . ***\n*******. . . . . . . . .**\n.*******. . . . . . . . *\n. ******. . . . . . . . * *\n. .***. . *. . . . . . .**\n. . . . . . .*. . . . . *\n. . . . .****.*. . . .*\n. . . *******. .*. .*\n. . .*******. . . *.\n. . .*****. . . . *\n. . .**. . . . . .*\n. . .*. . . . . . **.*\n. . . . . . . . . **\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . *\n. . . . . . . . *\n▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█\n╚═────────┅═ই۝ई═┅─────────",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":True,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }    

wait3 = {
    "copy":False,
    "copy2":"target",
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}


setTime = {}
setTime = wait2['setTime']

contact = nadya.getProfile()
backup = nadya.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


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

def restart_program():
    python = sys.executable
    os.exenadya(python, python, * sys.argv)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
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
    print "[Command] Tag"
    try:
       nadya.sendMessage(msg)
    except Exception as error:
       print error
def sendMessage(self, messageObject):
        return self.Talk.nadyaient.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.nadyaient.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._nadyaient.sendMessage(M).id
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
        r = self._nadyaient.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = nadya.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
           if wait["autoAdd"] == True:
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata = {'mid': "ubd7b4dd119abd73ab3df542fb58a8a65','"}
              if (wait["message"] in [""," ","\n",None]):
                  pass
              else:
                  nadya.sendText(op.param1,str(wait["message"]))
                  nadya.sendMessage(c)


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
                            Name = nadya.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n☠ "   + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        nadya.sendText(op.param1, "Nahhh " + "❂•••{ "  + Name +  " }•••❂" + "\n\nJones Lagi Ngintip")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        nadya.sendText(op.param1, "Nahhh " + "❂•••{ "  + Name +  " }•••❂" + "\n\nJangan Ngintip Aja Mbloo")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    nadya.sendText(op.param1, "Nahhh " + "❂•••{ "  + Name +  " }•••❂" + "\n\nSinih Deh Banyak Tikungan Nih")
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
	      

        if op.type == 22:
            nadya.leaveRoom(op.param1)

        if op.type == 21:
            nadya.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    nadya.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = nadya.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        nadya.acceptGroupInvitation(op.param1)
                        nadya.sendText(op.param1,"Maaf " + nadya.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        nadya.leaveGroup(op.param1)                        
		    else:
                        nadya.acceptGroupInvitation(op.param1)
			nadya.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = nadya.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        nadya.rejectGroupInvitation(op.param1)
		    else:
                        nadya.acceptGroupInvitation(op.param1)
			nadya.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        nadya.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			nadya.cancelGroupInvitation(op.param1, [op.param3])
			nadya.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    nadya.cancelGroupInvitation(op.param1,[op.param3])
                    nadya.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               nadya.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    nadya.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        nadya.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        nadya.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        nadya.kickoutFromGroup(op.param1,[op.param2])
			nadya.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    nadya.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        nadya.kickoutFromGroup(op.param1,[op.param2])
			nadya.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                nadya.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        nadya.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("nadyaient Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    nadya.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    nadya.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = nadya.getGroup(op.param1)
            contact = nadya.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            nadya.sendText(op.param1,"🄷🄰🄻🄻🄾... " + nadya.getContact(op.param2).displayName + "\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n█░░╔╦╗ ╔╗░░█\n█░░─║─ ║║░░█\n█░░─╩ ─╚╝░░█\n\n⛦•••{ " + str(ginfo.name) + " }•••⛦" + "\n\nBudayakan Cek Note\nDan Semoga Betah Disini..\nJangan Lupa Nikung Kak,..Yehkan..\n\nDah Gitu Ajah..\n\n\n===❍•••{☠ʟᴇᴠᴀɴᴀ☠}•••❍===\n"+ datetime.now().strftime('%H:%M:%S'))
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            nadya.sendMessage(c)  
            nadya.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269548",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            nadya.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            nadya.sendText(op.param1,"Nahhhh Lohhhhh " + nadya.getContact(op.param2).displayName +  "\nBaper Tuh Orang . . . (p′︵‵。) 🤗")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269542",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            nadya.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 26:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        nadya.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                nadya.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = nadya.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  nadya.sendText(msg.to,ret_)
                                  nadya.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait['Tagvirus'] == True:
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': "ubd7b4dd119abd73ab3df542fb58a8a65'"}
                                  nadya.sendMessage(msg)
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = nadya.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Sekali lagi nge tag gw sumpahin jomblo seumur hidup!","Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Woii " + cName + " Jangan Ngetag, Riibut!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  nadya.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "20001316",
                                                       "STKPKGID": "1582380",
                                                       "STKVER": "1" }
                                  nadya.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:
                    contact = nadya.getContact(msg.from_)
                    cName = contact.displayName
                    #balas = ""
                    balas1 = "Tak Ada Kata 💬 Yang Lebih Indah 🎆🌠Selain Dari Namamu🎉🎈 "  +cName
                    #ret_ = random.choice(balas)
                    image ="http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  #nadya.sendText(msg.to,ret_)
                                  nadya.sendText(msg.to,balas1)
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': msg.from_}
                                  nadya.sendMessage(msg)
                                  #nadya.sendText(msg.to,"😉")
                                  #h = nadya.getContact(msg.from_)
                                  #nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)                       
                                  #h = nadya.getContact(msg.from_)
                                  #cu = nadya.channel.getCover(msg.from_)
                                  #path = str(cu)
                                  #nadya.sendImageWithURL(msg.to, path)
                                  #msg.contentType = 7   
                                  #msg.text = None
                                  #msg.contentMetadata = {
                                                       #"STKPKGID": "11538",
                                                       #"STKTXT": "[]",
                                                       #"STKVER": "1",
                                                       #"STKID": "51626499"}
                                  #nadya.sendMessage(msg)
                                  break  
                                  
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                nadya.sendText(msg.to,"Bot Sudah On Boss Quh.")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.contentType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                nadya.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    nadya.sendChatChecked(msg.from_,msg.id)
                else:
                    nadya.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndurl"]
                     nadya.like(url[25:58], url[66:], likeType=1005)
                     nadya.comment(url[25:58], url[66:], wait["comment"])
                     nadya.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False

            if "Show " in msg.text:
                    key = msg.text[-33:]
                    sendMessage(msg.to, text=None, contentMetadata={'mid': key}, contentType=13)
                    contact = nadya.getContact(key)
                    sendMessage(msg.to, ""+contact.displayName+"'s contact")

            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            nadya.sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            nadya.sendText(msg.to,"Ditambahkan")
		    else:
			nadya.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        nadya.sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        nadya.sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     nadya.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = nadya.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = nadya.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         nadya.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = nadya.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = nadya.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         nadya.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = nadya.getGroup(msg.to)
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
                            u = "nadyaose"
                        else:
                            u = "open"
                        nadya.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nurl:" + u + "it is inside")
                    else:
                        nadya.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"Can not be used outside the group")
                    else:
                        nadya.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': tjia}
                nadya.sendText(msg.to,"❂••••••=═ই✪͜͡✪۝✪͜͡✪ई═=•••••❂")
                nadya.sendText(msg.to,"❂••••••••••✧✧✧••••••••••❂")
                nadya.sendMessage(msg)
                h = nadya.getContact(mid)
                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                nadya.sendMessage(msg)
		nadya.sendText(msg.to,"❂•••••{ C_R_E_A_T_O_R }•••••❂")
		nadya.sendText(msg.to,"❂••••••=═ই✪͜͡✪۝✪͜͡✪ई═=•••••❂")

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = nadya.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                nadya.sendMessage(msg)
		nadya.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post url\n" + msg.contentMetadata["postEndurl"]
                    nadya.sendText(msg.to,msg.text)


            elif "Add" in msg.text:
                    nadya.sendText(msg.to,"❂••••••[_Ꭺ҉ Ꭰ҉ Ꭰ҉ _]••••••❂ ")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u978f7e8d02351b3d1d4a3973000c2080"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u5818cb4404411c2e2e6e6937d172cca8"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u17a086ccff618e754588a1108335867f"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua028b2a4f96dff4b4a52ae25223e5073"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "udfaf52176415b46cb445ae2757ec85f3"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u29ad304bbe5e9025b8431e65832a4cfa"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u565281632a958bb2795f6434f6872e3b"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u30ceda3992172f0861558a2b7a6ef5ab"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u224e7f2fd36e3565b0756319936450c5"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u604ca77dec7ab8d450ae762d5d08cd93"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2ca90ea24d7ba639272925d715d8a99c"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2552e86aab1b1426749dd0439b0f8c7f"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "uc67a847198ce188b412a058d86f10367"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u190afbb99dd1c28cc57642627f2aa1a2"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u12322ff2ca2b48474389f3d91b9ff385"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2beb70887d61c0e3abf3ac327b7b21d9"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ub08e59948aaf244041d99091254e743c"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u2c83fe9f836a2f74f7f9316e0c184f9d"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u02c62ba90a4f9ff95950d1a5ee9f2154"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u47b8e60143e0e1c6fdebe67e6a355ad2"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u70489ca3e0d013e866a556665ee9d99b"}
                    nadya.sendMessage(msg)
                    nadya.sendText(msg.to,"❂••••••• [_TQ_] ••••••❂ ")
                    nadya.sendText(msg.to,"ADD AJA BOSS...")

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = nadya.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                nadya.findAndAddContactsByMid(target)
                                contact = nadya.getContact(target)
                                cu = nadya.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                nadya.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                nadya.sendText(msg.to,"Profile Picture " + contact.displayName)
                                nadya.sendImageWithURL(msg.to,image)
                                nadya.sendText(msg.to,"Cover " + contact.displayName)
                                nadya.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = nadya.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                nadya.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                nadya.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break

            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = nadya.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        nadya.sendText(msg.to, "Ok...")
                        pass
                    else:
                        for target in targets:
                            try:
                                nadya.nadyaoneContactProfile(target)
                                nadya.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = nadya.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             nadya.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 nadya.findAndAddContactsByMid(target)
                                 nadya.inviteIntoGroup(msg.to,[target])
                                 nadya.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      nadya.sendText(msg.to,"Success Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
                nadya.sendText(msg.to,creatorMessage)

            elif msg.text in ["Aku","Bot","Comand"]:
                nadya.sendText(msg.to,akuMessage)

            elif msg.text in ["Key","help","Help"]:
                nadya.sendText(msg.to,helpMessage)

            elif msg.text in ["Key self","help self","Self"]:
                nadya.sendText(msg.to,selfMessage)

            elif msg.text in ["Key bot","help bot","Help bot"]:
                nadya.sendText(msg.to,botMessage)

            elif msg.text in ["Key set","help set","Help set"]:
                nadya.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help media"]:
                nadya.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
                nadya.sendText(msg.to,adminMessage)               
                

 
            elif msg.text in ["List group"]:
                    gid = nadya.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = nadya.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    nadya.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = nadya.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = nadya.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    nadya.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    nadya.sendText(msg.to, "Khusus Nadya")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        nadya.sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +nadya.getGroup(gid).name + "\n"
                        nadya.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    nadya.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if nadya.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    nadya.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    nadya.sendText(msg.to, "Khusus Nadya")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = nadya.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = nadya.getGroup(i).name
		            if h == ng:
		                nadya.inviteIntoGroup(i,[Creator])
			        nadya.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        nadya.sendText(msg.to,"Khusus Nadya")
		except Exception as e:
		    nadya.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = nadya.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = nadya.getGroup(i).name
		        if h == ng:
			    nadya.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            nadya.leaveGroup(i)
			    nadya.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")
 
	    elif "Leave all group" == msg.text:
		gid = nadya.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			nadya.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        nadya.leaveGroup(i)
		    nadya.sendText(msg.to,"Success Leave All Group")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = nadya.getGroupIdsJoined()
                for i in gid:
                    h = nadya.getGroup(i).name
                    gna = nadya.getGroup(i)
                    if h == saya:
                        nadya.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        nadya.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        nadya.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    nadya.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","url on"]:
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    nadya.updateGroup(X)
                    nadya.sendText(msg.to,"url Sudah Aktif")
                else:
                    nadya.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","url off"]:
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    nadya.updateGroup(X)
                    nadya.sendText(msg.to,"url Sudah Di Nonaktifkan")

                else:
                    nadya.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    nadya.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    nadya.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    nadya.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    nadya.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")		    
		    
 
            elif msg.text in ["Virus on"]:
		if msg.from_ in admin:
                    wait["Tagvirus"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    nadya.sendText(msg.to,"Virus Tag Sudah Aktif Mohon Berhati-hatilah")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")

            elif msg.text in ["Virus off"]:
		if msg.from_ in admin:
                    wait["Tagvirus"] = False
                    nadya.sendText(msg.to,"Virus Tag Sudah Off")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")	
		    
		    
            elif msg.text in ["Virus on"]:
		if msg.from_ in admin:
                    wait["Tagvirus"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    nadya.sendText(msg.to,"Tag Virus Sudah Aktif Harap Berhati-Hati..!!!")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    nadya.sendText(msg.to,"Virus Tag Sudah Off")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")	
		    

            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    nadya.sendText(msg.to,"Auto Respon3 Sudah Aktif")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    nadya.sendText(msg.to,"Auto Respon3 Sudah Off")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")	
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    nadya.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    nadya.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")			  
		 
            elif msg.text in ["Add:on","Add on"]:
                if wait["autoAdd"] == True:
                   if wait["lang"] == "JP":
                       nadya.sendText(msg.to,"Sudah On Bos Quh")
                   else:
                       nadya.sendText(msg.to,"Sudah On Bos Quh")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"Sudah On Bos Quh")
                    else:
                        acil.sendText(msg.to,"Hal ini sudah on")
            elif msg.text in ["Add:off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"Hal ini sudah off")
                    else:
                        nadya.sendText(msg.to,"Hal ini sudah dimatikan")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"Sudah Off Bos Quh")
                    else:
                        nadya.sendText(msg.to,"Untuk mengaktifkan-off")

 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                nadya.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    nadya.sendText(msg.to,"Khusus Nadya")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                nadya.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    nadya.sendText(msg.to,"Khusus Nadya")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                nadya.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    nadya.sendText(msg.to,"Khusus Nadya")		

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                nadya.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    nadya.sendText(msg.to,"Khusus Nadya")		    

	    elif "Qr on" in msg.text:
	     if msg.from_ in admin:	        
	        wait["Qr"] = True
	    	nadya.sendText(msg.to,"QR Protect Sudah Aktif")
	     else:
		    nadya.sendText(msg.to,"Khusus Nadya")	    	

	    elif "Qr off" in msg.text:
	     if msg.from_ in admin:	        
	    	wait["Qr"] = False
	    	nadya.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    nadya.sendText(msg.to,"Khusus Nadya")	    	

                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = True
		     nadya.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        nadya.sendText(msg.to,"Khusus Nadya")	     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in admin:	 	        
		     wait["AutoKick"] = False
		     nadya.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        nadya.sendText(msg.to,"Khusus Nadya")	     


            elif msg.text in ["Allprotect on"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    nadya.sendText(msg.to,"All Protect Sudah Aktif Semua")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in admin:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    nadya.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    nadya.sendText(msg.to,"Khusus Nadya")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                nadya.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                nadya.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                nadya.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                nadya.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                


            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"Sambutan Di Aktifkan")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"Sudah Off(p′︵‵。)")

            elif "Send " in msg.text:
                    cond = msg.text.split(" ")
                    target = cond[1]
                    text = msg.text.replace("Send " + str(target) + " Chat ","")
                    try:
                        nadya.findAndAddContactsByMid(target)
                        sendMessage(target,"From Alin : \"" + text + "\"")
                        sendMessage(msg.to,"Berhasil mengirim pesan")
                    except:
                        sendMessage(msg.to,"Gagal mengirim pesan, mungkin midnya salah")
                        
            elif "Sniper on" in msg.text:
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
                nadya.sendText(msg.to,"Mode Sniper On")
                
            elif "Sniper off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    nadya.sendText(msg.to, "Mode Sniper Off")
                else:
                    nadya.sendText(msg.to, "Heh Belom Di Set")                         

            elif msg.text in ["Settings"]:
                md = ""
		if wait["Sambutan"] == True: md+="🔧🔓 Sambutan : On\n"
		else:md+="🔧🔒 Sambutan : Off\n"
		if wait["AutoJoin"] == True: md+="🔧🔓 Auto Join : On\n"
                else: md +="🔧🔒 Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="🔧🔓 Auto Join Cancel : On\n"
                else: md +="🔧🔒 Auto Join Cancel : Off\n"                
		if wait["Contact"] == True: md+="🔧🔓 Info Contact : On\n"
		else: md+="🔧🔒 Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="🔧🔓 Auto Cancel : On\n"
                else: md+= "🔧🔒 Auto Cancel : Off\n"
                if wait["autoAdd"] == True:md+="🔧🔓 Auto Add : On\n"
                else: md+= "🔧🔒 Auto Add : Off\n"
                if wait["inviteprotect"] == True:md+="🔧🔓 Invite Protect : On\n"
                else: md+= "🔧🔒 Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="🔧🔓 Qr Protect : On\n"
		else:md+="🔧🔒 Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="🔧🔓 Auto Kick : On\n"
		else:md+="🔧🔒 Auto Kick : Off\n"
		if wait["alwaysRead"] == True: md+="🔧🔓 Always Read : On\n"
		else:md+="🔧🔒 Always Read: Off\n"
		if wait["Tagvirus"] == True: md+="🔧🔓 Virus : On\n"
		else:md+="🔧🔒 Virus : Off\n"		
		if wait["detectMention2"] == True: md+="🔧🔓 Auto Respon2 : On\n"
		else:md+="🔧🔒 Auto Respon2 : Off\n"	
		if wait["detectMention3"] == True: md+="🔧🔓 Auto Respon3 : On\n"
		else:md+="🔧🔒 Auto Respon3 : Off\n"			
		if wait["kickMention"] == True: md+="🔧🔓 Auto Respon Kick : On\n"
		else:md+="🔧🔒 Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="🔧🔓 Auto Sider : On\n"
		else:md+="🔧🔒 Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="🔧🔓 Simisimi : On\n"
		else:md+="🔧🔒 Simisimi: Off\n"		
                nadya.sendText(msg.to,"⛥҉ S҉ E҉ T҉ T҉ I҉ N҉ G҉ S҉ ⛦҉ "+md+"")

            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                nadya.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = nadya.getGroup(msg.to)
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
                                    nadya.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    nadya.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)
                

            elif "tag all" == msg.text.lower():
                 group = nadya.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 nadya.sendMessage(cnt)
                 
#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag","Cuy","Hem","Crit"]:
                  group = nadya.getGroup(msg.to)
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
                  cnt.text = "Total : " + str(jml) +  " Nyawa "
                  cnt.text = "❍••••••{Mention By:}••••••❍\n\n❍•••{ᎪᏙᎡᏆᏞᏆᎪ_ᏞᎬᏙᎪNᎪ}•••❍\n\nTotal: " + str(jml) +  " Nyawa\n"+ datetime.now().strftime('%H:%M:%S')
                  cnt.to = msg.to
                  nadya.sendMessage(cnt)
                  if jml > 500:
                      cnt = Message()
                      cnt.text = "❂••••••{Mention By:}••••••❂\n\n❂•••{ᎪᏙᎡᏆᏞᏆᎪ_ᏞᎬᏙᎪNᎪ}•••❂\n\n"+ datetime.now().strftime('%H:%M:%S')
                      cnt.to = msg.to
                      nadya.sendMessage(cnt)
#-------------Fungsi Tag All Finish--------------#
            elif "Blereng gaes" == msg.text.lower():
                 group = nadya.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 nadya.sendMessage(cnt)                 


            elif msg.text in ["Setview","Start","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                nadya.sendText(msg.to, "L O A D I N G S . . . .")
                nadya.sendText(msg.to, "███████████▒%")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Finish","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('success')
                            pass
                    contactId = nadya.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔❂•┅═ই✪͜͡ KANG NGINTIP ͜͡✪ई═┅•❂\n║\n╠ ͜͡✪➢"
                        grp = '\n╠ ͜͡✪➢ '.join(str(f) for f in dataResult)
                        total = '\n║\n╠❂•••┅═ই✪͜͡ ❂❂❂ ͜͡✪ई═┅•••❂\n║\n╠ ͜͡✪➢ Total %i Kang Ngintip (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n║\n║\n╚❂•┅═ই✪͜͡ KANG NGINTIP ͜͡✪ई═┅•❂"
                        nadya.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        nadya.sendText(msg.to, "Cctv Jones Seumur Hidup...amiin ")                        
                    else:
                        nadya.sendText(msg.to, "☆Belum Ada Viewers☆")
                    print "Viewseen"


	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    nadya.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    nadya.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = nadya.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    nadya.findAndAddContactsByMids(mi_d)
		    nadya.sendText(msg.to,"Success Add all")


            elif msg.text in ["Invite"]:
                wait["invite"] = True
                nadya.sendText(msg.to,"Send Contact")
                
                

            elif msg.text in ["Like on"]:
                wait["likeOn"] = True
                nadya.sendText(msg.to,"Likers Activ")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                nadya.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                nadya.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Copycontact"]:
                wait["copy"] = True
                nadya.sendText(msg.to,"Send Contact") 
                
            elif msg.text in ["Sticker on"]:
                wait["sticker"] = True
                nadya.sendText(msg.to,"Sticker ID Detect Already On.")  
                
            elif msg.text in ["Bot off"]:
                wait["Bot"] = False
                nadya.sendText(msg.to,"Bot Sudah Di Nonaktifkan Boss Quh...")  

	    elif "Recover" in msg.text:
		thisgroup = nadya.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		nadya.createGroup("Recover", mi_d)
		nadya.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = nadya.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    nadya.updateGroup(X)
                else:
                    nadya.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		if midd not in admin:
		    nadya.kickoutFromGroup(msg.to,[midd])
		else:
		    nadya.sendText(msg.to,"Admin Detected")

            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                nadya.findAndAddContactsByMid(midd)
                nadya.inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
                midd = "ubd7b4dd119abd73ab3df542fb58a8a65"
                nadya.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = nadya.getGroup(msg.to)
                nadya.sendText(msg.to,"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n█░░╔╦╗ ╔╗░░█\n█░░─║─ ║║░░█\n█░░─╩ ─╚╝░░█\n\n❍•••{☠ :" + gs.name+ ": ☠}•••❍\n\nSemoga Betah Kakak\nJangan Lupa Nikung Yehkan...\nDah Gitu Ajah\n\n[TQ]\n\n\n===❍•••{☠ʟᴇᴠᴀɴᴀ☠}•••❍===\n\n"+ datetime.now().strftime('%H:%M:%S'))
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                nadya.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = nadya.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			nadya.sendText(i,"╔═──────┅═ই✪͜͡ B⃫̳̳ ̳R⃫̳̳ ̳O⃫̳̳ ̳A⃫̳̳ ̳D⃫̳̳ ̳C⃫̳̳ ̳A⃫̳̳ ̳S⃫̳̳ ̳T⃫̳̳ ̳ ͜͡✪ई═┅───────\n\n"+bc+"\n\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠̶A̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེV̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེR̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེI̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེL̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེI̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ ̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེA̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶̶ེ҉̶̶̶̶̶̶̶̶ེེ࿆ ̶̶̶ེ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────\n"+ datetime.now().strftime('%H:%M:%S'))
		    nadya.sendText(msg.to,"Success BC BosQ")
		else:
		    nadya.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Cancel"]:
                gid = nadya.getGroupIdsInvited()
                for i in gid:
                    nadya.rejectGroupInvitation(i)
                nadya.sendText(msg.to,"All invitations have been refused")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = nadya.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        nadya.updateGroup(x)
                    gurl = nadya.reissueGroupTicket(msg.to)
                    nadya.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        nadya.sendText(msg.to,"Can't be used outside the group")
                    else:
                        nadya.sendText(msg.to,"Not for use less than group")


            elif msg.text in ["timeline"]:
		try:
                    url = nadya.activity(limit=5)
		    nadya.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["@bye","@Bye"]:
		    nadya.leaveGroup(msg.to)		    
		    
#-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Jam",""]:
              #if msg.from_ in admin:
                nadya.sendText(msg.to,"ᴛɪᴍᴇʀ: " + datetime.now().strftime('%H:%M:%S'))


            elif msg.text.lower() in ["respon"]:
                nadya.sendText(msg.to,responsename)

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start                
                nadya.sendText(msg.to, "===❍•••{☠full speed☠}•••❍===")
                nadya.sendText(msg.to, "███████████%")
                nadya.sendText(msg.to, "%sseconds" % (elapsed_time))
                                
            elif msg.text in ["Testing"]:
                start = time.time()
                nadya.sendText(msg.to, "「Progress...」")
                nadya.sendText(msg.to, "「Debuging Speed」")
                elapsed_time = time.time() - start
                nadya.sendText(msg.to, "%sseconds" % (elapsed_time))                
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    nadya.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    nadya.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    nadya.sendText(msg.to,"Succes BosQ")
                                except:
                                    nadya.sendText(msg.to,"Success")
			    else:
				nadya.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    nadya.sendText(msg.to,"send contact")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +nadya.getContact(mi_d).displayName + "\n"
                    nadya.sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                nadya.sendText(msg.to,"Succes BosQ")
                            except:
                                nadya.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    nadya.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            nadya.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            nadya.kickoutFromGroup(msg.to,[jj])
                        nadya.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    nadya.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            nadya.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                nadya.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Bar" in msg.text:
                if msg.toType == 2:
                    print "Kick all member"
                    _name = msg.text.replace("Bar","")
                    gs = nadya.getGroup(msg.to)
                    gs = nadya.getGroup(msg.to)
                    gs = nadya.getGroup(msg.to)
                    gs = nadya.getGroup(msg.to)
                    gs = nadya.getGroup(msg.to)
                    gs = nadya.getGroup(msg.to)
                    gs = nadya.getGroup(msg.to)
                    gs = nadya.getGroup(msg.to)
                    h = nadya.getContact(mid)
                    nadya.sendText(msg.to,"──────┅═ই✪͜͡ ۝ ͜͡✪ई═┅───────")
                    nadya.sendText(msg.to,"🅆🄴🄻🄲🄾🄼🄴 🅃🄾\n🄺🄸🄲🄺🄴🅁 🄰🅁🄴🄽🄰\n_______________________________ ")
                    nadya.sendText(msg.to,"【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】")
                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+h.pictureStatus)
                    #nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/0h4f8Us-i0a0kFLEezZY8UHjlpZSRyAm0BfU12fXV_PCwtTipPOxghe3IkPHshFS5Pakl0LXcuYi0h")
                    nadya.sendText(msg.to,"⚠️⚠️__AWAS!!! __⚠️⚠️\n___TANPA PERMISI GW___\n🔥 BAKAR GRUP LO NYET!!🔥\n___JANGAN TANYA KENAPA___\n😎KARNA KAMI PUNYA PRINSIF 😎\n  KALO GAK RATA ZOOM MUKA KANG KIBAR\n\n\n──────┅═ই۝ई═┅──────\n【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n       ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n      line.me/ti/p/AqTXMqygnD\n──────┅═ই۝ई═┅──────\n\n\nKAMI TAU APA!!?? KAMI HANYA NUMPANG KIBAR&PLAY\n\n\nDAH GITU AJA TQ\n\n\n(itu)JADI TANGKIS AJE BOSS (itu)\n\n\nGO!!  GO!!  GO!!  GO!!  GO!!\n\n\n________ (go)________ ")
                    nadya.sendText(msg.to,"❂•••••••••••✧•••••••••••❂ ")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u978f7e8d02351b3d1d4a3973000c2080"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u5818cb4404411c2e2e6e6937d172cca8"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u17a086ccff618e754588a1108335867f"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua028b2a4f96dff4b4a52ae25223e5073"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "udfaf52176415b46cb445ae2757ec85f3"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u29ad304bbe5e9025b8431e65832a4cfa"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u565281632a958bb2795f6434f6872e3b"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u30ceda3992172f0861558a2b7a6ef5ab"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u224e7f2fd36e3565b0756319936450c5"}
                    nadya.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u604ca77dec7ab8d450ae762d5d08cd93"}
                    nadya.sendMessage(msg)
                    nadya.sendText(msg.to,"❂•••••••••••✧•••••••••••❂ ")
                    nadya.sendText(msg.to,"★_____TANGKIS NYETT_____★\n\nUDAH GITU  AJA YANG PENTING KIBAR\n\n🔥RATA KAMI SENANG GAK RATA BULY AJE KAMI  DISINI🔥\n\n\n__JADI TANGKIS AJA GO_GO_GO_!!!!!__\n\n______【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】______ ")
                    nadya.sendText(msg.to,"──────┅═ই✪͜͡ ۝ ͜͡✪ई═┅─────── ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Set Kibaran Succes Boss Quh ...Dah Gitu Aja...\nTQ")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[nadya,]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                nadya.sendText(msg,to,"Group nadyaeanse")

            elif "Sikat all" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Sikat all","")
                        gs = nadya.getGroup(msg.to)
                        nadya.sendText(msg.to,"Go_Go_Go......")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            nadya.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        nadya.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        nadya.sendText(msg.to,str(e))
			    #nadya.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Restart","Reboot"]:
		if msg.from_ in Creator:
		    nadya.sendText(msg.to, "Bot Restarted Loadings...ฺ")
		    nadya.sendText(msg.to, "███████████▒99%")
		    nadya.sendText(msg.to, "Succes Restarted Bot ✔")
		    restart_program()
		    print "@Restart"
		else:
		    nadya.sendText(msg.to, "Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Code #13' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ubd7b4dd119abd73ab3df542fb58a8a65'"}
                nadya.sendMessage(msg)

 
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = nadya.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       nadya.sendText(msg.to, "Ok...")
                   else:
                       for target in targets:
                            try:
                               nadya.nadyaoneContactProfile(target)
                               nadya.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Mybackup"]:
                try:
                    nadya.updateDisplayPicture(backup1.pictureStatus)
                    nadya.updateProfile(backup1)
                    nadya.sendText(msg.to, "Done (^_^)")
                except Exception as e:
                    nadya.sendText(msg.to, str(e))

 
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						nadya.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						nadya.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						nadya.sendAudioWithurl(msg.to,abc)
						nadya.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        nadya.sendText(msg.to, hasil)
                except Exception as wak:
                        nadya.sendText(msg.to, str(wak))
                        
	    elif "Musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						nadya.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						nadya.sendAudioWithurl(msg.to,abc)
						nadya.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						nadya.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
             
            
            
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    nadya.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Ok")
                    else:
                        for target in targets:
                            try:
                                h = nadya.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                nadya.sendText(msg.to,"Upload image success.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Ok")
                    else:
                        for target in targets:
                            try:
                                h = nadya.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                nadya.sendText(msg.to,"Upload image success.")
                                
            elif "Cpp" in msg.text:
                if msg.from_ in admin:
                    path = "nadya.jpg"
                    nadya.sendText(msg.to,"Update PP :")
                    nadya.sendImage(msg.to,path)
                    nadya.updateProfilePicture(path)                                
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Ok")
                    else:
                        for target in targets:
                            try:
                                h = nadya.getContact(target)
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                nadya.sendText(msg.to,"Upload image success.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = nadya.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendText(msg.to,"Ok")
                    else:
                        for target in targets:
                            try:
                                h = nadya.getContact(target)
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                nadya.sendText(msg.to,"Upload image success.")

            elif msg.text in ["pap owner","pap creator"]:
                                h = nadya.getContact(mid)
                                nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+ h.pictureStatus)

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    nadya.sendText(msg.to,"spam changed")
                else:
                    nadya.sendText(msg.to,"Done")
 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 100
                  while(t):
                    nadya.sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = nadya.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      nadya.sendText(manusia, (bctxt))
                      t-=1

            elif "Cbc " in msg.text:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = nadya.getAllContactIds()
                  for manusia in orang:
                    nadya.sendText(manusia, (broadcasttxt))
                   
            elif msg.text in ["Gspam on"]:
	          if msg.from_ in admin:
				wait["S "] = True
				nadya.sendText(msg.to,"send contact")
#==============================================
            elif "Sp @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Sp @","")
                _nametarget = _name.rstrip(' ')
                gs = nadya.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                        nadya.sendText(g.mid,"╔═────────┅═ই۝ई═┅─────────\n║  ❂•••••••••••✧•••••••••••❂\n║          【ᏴᏞᎪᏟK\_☠☬☠_/ᎪNᏩᎬᏞᏚ】\n║                   ᎪᏙᎡᏆᏞᏆᎪ ᏞᎬᏙᎪNᎪ\n║  ❂•••••••••••✧•••••••••••❂\n╠═────────┅═ই۝ई═┅─────────\n║    ❂•••{☠ᏴᏞᎪᏟK ᎪNᏩᎬᏞᏚ☠}•••❂\n  http://line.me/ti/p/~avrilia_quester\n╚═────────┅═ই۝ई═┅─────────")
                    else:
                        pass
                        
            elif "Kelinci @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Kelinci @","")
                _nametarget = _name.rstrip(' ')
                gs = nadya.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       xname = g.displayName
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(g.mid,"....▓▓▓▓\n..▓▓......▓\n..▓▓......▓▓..................▓▓▓▓\n..▓▓......▓▓..............▓▓......▓▓▓▓\n..▓▓....▓▓..............▓......▓▓......▓▓\n....▓▓....▓............▓....▓▓....▓▓▓....▓▓\n......▓▓....▓........▓....▓▓..........▓▓....▓\n........▓▓..▓▓....▓▓..▓▓................▓▓\n........▓▓......▓▓....▓▓\n.......▓......................▓\n.....▓.........................▓\n....▓......^..........^......▓\n....▓............❤............▓\n....▓..........................▓\n......▓..........◡..........▓\n..........▓▓..........▓▓")
                       nadya.sendText(msg.to, "Success To Pm Target")
                       print " Spammed !"
                       
            elif "To @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("To @","")
                _nametarget = _name.rstrip(' ')
                gs = nadya.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       xname = g.displayName
                       nadya.sendText(g.mid,"_░▒███████\n░██▓▒░░▒▓██\n██▓▒░__░▒▓██___██████\n██▓▒░____░▓███▓__░▒▓██\n██▓▒░___░▓██▓_____░▒▓██\n██▓▒░_______________░▒▓██\n_██▓▒░______________░▒▓██\n__██▓▒░____________░▒▓██\n___██▓▒░__________░▒▓██\n____██▓▒░________░▒▓██\n_____██▓▒░_____░▒▓██\n______██▓▒░__░▒▓██\n_______█▓▒░░▒▓██\n_________░▒▓██\n_______░▒▓██\n_____░▒▓██")
                       nadya.sendText(g.mid,". . . . . . . . . . .*. . . . . . . ** *\n. . . . .. . . . . .*** . . * . . *****\n. . . . . . . . . . .** . . **. . . . .*\n. . . . . . . . . . ***.*. . *. . . . .*\n. . . . . . . . . .****. . . .** . . . ******\n. . . . . . . . . ***** . . . .**.*. . . . . **\n. . . . . . . . .*****. . . . . **. . . . . . *.**\n. . . . . . . .*****. . . . . .*. . . . . . *\n. . . . . . . .******. . . . .*. . . . . *\n. . . . . . . .******* . . .*. . . . .*\n. . . . . . . . .*********. . . . . *\n. . . . . . . . . .******* . ***\n*******. . . . . . . . .**\n.*******. . . . . . . . *\n. ******. . . . . . . . * *\n. .***. . *. . . . . . .**\n. . . . . . .*. . . . . *\n. . . . .****.*. . . .*\n. . . *******. .*. .*\n. . .*******. . . *.\n. . .*****. . . . *\n. . .**. . . . . .*\n. . .*. . . . . . **.*\n. . . . . . . . . **\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . .*\n. . . . . . . . *\n. . . . . . . . *")
                       nadya.sendText(g.mid,"(¯`v´¯) Love Me\n`*.¸.*´ ?\n¸.•´¸.•*¨) ¸.•*¨)?\n(¸.•´ (¸.•´ .•´ ¸¸.•¨¯`•.\n(¯`v´¯)\n.`·.¸.·´ ?\n¸.·´¸.·´¨) ¸.·*¨)\n(¸.·´ (¸.·´ .·´ ¸")
                       nadya.sendText(msg.to, "Succes To Pm Target")
                       print " Spammed !"
                       
            elif "S @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("S ","")
                _nametarget = _name.rstrip(' ')
                gs = nadya.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       xname = g.displayName
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(g.mid,"______________________________\n_______________¶______________\n______________¶¶¶_____________\n_____________¶¶¶¶¶____________\n___________¶¶¶¶¶¶¶¶___________\n__________¶¶¶¶¶_¶¶¶¶¶_________\n_________¶¶¶¶_____¶¶¶¶________\n________¶¶¶____¶____¶¶¶_______\n______¶¶¶_____¶¶¶¶____¶¶¶_____\n_____¶¶_____¶¶¶¶¶¶¶_____¶¶____\n____¶______¶¶¶¶¶¶¶¶¶______¶___\n__________¶¶¶¶___¶¶¶¶_________\n________¶¶¶¶_______¶¶¶¶_______\n_______¶¶¶___________¶¶¶______\n______¶¶_______________¶¶_____\n_____¶___________________¶¶___\n____¶_____________________¶¶__\n______________________________")
                       nadya.sendText(msg.to, "Success To Spam Target.")
                       print " Spammed !"
 
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    nadya.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    nadya.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	nadya.sendText(msg.to, str(njer))
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                nadya.sendVideoWithurl(msg.to,url)
                            else:
                                print (node['display_src'])
                                nadya.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'nadyaass':'yt-uix-tile-link'})
                    nadya.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    nadya.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo: ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo: ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'nadyaass': 'yt-uix-tile-link'})
                        nadya.sendVideoWithurl(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        nadya.sendText(msg.to, "Could not find it")                    

 
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = nadya.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")


            elif msg.text.lower() in ["hy","hai","halo","hallo"]:
                    beb = "Hay Sayang 😘 Miss You " +nadya.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    nadya.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                nadya.sendText(msg.to,"Sedang Mencari...")
                nadya.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                nadya.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = nadya.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        nadya.sendText(msg.to, g.mid)
                    else:
                        pass


            elif "Mybio " in msg.text:
                    string = msg.text.replace("Mybio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = nadya.getProfile()
                        profile.statusMessage = string
                        nadya.updateProfile(profile)
                        nadya.sendText(msg.to,"Done")

            elif "Myname " in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("Myname ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = nadya.getProfile()
                        profile.displayName = string
                        nadya.updateProfile(profile)
                        nadya.sendText(msg.to,"Done")



            elif msg.text.lower() in ["mymid","myid"]:
                middd = "Name : " +nadya.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                nadya.sendText(msg.to,middd)

            elif msg.text in ["Me"]:
	      if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                nadya.sendText(msg.to,"❂•••••••┅═ই۝ई═┅••••••••❂") 
                nadya.sendMessage(msg)
                nadya.sendText(msg.to,"❂•••••••┅═ই۝ई═┅••••••••❂")
                #h = nadya.getContact(mid)
                #nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                #nadya.sendText(msg.to,"❂•••••••┅═ই۝ई═┅••••••••❂")
                nadya.sendText(msg.to,"[Avrilia Ini Mahh...!!!]\nDah Gitu Aja\n[TQ]\n\n"+ datetime.now().strftime('%H:%M:%S'))

            elif "Apakah " in msg.text:
                apk = msg.text.replace("Apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")
                
            elif "Hari " in msg.text:
                apk = msg.text.replace("Hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")   


            elif "Berapa " in msg.text:
                apk = msg.text.replace("Berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")
                
            elif "Berapakah " in msg.text:
                apk = msg.text.replace("Berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")                

            elif "Kapan " in msg.text:
                apk = msg.text.replace("Kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                nadya.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                nadya.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                nadya.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    nadya.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nurl : http://www.youtube.com' + a['href'],'\n\n'))
                        nadya.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                nadya.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                nadya.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                nadya.sendText(msg.to, A)                

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'nadyaass="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                nadya.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'nadyaass="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                nadya.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'nadyaass="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                nadya.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'nadyaass="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                nadya.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = nadya.getAllContactIds()
                kontak = nadya.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                nadya.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = nadya.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                nadya.sendText(msg.to, msgs)

            

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = nadya.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    nadya.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = nadya.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            nadya.sendVideoWithurl(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = nadya.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                nadya.sendImageWithURL(msg.to,path)

            elif "urlgroup image" in msg.text:
                group = nadya.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                nadya.sendText(msg.to,path)
 
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    nadya.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    nadya.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    nadya.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    nadya.sendText(msg.to,"Profile Picture " + contact.displayName)
                    nadya.sendImageWithURL(msg.to,image)
                    nadya.sendText(msg.to,"Cover " + contact.displayName)
                    nadya.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "You" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = nadya.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                nadya.sendMessage(msg)

            elif "Info" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    nadya.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    nadya.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Bio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = nadya.getContact(key1)
                cu = nadya.channel.getCover(key1)
                try:
                    nadya.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    nadya.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "===❍•••{☠ʙᴏᴛ\nsᴜᴅᴀʜ ʙᴇʀᴊᴀʟᴀɴ\nsᴇʟᴀᴍᴀ☠}•••❍=== :\n"+waktu(eltime)
                nadya.sendText(msg.to,van)
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                nadya.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                nadya.sendText(msg.to, rst)                
                 
                
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = nadya.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                nadya.sendMessage(msg)
                
            elif "Searchid: " in msg.text:
                userid = msg.text.replace("Searchid: ","")
                contact = nadya.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                nadya.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        nadya.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        nadya.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        nadya.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        nadya.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            nadya.findAndAddContactsByMid(msg.from_)
                            nadya.inviteIntoGroup(gid,[msg.from_])
                        except:
                            nadya.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                nadya.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = nadya.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠➩" + "%s\n" % (nadya.getGroup(i).name +" ~> ["+str(len(nadya.getGroup(i).members))+"]")
                nadya.sendText(msg.to,"╔═════════════════════════\n║          ☆☞ LIST GROUPS☜☆\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚═════════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = nadya.getGroupIdsJoined()
                kontak = nadya.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                nadya.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    nadya.sendText(msg.to,"Sedang Mencari...")
                    nadya.sendText(msg.to, "https://www.google.com/" + b)
                    nadya.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        nadya.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = nadya.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            nadya.sendText(msg.to,h)
                        except Exception as error:
                            nadya.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = nadya.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                nadya.rejectGroupInvitation(i)
                            except:
                                nadya.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        nadya.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        nadya.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = nadya.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = nadya.getGroup(i)
                            _list += gids.name
                            nadya.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        nadya.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        nadya.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  


            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                nadya.sendGifWithurl(msg.to,gore)
                

                
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        nadya.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        nadya.sendText(msg.to,"Fail !")
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
                        nadya.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        nadya.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Minadyaist"]:
                        if mimic["target"] == {}:
                            nadya.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+nadya.getContact(mi_d).displayName + "\n"
                            nadya.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                nadya.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                nadya.sendText(msg.to,"Mimic change to target")
                            else:
                                nadya.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        nadya.sendText(msg.to,"Reply Message on")
                    else:
                        nadya.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        nadya.sendText(msg.to,"Reply Message off")
                    else:
                        nadya.sendText(msg.to,"Sudah off")
#------------------------------------------------------------------
            elif msg.text in ["clear"]:
                if msg.toType == 2:
                    group = nadya.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        nadya.cancelGroupInvitation(msg.to,[_mid])
                    nadya.sendText(msg.to,"Success vril...")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = nadya.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            group.name = name
                            nadya.updateGroup(group)
                    except:
                        nadya.sendText(msg.to,"Success")
                        pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = nadya.fetchOps(nadya.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(nadya.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            nadya.Poll.rev = max(nadya.Poll.rev, Op.revision)
            bot(Op)

