# $Id: Makefile,v 1.4 2004/03/30 00:13:55 jschauma Exp $

TARGET	=	slides
BIBLIO	=	slides.bib

LATEX	=	latex
BIBTEX	=	bibtex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

PICTURES=	pics/bandaid.eps \
		pics/BIOS.eps \
		pics/apache.eps \
		pics/beastie.eps \
		pics/bios.eps \
		pics/black-hat.eps \
		pics/nutrition-facts.eps \
		pics/blue-hat.eps \
		pics/green-hat.eps \
		pics/red-hat.eps \
		pics/block.eps \
		pics/bower.eps \
		pics/bucket.eps \
		pics/buckets.eps \
		pics/build-automation.eps \
		pics/car-firmware.eps \
		pics/car_radio-applications.eps \
		pics/cards.eps \
		pics/cat-in-bucket.eps \
		pics/dashboard-system-software.eps \
		pics/delete.eps \
		pics/devices.eps \
		pics/directory.eps \
		pics/dogfood.eps \
		pics/dolly.eps \
		pics/duck_tape.eps \
		pics/engine-kernel.eps \
		pics/engine-os.eps \
		pics/fhs.eps \
		pics/file.eps \
		pics/filesystem-tree-mountpoints.eps \
		pics/gollum.eps \
		pics/grub.eps \
		pics/headless.eps \
		pics/headwall.eps \
		pics/ide-drive.eps \
		pics/ignition-firmware.eps \
		pics/install-method.eps \
		pics/irix-install.eps \
		pics/kernel-dmesg.eps \
		pics/kernel.eps \
		pics/kfc1.eps \
		pics/labels.eps \
		pics/leftshark.eps \
		pics/lego.eps \
		pics/link.eps \
		pics/linksys.eps \
		pics/logo_oracle.eps \
		pics/magic_hat.eps \
		pics/many-cats-in-basket.eps \
		pics/map.eps \
		pics/mysql.eps \
		pics/netbsd-install.eps \
		pics/numbered-cats.eps \
		pics/one-bucket-full.eps \
		pics/os-screenshot.eps \
		pics/os.eps \
		pics/php-logo.eps \
		pics/pip.eps \
		pics/pipe.eps \
		pics/post.eps \
		pics/python.eps \
		pics/remote.eps \
		pics/several-cats.eps \
		pics/sharing.eps \
		pics/socket.eps \
		pics/solaris-install.eps \
		pics/stage1.eps \
		pics/sun-firmware.eps \
		pics/system-software.eps \
		pics/tetris.eps \
		pics/three-buckets.eps \
		pics/two-buckets.eps \
		pics/two-cats-one-bucket.eps \
		pics/types-of-software.eps \
		pics/ufs-details.eps \
		pics/unikernel.eps \
		pics/usb-icon.eps



#FIGURES=	decision-tree.eps two-rules.eps combined.eps area.eps

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .png .gif

all:	$(PICTURES) $(TARGET).dvi
#	${BIBTEX} $(TARGET)


show: ${TARGET}.dvi
	xdvipresent xga ${TARGET}.dvi -paper 25.8x19.3 -geometry 1024x764+0-0

slides:	${PICTURES}

.tex.dvi: ${PICTURES}
	$(LATEX) $<
	$(LATEX) $<

.fig.eps:
	fig2dev -L eps $< > $@

.dot.eps:
	dot -Tps $< > $@

.jpg.eps:
	convert $< $@

.png.eps:
	convert $< $@

.gif.eps:
	convert $< $@

ps:     $(TARGET).dvi $(TARGET).ps


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
