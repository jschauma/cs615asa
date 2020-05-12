# $Id: Makefile,v 1.4 2004/03/05 04:12:51 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES= \
	pics/2computers.eps \
	pics/3computers.eps \
	pics/broadcast-domain.eps \
	pics/asns.eps \
	pics/AS-interconnection.eps \
	pics/Room_641A.eps \
	pics/cable-layer.eps \
	pics/cablemap.eps \
	pics/car-duct-tape.eps \
	pics/cerf.eps \
	pics/redbox.eps \
	pics/classfull.eps \
	pics/cloud.eps \
	pics/hub.eps \
	pics/tcp-encapsulation.eps \
	pics/tcp-packet.eps \
	pics/internet-undersea-cable.eps \
	pics/map-of-internet.eps \
	pics/osi-stack.eps \
	pics/osi-stack2.eps \
	pics/peered-networks.eps \
	pics/rirs.eps \
	pics/routed.eps \
	pics/router.eps \
	pics/switch.eps \
	pics/syria-disappears.eps \
	pics/tubes.eps \
	pics/wolfram.eps

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .gif .png

all:	${PICTURES} $(FIGURES) $(TARGET).dvi

show: ${PICTURES} ${TARGET}.dvi
	xdvipresent xga ${TARGET}.dvi -paper 25.8x19.3 -geometry 1024x764-0-0

slides:	${PICTURES} #example.knuth.eps example.knuth2.eps example.knuth3.eps

.tex.dvi:
	$(LATEX) $<
	$(LATEX) $<

.fig.eps:
	fig2dev -L eps $< > $@

.jpg.eps:
	convert $< $@

.gif.eps:
	convert $< $@

.png.eps:
	convert $< $@

ps:	$(TARGET).dvi $(TARGET).ps

# PS will be upside down - add the following line after each "%%Page: "
# directive:
# 180 rotate -612 -792 translate
.dvi.ps:
	$(DVIPS) $@ $<

pdf:  $(PICTURES) $(TARGET).dvi $(TARGET).ps $(TARGET).pdf

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
