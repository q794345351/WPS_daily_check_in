invite_userids = [639314372,543432394]

import json, os, time
import requests


sids = [
    "V02SEPVt7lx4JA1JnFbsejvxbz4VVJA00a56ec7a004910bd95",
    "V02SmfzVunbRzHQl-n--N-QGvCG6okQ00a7fbe37004912408e",
    "V02SmdkLCQ7q8GprgFOCV4F6GDhKVoA00a5382570034b345f2",
    "V02SKHPYCVzUdQQC2SIqMpy79q6prVs00a222a3200491249d9",
    "V02S5JoNBz4kiJyoOMCEUvx-9509bwA00ac08452004910c962",
    "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
    "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
    "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
    "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
    "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
    "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
    "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d"
]
mk = 0

def request_re(sid, invite_userid, rep = 30):
    invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
    r = requests.post(invite_url, headers={'sid': sid}, data={'invite_userid': invite_userid})
    js = json.loads(r.content)
    if js['msg'] == 'tryLater' and rep > 0:
        rep -= 1
        time.sleep(2)
        r = request_re(sid, invite_userid, rep)
    return r

for i in invite_userids:
    for j in sids:
        r = request_re(j, i)
        js = json.loads(r.content)
        if js['result'] == 'ok':
            mk += 1
            
print('成功邀请%d位好友'%(mk))   

SERVER_KEY = os.getenv('SERVER_KEY')
if SERVER_KEY:
    data = {
        'text':'WPS邀请好友任务：成功邀请到%d位好友'%(mk),
        'desp':'成功邀请%d位好友'%(mk)
    }
    requests.post('https://sc.ftqq.com/%s.send'%(SERVER_KEY.strip()), data = data)
