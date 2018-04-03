import requests
import json

##
# Created with 💙 For Pay.ir From M.Mohamadi :)
##
class payment:
    apikey = None
    def __init__(self,api):
        self.apikey = api
    def GetTransId(self,amount,redirect,factNumber):
        """Get Transaction Url"""
        postdata = {
            "api":self.apikey,
            "amount":amount,
            "redirect":redirect,
            "factorNumber":factNumber
        }
        resp = requests.post("https://pay.ir/payment/send",data=postdata)
        
        jdata = json.loads(resp.text)
        if(jdata["status"]==1):
            return str(jdata["transId"]),"https://pay.ir/payment/gateway/" + str(jdata["transId"])
        else:
            return "false" 
    def VerifyTrans(self,transId):
        """Verify Trans"""
        postdata = {
            "api":self.apikey,
            "transId":transId
        }
        resp = requests.post("https://pay.ir/payment/verify",data=postdata)
        
        jdata = json.loads(resp.text)
        if(jdata["status"]==1):
            return "ok"
        else:
            return "faild"    


        
