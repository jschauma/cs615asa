# $Id: Makefile,v 1.4 2004/03/30 00:13:55 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES=	\
		pics/angel-devil.eps \
		pics/angel.eps \
		pics/documents.eps \
		pics/headless.eps \
		pics/teamwork.eps \
		pics/thumbsup-borat.eps \
		pics/user.eps \
		pics/exponential_growth.eps \
		pics/animal_farm.eps \
		pics/responsibility.eps \
		pics/baseball.eps \
		pics/bow-before-me-white.eps \
		pics/user-sets0.eps \
		pics/user-sets1.eps \
		pics/user-sets2.eps \
		pics/uncle-ben.eps \
		pics/kids_fighting.eps \
		pics/hyperbolic_tangent.eps \
		pics/superman.eps \
		pics/groups-machines.eps \
		pics/ls-l.eps \
		pics/snowden.eps

#FIGURES=	decision-tree.eps two-rules.eps combined.eps area.eps

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .png .gif

all:	$(PICTURES) $(TARGET).dvi
#	${BIBTEX} $(TARGET)

show: ${TARGET}.dvi
	xdvipresent xga ${TARGET}.dvi -paper 25.8x19.3 -geometry 1024x764-0-0

slides:	#example.knuth.eps example.knuth2.eps example.knuth3.eps

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

.dot.eps:
	dot -Tps $< > $@

.jpg.eps:
	convert $< $@

.png.eps:
	convert $< $@

.gif.eps:
	convert $< $@


pdf: $(PICTURES) $(TARGET).dvi $(TARGET).ps $(TARGET).pdf

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
