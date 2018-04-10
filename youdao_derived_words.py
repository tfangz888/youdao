#!/usr/bin/python
# -*- coding: utf-8 -*-

# 抓取有道单词的同根词
# 去年每行的第一个空格frq15.txt
# cut -c2- frq15.txt |grep -v ' ' > tmp.txt
# 运行 youdao_derived_words.py tmp.txt
# 结果还需要去重

import urllib2, time
from lxml import etree

def find_derived_words(word):
    time.sleep(1) # 延时1秒，以免网站有流速限制
    line = ''
    try:
        response = urllib2.urlopen("http://youdao.com/w/eng/" + word)
        # print response.read()
        page = response.read()
        html = etree.HTML(page.decode('utf-8'))
        words = html.xpath(u'//div[@id="relWordTab"]//span/a')
        for word in words:
            line += word.text
            line += ' '
    finally:
        return line



import sys, string
inputfile = sys.argv[1]

inputfile = '/tmp/tmp.txt'
with open(inputfile, "rb") as file:
    alllines = file.readlines()
allwords = [string.strip(item) for item in alllines]

# write to file
file_found_derived = open('/tmp/tmp_found_derived.txt', "wb")
file_found = open('/tmp/tmp_found.txt', "wb") 
no_found = open('/tmp/tmp_no_found.txt', "wb") 
for word in allwords:
    line = find_derived_words(word)
    if (len(line) > 0):
        file_found_derived.write(string.strip(line) + '\n')
        file_found.write(word + '\n')
        print line
    else:
        no_found.write(word + '\n')
no_found.close()
file_found.close()
file_found_derived.close()


