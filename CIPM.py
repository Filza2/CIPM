from requests import post
print("""
 ██████╗██╗██████╗ ███╗   ███╗
██╔════╝██║██╔══██╗████╗ ████║
██║     ██║██████╔╝██╔████╔██║
██║     ██║██╔═══╝ ██║╚██╔╝██║
╚██████╗██║██║     ██║ ╚═╝ ██║
 ╚═════╝╚═╝╚═╝     ╚═╝     ╚═╝
    By @TweakPY - @vv1ck""")
try:
    url_red=input('[+] Enter Your url: ')
    if url_red=='':exit('[!] Enter url please ..')
    if 'http://' in url_red:pass
    else:
        if 'https://' in url_red:pass
        else:exit('[!] Enter vaild url please ..')
    email=input("[+] Enter Your Email: ")#i suggest you to use this tool https://github.com/Filza2/Fake-Email 
    if email=='':exit('[!] Enter email please ..')
    elif '@' not in email:exit('[!] Enter vaild email please ..')
except KeyboardInterrupt:exit()
d=f"""
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="type"

fast_redirect
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="email"

{email}
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="webhook"


-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="fmt"


-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="memo"

{url_red}
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="clonedsite"


-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="sql_server_table_name"

TABLE1
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="sql_server_view_name"

VIEW1
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="sql_server_function_name"

FUNCTION1
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="sql_server_trigger_name"

TRIGGER1
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="redirect_url"

{url_red}
-----------------------------8386526011242191222501571313--"""
req=post("https://canarytokens.org/generate",headers={'Host': 'canarytokens.org','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Content-Type': 'multipart/form-data; boundary=---------------------------8386526011242191222501571313','Content-Length': '1451','Origin': 'https://canarytokens.org','Referer': 'https://canarytokens.org/generate','Te': 'trailers','Connection': 'close'},data=d).json()
try:
    token=req["Token"];em=req["Email"];url=f'https://canarytokens.com/TweakPY.vv1ck/{token}'
    try:
        res=post('https://hideuri.com/api/v1/shorten',headers={'Host': 'hideuri.com','Cookie': '_cfvdata=as874as89sa9as84s89f4asfa8f','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://hideuri.com/','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '47','Origin': 'https://hideuri.com','Te': 'trailers'},data=f'url={url}')
        if 'result_url' in res.json():shorted_url=res.json()['result_url']
        else:pass
    except:shorted_url='Null'
    print("-------------------------------")
    print(f'[+] Your Token: {token}')
    print(f'[+] Your url: {url}')
    print(f'[+] Shorted url: {shorted_url}')
    print(f'[+] Your Email: {em}')
except:exit('[!] Error ..')
