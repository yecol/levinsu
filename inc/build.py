#!/bin/env python
# -*- coding: utf-8 -*-
import os,sys,yaml,time,datetime,commands,collections
from collections import OrderedDict
reload(sys)  
sys.setdefaultencoding('utf8')  

#config
ISOTIMEFORMAT="%Y-%m-%d %X"
ISODATEFORMAT="%Y-%m-%d"
pwd = os.getcwd();
RELEASE = False;
if os.name == "posix" and RELEASE:
	#deploy-env
	root_dir = "/var/www/mopic/"
else:
	#dev-env
	root_dir = "../"
output_dir = root_dir
imageBase = "https://mo-pic.oss-cn-hangzhou.aliyuncs.com/"
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
blackPages = {};


def getBlackPages(dict):
	# pass;
	global blackPages;
	for key in dict.keys():
		if key == "index":
			pass;
		else: 
			for l2key in dict.get(key).get("list"):
				if(str(l2key.get("black"))=="1"):
					blackPages[key+"/"+str(l2key.get("bucket"))]=1


def buildMenu(dict):
	# menu - diary
	global navString;
	global diaryString;
	navString = '<nav class="site-nav $THEME$" tabindex="-1">\n'\
				'<ul class="nav-list">\n'

	# diaryString = '<div class="diary-nav $THEME$ desktop-only">\n'\
					# '<div class="diary-arrow arrow-up"></div>\n'\
					# '<div class="diary-content">\n'\
					# '<ul>\n'

	for key in dict.keys():

		if key=="index":
			navString += '\t<li class="nav-list-item" name="index"><a class="l1-a" href="#"></a></li>\n'
		else:		
			navString += '\t<li class="nav-list-item" name="'+key+'">\n'
			navString += '\t\t<a class="l1-a" href="#">'+dict.get(key).get("display")+'</a>\n'
			
			navString += '\t\t\t<ul class="nav-list-2">\n'
			
			for l2dict in dict.get(key).get("list"):
				if not l2dict.get("type") is None:
					navString += '\t\t\t\t<li><a href="/pdf/'+str(l2dict.get("link"))+'">'+str(l2dict.get("display"))+'</a></li>\n'
				else:
					navString += '\t\t\t\t<li><a name="'+str(l2dict.get("bucket"))+'" href="/'+key+'/'+str(l2dict.get("bucket"))+'/">'+str(l2dict.get("display"))+'</a></li>\n'

			navString += '\t\t\t</ul>\n'
		navString +="\t</li>\n"	

	navString +='\t<li class="bio-item">\n'\
				'\t\t<a href="#">BIO</a></li>\n'\
				'\t<li class="contact-item">\n'\
				'\t\t<a href="#">CONTACT</a></li>\n'
	navString += "</ul></nav>\n"

	navString += """
				<ul class="foot-nav-mobile mobile-only">
					<li class="bio-item-mobile">
						<a href="#">BIO</a></li>
					<li class="contact-item-mobile">
						<a href="#" class="contact-mobile-expand">CONTACT</a>
							<div class="mobile-only contact-mobile-detail">
                                <p>TEL&nbsp;&nbsp;&nbsp;+86 18521092134</p>
       							<p>EMAIL&nbsp;&nbsp;&nbsp;INFO@MO-PIC.COM</p>
    						</div>
					</li>	
				</ul>


				<div class="contact-div animated fadeInDown desktop-only">	
    				<a class="close-contact-div" href="#">X</a>
    				<div class="wording">
        				<p>EMAIL&nbsp;&nbsp;INFO@MO-PIC.COM</p>
        				<p>TEL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+86 185 2109 2134</p>
        				<p>SITE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WWW.MO-PIC.COM</p>
        				<p class="wbwx"><a class="wb-link" href="http://weibo.com/atget" target="blank">WB</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a class="wx-link" href="#">WX</a></p>
    				</div>
				</div>
				<div class="wx-code d2-code desktop-only">
				</div>
				"""

def processIndexPage(dict):
	
	#generate index page
	#affected pages : index
	
	print time2String(time.time())+"\tINFO\t"+"Processing index page"
	path = output_dir
	output_handle = open(path+ filename,'w')
	page_file_handle = open(root_dir+"inc/index.tpl")
	content = "<!--This page is cached on "+time2String(time.time())+"-->"+"\n";
	content += page_file_handle.read();
	content = content.replace('$NAV$',navString);
	slides = '<div id="slides">\n'
	for item in dict.get("index").get("pics"):
		slides +='<img src="'+imageBase+'/index/'+item+'!2048"/>\n'
	slides += "</div>"
	content = content.replace('$SLIDES$',slides);
	output_handle.write(content);
	page_file_handle.close()
	output_handle.close()
	print time2String(time.time())+"\tINFO\t"+"Generated index.html file on "+ path

def processSinglePage(key,bucket,curList):
	
	if bucket is None:
		return;
	#generate a single file with key
	#affected pages : about, portfolio
	
	print time2String(time.time())+"\tINFO\t"+"Processing single page ["+ key +"]"
	path = output_dir + key +"/"+str(bucket)+"/"
	if not os.path.exists(path):
		os.makedirs(path)
	output_handle = open(path+ filename,'w')
	page_file_handle = open(root_dir+"inc/single.tpl")
	content = "<!--This page is cached on "+time2String(time.time())+"-->"+"\n";
	content += page_file_handle.read();
	content = content.replace("$NAV$",navString);
	imageString = "<section class='full-page'>\n"
	for item in curList.get("pics"):
		imageString+='<img src="'+imageBase+'/'+key+'/'+str(bucket)+'/'+item+'!2048" />\n'
	
	if(curList.has_key("words")):
		wordingString = "<div class='wording'>"
		for para in curList.get("words"):
			wordingString+="<p>"+para+"</p>";
		wordingString +="</div>";
		imageString+=wordingString;

	imageString +="</section>"

	content = content.replace("$PHOTOS$",imageString);
	if(blackPages.has_key(key+"/"+str(bucket))):
		# this page is set to be blackfont
		content = content.replace("$THEME$","btheme");
	else:
		content = content.replace("$THEME$","");
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
	# content = content.replace("$DIARY$",diaryString);
	imageString = "<section class='full-page'>\n"
	for item in curList.get("pics"):
		imageString+='<img src="'+imageBase+'/'+key+'/'+bucket+'/'+item+'" />\n'
	imageString +="</section>"
	content = content.replace("$PHOTOS$",imageString);
	if(blackPages.has_key(key+"/"+bucket)):
		# this page is set to be blackfont
		content = content.replace("$THEME$","btheme");
	else:
		content = content.replace("$THEME$","");
	output_handle.write(content);
	# output_handle.write(add_footer(key)+"\n")
	page_file_handle.close()
	output_handle.close()
	print time2String(time.time())+"\tINFO\t"+"Generated index.html file on "+ path


if __name__ == '__main__':

	getBlackPages(dict);
	buildMenu(dict);
	print str(blackPages);
	processIndexPage(dict);
	for key in dict.keys():
		# if key =="diary":
			# for listItem in dict.get(key).get("list"):
				# processDiaryPage(key,listItem.get("bucket"),listItem)
		if key!="index":
			for listItem in dict.get(key).get("list"):
				processSinglePage(key,listItem.get("bucket"),listItem)
	print "build successful."




