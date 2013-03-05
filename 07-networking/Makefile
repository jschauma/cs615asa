# $Id: Makefile,v 1.4 2004/03/05 04:12:51 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES= \
	pics/cloud.eps \
	pics/map-of-internet.eps \
	pics/2computers.eps \
	pics/3computers.eps \
	pics/routed.eps \
	pics/peered-networks.eps \
	pics/car-duct-tape.eps \
	pics/internet-undersea-cable.eps \
	pics/internet-undersea-cable.eps \
	pics/cable-layer.eps \
	pics/osi.eps \
	pics/CatinBox.eps \
	pics/natural-stack-boxes-l.eps \
	pics/osi-encapsulation.eps \
	pics/4layer-encapsulation.eps \
	pics/ipv4-exhausted.eps \
	pics/ipv4-exhausted-stats.eps \
	pics/dual-stack.eps \
	pics/test-ipv6.eps \
	pics/test-ipv6-6.eps \
	pics/ipv6-launch.eps \
	pics/3computers-arp.eps \
	pics/3computers-ping.eps \
	pics/traceroute1.eps \
	pics/traceroute2.eps \
	pics/traceroute3.eps \
	pics/traceroute4.eps \
	pics/tcpip-stack.eps \
	pics/rirs.eps

#FIGURES=	decision-tree.eps two-rules.eps combined.eps area.eps

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .gif .png

all:	${PICTURES} $(FIGURES) $(TARGET).dvi
#	${BIBTEX} $(TARGET)

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
