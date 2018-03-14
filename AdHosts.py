#!/usr/bin/python3

# Original script by ildoc @ https://github.com/ildoc/HostBlock
# Copyright (C) 2018 games195. Licensed under MIT License.

import urllib.request, datetime, os

File = 'host/hosts.txt'

List = []

# Thanks to all maintainers of ad-hosts lists.
Sources = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts',
    'https://raw.githubusercontent.com/biroloter/Mobile-Ad-Hosts/master/hosts',
    'https://raw.githubusercontent.com/vokins/yhosts/master/hosts',
    'https://hosts-file.net/ad_servers.txt'
]

for Link in Sources:
    try:
        print('[+] Retrieving list from: %s' % Link)
        r = urllib.request.urlopen(Link)
        Host = r.readlines()
        Host = [x.decode('utf-8') for x in Host]
        Host = [x.strip() for x in Host]
        Host = [z for z in Host if z != '' and z[0] != '#']
        Host = [h.split()[1] for h in Host if h.split()[0] in ['0.0.0.0', '127.0.0.1']]
        Host = [x for x in Host if x not in ['localhost', 'localhost.localdomain', 'locals']]
        print('[+] %s blocked domains found.' % str(len(Host)))
        r.close()
        List += Host
    except:
        print('[-] ERROR: I can\'t retrieve the list from: %s' % Link)

print('[+] Removing duplicates and sorting...')
List = sorted(list(set(List)))
print('[+] Total domains count %s.' % str(len(List)))

if not os.path.exists(os.path.dirname(File)):
    os.makedirs(os.path.dirname(File))

with open(File, 'w') as f:
    print('[+] Writing to file...')
    f.write('''
# This file was generated thanks to various sources.
# Repo: https://github.com/games195/AdHosts
# Last updated: %s\n
''' % datetime.datetime.now().strftime('%a, %d %b %y %X'))
    f.write('\n'.join('127.0.0.1 ' + url for url in List))
    print('[+] Done!')
