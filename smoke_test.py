"""Run against two already-running APIs. Standard library only."""
import json, os, urllib.request, urllib.error
CATALOG=os.getenv('CATALOG_URL','http://localhost:8001')
SESSION=os.getenv('SESSION_URL','http://localhost:8002')
records=[]
def request(method,url,body=None,expected=200):
    raw=None if body is None else json.dumps(body).encode()
    req=urllib.request.Request(url,data=raw,method=method,headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(req,timeout=10) as r: code,data=r.status,json.load(r)
    except urllib.error.HTTPError as e: code,data=e.code,json.load(e)
    records.append({'method':method,'url':url,'request':body,'status':code,'response':data})
    assert code==expected,(url,code,data)
    return data

game=request('POST',CATALOG+'/games',{'title':'Twin Trails','platform':'PC','display_mode':'split_screen','min_players':2,'max_players':2},201)
request('GET',CATALOG+'/games?display_mode=split_screen&players=2')
s=request('POST',SESSION+'/sessions',{'game_id':game['id'],'host_id':'alice','controller_count':2},201)
p=SESSION+'/sessions/'+s['id']
request('POST',p+'/start',{'player_id':'alice'},409)
request('POST',p+'/players',{'player_id':'bob'})
request('POST',p+'/players',{'player_id':'eve'},409)
for player in ['alice','bob']: request('PUT',p+'/players/'+player+'/ready',{'ready':True})
request('POST',p+'/start',{'player_id':'alice'})
request('POST',p+'/finish',{'player_id':'alice'})
assert request('GET',p)['status']=='COMPLETED'
print(json.dumps({'environment':'URLs identify the APIs tested; deployment type must be recorded separately','checks':len(records),'calls':records},indent=2))
