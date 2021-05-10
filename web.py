import requests

def test1():
    url = "https://httpbin.org/anything"
    params = {"msg": "welcomeuser", "isadmin": 1}
    headers_mobile = { 'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'}

    #Post request with params
    res = requests.post(url, data=params)
    print(res.json())

    #Post request as mobile user
    res = requests.post(url, data=params, headers=headers_mobile)
    print(res.json())

def main():
    test1()

if __name__ == "__main__":
    main()