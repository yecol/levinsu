#!/bin/env python
# -*- coding: utf-8 -*-
import os,yaml,time,datetime,commands,collections
from collections import OrderedDict

#config
ISOTIMEFORMAT="%Y-%m-%d %X"
ISODATEFORMAT="%Y-%m-%d"
pwd = os.getcwd();
if os.name == "posix":
	#deploy-env
	root_dir = "/var/www/mopic/"
else:
	#dev-env
	root_dir = "../"
output_dir = root_dir
imageBase = "http://mo-cdn.b0.upaiyun.com"
filename = "index.html"

curTime = time.localtime()
threshold = 86400*30*3
baseLiMargin = 0.00001

config = root_dir + "inc/photos.cfg.txt"

def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader, node: object_pairs_hook(loader.construct_pairs(node)))
    return yaml.load(stream, OrderedLoader)

def time2String( s ):
	#time format to string
    return time.strftime( ISOTIMEFORMAT, time.localtime( float(s)) )

def offsetTime( s1,s2 ):
	#string time format to float
    return abs(time.mktime(time.strptime(s1, ISODATEFORMAT)) - time.mktime(time.strptime(s2, ISODATEFORMAT)))

stream = open(config,"r")
# dict = OrderedDict()
dict = ordered_load(stream, yaml.SafeLoader, collections.OrderedDict);

#global content
navString = ''
diaryString = ''

def buildMenu(dict):
	# menu - diary
	global navString;
	global diaryString;
	navString = '<nav class="site-nav" tabindex="-1">\n'\
				'<ul class="nav-list">\n'

	diaryString = '<div class="diary-nav">\n'\
					'<div class="diary-arrow arrow-up"></div>\n'\
					'<div class="diary-content">\n'\
					'<ul>\n'

	for key in dict.keys():
		navString += '\t<li class="nav-list-item" name="'+key+'">\n'
		
		if key=="index":
			pass;

		elif key!="diary":
			navString += '\t\t<a class="l1-a" href="#">'+dict.get(key).get("display")+'</a>\n'
			navString += '\t\t\t<ul class="nav-list-2">\n'
			for l2dict in dict.get(key).get("list"):
				navString += '\t\t\t\t<li><a name="'+l2dict.get("bucket")+'" href="/'+key+'/'+l2dict.get("bucket")+'/">'+l2dict.get("display")+'</a></li>\n'

			navString += '\t\t\t</ul>\n'
		navString +="\t</li>\n"	
			# navString += l2dict.bucket
		if key=="diary":
			basetime = ''
			defaultPage = ''
			offset = 0
			for l2dict in dict.get(key).get("list"):
				if basetime!='':
					offset = min(100,round(offsetTime(str(basetime),str(l2dict.get("date")))*baseLiMargin))
					# print offset
				diaryString += '<li style="margin-top:'+str(offset)+'px"><a href="/'+key+'/'+l2dict.get("bucket")+'/">'+l2dict.get("display")+'</a></li>\n'
				basetime = l2dict.get("date")
				defaultPage = "/"+key+"/"+l2dict.get("bucket")


			diaryString += "</ul></div>\n"\
							'<div class="diary-arrow arrow-down"></div></div>'

			navString += '\t\t<a class="l1-a" href="'+defaultPage+'">'+dict.get(key).get("display")+'</a>\n'

	navString +='\t<li class="bio-item">\n'\
				'\t\t<a href="#">BIO</a></li>\n'\
				'\t<li class="contact-item">\n'\
				'\t\t<a href="#">CONTACT</a></li>\n'
	navString += "</ul></nav>\n"

	navString += '<ul class="foot-nav mobile-only">\n'\
				'\t<li class="bio-item">\n'\
				'\t\t<a href="#">BIO</a></li>\n'\
				'\t<li class="contact-item">\n'\
				'\t\t<a href="#">CONTACT</a></li>\n'\
				'</ul>\n'

def processIndexPage(dict):
	
	#generate index page
	#affected pages : index
	
	print time2String(time.time())+"\tINFO\t"+"Processing index page"
	path = output_dir
	output_handle = open(path+ filename,'w')
	page_file_handle = open(root_dir+"inc/index.tpl")
	content = page_file_handle.read();
	content = content.replace('$NAV$',navString);
	slides = '<div id="slides">\n'
	for item in dict.get("index").get("pics"):
		slides +='<img src="'+imageBase+'/index/'+item+'"/>\n'
	slides += "</div>"
	content = content.replace('$SLIDES$',slides);
	output_handle.write(content);
	page_file_handle.close()
	output_handle.close()
	print time2String(time.time())+"\tINFO\t"+"Generated index.html file on "+ path

def processSinglePage(key,bucket,curList):
	
	#generate a single file with key
	#affected pages : about, portfolio
	
	print time2String(time.time())+"\tINFO\t"+"Processing single page ["+ key +"]"
	path = output_dir + key +"/"+bucket+"/"
	if not os.path.exists(path):
		os.makedirs(path)
	output_handle = open(path+ filename,'w')
	page_file_handle = open(root_dir+"inc/single.tpl")
	# output_handle.write(add_header(key)+"\n")
	content = page_file_handle.read();
	content = content.replace("$NAV$",navString);
	imageString = "<section class='full-page'>\n"
	for item in curList.get("pics"):
		imageString+='<img src="'+imageBase+'/'+key+'/'+bucket+'/'+item+'" />\n'
	imageString +="</section>"
	content = content.replace("$PHOTOS$",imageString);
	content = content.replace("assets","../../assets")
	output_handle.write(content);
	# output_handle.write(add_footer(key)+"\n")
	page_file_handle.close()
	output_handle.close()
	print time2String(time.time())+"\tINFO\t"+"Generated index.html file on "+ path

def processDiaryPage(key,bucket,curList):
	
	#generate a single file with key
	#affected pages : about, portfolio
	
	print time2String(time.time())+"\tINFO\t"+"Processing diary page ["+ key +"]"
	path = output_dir + key +"/"+bucket+"/"
	if not os.path.exists(path):
		os.makedirs(path)
	output_handle = open(path+ filename,'w')
	page_file_handle = open(root_dir+"inc/diary.tpl")
	# output_handle.write(add_header(key)+"\n")
	content = "<!--This page is cached on "+time2String(time.time())+"-->"+"\n";
	content += page_file_handle.read();
	content = content.replace("$NAV$",navString);
	content = content.replace("$DIARY$",diaryString);
	imageString = "<section class='full-page'>\n"
	for item in curList.get("pics"):
		imageString+='<img src="'+imageBase+'/'+key+'/'+bucket+'/'+item+'" />\n'
	imageString +="</section>"
	content = content.replace("$PHOTOS$",imageString);
	content = content.replace("assets","../../assets")
	output_handle.write(content);
	# output_handle.write(add_footer(key)+"\n")
	page_file_handle.close()
	output_handle.close()
	print time2String(time.time())+"\tINFO\t"+"Generated index.html file on "+ path


if __name__ == '__main__':
	buildMenu(dict)
	processIndexPage(dict);
	for key in dict.keys():
		if key =="diary":
			for listItem in dict.get(key).get("list"):
				processDiaryPage(key,listItem.get("bucket"),listItem)
		elif key!="index":
			for listItem in dict.get(key).get("list"):
				processSinglePage(key,listItem.get("bucket"),listItem)
	print "build successful."




