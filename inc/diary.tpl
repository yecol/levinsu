<!DOCTYPE html>
<html lang="zh-cn">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" user-scalable="no">
        <meta name="keywords" content="LEIXUJUN, OFFICIAL, MO, MOPIC, 雷徐君, 中国">
        <meta name="description" content="LEIXUJUN OFFICIAL" />

        <link rel="shortcut icon" href="/assets/img/favicon.ico" />
        <title>LEIXUJUN</title>
        <link type="text/css" rel="stylesheet" href="/assets/css/style.css">

        <!--[if lt IE 9]>
        <script src="assets/js/html5shiv.js"></script>
        <script src="assets/js/respond.min.js"></script>
        <![endif]-->

        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-2WZYM6F2BY"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-2WZYM6F2BY');
        </script>

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
<footer>
        <div class="beian desktop-only">
            <p>
                <a target="_blank" href="http://www.beian.gov.cn">浙ICP备13015016号</a>
                <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33118102000116">浙公网安备 33118102000116号</a>
            </p>
        </div>
</footer>
<!--JAVASCRIPT-->
<script type="text/javascript" src="/assets/js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.lazyload.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.easing.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.dimensions.js"></script>
<script type="text/javascript" src="/assets/js/jquery.accordion.2.0.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){


    if ($(window).width()<=1024) {
        $('img').each(function(){
            $(this).attr('src',$(this).attr('src').substring(0,$(this).attr('src').lastIndexOf("!"))+'?x-oss-process=image/resize,l_1024');
        });
    }
    else{
        $('img').each(function(){
            $(this).attr('src',$(this).attr('src').substring(0,$(this).attr('src').lastIndexOf("!"))+'?x-oss-process=image/resize,l_1500');
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

    if($(".foot-nav-mobile").offset().top+$(".foot-nav-mobile").height()<$(window).height()){
        $(".foot-nav-mobile").height($(window).height()-$(".foot-nav-mobile").offset().top);
    }
});
</script>
	</body>
</html>
<!-- ====================================END OF FOOTERFILE====================================
