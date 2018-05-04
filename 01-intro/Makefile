# $Id: Makefile,v 1.1 2005/01/17 20:10:57 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

FIGURES=	pics/sysadmin-personalities.eps	\
		pics/chicken-egg.eps		\
		pics/Cable_Tie.eps	\
		pics/Caffeine_molecule.eps	\
		pics/DuckTape.eps	\
		pics/MagrittePipe.eps	\
		pics/System-Call-and-Library-Function.eps	\
		pics/altix.eps	\
		pics/may-you-realize-your-ambitions.eps	\
		pics/armchair.eps	\
		pics/big-red-button.eps	\
		pics/blades.eps	\
		pics/cables2.eps	\
		pics/wrong-usability.eps	\
		pics/better-usability.eps	\
		pics/kiss.eps	\
		pics/car-duct-tape.eps	\
		pics/usability-security.eps	\
		pics/camera.eps	\
		pics/circularsaw.eps	\
		pics/cloud.eps	\
		pics/coffee.eps	\
		pics/computer-cables-big.eps	\
		pics/computers.eps	\
		pics/computers.eps	\
		pics/data-center-servers-t001.eps	\
		pics/datacenter.eps	\
		pics/datacenter2.eps	\
		pics/dmesg.eps	\
		pics/dogcart.eps	\
		pics/diesel-generator.eps	\
		pics/enter-the-dragon.eps	\
		pics/little-dragon.eps	\
		pics/google_whiteboard_large.eps	\
		pics/hand-scanner.eps	\
		pics/hats.eps	\
		pics/homer-brain.eps	\
		pics/internet.eps	\
		pics/juniper.eps	\
		pics/kernel-programs.eps	\
		pics/keyboard.eps	\
		pics/kinesis.eps	\
		pics/labelmaker.eps	\
		pics/leatherman.eps	\
		pics/macmini.eps	\
		pics/matrix.eps	\
		pics/mushroom_cloud.eps	\
		pics/office-chair.eps	\
		pics/pdp11.eps	\
		pics/punchcard.eps	\
		pics/quincy-panorama.eps	\
		pics/raid.eps	\
		pics/remote_hands.eps	\
		pics/screwdrivers.eps	\
		pics/switches.eps	\
		pics/unix-parts.eps	\
		pics/unix_history.eps	\
		pics/donkey_too_small_for_load.eps \
		pics/ardennes-horse.eps \
		pics/vierspaenner.eps \
		pics/lego-block.eps \
		pics/millennium-falcon.eps \
		pics/as-seen-by.eps \
		pics/as-seen-by-not-helping.eps	\
		pics/security-usability.eps	\
		pics/banana-wifi.eps		\
		pics/wifi.eps	\
		pics/sample-infrastructure-0.eps \
		pics/sample-infrastructure-1.eps \
		pics/sample-infrastructure-2.eps \
		pics/sample-infrastructure-3.eps \
		pics/sample-infrastructure-4.eps \
		pics/sample-infrastructure-5.eps \
		pics/sample-infrastructure-6.eps \
		pics/sample-infrastructure-7.eps \
		pics/hdmi.eps \
		pics/CS-venn.eps \
		pics/containers.eps \
		pics/ship-shipping-ships.eps


.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .png .jpg .gif

all:	$(FIGURES) $(TARGET).dvi
#	${BIBTEX} $(TARGET)

show: ${TARGET}.dvi
	xsetroot -solid white
	xdvipresent xga ${TARGET}.dvi -fullscreen -paper 25.8x19.3 -geometry 1440x900+70-0 -p 700
#show: ${TARGET}.pdf
#	open ${TARGET}.pdf

slides:	${FIGURES}

.tex.dvi:
	$(LATEX) $<
	$(LATEX) $<

.fig.eps:
	fig2dev -L eps $< > $@

.png.eps:
	convert $< $@

.jpg.eps:
	convert $< $@

.gif.eps:
	convert $< $@

ps:	$(TARGET).dvi $(TARGET).ps

# PS will be upside down - add the following line after each "%%Page: "
# directive:
# 180 rotate -612 -792 translate
.dvi.ps:
	$(DVIPS) $@ $<

pdf:  ${FIGURES} $(TARGET).dvi $(TARGET).ps $(TARGET).pdf

txt: $(TARGET).dvi $(TARGET).ps $(TARGET).pdf $(TARGET).txt

html:
	latex2html $(LATEX2HTMLOPTS) $(TARGET).tex

.ps.pdf:
	$(PS2PDF) $< $@

.pdf.txt:
	$(PDFTOTEXT) $< $@

clean:
	rm -f *.out **.bbl *.blg *.log *.aux *.dvi *.ps *.pdf *.toc *.bak *.lof ${FIGURES}
	rm -fr $(TARGET)/
