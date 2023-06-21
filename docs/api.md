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


