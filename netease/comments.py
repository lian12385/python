

# params=rsB0fuMAdnO%2B81cq5E70XsX6J7BwgvwLZBYVF9izDzmfWm18YHLkEexuJniY3uDdAQMZnuKKQorGU9oRfiZtGvrKCWXUs5yc0PwsOqgZTJ0Qw%2FrB%2BQwMhWDb7ETBN2rzJngf2Ox%2BN%2BHYKFYsFD88QrfR3GGqV8lEAS5zvrW1z3qetE50BMrgte7cXuIcOv92dHDwaFv0VRDPGr%2FugJVBHN8OMZqlgDkjeprD%2FfsmU3WsF1XWxfODjAqWzrU2qbYhMXxjVDBW9JlyvhOHuoo%2BX%2BAgA5oZOTLnlYMxdCLk5UA%3D&encSecKey=c5b16a045aad991304e2d19157aae19a5aec4ddefa935761cdd07eb176e91044b85beeabd630c3895d3a3508cbd0bf2526a1e1859d84f9fb7c3b6d925c28263baed0810f2f01565fa9b82f5bd86c802e22c17890fe2454e4cde6da4dbb180a430247fa2baec8ad31be26dd30098a4b980141399fc9e774b1570683556fa00f22
from Crypto.Cipher import AES
from base64 import b64encode
import json
import requests
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
# 处理加密过程
'''    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }'''

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "d5bpgMn9byrHNtAh"  # 手动固定的. -> 人家函数中是随机的


def get_encSecKey():
    return "1b5c4ad466aabcfb713940efed0c99a1030bce2456462c73d8383c60e751b069c24f82e60386186d4413e9d7f7a9c7cf89fb06e40e52f28b84b8786b476738a12b81ac60a3ff70e00b085c886a6600c012b61dbf418af84eb0be5b735988addafbd7221903c44d027b2696f1cd50c49917e515398bcc6080233c71142d226ebb"


def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))
    return str(b64encode(bs),"utf-8")



resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})
print(resp.text)