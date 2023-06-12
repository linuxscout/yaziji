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
	cd web;python3  testy.py
serverlang:
	cd web;python3  testylang.py

select:
	python3 yaziji/components_set.py > tests/output/select.html

ods:
	$(LIBREOFFICE) --headless --convert-to "csv:Text - txt - csv (StarCalc):9,34,UTF8" --outdir tests/samples/tmp/ tests/samples/*.ods
gettext:
	# extract messages from main template
	xgettext -L python --from-code=UTF-8 web/views/main2.tpl -o web/locales/main.po
copy_locales:
	cd web/locales; cp main.po ar/LC_MESSAGES/
	cd web/locales; cp main.po ar_DZ/LC_MESSAGES/
	cd web/locales; cp main.po en/LC_MESSAGES/
	cd web/locales; cp main.po fr/LC_MESSAGES/
update_locales:
	echo '' > messages.po # xgettext needs that file, and we need it empty
	find . -type f -iname "*.py" | xgettext -j -f - # this modifies messages.po
	msgmerge -N existing.po messages.po > new.po
	mv new.po existing.po
	rm messages.po	
