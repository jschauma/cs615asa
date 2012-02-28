# $Id: Makefile,v 1.4 2004/03/30 00:13:57 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES= pics/Time_Machine.eps \
		pics/bert-ernie.eps \
		pics/broken-windows.eps \
		pics/bugs.eps \
		pics/clean-slate.eps \
		pics/compiling.eps \
		pics/complexity.eps \
		pics/consistency.eps \
		pics/daily-tapes.eps \
		pics/disaster1.eps \
		pics/disaster2.eps \
		pics/dlt-library.eps \
		pics/donkey.eps \
		pics/dumb-user.eps \
		pics/elevator_buttons-reverse.eps \
		pics/feeping.eps \
		pics/feepingcreatures.eps \
		pics/flux-capacitor.eps \
		pics/flux-capacitor2.eps \
		pics/hacker.eps \
		pics/headcrash-closeup.eps \
		pics/headcrash.eps \
		pics/kinder-surprise.eps \
		pics/kiss.eps \
		pics/libraries.eps \
		pics/manual.eps \
		pics/manual2.eps \
		pics/pipe.eps \
		pics/sign.eps \
		pics/switch-on-off.eps \
		pics/switch.eps \
		pics/tdd.eps \
		pics/waffles.eps \
		pics/wafl-snapshot.eps \
		pics/wafl.eps \
		pics/wafl0.eps \
		pics/wafl1.eps \
		pics/wafl2.eps \
		pics/waste.eps

MANPAGES=	ec2-backup.txt ec2-start-instance.txt

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .png .gif .1

all:	$(MANPAGES) $(PICTURES) $(FIGURES) $(TARGET).pdf
#	${BIBTEX} $(TARGET)



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
