<!DOCTYPE html>
<html lang="zh-cn">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" user-scalable="no">
		<title>Levinsu.com</title>
		<link type="text/css" rel="stylesheet" href="assets/css/style.css">

        <!--[if lt IE 9]>
        <script src="assets/js/html5shiv.js"></script>
        <script src="assets/js/respond.min.js"></script>
        <![endif]-->

	</head>
	<body>
        <div class="site-logo">MO</div>

        $NAV$

        $PHOTOS$
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
<script type="text/javascript" src="assets/js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="assets/js/jquery.lazyload.min.js"></script>
<script type="text/javascript" src="assets/js/jquery.easing.min.js"></script>
<script type="text/javascript" src="assets/js/jquery.dimensions.js"></script>
<script type="text/javascript" src="assets/js/jquery.accordion.2.0.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){
    $("img").lazyload({
      threshold : 400
    });

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
});
</script>


	</body>
</html>
<!-- ====================================END OF FOOTERFILE====================================