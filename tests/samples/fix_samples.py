# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import json
true=True
false=False
# How to fix samples with examples number
ls =  [{"subject": "أَحْمَد", "object": "", "verb": "بَاعَ", "time": "دَائِمًا", "place": "سُوقٌ", "tense": "المضارع المعلوم", "voice": "مبني للمجهول", "auxiliary": "أَرَادَ", "negative": "منفي", "phrase_type": "جملة اسمية", "phrase": "الْأَحْمَدُ لَنْ يُرَادَ أَنْ يُبَاعَ فِي السُّوقِ دَائِمًا", "inflection": "إعراب الجملة", "errors": "", "valid":true}
,{"subject": "أَحْمَد", "object": "", "verb": "سَاعَدَ", "time": "سَنَةً", "place": "مَطْبَخٌ", "tense": "الماضي المعلوم", "voice": "مبني للمجهول", "auxiliary": "كَادَ", "negative": "منفي", "phrase_type": "جملة فعلية", "phrase": "لَمْ يُكَدْ أَنْ يُسَاعَدَ فِي الْمَطْبَخِ سَنَةً", "inflection": "إعراب الجملة", "errors": "", "valid":true}
]

index = [4, 5, 8, 11, 13, 15, 16, 17, 19, 21, 23, 24, 25, 26, 28, 29, 31, 32, 33, 34, 35, 37, 41, 43]
new_ls = []
for num, item in enumerate(ls):
    if num in index:
        item["valid"]=False
    new_ls.append(item)
print(json.dumps(new_ls, ensure_ascii=False))
        
