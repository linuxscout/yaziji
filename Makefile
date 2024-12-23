#/usr/bin/sh
# Build yaziji package

LIBREOFFICE=libreoffice6.3

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: 

# Publish to github
publish:
	git push origin master 

md2rst:
	pandoc -s -r markdown -w rst README.md -o README.rst
md2html:
	pandoc -s -r markdown -w html README.md -o README.html

wheel:
	sudo python3 setup.py bdist_wheel
install:
	sudo python3 setup.py install

sdist:
	sudo python3 setup.py sdist
upload:
	echo "use twine upload dist/yaziji-0.1-py2-none-any.whl"

doc:
	epydoc -v --config epydoc.conf
	
test1:
	python3  yaziji/phrase_generator.py> tests/output/text.out.txt
test:
	cd tests;python3  test.py -c test --limit 10 -o output/text.out.csv
gen:
	cd tests;python3  test.py -c generate --limit 10 -o output/text.sample.csv
eval:ods
	
	cd tests;python3  test.py -c test --limit 10 -f samples/tmp/sample10.csv -o output/text.eval.csv

server:
	cd web;python3  yaziji_webserver.py


select:
	python3 yaziji/components_set.py > tests/output/select.html

ods:
	$(LIBREOFFICE) --headless --convert-to "csv:Text - txt - csv (StarCalc):9,34,UTF8" --outdir tests/samples/tmp/ tests/samples/*.ods
gettext:
	# extract messages from main template
	xgettext -L python --from-code=UTF-8 web/views/main2.tpl -o web/locales/main.po
copy_locales:
	cp translations/ar/main_ar.po web/locales/ar/LC_MESSAGES/main.po
	cp translations/en/main_en.po web/locales/en/LC_MESSAGES/main.po
	cp translations/fr/main_fr.po web/locales/fr/LC_MESSAGES/main.po
	cp translations/id/main_id.po web/locales/id/LC_MESSAGES/main.po
	cp translations/bn/main_bn.po web/locales/bn/LC_MESSAGES/main.po
	cp translations/es/main_es.po web/locales/es/LC_MESSAGES/main.po
	cp translations/ja/main_ja.po web/locales/ja/LC_MESSAGES/main.po
	cp translations/zh/main_zh.po web/locales/zh/LC_MESSAGES/main.po
	cp translations/de/main_de.po web/locales/de/LC_MESSAGES/main.po
	cp translations/ku/main_ku.po web/locales/ku/LC_MESSAGES/main.po
mo:
	#create mo files
	cd web/locales/ar/LC_MESSAGES/; msgfmt main.po
	cd web/locales/en/LC_MESSAGES/; msgfmt main.po
	cd web/locales/fr/LC_MESSAGES/; msgfmt main.po
	cd web/locales/id/LC_MESSAGES/; msgfmt main.po
	cd web/locales/bn/LC_MESSAGES/; msgfmt main.po
	cd web/locales/es/LC_MESSAGES/; msgfmt main.po
	cd web/locales/de/LC_MESSAGES/; msgfmt main.po
	cd web/locales/zh/LC_MESSAGES/; msgfmt main.po
	cd web/locales/ja/LC_MESSAGES/; msgfmt main.po
	cd web/locales/ku/LC_MESSAGES/; msgfmt main.po


update_pot:
	#extract new messages and update global message file
	echo '' > messages.po # xgettext needs that file, and we need it empty
	find . -type f -iname "*.py" | xgettext -j -f - # this modifies messages.po
	cp translations/main.pot translations/main.pot.backup
	msgmerge -N translations/main.pot messages.po > translations/new.pot
	mv translations/new.pot translations/main.pot
	rm messages.po

update_po:LANG=en
update_po:LANG=fr
update_po:LANG=ar
update_po:LANG=id
update_po:
	# merge updated messages to existing languages files
	cd translations;msgmerge -N $(LANG)/main_$(LANG).po main.pot >$(LANG)/new.po
	cd translations/$(LANG);mv new.po main_$(LANG).po



testurl:
	curl -o tests/output/testajax1.json http://127.0.0.1:8080/fr/ajaxGet
	curl -o tests/output/testajax2.json http://127.0.0.1/yaziji/fr/ajaxGet
	curl -o tests/output/testselect1.json http://127.0.0.1:8080/fr/selectGet
	curl -o tests/output/testselect2.json http://127.0.0.1/yaziji/fr/selectGet

update_pofrompo:
	# import translation from en.po to main_en
	msgcat main_en.po en.po --use-first > main_en1.po
