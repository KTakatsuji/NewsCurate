#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:14:20 2017

@author: Tacosushi
"""

import urllib2
import smtplib

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    
    message = message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()


page = urllib2.urlopen("https://www.nytimes.com/").read()

f= open("news.txt","w+")
f.write("Today's News:")
f.write("\n")
f.write("\n")

first_block_nytimes_1 = page[page.find('"story-heading"')+25:page.find('"story-heading"')+10000]
begin1 = first_block_nytimes_1.find('>')
end1 = first_block_nytimes_1.find('<')

nytimes_title = first_block_nytimes_1[begin1+1:end1]
f.write(nytimes_title)
f.write(":")
f.write("\n")

begin2 = first_block_nytimes_1.find('<p class="summary"')
next_para = first_block_nytimes_1[begin2:]
end2 = next_para.find('</p>')
next_para2 = next_para[:end2+4]

start_list = list(find_all(next_para2,'<li>'))
end_list = list(find_all(next_para2,'</li>'))

summary_nytimes = [0] * len(start_list)
for x in range(0,len(start_list)):
    summary_point = next_para2[start_list[x]+4:end_list[x]-1]
    summary_point.replace('\xe2\xe80\x99s', "'")
    f.write(summary_point)
    f.write("\n")
    summary_nytimes[x] = summary_point

f.write("\n")
#print(nytimes_title)
#print(summary_nytimes)
#print(" ")


#Second article finding here
page2 = urllib2.urlopen("https://www.nytimes.com/section/technology?WT.nav=page&action=click&contentCollection=Tech&module=HPMiniNav&pgtype=Homepage&region=TopBar").read()
first_block_nytimes_2 = page2[page2.find('<h2 class="headline">')+1:page2.find('<h2 class="headline">')+1500]
end1 = first_block_nytimes_2.find('<')
first_block_nytimes_2 = first_block_nytimes_2[end1+1:]

begin1 = first_block_nytimes_2.find('>')
end1 = first_block_nytimes_2.find('<')
nytimes_title2 = first_block_nytimes_2[begin1+1:end1]

f.write(nytimes_title2)
f.write(":")
f.write("\n")


begin2 = first_block_nytimes_2.find('<p class="summary"')
next_para = first_block_nytimes_2[begin2+19:]
end2 = next_para.find('</p>')
tech_summary_nytimes = next_para[:end2]

f.write(tech_summary_nytimes)
f.write("\n")
f.write("\n")

#print(nytimes_title2)
#print(tech_summary_nytimes)
#print(" ")

#Third article finding here
page3 = urllib2.urlopen("https://www.nytimes.com/section/world?WT.nav=page&action=click&contentCollection=World&module=HPMiniNav&pgtype=Homepage&region=TopBar").read()
first_block_nytimes_3 = page3[page3.find('<h2 class="headline">')+1:page3.find('<h2 class="headline">')+1500]
end1 = first_block_nytimes_3.find('<')
first_block_nytimes_3 = first_block_nytimes_3[end1+1:]

begin1 = first_block_nytimes_3.find('>')
end1 = first_block_nytimes_3.find('<')
nytimes_title3 = first_block_nytimes_3[begin1+1:end1]

f.write(nytimes_title3)
f.write(":")
f.write("\n")


begin2 = first_block_nytimes_3.find('<p class="summary"')
next_para = first_block_nytimes_3[begin2+19:]
end2 = next_para.find('</p>')
world_summary_nytimes = next_para[:end2]

f.write(world_summary_nytimes)
f.write("\n")
f.write("\n")



#print(nytimes_title3)
#print(world_summary_nytimes)
#print(" ")

#Fourth article finding here
page4 = urllib2.urlopen("https://www.nytimes.com/section/us?WT.nav=page&action=click&contentCollection=U.S.&module=HPMiniNav&pgtype=Homepage&region=TopBar").read()
first_block_nytimes_4 = page4[page4.find('<h2 class="headline">')+1:page4.find('<h2 class="headline">')+1500]
end1 = first_block_nytimes_4.find('<')
first_block_nytimes_4 = first_block_nytimes_4[end1+1:]

begin1 = first_block_nytimes_4.find('>')
end1 = first_block_nytimes_4.find('<')
nytimes_title4 = first_block_nytimes_4[begin1+1:end1]

begin2 = first_block_nytimes_4.find('<p class="summary"')
next_para = first_block_nytimes_4[begin2+19:]
end2 = next_para.find('</p>')
us_summary_nytimes = next_para[:end2]

f.write(nytimes_title4)
f.write(":")
f.write("\n")
f.write(us_summary_nytimes)

#print(nytimes_title4)
#print(us_summary_nytimes)


#write onto a new file

f.close


