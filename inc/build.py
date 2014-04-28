#!/bin/env python
# -*- coding: utf-8 -*-
import os,yaml,time,datetime,commands,collections
from collections import OrderedDict

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

#config
ISOTIMEFORMAT="%Y-%m-%d %X"
pwd = os.getcwd();
if os.name == "posix":
	#deploy-env
	root_dir = "/var/www/html/"
else:
	#dev-env
	root_dir = "../"
output_dir = root_dir
imageBase = "http://mo-img.b0.upaiyun.com/"
filename = "index.html"

curTime = time.localtime()
threshold = 86400*30*3

config = root_dir + "inc/photos.cfg.txt"

stream = open(config,"r")
# dict = OrderedDict()
dict = ordered_load(stream, yaml.SafeLoader, collections.OrderedDict);

#global content
navString = ''

def buildMenu(dict):
	# menu - diary
	global navString;
	navString = '<nav class="site-nav" tabindex="-1">\n'\
				'<ul class="nav-list">\n'
	for key in dict.keys():
		print key;
		navString += '\t<li class="nav-list-item">\n'\
					 '\t\t<a class="l1-a" href="#">'+dict.get(key).get("display")+'</a>\n'
		
		if key!="diary":
			navString += '\t\t\t<ul class="nav-list-2">\n'
			for l2dict in dict.get(key).get("list"):
				navString += '\t\t\t\t<li><a href="/'+key+'/'+l2dict.get("bucket")+'/">'+l2dict.get("display")+'</a></li>\n'\

			navString += '\t\t\t</ul>\n'
		navString +="\t</li>\n"	
			# navString += l2dict.bucket

	navString += "</ul></nav>\n"
	print navString;

def processIndexPage():
	
	#generate index page
	#affected pages : index
	
	print time2String(time.time())+"\tINFO\t"+"Processing index page"
	path = output_dir
	output_handle = open(path+ filename,'w')
	page_file_handle = open("index.tpl")
	# output_handle.write(add_header(key)+"\n")
	content = page_file_handle.read();
	content = content.replace('$NAV$',navString);
	output_handle.write(content);
	# output_handle.write(add_footer(key)+"\n")
	page_file_handle.close()
	output_handle.close()
	print time2String(time.time())+"\tINFO\t"+"Generated index.html file on "+ path

def processSinglePage(key,bucket,curList):
	
	#generate a single file with key
	#affected pages : about, portfolio
	
	print time2String(time.time())+"\tINFO\t"+"Processing single page ["+ key +"]"
	path = output_dir + "levinsu/" + key +"/"+bucket+"/"
	if not os.path.exists(path):
		os.makedirs(path)
	output_handle = open(path+ filename,'w')
	page_file_handle = open("single.tpl")
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


if __name__ == '__main__':
	buildMenu(dict)
	processIndexPage();
	for key in dict.keys():
		print key;
		for listItem in dict.get(key).get("list"):
			processSinglePage(key,listItem.get("bucket"),listItem)



