# $Id: Makefile,v 1.4 2004/03/30 00:13:57 jschauma Exp $

TARGET	=	slides

LATEX	=	latex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf

PICTURES=	pics/throw.eps \
		pics/host-states.eps \
		pics/change-sets.eps \
		pics/groups-machines.eps \
		pics/host-sets.eps \
		pics/cm-overlap.eps \
		pics/schrodinger.eps

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .png .gif .1

all:	$(PICTURES) $(TARGET).pdf

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

.ps.pdf:
	$(PS2PDF) $< $@

clean:
	rm -f *.txt *.out **.bbl *.blg *.log *.aux *.dvi *.ps *.pdf *.toc *.bak *.lof ${PICTURES}
	rm -fr $(TARGET)/
