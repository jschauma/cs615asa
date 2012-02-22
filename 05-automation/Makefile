# $Id: Makefile,v 1.5 2004/09/29 21:34:28 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES= pics/DinnerForOne.eps \
	pics/waldo.eps \
	pics/waldo2.eps \
	pics/big-tool.eps \
	pics/donquixote.eps \
	pics/flexibility.eps \
	pics/growmoney.eps \
	pics/hammer.eps \
	pics/hammer-screw.eps \
	pics/ingenuity-can-should.eps \
	pics/ingenuity.eps \
	pics/mchammer.eps \
	pics/mchammer2.eps \
	pics/money-tree.eps \
	pics/nails.eps \
	pics/patience.eps \
	pics/power-tools.eps \
	pics/tools.eps \
	pics/try_try_again.eps \
	pics/height_of_laziness.eps

#FIGURES=	decision-tree.eps two-rules.eps combined.eps area.eps

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .png .jpg .gif

all:	$(PICTURES) $(PICTURES) $(TARGET).dvi
#	${BIBTEX} $(TARGET)

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
