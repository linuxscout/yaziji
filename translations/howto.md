# How to do to prepare a new language

1- use the google sheet to translate from Arabic,
2- save arabic and translation into csv
3- Make a three fields csv file (location, source, target)
* location: empty
* source: the arabic string
* target: the translated one
4- convert csv into po with a template
```sh
csv2po bn.csv -t ../main.pot  -o bn.po
```
5- create a folder with name as language code for example 'bn' for bangla
6- copy lang.po rename file as main_lang.po (lang is 2 letters code)

`cp bn.po bn/main_bn.po`



7- create a directory on web/locales
mkdir -p web/locales/bn/LC_MESSAGES/
8- copy into locales
add a line for the language

```sh
make copy_locales
```
9- compile mo files
 add line for this language
 then
```sh
make mo
```
10- update web/yaziji_webserver.py
add bn language to language list
## references:
 native language names
https://omniglot.com/language/names.htm

