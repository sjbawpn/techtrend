import urllib.request
import urllib.parse
import time
import os
from datetime import date, timedelta
home = 'S:\\Media\\SkyDrive\\Documents\\TechTrends\\logs'

procuts = {}
'''
#Nokia
nokia_world = {'page':'Nokia'},
nokia_us = {'page':'NokiaUS'}
nokia_india = {'page':'NokiaIndia'}
nokia_hk = {'page':'NokiaHongKong'}
nokia_ge = {'page':'nokiadeutschland'}
nokia_uk = {'page':'nokia.uk'}
nokia_fr = {'page':'nokiafrance'}

#Samsung
samsung_world = {'page':'SamsungMobile'}

#blackberry
bbry_world = {'page':'BlackBerry'}

#htc
htc_world = {'page':'HTC'}

#apple
apple_world = {'page':'137947732957611'}

#microsoft
ms_world = {'page':'Microsoft'}

#google
google_world = {'page':'Google'}

world = {}
world['nokia'] = nokia_world
world['samsung'] = samsung_world
world['samsung'] = samsung_world
world['google'] = google_world
'''

pages = ['Nokia','SamsungMobile','BlackBerry','HTC','137947732957611','Microsoft','Google']
na = ['NokiaUS','SamsungMobileUSA','HTCUSA']
asia = ['NokiaIndia','NokiaHongKong','SamsungMobileIndia','SamsungMobileHK','HTCIndia',]
europe = ['nokiadeutschland','Nokia.uk','NokiaFrance','SamsungMobileDeutschland','SamsungMobileUK','SamsungMobileFrance','HTCUK','HTCFR']
flagships = ['OfficialNokiaLumia920','253235488046600','BlackBerryZ10','336713623104264','109336685751749']

url = 'https://graph.facebook.com/'
fields= '?fields=likes'
#yesterday = str(date.today() - timedelta(1))
today = str(date.today())
general_file = open(os.path.join(home,'trend.log'),'a')
daily_file = open(os.path.join(home,today+'.log'),'w')
#print('['+yesterday+']')

print('['+today+']')
general_file.write('['+today+']\n')

print('[Global]')
general_file.write('[Global]\n')
daily_file.write('[Global]\n')
for page in pages:
    request = url+page+fields
    f = urllib.request.urlopen(request)
    response = f.read().decode('utf-8')
    data = eval(response)
    print(page+'='+str(data['likes']))
    general_file.write('\t'+page+'='+str(data['likes'])+'\n')
    daily_file.write('\t'+page+'='+str(data['likes'])+'\n')
    
    
print('[North America]')
general_file.write('[North America]\n')
daily_file.write('[North America]\n')
for page in na:
    request = url+page+fields
    f = urllib.request.urlopen(request)
    response = f.read().decode('utf-8')
    data = eval(response)
    print(page+'='+str(data['likes']))
    general_file.write('\t'+page+'='+str(data['likes'])+'\n')
    daily_file.write('\t'+page+'='+str(data['likes'])+'\n')

print('[Asia]')
general_file.write('[Asia]\n')
daily_file.write('[Asia]\n')
for page in asia:
    request = url+page+fields
    f = urllib.request.urlopen(request)
    response = f.read().decode('utf-8')
    data = eval(response)
    print(page+'='+str(data['likes']))
    general_file.write('\t'+page+'='+str(data['likes'])+'\n')
    daily_file.write('\t'+page+'='+str(data['likes'])+'\n')

print('[Europe]')
general_file.write('[Europe]\n')
daily_file.write('[Europe]\n')
for page in europe:
    request = url+page+fields
    f = urllib.request.urlopen(request)
    response = f.read().decode('utf-8')
    data = eval(response)
    print(page+'='+str(data['likes']))
    general_file.write('\t'+page+'='+str(data['likes'])+'\n')
    daily_file.write('\t'+page+'='+str(data['likes'])+'\n')

print('[Flagship]')
general_file.write('[Flagship]\n')
daily_file.write('[Flagship]\n')
for page in flagships:
    request = url+page+fields
    f = urllib.request.urlopen(request)
    response = f.read().decode('utf-8')
    data = eval(response)
    print(page+'='+str(data['likes']))
    general_file.write('\t'+page+'='+str(data['likes'])+'\n')
    daily_file.write('\t'+page+'='+str(data['likes'])+'\n')

general_file.write('\n')
general_file.close()
daily_file.close()
