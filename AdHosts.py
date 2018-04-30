#!/usr/bin/python3

# Original script by ildoc @ https://github.com/ildoc/HostBlock
# Copyright (c) 2018 games195 <games195dev@gmail.com>. Licensed under MIT License.

import urllib.request, datetime, os

File = 'host/hosts.txt'

List = []

# Thanks to all maintainers of ad-hosts lists.
Sources = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts',
    'https://gist.githubusercontent.com/games195/4dced15b925a4cc28e40285b0c05ac31/raw/hosts.txt',
    'https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt',
    'https://raw.githubusercontent.com/biroloter/Mobile-Ad-Hosts/master/hosts',
    'https://raw.githubusercontent.com/vokins/yhosts/master/hosts',
    'https://hosts-file.net/ad_servers.txt'
]

for Link in Sources:
    try:
        print('[+] Retrieving list from: {}'.format(Link))
        r = urllib.request.urlopen(Link)
        Host = r.readlines()
        Host = [x.decode('utf-8') for x in Host]
        Host = [x.strip() for x in Host]
        Host = [z for z in Host if z != '' and z[0] != '#']
        Host = [h.split()[1] for h in Host if h.split()[0] in ['0.0.0.0', '127.0.0.1']]
        Host = [x for x in Host if x not in ['localhost', 'localhost.localdomain', 'locals']]
        print('[+] {} blocked domains found.'.format(str(len(Host))))
        r.close()
        List += Host
    except:
        print('[-] ERROR: I can\'t retrieve the list from: {}'.format(Link))

print('[+] Removing duplicates and sorting...')
List = sorted(list(set(List)))
print('[+] Total domains count {}.'.format(str(len(List))))

if not os.path.exists(os.path.dirname(File)):
    os.makedirs(os.path.dirname(File))

with open(File, 'w') as f:
    print('[+] Writing to file...')
    f.write('''
# This file was generated thanks to various sources.
# Repo: https://github.com/games195/AdHosts
# Last updated: {}\n
'''.format(datetime.datetime.now().strftime('%a, %d %b %y %X')))
    f.write('\n'.join('127.0.0.1 ' + url for url in List))
    print('[+] Done!')
