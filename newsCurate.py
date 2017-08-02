#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:14:20 2017

@author: Tacosushi
"""
#This is a python program that creates a new text file calle "News" or updates it (writes over anything previously in the text file)
#with the title and summary of articles from the NYTimes

#Import urllib2 to access source code of given websites
import urllib2

#Because we will be accessing the source code of NYTimes as a string file, we want a method to find ALL instances 
#where a "key word" is found. Function "find_all()" does this. 
#This function was taken from some article online, and I could not re find it.
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

#Create a new text file called "news.txt" and write the header
#Header is
#"Today's News:" followed by one blank lines of text signified by "\n" which means to start a new line
f= open("news.txt","w+")
f.write("Today's News:")
f.write("\n")
f.write("\n")

#First sourcing
#Access the source code from NYTimes main page and save the generated string in variable named "page"
page = urllib2.urlopen("https://www.nytimes.com/").read()

#Find the title of the first article of interest
#Do this by trimming the entire source code into a manageable bite sized text: first_block_nytimes_1
#In my case I new the general area I was interested in started from 25 characters after "story-heading" appeared. 
first_block_nytimes_1 = page[page.find('"story-heading"')+25:page.find('"story-heading"')+10000]

#The title of the article I was interested in (the first article mentioned on the front page of NYTimes) was found between > and < 
#from the block of text: first_block_nytimes_1
begin1 = first_block_nytimes_1.find('>')
end1 = first_block_nytimes_1.find('<')

#Create a new variable nytimes_title and retrieve the title of the article then upload this into the text file news.txt
#It automatically refers to the text file news.txt because I did not close the file
nytimes_title = first_block_nytimes_1[begin1+1:end1]
f.write(nytimes_title)
f.write(":")
f.write("\n")

#Find the summary section of the article title found above and trim everything else
begin2 = first_block_nytimes_1.find('<p class="summary"')
next_para = first_block_nytimes_1[begin2:]
end2 = next_para.find('</p>')
next_para2 = next_para[:end2+4]

#Because NYtimes made the summary into a list of bullet points, we find all of the bulletpoints using the function find_all() made above. 
start_list = list(find_all(next_para2,'<li>'))
end_list = list(find_all(next_para2,'</li>'))

#Now that we know where all of the bullet points start and end, we then create a variable to store the "summary text" and upload that into
#the news.txt file we created. \n is the equivalent of starting a new line. 
summary_nytimes = [0] * len(start_list)
for x in range(0,len(start_list)):
    summary_point = next_para2[start_list[x]+4:end_list[x]-1]
    summary_point.replace('\xe2\xe80\x99s', "'")
    f.write(summary_point)
    f.write("\n")
    summary_nytimes[x] = summary_point

f.write("\n")



#Second article finding here
#Do the same as above but with a different url: Taken from the technology section of NYTimes
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



#Third article finding here
#Do the same as above but with a different url: Taken from the world section of NYtimes
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



#Fourth article finding here
#Do the same as above but with a different url: Taken from the US section of NYTimes
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

#This news.txt file now has 4 article titles and summaries and is closed at the end of the program 
f.close
