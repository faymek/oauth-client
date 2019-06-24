from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
import json, requests, jwt

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
                                "redirect_uri": "http://127.0.0.1:8000/oauth/authorize",
                                "client_id": "6igXEhGusBZsIuxHkmWN",
                                "client_secret": "988F890BA1B5CBAB58E5C7F298610B6D9498E05BCEBF7C67"
                            })
        r2.encoding = 'utf-8'
        datas = json.loads(r2.text)
        info = jwt.decode(datas["id_token"], verify=False)
        print(info)
        return HttpResponseRedirect('http://youth.sjtu.edu.cn/a/verify.htm?id='+info['sub'])
    except Exception as e:
        return HttpResponse('error')
    # return redirect('/oauth/test')
        # return HttpResponseRedirect('http://192.168.10.18:8002/oauth/server?callback=192.168.10.18:8001/oauth/client')
    return HttpResponse('no url')

def test(request):
    return render(request, 'test.html', locals())