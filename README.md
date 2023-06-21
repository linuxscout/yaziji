# Yaziji: Arabic Phrase Generator
# يازجي: مولّد الجمل العربية
Yaziji : Arabic phrase generator
<div dir="rtl">
أداة لمساعدة المتعلم في تكوين جمل عربية صحيحة
</div>

## Idea
<div dir="rtl">
موقع أو تطبيق يساعد المتعلم للعربية غير الناطق بها لتركيب جمل بسيطة بالاعتماد على مدخلات نمطية
مثلا:

* الضمير: أنا
* الفعل : ذهب
* المفعول به: السوق
* ظرف الزمان: غدا 

النتيجة :  سَأُذْهِبُ إِلَى السُّوقِ غَدَا

</div>

## Name meaning

Yaziji, alternatively Yazigi or Yazji (Arabic: يازجي‎ [jɑzɪdʒiː], Yāzijī) is an Arabic surname of Turkish origin meaning 'clerk' or 'writer'. The Arabic definite article "Al-" is often added to render it Al-Yaziji or Al-Yazigi.

The Turkish equivalent is Yazici ([jazɯdʒɯ])

Yaziji/Yazigi/Yazji may refer to:

* Ibrahim al-Yaziji, Lebanese philologist
* John X (Yazigi) of Antioch (born 1955), Patriarch of Antioch and All The East, primate of the Greek Orthodox Patriarchate of Antioch and All The East
* Nasif al-Yaziji, Lebanese author
* Rosie Yazigi, Lebanese actress and voice actress
* Zina Yazji, Syrian journalist, news agency reporter and news anchor

## Demo
## To Do

نحتاج إلى ملء بيانات البرنامج بالكلمات الشائعة عند المبتدئين المتعلمين الناطقين بالعربية او بغيرها،

وأقصد بالبيانات
### المفردات

- الأفعال مثل شرب، أكل، سمع
- الأسماء التي تأتي فاعلا مثل الولد، البنت، الأسد 
- ما يأتي مفعولا، مثل التفاح، الطعام، الحليب،
- ما يأتي اسم مكان، مثل السوق، البيت، الحديقة،
- ما يأتي اسم زمان او ظرفا، مثل غدا وامس،

### العلاقات الدلالية 
ثم نحتاج إلى ضبط العلاقات الدلالية بما يجوز وما لا يجوز من ربط الأفعال بالفاعلين والمفعول بهم،
- مثلا يجوز استعمل الفعل شرب  مع فاعل مثل ولد وبنت وأسد
- ولا يجوز مع فاعل مثل شجرة وطاولة.
- و يجوز أن يشرب الحليب مفعولا به أو الماء ولا يجوز  أن تُشرب الطاولة أو الفنجان.
- والعلاقة بين الفاعل والمفعول فالولد يشرب القهوة، والأسد لا يشربها.

### ترجمة المفردات
- ثم سنترجم كل هذه البيانات للغات مثا الفرنسية والإنجليزية واليابانية

[Demo](http://tahadz.com/yaziji/) 

# Yaziji-web Front end

# How to Connect to yaziji

## Import Data
The query is like:
```
https://tahadz.com/yaziji/en/selectGet
```
This query ask for data in English `en`, the values are in Arabic.

The reponse is like:

```json
{
   "fields":[
      "subject",
      "verb",
      "auxiliary",
      "tense",
      "voice",
      "negative",
      "object",
      "time",
      "place",
      "phrase_type"
   ],
   "web-labels":{
      "الاستضافة بدعم من شركة":"Supported by",
      "بناء":"Build",
      "جملة اسمية":"Nominal Phrase",
      "جملة فعلية":"Verbal phrase",
      "حركة الإعراب":"Inflection mark",
      "زمن:":"Tense:",
      "ظرف زمان:":"Time:",
      "ظرف مكان:":"Place:",
      "عشوائي":"Random",
      "عينة":"sample",
      "فاعل":"Subject",
      "فعل مساعد":"Auxiliary",
      "فعل:":"Verb:",
      "مبني للمعلوم/مجهول:":"Voice:",
      "مثبت/منفي:":"affirmative/negative:",
      "مدونتي":"My blog",
      "مفعول":"Object",
      "نوع الجملة:":"Phrase type:"
   },
   
   "auxiliary":{
      "أَرَادَ":"Want",
      "اِسْتَطَاعَ":"Can",
      "كَادَ":"May"
   },
   "negative":{
      "مثبت":"Affirmative",
      "منفي":"Negative"
   },
   "object":{
      "أنا":"I",
      "تُفَاحَةٌ":"apple",
      "تِلْمِيذٌ":"pupil"
   },
   "phrase_type":{
      "جملة اسمية":"Nominal Phrase",
      "جملة فعلية":"Verbal phrase"
   },
   "place":{
      "بَيْتٌ":"house",
      "حَدِيقَةٌ":"garden",
      "سُوقٌ":"market"
   },
   "subject":{
      "أنا":"I",
      "أَحْمَدُ":"Ahmed"
   },
   "tense":{
      "الأمر":"Imperative",
      "الماضي المعلوم":"Past",
      "المضارع المعلوم":"Present/Future"
   },
   "time":{
      "أَحْيَانًا":"Sometimes",
      "أَمْسِ":"أَمْسِ",
      "أَوَّلَ أَمْسِ":"أَوَّلَ أَمْسِ"
   },
   "verb":{
      "أَخَذَ":"to take",
      "أَخْبَرَ":"to tell"
   },
   "voice":{
      "مبني للمجهول":"passive",
      "معلوم":"Active"
   }
}
```
Explain keys
-  "fields": contains fields names which will be used as inputs.
  those fields are be used as names of SELECT inputs and get values from the data given
-  "web-labels": contains translated string used in web page.
-  fields cited in "fields", represent keys and values of respective fields names,
-  for example "verb" contains a list of verbs.
-  for example "Subject" contains a list of nouns to be used as Subjects.
-  etc.


## Build a phrase with given inputs
The query is like:
```
https://tahadz.com/yaziji/en/ajaxGet?text=فَرَاشَةٌ&action=phrase&subject=فَرَاشَةٌ&object=&verb=لَعِبَ&time=بَعْدَ غَدٍ&place=&tense=المضارع المعلوم&voice=معلوم&auxiliary=كَادَ&negative=مثبت&phrase_type=جملة فعلية
```
The Reponse is given like
```json
{
  "order": 0,
  "result": "يَكَادُ الْفَرَاشَةُ أَنْ يَلْعَبَ بَعْدَ غَدٍ[جملة فعلية]"
}
```







