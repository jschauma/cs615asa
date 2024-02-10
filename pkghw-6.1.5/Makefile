NAME=pkghw
PREFIX?=/usr/local

all: src/pkghw

src/pkghw: src/pkghw.c
	${CC} ${CFLAGS} $? -o $@ ${LDFLAGS}

src/pkghw.c src/pkghw.pl:
	@echo "Please run './configure' first."
	@echo "If you want to specify a different prefix or perl interpreter,"
	@echo "pass the '--prefix' and/or '--perl' options."
	@echo
	@false

install: src/pkghw src/pkghw.pl
	mkdir -p $(PREFIX)/sbin $(PREFIX)/libexec $(PREFIX)/etc
	install -c -o cs615 -m 4755 src/$(NAME) $(PREFIX)/sbin/$(NAME)
	install -c -o cs615 -m 500 src/$(NAME).pl $(PREFIX)/libexec/$(NAME).pl
	install -c -m 444 conf/$(NAME).conf $(PREFIX)/etc/$(NAME).conf

uninstall:
	rm -f $(PREFIX)/sbin/$(NAME)
	rm -f $(PREFIX)/libexec/$(NAME).pl
	rm -f $(PREFIX)/etc/$(NAME).conf

clean:
	@rm -f src/pkghw.c src/pkghw src/pkghw.pl
