# $Id: Makefile,v 1.2 2006/04/10 14:22:04 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES= \
		pics/20th-and-C.eps \
		pics/Time_Machine.eps \
		pics/bugs.eps \
		pics/cpu-12h.eps	\
		pics/cpu-30day.eps	\
		pics/cpu-7day.eps	\
		pics/daily-tapes.eps \
		pics/disk-io-12h.eps	\
		pics/disk-io-30day.eps	\
		pics/disk-io-7day.eps	\
		pics/dlt-library.eps \
		pics/dumb-user.eps \
		pics/events-metrics.eps \
		pics/flux-capacitor.eps \
		pics/flux-capacitor2.eps \
		pics/glass-needle.eps	\
		pics/hacker.eps \
		pics/headcrash-closeup.eps \
		pics/libraries.eps \
		pics/load-average-12h.eps \
		pics/load-average-30day.eps \
		pics/load-average-7day.eps \
		pics/logs.eps		\
		pics/memory-12h.eps	\
		pics/memory-30day.eps \
		pics/memory-7day.eps	\
		pics/monkey.eps		\
		pics/schrodinger.eps \
		pics/tar.eps \
		pics/waffles.eps \
		pics/wafl.eps \
		pics/wafl0.eps \
		pics/wafl1.eps \
		pics/wafl2.eps

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .gif .jpg .png

all:	$(PICTURES) $(FIGURES) $(TARGET).dvi
#	${BIBTEX} $(TARGET)

show: $(PICTURES) ${TARGET}.dvi
	xdvipresent xga ${TARGET}.dvi -paper 25.8x19.3 -geometry 1024x764-0-0

slides:	$(PICTURES)

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
