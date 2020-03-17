import requests
import bs4
import lxml
if __name__ == "__main__":
    url="https://accounts.douban.com/j/mobile/login/basic"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://accounts.douban.com/passport/login_popup?login_source=anony",
        "Host": "accounts.douban.com",
    }
    data={
        "name":"18222796870",
        "password":"13933098707",
        "remeber":False,
        "ck":"",
        "ticket":""
    }
    req=requests.post(url,headers=headers,data=data)
    print(req.status_code)
    print(req.headers)
    print(req.cookies)
    #以下是测试是否登录成功的，打印后可以看到个人信息
    # url2="https://www.douban.com"
    # headers2={
    #     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    #     "Referer":"https://www.douban.com",
    #     "Host":"www.douban.com"
    # }
    
    # req2=requests.get(url2,headers=headers2,cookies=req.cookies)
    # print(req2.status_code)
    # print(req2.text)