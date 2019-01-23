import json

class MessageInfo:

    def __init__(self,error,reason,data):
        self.error = error              #0成功，非O失败。
        self.reason = reason
        self.data = data
    @staticmethod
    def success(msg='OK',data=''):
        msgInfo = MessageInfo(0,msg,data)
        return msgInfo

    @staticmethod
    def fail(errorCode=-1,data='FAIL'):
        msgInfo = MessageInfo(errorCode,data,"")
        return msgInfo


if __name__ == '__main__':
    print(json.dumps(MessageInfo.success().__dict__))