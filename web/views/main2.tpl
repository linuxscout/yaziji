<!DOCTYPE html>
<html lang="ar">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <!--[if lt IE 9]>
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>  <![endif]-->
    <title>مولد الجمل العربية</title>
    <link href="_files/favicon1.png" rel="icon" type="image/png">
    <link href="_files/adawatstyle.css" rel="stylesheet">

    <!-- <link href="_files/xzero-rtl/css/bootstrap-arabic.reduced.css" rel="stylesheet">  -->
    <link href="_files/xzero-rtl/css/bootstrap-arabic.min.css" rel="stylesheet">
    <!--
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">-->
    <!--
    <link href="_files/bootstrap-rtl.min.css" rel="stylesheet">-->
    <meta content="width=device-width, initial-scale=1" name="viewport">
  </head>
  <body dir="rtl">
                   <p> <a href="main"><img alt="مولد الجمل العربية" height="120px" src="_files/logo.png" style='float:right; margin-top:-20px;'> </a></p>
    <!--<h2>يازجي</h2>
    <h3>مولد الجمل العربية</h3>--><h3>مولد الجمل العربية</h3>
<h4> <a href="/ar">ar</a>&nbsp;<a href="/fr">Fr</a>&nbsp;<a href="/en">En</a>&nbsp;</h4>
    <div class="container">
      <div class="row clearfix">
        <div class="col-md-9 column">
          <form id="NewForm" name="NewForm" onsubmit="return false"><br>
          <h3>{{ _('My Language test') }}</h3>
{{ _('نوع الجملة:') }}
           <select id='phrase_type'  class='form-inline' name='phrase_type'>
    <option value="جملة فعلية">
    {{_('جملة فعلية')}}</option>
    <option value="جملة اسمية">{{ _('جملة اسمية') }}</option>
</select>
<br/>{{ _('فاعل') }} <select id='subject'  class='form-inline' name='subject'>
    <option value=""></option>
    <option value="أَحْمَد">{{ _('أَحْمَد') }}</option>
    <option value="وَلَدٌ">{{ _('وَلَدٌ') }}</option>
    <option value="أنا">{{ _('أنا') }}</option>
    <option value="نحن">{{ _('نحن') }}</option>
    <option value="أنت">{{ _('أنت') }}</option>
    <option value="أنتِ">{{ _('أنتِ') }}</option>
    <option value="أنتما">{{ _('أنتما') }}</option>
    <option value="أنتما مؤ">{{ _('أنتما مؤ') }}</option>
    <option value="أنتم">{{ _('أنتم') }}</option>
    <option value="أنتن">{{ _('أنتن') }}</option>
    <option value="هو">{{ _('هو') }}</option>
    <option value="هي">{{ _('هي') }}</option>
    <option value="هما">{{ _('هما') }}</option>
    <option value="هما مؤ">{{ _('هما مؤ') }}</option>
    <option value="هم">{{ _('هم') }}</option>
    <option value="هن">{{ _('هن') }}</option>
</select>
<br/>{{ _('فعل مساعد') }}
: <select id='auxiliary'  class='form-inline' name='auxiliary'>
    <option value=""></option>
    <option value="اِسْتَطَاعَ">{{ _('اِسْتَطَاعَ') }}</option>
<option value="أَرَادَ">{{ _('أَرَادَ') }}</option>
    <option value="كَادَ">{{ _('كَادَ') }}</option>
</select>
{{ _('فعل:') }}
<select id='verb'  class='form-inline' name='verb'>
    <option value=""></option>
    <option value="شَرِبَ">{{ _('شَرِبَ') }}</option>
    <option value="ضَرَبَ">{{ _('ضَرَبَ') }}</option>
    <option value="ذَهَبَ">{{ _('ذَهَبَ') }}</option>
    <option value="جَلَسَ">{{ _('جَلَسَ') }}</option>
</select>
{{ _('زمن:') }}
<select id='tense'  class='form-inline' name='tense'>
    <option value="الماضي المعلوم">{{ _('الماضي المعلوم') }}</option>
    <option value="المضارع المعلوم">{{ _('المضارع المعلوم') }}</option>
    <option value="الأمر">{{ _('الأمر') }}</option>
</select>
{{ _('مبني للمعلوم/مجهول:') }}
<select id='voice'  class='form-inline' name='voice'>
    <option value="معلوم">{{ _('معلوم') }}</option>
    <option value="مبني للمجهول">{{ _('مبني للمجهول') }}</option>

</select>
{{ _('مثبت/منفي:') }}
<select id='negative'  class='form-inline' name='negative'>
    <option value="مثبت">{{ _('مثبت') }}</option>
    <option value="منفي">{{ _('منفي') }}</option>
