# $Id: Makefile,v 1.5 2004/09/29 21:34:28 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES= \
		pics/switch.eps \
		pics/switch.eps \
		pics/complexity.eps \
		pics/sign.eps \
		pics/elevator_buttons-reverse.eps \
		pics/manual.eps \
		pics/manual2.eps \
		pics/kinder-surprise.eps \
		pics/donkey.eps \
		pics/feeping.eps \
		pics/bert-ernie.eps \
		pics/broken-windows.eps \
		pics/waste.eps \
		pics/donkey.eps \
		pics/feeping.eps \
		pics/bert-ernie.eps \
		pics/broken-windows.eps \
		pics/drown.eps \
		pics/tools.eps \
		pics/hammer.eps \
		pics/nails.eps \
		pics/big-tool.eps \
		pics/power-tools.eps \
		pics/hammer-screw.eps 

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .png .jpg .gif

all:	$(PICTURES) $(PICTURES) $(TARGET).dvi

show: $(PICTURES) ${TARGET}.dvi
	xdvipresent xga ${TARGET}.dvi -paper 25.8x19.3 -geometry 1024x764-0-0

slides:	$(PICTURES)

.tex.dvi:
	$(LATEX) $<
	$(LATEX) $<

.fig.eps:
	fig2dev -L eps $< > $@

ps:	$(TARGET).dvi $(TARGET).ps

# PS will be upside down - add the following line after each "%%Page: "
# directive:
# 180 rotate -612 -792 translate
.dvi.ps:
	$(DVIPS) $@ $<

.jpg.eps:
	convert $< $@

.png.eps:
	convert $< $@

.gif.eps:
	convert $< $@


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
