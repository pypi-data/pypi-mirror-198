import os
import requests,json,os,string,sys,threading,random



class lsedb:

  user = None
  password = None
  db = None
  stable = None

  def __init__(self,user,password,db,table):
    self.user = enc(user)
    self.password = enc(password)
    self.db = enc(db)
    self.table = enc(table)
    self.url = "https://stormghosts.pythonanywhere.com/api/"
    self.map = {"user":self.user,"password":self.password,"db":self.db,"table":self.table}


  def get(self):
    dd = json.loads(dec(requests.get(self.url+"get",params=self.map).text).replace("'",'"'))
    return dd

  def add(self,maap):
    map = self.map
    map["data"] = enc(json.dumps(maap))
    dd = json.loads(dec(requests.get(self.url+"add",params=map).text).replace("'",'"'))
    return dd

  def edit(self,maap,all=False,key="",value=""):
   if all:
    map = self.map
    map["key"] = enc(key)
    map["value"] = enc(value)
    dd = json.loads(dec(requests.get(self.url+"editall",params=map).text).replace("'",'"'))
    return dd
   else:
    map = self.map
    map["data"] = enc(json.dumps(maap))
    dd = json.loads(dec(requests.get(self.url+"edit",params=map).text).replace("'",'"'))
    return dd
  
  
  
  def delete(self, maap):
    map = self.map
    map["key"] = enc(maap["key"])
    dd = json.loads(dec(requests.get(self.url+"delete",params=map).text).replace("'",'"'))
    return dd









def enc(text):
    if not text:
        return ""
    endText = ""
    for character in text:
        if not character == "\n":
            endText += str(ord(character))+" "
        else:
            endText += str(ord("\n"))+" "
    return endText[:len(endText)-1]




def dec(text):
    if not text:
        return ""
    endText = ""
    txt = text.split(" ")
    for c in txt:
        try:
            endText += chr(int(c))
        except:
            pass
    return endText



def getCode(length = random.randint(12,20), char = string.ascii_uppercase + string.digits + string.ascii_lowercase): 
    return ''.join(random.choice( char) for x in range(length))

