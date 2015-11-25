#!/usr/bin/python3

import re
import sys
import time

if len(sys.argv) != 2:
    print('Usage: ./main.py file-name.df')
    sys.exit(1)

file_from_cli = sys.argv[1]

art_title = re.compile(r'\[title=(.*?)\]')
art_desc = re.compile(r'\[description=(.*?)\]')
art_cat = re.compile(r'\[category=(.*?)\]')
art_date = re.compile(r'\[date=(.*?)\]')
art_content = re.compile(r'\[content\]([\s\S]*?)\[\/content\]')
now = time.strftime("%d %B %y -- %X")

file_name = file_from_cli
if file_name.lower().endswith(".df"):
    access_log_file = open(file_name,"r").read()
else:
    print("Ups! File extension must be '.df'")
    sys.exit(1)

title_read = desc_read = cat_read = date_read = content_read = access_log_file
title_show = re.search(art_title, title_read)
desc_show = re.search(art_desc, desc_read)
cat_show = re.search(art_cat, cat_read)
date_show = re.search(art_date, date_read)
content_show = re.search(art_content, content_read)

title = title_show.group(1)
desc = desc_show.group(1)
cat = cat_show.group(1)
content = content_show.group(1)
date = date_show.group(1)

if not title:
    print("Title can't empty")
    sys.exit(1)

if not desc:
    print("Description can't empty")
    sys.exit(1)

if not cat:
    cat = "Uncategorized"

if date != "now":
    now = date

if not date:
    now = time.strftime("%d %B %y -- %X")

if not content.strip('\n'):
    print("Content can't be empty")
    sys.exit(1)

link_from_title = title_show.group(1).lower().replace(" ", "-")
file_to = '%s.html' % link_from_title

with open(file_to, 'a') as the_file:
    the_file.write("<html>\n\t")
    the_file.write("<head>\n\t\t")
    the_file.write("<meta charset='utf8' />\n\t\t")
    the_file.write("<title>%s</title>\n\t" % title)
    the_file.write("</head>\n\t")
    the_file.write("<body>\n\t\t")
    the_file.write("<h1>%s</h1>\n\t\t" % title)
    the_file.write("<span>%s</span>\n\t\t" % desc)
    the_file.write("<p>%s</p>\n\t\t" % cat)
    the_file.write("<abbr title='{0}'>{0}</abbr>\n\t\t".format(now))
    the_file.write("\n\t\t<blockquote>\n\t\t\t\t%s\n\t\t</blockquote>\n\t" % content)
    the_file.write("</body>\n")
    the_file.write("</html>\n")
    the_file.write("<!-- Created DF Template Parser: %s -->" % now)

print("The", file_to, "file is created...")
