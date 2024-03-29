from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
import json, requests, jwt
import sqlite3, time

# Create your views here.
def client(request):
    return render(request, 'client.html', locals())


def authorize(request):
    try:
        # if request.method == "GET":
        r2 = requests.post(url='https://jaccount.sjtu.edu.cn/oauth2/token',
                            headers={'Content-Type':'application/x-www-form-urlencoded'},
                            params={
                                "grant_type": "authorization_code",
                                "code": request.GET['code'],
                                "redirect_uri": "http://39.100.121.105/oauth/authorize",
                                "client_id": "6igXEhGusBZsIuxHkmWN",
                                "client_secret": "988F890BA1B5CBAB58E5C7F298610B6D9498E05BCEBF7C67"
                            })
        r2.encoding = 'utf-8'
        datas = json.loads(r2.text)
        info = jwt.decode(datas["id_token"], verify=False)

        conn = sqlite3.connect('/home/faymek/oauth-client/oauthClient/test.db')
        c = conn.cursor()
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        c.execute("INSERT INTO Student VALUES (?,?,?,?,?,?)", (None, t, info["sub"], info["name"], info["type"], info["code"]))
        conn.commit()
        c.close()
        conn.close()

        return HttpResponseRedirect('http://youth.sjtu.edu.cn/a/verify.htm?id='+info['sub'])
    except Exception as e:
        print(e)
        return HttpResponse('error')
    # return redirect('/oauth/test')
        # return HttpResponseRedirect('http://192.168.10.18:8002/oauth/server?callback=192.168.10.18:8001/oauth/client')
    return HttpResponse('no url')

def test(request):
    return render(request, 'test.html', locals())

