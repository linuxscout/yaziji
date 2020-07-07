<!DOCTYPE html>
<html lang="ar">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <!--[if lt IE 9]>
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>  <![endif]-->
    <title>مولد الجمل العربية</title>
    <link href="/_files/favicon1.png" rel="icon" type="image/png">
    <link href="/_files/adawatstyle.css" rel="stylesheet">
    <!-- <link href="/_files/xzero-rtl/css/bootstrap-arabic.reduced.css" rel="stylesheet">  -->
    <link href="/_files/xzero-rtl/css/bootstrap-arabic.min.css" rel="stylesheet">
    <!--
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">-->
    <!--
    <link href="/_files/bootstrap-rtl.min.css" rel="stylesheet">-->
    <meta content="width=device-width, initial-scale=1" name="viewport">
  </head>
  <body dir="rtl">
                   <p> <a href="/mishkal/main"><img alt="مشكال: تشكيل النصوص العربية" height="120px" src="/_files/logo.png" style='float:right; margin-top:-20px;'> </a></p>
    <!--<h2>يازجي</h2>
    <h3>مولد الجمل العربية</h3>-->

    <div class="container">
      <div class="row clearfix">
        <div class="col-md-9 column">
          <form id="NewForm" name="NewForm" onsubmit="return false"><br>
فاعل: <select id='subject'  class='form-inline' name='subject'>
	<option>أنا</option>
	<option>نحن</option>
	<option>أنت</option>
	<option>أنتِ</option>
	<option>أنتما</option>
	<option>أنتما مؤ</option>
	<option>أنتم</option>
	<option>أنتن</option>
	<option>هو</option>
	<option>هي</option>
	<option>هما</option>
	<option>هما مؤ</option>
	<option>هم</option>
	<option>هن</option>
</select>
فعل مساعد: <select id='auxiliary'  class='form-inline' name='auxiliary'>
	<option>َاِسْتَطَاع</option>
	<option>أَرَادَ</option>
	<option>كَادَ</option>
</select>
مفعول: <select id='object'  class='form-inline' name='object'>
	<option>أنا</option>
	<option>نحن</option>
	<option>أنت</option>
	<option>أنتِ</option>
	<option>أنتما</option>
	<option>أنتما مؤ</option>
	<option>أنتم</option>
	<option>أنتن</option>
	<option>هو</option>
	<option>هي</option>
	<option>هما</option>
	<option>هما مؤ</option>
	<option>هم</option>
	<option>هن</option>
	<option>حليب</option>
</select>
ظرف زمان: <select id='time'  class='form-inline' name='time'>
	<option>أحيانا</option>
	<option>أول أمس</option>
	<option>أمس</option>
	<option>غدا</option>
	<option>دائما</option>
	<option>بعد غد</option>
	<option>كل يوم</option>
	<option>مساء</option>
	<option>البارحة</option>
	<option>اليوم</option>
	<option>صباحا</option>
</select>
فعل: <select id='verb'  class='form-inline' name='verb'>
	<option>شَرِبَ</option>
	<option>ضَرِبَ</option>
	<option>ذَهَبَ</option>
	<option>قَالَ</option>
</select>
مثبت/منفي: <select id='negative'  class='form-inline' name='negative'>
	<option>مثبت</option>
	<option>منفي</option>
</select>
مبني للمعلوم/مجهول: <select id='voice'  class='form-inline' name='voice'>
	<option>معلوم</option>
	<option>مبني للمجهول</option>
</select>
زمن: <select id='tense'  class='form-inline' name='tense'>
	<option>الماضي المعلوم</option>
	<option>المضارع المعلوم</option>
	<option>المضارع المؤكد الثقيل</option>
	<option>الأمر</option>
	<option>الأمر المؤكد</option>
</select>
ظرف مكان: <select id='place'  class='form-inline' name='place'>
	<option>بيت</option>
	<option>السوق</option>
	<option>المدرسة</option>
</select>


    <br>
            <div class="form-inline"><a class="btn btn-primary" id="phrase" title="بناء الجملة"><span>بناء</span></a>
            <a class="btn btn-primary" id="random_select" title="عشوائي"><span>عشوائي</span></a>
              <input checked="checked" class="checkbox" id="LastMark" value="1"
                type="checkbox"> حركة الإعراب</div>
          </form>
          <!--<section class="bg-danger text-white"> أضفنا زرا لتسهيل النسخ</section>-->
          <output id="result" class="form-control" width="100%%">{{ResultText}}</output>
          <section class="bg-info" id="small_hint"></section>
        </div>
        <div class="col-md-3 column"> <progress id="loading"></progress>
          <!--              <div class="panel panel-default">
               <div class="panel-heading"> ادعم مشكال</div>               <div class="panel-body"><a href="https://www.patreon.com/bePatron?u=23679540" data-patreon-widget-type="become-patron-button">ادعمنا على باتريون</a><script async src="https://c6.patreon.com/becomePatronButton.bundle.js"></script>           <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top"><input type="hidden" name="cmd" value="_s-xclick" /><input type="hidden" name="hosted_button_id" value="SAEUNQU5QW834" /><input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_DZ/i/scr/pixel.gif" width="1" height="1" /></form></div>--></div>
        <section class="bg-info" id="hint"></section>
      </div>
    </div>
    <div class="row clearfix">
      <div class="col-md-9 column"> </div>
      <div class="col-md-3 column"> </div>
    </div>
    <div class="container"><br>
      <div class="row clearfix">
        <div class="row clearfix" id="myfooter">
          <div class="col-md-3 column" id="myprojects">
            <div class="panel panel-default">
              <div class="panel-body"> <a href="http://blog.tahadz.com"><span class="glyphicon glyphicon-globe"></span>
                  مدونتي</a>
                <!--
                            <div class="media">-->
                <!--
  <div class="media-right">    <img src="/_files/images/dreamdevdz.png" class="media-object" style="width:100px">  </div>  <div class="media-body">    <h4 class="media-heading">الاس</h4>     من شركة <a href="https://dreamdev.dz/"> DreamDev.dz    </a>  </div>
--><!--
</div>--> <br>
                الاستضافة بدعم من شركة <a href="https://dreamdev.dz/">
                  DreamDev.dz<span class="glyphicon glyphicon-globe"></span></a>
                <script>//~ var script = "%(script)s";
        var script = "";
    </script>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                <!--<script  src="/_files/jquery-3.3.1.min.js"></script>-->
                <script async="" src="/_files/xzero-rtl/js/bootstrap-arabic.min.js"></script>
                <script async="" src="/_files/cytoscape.min.js"></script>
                <!--
    <script async src="/_files/adawat.min.js"></script>-->
                <script async="" src="/_files/adawat.js"></script> </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
