import requests
import os


def search(p, k):  # p是整数，k是搜索关键词
    ss = requests.get("https://api.pixivic.com/illustrations",params={'page': p, 'keyword': k})                  
    print(ss.status_code)
    if(ss.status_code == 200):
        data = ss.json()['data']
        folder = os.path.exists(".\\pic\\"+k)
        if not folder:
            os.makedirs(".\\pic\\"+k)
        for li in data:
            url = li['imageUrls'][0]['original']
            name = repr(li['title']+"-"+str(li['artistId'])+url[-4:])[1:-1]
            url = url.replace("_webm", " ").replace("i.pximg.net", "original.img.cheerfun.dev")                
            print(name+"  "+url)
            if url.find('original') != -1:
                r = requests.get(url, headers={"referer": "https://pixivic.com/popSearch"})                    
                print(r.status_code)
                with open(".\\pic\\"+k+"\\"+name, "wb") as fb:
                    fb.write(r.content)


'''
搜索keyword可以更改
page决定数量，一页30个
返回json
URL转换由第9行给出
原title有许多问题，要是有能忽略所有特殊字符的方法就好了_______问题解决了，python中可以使用原始字符串，在第一个引号前加r或使用repr()
请求图片时要有headers={'referer':'https://pixivic.com/popSearch'}
'''
if __name__ == "__main__":
    search(1, r"yuni")
