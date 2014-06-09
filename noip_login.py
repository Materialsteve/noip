#!/usr/bin/python

import sys, mechanize, cookielib, re, os

# Variables

login_site = 'https://www.no-ip.com/login/'
host_ids   = [<ID1>,<ID2>,<ID3>]
update_site = 'https://www.no-ip.com/members/dns/host.php?host_id='
logout_url = 'https://www.no-ip.com/login/?logout=1'
username   = ''
password   = ''

# Initialize browser and cookie handling

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Open the login page and apply credentials

print "Connecting to",login_site
br.open(login_site)
br.select_form(nr=0)
br.form['username'] = username
br.form['password'] = password
print "Logging in..."
br.submit()
print 'Currently on page:', br.title()

for host_id in host_ids:
     print 'Updating host ID:', host_id
     br.open(update_site+str(host_id))
     br.select_form(nr=0)
     br.submit()

# Logout
print 'Done, logging out.'
br.open(logout_url)
