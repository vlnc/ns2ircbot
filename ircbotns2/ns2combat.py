#&/usr/bin/env python

import urllib2
import urllib
import cookielib
import socket
import json
import irclib
import ircbot



# IRC
serverIRC = "irc.quakenet.org"
portIRC = 6667
channel = "#ns2france"
botName = "ns2combat"
botInfo = ""

# Serveur de jeux
ip = ""
port = ""
username = ""
password = ""

#URL
theurl = "http://" + ip + ":" + port + "/"
status = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_status"


 
def auth():

	    #authhandler=urllib2.HTTPHandler(debuglevel=1)
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, theurl, username, password)
        authhandler = urllib2.HTTPDigestAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        

              
class Bot(ircbot.SingleServerIRCBot):

    def __init__(self):
        ircbot.SingleServerIRCBot.__init__(self, [(serverIRC, int(portIRC))],
                                           botName, botInfo)
    def on_welcome(self, serv, ev):
        serv.join(channel)
        
    def on_pubmsg(self, serv, ev):
        firstCom = ev.arguments()[0]
        auteur = irclib.nm_to_n(ev.source())
        canal = (ev.target(), self.channels[ev.target()]) # tuple (nom, ircbot.Channel)
        #message = ev.arguments()[0].lower()
        
        
        
        if bool(canal[1].is_oper(auteur)) == True:
                
                if "&say" in firstCom:
                    
                    try:
                            space = chr(32)
                            spaceSay = firstCom[5:100].replace(space, "%20")
                            
                            # TESTING
                            test1 = ev.source()
                            test2 = ev.eventtype()
                            

                            
                                                
                            sayAll = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_say%20" + spaceSay
                            pagehandleSay = urllib2.urlopen(sayAll, timeout=2)
                            urlSayAll = pagehandleSay.geturl()
                            #serv.privmsg(channel, "Admin dit : " + firstCom[5:100] + " sur le serveur")
                  
                    except urllib2.URLError, e:
                            serv.privmsg(channel, "URLError -> " + urlSayAll)
                   
                     
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)    
                    else:   
                            serv.privmsg(channel, "message sent")
                            #serv.privmsg(channel, test1)
                            #serv.privmsg(channel, test2)

                            
                if "&listbans" in firstCom:
                
                    try:                                
                            listBans = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_listbans"
                            pagehandleListBans = urllib2.urlopen(listBans, timeout=2)                            
                            urlListBans = pagehandleListBans.geturl()
                            
                    except urllib2.URLError, e:            
                            serv.privmsg(channel, "URLError -> " + listBans)
                                
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)   
                    
                    else:
                            serv.privmsg(channel, "ok")
                            serv.privmsg(channel, urlListBans)                     
                
                    
                if "&auth" in firstCom:
                    serv.privmsg(channel, "Connected to " + theurl)
                
                if "&changemap" in firstCom:
                
                    try:
                            changemap = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_changemap%20" + firstCom[11:100]
                            pagehandleChangemap = urllib2.urlopen(changemap, timeout=5)
                            urlChangeMap = pagehandleChangemap.geturl()
                            
                    except urllib2.URLError, e:
                            serv.privmsg(channel, "URLError -> " + urlChangeMap)
                   
                     
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)
                            
                    else:            
                            serv.privmsg(channel, "Loading : " + firstCom[11:100] + " !")
               
               # if "&biere" in firstCom or "&beer" in firstCom:
                    
               #     if firstCom == "&biere":        
               #         serv.privmsg(channel, "et une biere pour " + firstCom[6:100] + " &")
               #     else:
               #         serv.privmsg(channel, "and one beer for " + firstCom[6:100] + " &")
                
                if "&password" in firstCom:

                    try:        
                            password = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_password%20" + firstCom[10:100]
                            pagehandlePassword = urllib2.urlopen(password, timeout=2)
                            urlPassword = pagehandlePassword.geturl()
                    
                    except urllib2.URLError, e:
                            serv.privmsg(channel, "URLError -> " + urlPassword)
                   
                     
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)
                    
                    else:
                            serv.privmsg(channel, "Password changed")
                    
                if "&kick" in firstCom:
                    
                    try:                    
                            space = chr(32)
                            spaceNick = firstCom[6:100].replace(space, "%20")
                            
                            kick = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_kick%20" + spaceNick                               
                            pagehandleKick = urllib2.urlopen(kick, timeout=2)                       
                            urlKick = pagehandleKick.geturl()
                    
                    except urllib2.URLError, e:
                            serv.privmsg(channel, "URLError -> " + urlKick)
                   
                     
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)
                    
                    else:
                            #serv.privmsg(channel, kick)
                            serv.privmsg(channel, firstCom[6:100] + " a ete kick")
                
                if "&slay" in firstCom:
                
                    try:
                            space = chr(32)
                            spaceNick = firstCom[6:100].replace(space, "%20")
                            
                            slay = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_slay%20" + spaceNick
                            pagehandleSlay = urllib2.urlopen(slay, timeout=2)
                            urlSlay = pagehandleSlay.geturl()
                            
                    except urllib2.URLError, e:
                            serv.privmsg(channel, "URLError -> " + urlSlay)
                   
                     
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)
                            
                    else:      
                            #serv.privmsg(channel, "DEBUGING : " + urlSlay)          
                            serv.privmsg(channel, spaceNick + " slayed")
                
                
                
                if "&eject" in firstCom:
                
                    try:
                            space = chr(32)
                            spaceNick = firstCom[7:100].replace(space, "%20")
                                        
                            eject = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_eject%20" + spaceNick
                            pagehandleEject = urllib2.urlopen(eject, timeout=2)
                            
                            urlEject = pagehandleEject.geturl()
                    
                    except urllib2.URLError, e:
                            serv.privmsg(channel, "URLError -> " + urlEject)
                   
                     
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)   
                            
                    else:
                            #serv.privmsg(channel, "DEBUGING : " + urlEject)
                            serv.privmsg(channel, spaceNick + " ejected")
                           
                if "&players" in firstCom:
                    
                    try:
                            urlStatus = urllib2.urlopen(status, timeout=2).geturl()
                            data = urllib2.urlopen(status, timeout=1).read() 
                            
                    except urllib2.URLError, e:
                            serv.privmsg(channel, "URLError -> " + status)
                   
                     
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)
                            
                    else:

                            if  data == "Server not running":
                                serv.privmsg(channel, "no json data")
                                       
                            else:
                                jr = json.loads(data)
                                
                                for i in range(len(jr['player_list'])):
                         
                                    serv.privmsg(channel, jr['player_list'][i]['name'] + " | " + str(jr['player_list'][i]['steamid']) + " | " + str(jr['player_list'][i]['ping']) + "ms" + " | " + str(jr['player_list'][i]['ipaddress']))
                
                if "&reset" in firstCom:
                
                    try:                               
                            resetRound = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_randomall"
                            pagehandleResetRound = urllib2.urlopen(resetRound, timeout=2)                            
                            urlResetRound = pagehandleResetRound.geturl()
                            
                    except urllib2.URLError, e:            
                            serv.privmsg(channel, "URLError -> " + urlResetRound)
                                
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)   
                    
                    else:
                            serv.privmsg(channel, "ok")                    
                
                if "&randomall" in firstCom:
                    
                    try:
                                
                            randomAll = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_randomall"
                            pagehandleRandomAll = urllib2.urlopen(randomAll, timeout=2)                            
                            urlRandomAll = pagehandleRandomAll.geturl()
                            
                    except urllib2.URLError, e:            
                            serv.privmsg(channel, "URLError -> " + urlRandomAll)
                                
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)   
                    
                    else:
                            serv.privmsg(channel, "ok")                                      
                    
                if "&readyroom" in firstCom:
                    
                    try:
                                
                            readyRoomAll = "http://" + ip + ":" + port + "/?request=json&command=Send&rcon=sv_rrall"
                            pagehandleReadyRoomAll = urllib2.urlopen(readyRoomAll, timeout=2)
                            
                            urlReadyRoomAll = pagehandleReadyRoomAll.geturl()
                            
                    except urllib2.URLError, e:            
                            serv.privmsg(channel, "URLError -> " + urlReadyRoomAll)
                                
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)   
                    
                    else:
                            serv.privmsg(channel, "ok")        
                            
                if "&maps" in firstCom:
                
                    serv.privmsg(channel, "ns2_co_core | ns2_co_faceoff | ns2_pulsecombat")        
                       
                       
                if "&status" in firstCom:
                
                    try:
                            urlStatus = urllib2.urlopen(status, timeout=2).geturl()
                            data = urllib2.urlopen(status, timeout=1).read() 
                            
                    except urllib2.URLError, e:
                            serv.privmsg(channel, "URLError -> " + status)
                   
                     
                    except urllib2.HTTPError, e:
                            serv.privmsg(channel, "HTTPError")
                            serv.privmsg(channel, "Reason: " + e.reason)
                            
                    else:

                            if data == "Server not running":
                                serv.privmsg(channel, "no json data")
                                
                            else:
                                jr = json.loads(data)
                                
                                # Server Informations
                                ns2ServerName = jr['server_name']
                                ns2Map = jr['map']
                                ns2Cheats = jr['cheats']
                                ns2PlayersOnline = jr['players_online']
                                ns2Marines = jr['marines']
                                ns2Aliens = jr['aliens']
                                ns2FrameRate = jr['frame_rate']
                                ns2DevMode = jr['devmode']
                                ns2UpTime = jr['uptime']
                                
                                serv.privmsg(channel, ns2ServerName + " | " + ns2Map + " | " + str(ns2PlayersOnline) + " | " + ns2Cheats + " | " + str(ns2FrameRate))
                
                if "&quit" in firstCom:
                    
                    serv.privmsg(channel, "bye all")
                    self.die()
                
                if "&help" in firstCom:
                
                    serv.privmsg(channel, "&auth | &status | &listbans | &players | &reset | &randomall | &readyroom | &eject | &slay | &maps | &changemap | &say | &password")       
            
        #else:
        #    serv.privmsg(channel, "you no op")
           
if __name__ == "__main__":

    auth()

    try:
        pagehandle = urllib2.urlopen(theurl, timeout=5)
        url = pagehandle.geturl()
        pagehandle.close()

    except urllib2.URLError, e:
        print "URLError -> %s" % (theurl)
        #print e.code
        exit("exiting ...")

    Bot().start()
