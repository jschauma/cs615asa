# $Id: Makefile,v 1.4 2004/03/30 00:13:57 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES= pics/Time_Machine.eps \
		pics/daily-tapes.eps \
		pics/disaster1.eps \
		pics/disaster2.eps \
		pics/dlt-library.eps \
		pics/dumb-user.eps \
		pics/flux-capacitor.eps \
		pics/flux-capacitor2.eps \
		pics/hacker.eps \
		pics/headcrash-closeup.eps \
		pics/libraries.eps \
		pics/waffles.eps \
		pics/wafl-snapshot.eps \
		pics/wafl.eps \
		pics/wafl0.eps \
		pics/wafl1.eps \
		pics/wafl2.eps \
		pics/20th-and-C.eps \
		pics/tar.eps \
		pics/bugs.eps \
		pics/github-unicorn.eps \
		pics/donkey_too_small_for_load.eps \
		pics/phonebook.eps \
		pics/root-servers.eps \
		pics/dns-space.eps \
		pics/vanilla.eps \
		pics/chocolate.eps \
		pics/2computers.eps \
		pics/2computers-nic.eps \
		pics/3computers.eps \
		pics/3computers-1.eps \
		pics/3computers-2.eps \
		pics/routed.eps \
		pics/hierarchical-dns.eps \
		pics/distributed-database.eps \
		pics/resolution.eps \
		pics/chicken-egg.eps \
		pics/anonymous.eps \
		pics/anonymous-tweet.eps \
		pics/arpanet1.eps




.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .png .gif .1

all:	$(PICTURES) $(FIGURES) $(TARGET).pdf



.1.txt:
	nroff -Tascii $< -mandoc | col -bx > $@

show: $(PICTURES) ${TARGET}.dvi
	xdvipresent xga ${TARGET}.dvi -paper 25.8x19.3 -geometry 1024x764-0-0

slides:	$(PICTURES) #example.knuth.eps example.knuth2.eps example.knuth3.eps

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
	rm -f *.txt *.out **.bbl *.blg *.log *.aux *.dvi *.ps *.pdf *.toc *.bak *.lof ${PICTURES}
	rm -fr $(TARGET)/
