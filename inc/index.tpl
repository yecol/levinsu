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
        <div class="site-logo">MO</div>

        $SLIDES$
        $NAV$
        

<!-- ====================================BEGIN OF FOOTERFILE==================================== -->
<footer></footer>
<!--JAVASCRIPT-->
<script type="text/javascript" src="/assets/js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.lazyload.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.easing.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.dimensions.js"></script>
<script type="text/javascript" src="/assets/js/jquery.accordion.2.0.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.slides.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){


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

    // $("img").lazyload({
    //   threshold : 400
    // });

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


    $('#slides').slidesjs({
        width: 1280,
        height: 960,
        navigation: {
          active:false
        },
        pagination: {
          active:false
        },
        play: {
          active:false,
          effect:"fade",
          interval:5000,
          auto:true
        },
        effect: {
            slide: {
            // Slide effect settings.
                speed: 1200
            // [number] Speed in milliseconds of the slide animation.
            },
            fade: {
                speed: 1200
            }
        }
      });
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