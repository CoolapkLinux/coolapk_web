# from https://github.com/ZCKun/CoolapkTokenCrack

import requests
import time
import hashlib
import base64


DEVICE_ID = "8513efac-09ea-3709-b214-95b366f1a185"

def get_app_token():
    t = int(time.time())
    hex_t = hex(t)

    # 把时间戳md5
    md5_t = hashlib.md5(str(t).encode('utf-8')).hexdigest()

    # 把固定的死token拼接上时间戳的md5跟deviceid
    a = 'token://com.coolapk.market/c67ef5943784d09750dcfbb31020f0ab?{}${}&com.coolapk.market' \
        .format(md5_t, DEVICE_ID)

    # 把拼接好的活token用base64解码一次再md5一次
    md5_a = hashlib.md5(base64.b64encode(a.encode('utf-8'))).hexdigest()
    # 活token的md5+deviceid+hex的时间戳就是最后的X-App-Token
    token = '{}{}{}'.format(md5_a, DEVICE_ID, hex_t)
    return token


def request(url: str) -> dict:
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; HLK-AL00 Build/HONORHLK-AL00) (#Build; HONOR; HLK-AL00; HLK-AL00 10.1.0.110(C00E105R6P2); 10) +CoolMarket/11.0-beta9-2101041",
        "X-App-Id": "com.coolapk.market",
        "X-Requested-With": "XMLHttpRequest",
        "X-Sdk-Int": "29",
        "X-Sdk-Locale": "zh-CN",
        "X-Api-Version": "11",
        "X-App-Version": "11.0-beta9",
        "X-App-Code": "2101041",
        "X-App-Device": "Q2NwIGOyEjMllTMl1SN3QWYtUTMjRTLkFTM50CNmZzYlVmM3sDMwwUQtsETIByOS9kTPhEI7kURXFUVIByOEFjOGZjOxYkO1MjO0kjODZEI7AyOgszN2cTNlBTNhF2MkdDZzUWY",
        "Host": "api.coolapk.com",
        "X-Dark-Mode": "0",
        "X-App-Token": get_app_token(),
    }
    __r = requests.get(url, headers=headers).json()
    return __r["data"]
