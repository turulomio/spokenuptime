DESTDIR ?= /

PREFIXBIN=$(DESTDIR)/usr/bin
PREFIXSHARE=$(DESTDIR)/usr/share/spoken-uptime
PREFIXLOCALE=$(DESTDIR)/usr/share/locale/


install:
	install -o root -d $(PREFIXBIN)
	install -o root -d $(PREFIXSHARE)

	install -m 755 -o root spoken-uptime.py $(PREFIXBIN)/spoken-uptime
	install -m 644 -o root GPL-3.txt CHANGELOG.txt AUTHORS.txt RELEASES.txt INSTALL.txt $(PREFIXSHARE)

#es
	install -o root -d $(PREFIXLOCALE)/es/LC_MESSAGES/
	xgettext -L Python --no-wrap --no-location --from-code='UTF-8' -o po/spoken-uptime.pot *.py
	msgmerge -N --no-wrap -U po/es.po po/spoken-uptime.pot
	msgfmt -cv -o $(PREFIXLOCALE)/es/LC_MESSAGES/spoken-uptime.mo po/es.po

uninstall:
	rm $(PREFIXBIN)/spoken-uptime
	rm -Rf $(PREFIXSHARE)
	rm $(PREFIXLOCALE)/es/LC_MESSAGES/spoken-uptime.mo

