<!DOCTYPE html>
<html lang="zh-cn">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" user-scalable="no">
        <link rel="shortcut icon" href="/assets/img/favicon.ico" />
		<title>MO | LEIXUJUN OFFICIAL</title>
		<link type="text/css" rel="stylesheet" href="/assets/css/style.css">

        <!--[if lt IE 9]>
        <script src="assets/js/html5shiv.js"></script>
        <script src="assets/js/respond.min.js"></script>
        <![endif]-->

	</head>
	<body>
        <div class="site-logo $THEME$"><a href="/">MO</a></div>

        $PHOTOS$
        $NAV$
        $DIARY$
        
<!--     <section class="full-page">
        <img src="assets/img/pixel.gif" data-original="photos/1.jpg" />
        <img src="assets/img/pixel.gif" data-original="photos/2.jpg" />
        <img src="assets/img/pixel.gif" data-original="photos/3.jpg" />
        <img src="assets/img/pixel.gif" data-original="photos/4.jpg" />
        <img src="assets/img/pixel.gif" data-original="photos/5.jpg" />
    </section> -->
<!-- ====================================BEGIN OF FOOTERFILE==================================== -->
<footer></footer>
<!--JAVASCRIPT-->
<script type="text/javascript" src="/assets/js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.lazyload.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.easing.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.dimensions.js"></script>
<script type="text/javascript" src="/assets/js/jquery.accordion.2.0.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){

    //get suitable image src according to the resolution.
    if ($(window).width()<=750) {
        $('img').each(function(){
            $(this).attr('src',$(this).attr('src')+'!750');
        });
    }
    else if ($(window).width()<1285) {
        $('img').each(function(){
            $(this).attr('src',$(this).attr('src')+'!1280');
        });
    }
    else if($(window).width()<1445){
        $('img').each(function(){
            $(this).attr('src',$(this).attr('src')+'!1440');
        });
    }
    else if($(window).width()<1925){
        $('img').each(function(){
            $(this).attr('src',$(this).attr('src')+'!1920');
        });
    }
    else if($(window).width()<2565){
        $('img').each(function(){
            $(this).attr('src',$(this).attr('src')+'!2560');
        });
    }
    else if($(window).width()<3105){
        $('img').each(function(){
            $(this).attr('src',$(this).attr('src')+'!2880');
        });
    }else{
        $('img').each(function(){
            $(this).attr('src',$(this).attr('src')+'!4096');
        });
    }

    //get menu opened/
    var $urlString = $(location).attr('href');
    var arr = new Array();
    arr = $urlString.split('/');
    activeA = arr[arr.length-2];
    activeLi = arr[arr.length-3];

    $("a[name="+activeA+"]").addClass('fix');
    $("li[name="+activeLi+"]").addClass('active');


    //animation of the menu hide/show
    if($(window).width()>750){
        $('.site-nav').css('opacity', '0');
        $('.site-nav').hover(function(){
            $('.site-nav').animate({opacity: 1}, 400);;
        },function(){
            $('.site-nav').animate({opacity: 0}, 400);;
        })
    
        //animation of the diary hide/show
        // $('.diary-content li').hover(function(){
        //     $(this).children('a').animate({opacity: 1}, 500);
        // },function(){
        //     $(this).children('a').animate({opacity: 0}, 500);
        // })
    }


    //mane accordion
    $('.nav-list').accordion({
        handle: ".l1-a", // Default: "h3"
        panel: ".nav-list-2", // Default: ".panel"
        speed: 500, // Default: 200
        easing: "easeInOutQuad", // Default "swing"
        canOpenMultiple: false, // Default: false
        canToggle: false, // Default: false
        activeClassPanel: "open", // Default: "open"
        activeClassLi: "active", // Default: "active"
        lockedClass: "locked", // Default: "locked"
        loadingClass: "loading" // Default: "loading"
    });

    //animation of the diary nav
    var speed = 300;
    var timeID; 
    $(".diary-content ul").css("margin-top", parseInt($(".diary-content").css("height"))-parseInt($(".diary-content ul").css("height"))+"px");

    $("div.arrow-down").hover(function(){
        // $('.diary-content li').children('a').animate({opacity: 1}, 500);;
        timeID =  setInterval(function(){
            if (parseInt($(".diary-content ul").css('margin-top'))<parseInt($(".diary-content").css("height"))-parseInt($(".diary-content ul").css("height"))){
               $(".diary-content ul").stop(true); 
            }
            else{
                $(".diary-content ul").animate({
                    "margin-top": "-=20px"
                }, speed, "linear");
            }
        },0);
    },function(){
        // $('.diary-content li').children('a').animate({opacity: 0}, 500);
        $(".diary-content ul").stop(true);
        clearInterval(timeID);
    }
    );

    $("div.diary-nav").hover(function(){
        $('.diary-content li').children('a').animate({opacity: 1}, 500);;
    },function(){
        $('.diary-content li').children('a').animate({opacity: 0}, 500);
    });

    $("div.arrow-up").hover(function(){
        // $('.diary-content li').children('a').animate({opacity: 1}, 500);
        timeID =  setInterval(function(){
            if (parseInt($(".diary-content ul").css('margin-top'))>0){
               $(".diary-content ul").stop(true); 
            }
            else{
                $(".diary-content ul").animate({
                    "margin-top":"+=20px"
                }, speed, "linear");
            }
        },0);
    },function(){
        // $('.diary-content li').children('a').animate({opacity: 0}, 500);
        $(".diary-content ul").stop(true);
        clearInterval(timeID);
    }
    );
});
</script>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-51513242-1', 'mo-pic.com');
  ga('send', 'pageview');

</script>


	</body>
</html>
<!-- ====================================END OF FOOTERFILE====================================