# $Id: Makefile,v 1.4 2004/03/30 00:13:57 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES=	\
		pics/phonebook.eps \
		pics/root-servers.eps \
		pics/dns-space.eps \
		pics/vanilla.eps \
		pics/chocolate.eps \
		pics/clown-computing.eps \
		pics/2computers.eps \
		pics/2computers-nic.eps \
		pics/3computers.eps \
		pics/3computers-1.eps \
		pics/3computers-2.eps \
		pics/routed.eps \
		pics/github-ddos.eps \
		pics/hierarchical-dns.eps \
		pics/distributed-database.eps \
		pics/resolution.eps \
		pics/chicken-egg.eps \
		pics/tzmap-namerica.eps \
		pics/anonymous.eps \
		pics/anonymous-tweet.eps \
		pics/arpanet1.eps \
		pics/http-proposal-detail.eps \
		pics/www.cs.stevens.edu.eps \
		pics/datatransfer.eps \
		pics/Lb101.eps \
		pics/One-armed-inbound.eps \
		pics/One-armed-outbound.eps \
		pics/DSR.eps \
		pics/revproxy.eps \
		pics/postel.eps \
		pics/cdn.eps

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
