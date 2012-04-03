# $Id: Makefile,v 1.4 2004/03/30 00:13:59 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES=	pics/ComputerChainedDown.eps \
		pics/broken-safe.eps \
		pics/computer_in_safe.eps \
		pics/computerwithworld.eps \
		pics/security.eps \
		pics/unplug.eps \
		pics/unplugged.eps \
		pics/sledgehammer.eps \
		pics/paranoid.eps \
		pics/symmetric-key-crypto.eps \
		pics/DES-f-function.eps \
		pics/Public_key_encryption.eps \
		pics/ddos.eps \
		pics/escalation.eps \
		pics/backdoor-trojans.eps \
		pics/leaking-bucket.eps \
		pics/social_engineering.eps \
		pics/computerwithworld.eps \
		pics/adapters.eps \
		pics/bobby-tables.eps \
		pics/security-usability.eps \
		pics/fishing.eps



.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .png .jpg .gif

all:	$(PICTURES) $(TARGET).dvi
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
