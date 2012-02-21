# $Id: Makefile,v 1.4 2004/03/30 00:13:55 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES=	pics/bandaid.eps \
		pics/barrel_of_donkey.eps \
		pics/bmonkey.eps \
		pics/cards.eps \
		pics/delete.eps \
		pics/dogfood.eps \
		pics/dolly.eps \
		pics/duck_tape.eps \
		pics/fhs.eps \
		pics/headless.eps \
		pics/headwall.eps \
		pics/install-method.eps \
		pics/irix-install.eps \
		pics/netbsd-install.eps \
		pics/solaris-install.eps \
		pics/gollum.eps \
		pics/sharing.eps \
		pics/magic_hat.eps \
		pics/BIOS.eps \
		pics/kfc1.eps \
		pics/kernel.eps \
		pics/engine-kernel.eps \
		pics/engine-os.eps \
		pics/car_radio-applications.eps \
		pics/dashboard-system-software.eps \
		pics/ignition-firmware.eps \
		pics/linksys.eps \
		pics/cell-phone.eps \
		pics/remote.eps \
		pics/sun-firmware.eps \
		pics/kernel-dmesg.eps \
		pics/os-screenshot.eps \
		pics/system-software.eps \
		pics/python.eps \
		pics/logo_oracle.eps \
		pics/php-logo.eps \
		pics/mysql.eps \
		pics/apache.eps \
		pics/os.eps \
		pics/beastie.eps \
		pics/build-automation.eps \
		pics/anonymous.eps



#FIGURES=	decision-tree.eps two-rules.eps combined.eps area.eps

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .png .gif

all:	$(PICTURES) $(TARGET).dvi
#	${BIBTEX} $(TARGET)


show: ${TARGET}.dvi
	xdvipresent xga ${TARGET}.dvi -paper 25.8x19.3 -geometry 1024x764+0-0

slides:	${PICTURES}

.tex.dvi: ${PICTURES}
	$(LATEX) $<
	$(LATEX) $<

.fig.eps:
	fig2dev -L eps $< > $@

.dot.eps:
	dot -Tps $< > $@

.jpg.eps:
	jpegtopnm $< | pnmtops > $@

.png.eps:
	pngtopnm $< | pnmtops > $@

.gif.eps:
	giftopnm $< | pnmtops >$@

ps:     $(TARGET).dvi $(TARGET).ps


ps:	$(TARGET).dvi $(TARGET).ps

# PS will be upside down - add the following line after each "%%Page: "
# directive:
# 180 rotate -612 -792 translate
.dvi.ps:
	$(DVIPS) $@ $<

pdf:  ${PICTURES} $(TARGET).dvi $(TARGET).ps $(TARGET).pdf

txt: $(TARGET).dvi $(TARGET).ps $(TARGET).pdf $(TARGET).txt

html:
	latex2html $(LATEX2HTMLOPTS) $(TARGET).tex

.ps.pdf:
	$(PS2PDF) $< $@

.pdf.txt:
	$(PDFTOTEXT) $< $@

clean:
	rm -f *.out **.bbl *.blg *.log *.aux *.dvi *.ps *.pdf *.toc *.bak *.lof ${PICTURES}
	rm -fr $(TARGET)/
