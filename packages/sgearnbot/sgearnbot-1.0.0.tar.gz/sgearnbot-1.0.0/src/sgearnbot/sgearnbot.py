import requests, random, string, os
from .lsedb import *



class sgearnbot:

    url = "https://sgearnbot-server.hellhour.repl.co/sgearnbot/"
    id = None
    link = None
    key = None
    serverdb = lsedb("lse","mahmoud123","sgearnbot","server")
    
    def __init__(self, id):
        self.id = id
    
    
    def get_link(self):
        r = requests.post(self.url+"getlink",data={"id":self.id}).json()
        if r["status"]:
            self.link = r["link"]
            self.key = r["key"]
            return r["link"]
        else:
            return None
        
        
    def check_code(self, code):
        server = self.serverdb.get()["msg"][0]
        r = requests.post(self.url+"checkcode",data={"id":self.id,"key":self.key,"code":code}, headers={"password":server["password"]}).json()
        if r["status"]:
            return True
        else:
            return False


    def default(self):
        link = self.get_link()
        if link:
            os.system("clear")
            print("~> Hello Sir,")
            print("~> Skip This Link To Continue :")
            print(f"\n  ~> {link}\n")
            print("~> After That Get Code and Print It Here\n")
            while True:
                code = input("  ~> Write Code : ")
                if code:
                    if self.check_code(code):
                        break
                    else:
                        print("Wrong Code")
                else:
                    print("Please Write Code")
        else:
            pass
        os.system("clear")