</select>
<br/>{{ _('مفعول') }} <select id='object'  class='form-inline' name='object'>
    <option value=""></option>
    <option value="حَلِيبٌ">{{ _('حَلِيبٌ') }}</option>
    <option value="بَابٌ">{{ _('بَابٌ') }}</option>
    <option value="أنا">{{ _('أنا') }}</option>
    <option value="نحن">{{ _('نحن') }}</option>
    <option value="أنت">{{ _('أنت') }}</option>
    <option value="أنتِ">{{ _('أنتِ') }}</option>
    <option value="أنتما">{{ _('أنتما') }}</option>
    <option value="أنتما مؤ">{{ _('أنتما مؤ') }}</option>
    <option value="أنتم">{{ _('أنتم') }}</option>
    <option value="أنتن">{{ _('أنتن') }}</option>
    <option value="هو">{{ _('هو') }}</option>
    <option value="هي">{{ _('هي') }}</option>
    <option value="هما">{{ _('هما') }}</option>
    <option value="هما مؤ">{{ _('هما مؤ') }}</option>
    <option value="هم">{{ _('هم') }}</option>
    <option value="هن">{{ _('هن') }}</option>
</select>
{{ _('ظرف زمان:') }}
<select id='time'  class='form-inline' name='time'>

    <option value=""></option>
    <option value="دَائِمًا">{{ _('دَائِمًا') }}</option>
    <option value="أَوَّلَ أَمْسِ">{{ _('أَوَّلَ أَمْسِ') }}</option>
    <option value="الْبَارِحَةَ">{{ _('الْبَارِحَةَ') }}</option>
    <option value="أَحْيَانًا">{{ _('أَحْيَانًا') }}</option>
    <option value="بَعْدَ غَدٍ">{{ _('بَعْدَ غَدٍ') }}</option>
    <option value="مَسَاءً">{{ _('مَسَاءً') }}</option>
    <option value="أَمْسِ">{{ _('أَمْسِ') }}</option>
    <option value="الْيَوْمَ">{{ _('الْيَوْمَ') }}</option>
    <option value="غَدًا">{{ _('غَدًا') }}</option>
    <option value="صَبَاحًا">{{ _('صَبَاحًا') }}</option>
    <option value="كُلَّ يَوْمٍ">{{ _('كُلَّ يَوْمٍ') }}</option>
</select>
{{ _('ظرف مكان:') }}
 <select id='place'  class='form-inline' name='place'>
    <option value=""></option>
    <option value="بيت">{{ _('بيت') }}</option>
    <option value="سوق">{{ _('سوق') }}</option>
    <option value="مدرسة">{{ _('مدرسة') }}</option>
</select>




    <br>
            <div class="form-inline"><a class="btn btn-primary" id="phrase" title="{{ _('بناء الجملة') }}"><span>{{ _('بناء') }}</span></a>
            <a class="btn btn-primary" id="random_select" title="{{ _('اختيار عشوائي للمفردات') }}"><span>{{ _('عشوائي') }}</span></a>
            <a class="btn btn-primary" id="sample" title="{{ _('نسخ عينة جيسون للتجارب البرمجية') }}"><span>{{ _('عينة') }}</span></a>
              <input checked="checked" class="checkbox" id="LastMark" value="1"
                type="checkbox" title="{{ _('إظهار حركة الإعراب في أواخر الكلمات') }}"> {{ _('حركة الإعراب') }}</div>

          </form>
                    <!--hidden parts only used to extract gettext
                    {{ _('إظهار حركة الإعراب في أواخر الكلمات') }}
                    {{ _('اختيار عشوائي للمفردات') }}
                    {{ _('نسخ عينة جيسون للتجارب البرمجية') }
                    {{ _('بناء الجملة') }}
                    
                    -->
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
              <div class="panel-body"> <a href="http://blog.tahadz.com"><span class="glyphicon glyphicon-globe"></span>{{ _('مدونتي') }}
                  </a>
                <!--
                            <div class="media">-->
                <!--
  <div class="media-right">    <img src="_files/images/dreamdevdz.png" class="media-object" style="width:100px">  </div>  <div class="media-body">    <h4 class="media-heading">الاس</h4>     من شركة <a href="https://dreamdev.dz/"> DreamDev.dz    </a>  </div>
--><!--
</div>--> <br>{{ _('الاستضافة بدعم من شركة') }} <a href="https://dreamdev.dz/">
                  DreamDev.dz<span class="glyphicon glyphicon-globe"></span></a>
                <script>//~ var script = "%(script)s";
        var script = ".";
    </script>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                <!--<script  src="_files/jquery-3.3.1.min.js"></script>-->
                <script async="" src="_files/xzero-rtl/js/bootstrap-arabic.min.js"></script>
                <script async="" src="_files/cytoscape.min.js"></script>
                <!--
    <script async src="_files/adawat.min.js"></script>-->
                <script async="" src="_files/adawat.js"></script> </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
