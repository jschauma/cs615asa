TARGET	=	slides

LATEX	=	latex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

FIGURES=	\
		pics/6platter.eps \
		pics/FireWire_4_6Pin.eps \
		pics/IRIX.filesystem.eps \
		pics/Installer_edit_partitions.eps \
		pics/S50JBOD.eps \
		pics/SFF_8086.eps \
		pics/SFF_8087.eps \
		pics/SFF_8088.eps \
		pics/SFF_8470.eps \
		pics/SFF_8484_angled.eps \
		pics/Sata_host_expansor_en.eps \
		pics/USB_Connector_End.eps \
		pics/USB_types.eps \
		pics/block.eps \
		pics/bucket.eps \
		pics/buckets.eps \
		pics/busted-disk.eps \
		pics/cable_scsi.eps \
		pics/cat-in-bucket.eps \
		pics/controlpanel.eps \
		pics/controlpanel.eps \
		pics/controlpanel2.eps \
		pics/cylinders.eps \
		pics/cloud.eps \
		pics/cloud-storage.eps \
		pics/das-versions.eps \
		pics/das.eps \
		pics/ddrdrive.eps \
		pics/disk-structure.eps \
		pics/devices.eps \
		pics/directory.eps \
		pics/disk.partition.eps \
		pics/fc-connectors.eps \
		pics/fc-connector.eps \
		pics/fc-optical.eps \
		pics/fc-switch.eps \
		pics/fc-switched.eps \
		pics/fc-topologies.eps \
		pics/file.eps \
		pics/filesystem-tree-mountpoints.eps \
		pics/fs-layout.eps \
		pics/fs-layout1.eps \
		pics/fs-layout2.eps \
		pics/fs-layout3.eps \
		pics/fw.eps \
		pics/fw1.eps \
		pics/fw2.eps \
		pics/fw3.eps \
		pics/hard-drive.eps \
		pics/ide-drive.eps \
		pics/iscsi-host-bus.eps \
		pics/jbod-front.eps \
		pics/jbod-inside.eps \
		pics/labels.eps \
		pics/lego.eps \
		pics/link.eps \
		pics/map.eps \
		pics/mounting.eps \
		pics/mounting.filesystem.eps \
		pics/nas.eps \
		pics/netapp.eps \
		pics/one-bucket-full.eps \
		pics/partition.eps \
		pics/pipe.eps \
		pics/raid-0.eps \
		pics/raid-1.eps \
		pics/raid-5.eps \
		pics/san.eps \
		pics/san.eps \
		pics/sata-ide_lg.eps \
		pics/satavide.eps \
		pics/satavpata.eps \
		pics/san-nas-das.eps \
		pics/scsi-disk.eps \
		pics/scsi-disk2.eps \
		pics/scsi-many.eps \
		pics/scsi-terminator.eps \
		pics/scsicard.eps \
		pics/socket.eps \
		pics/ssd-open.eps \
		pics/ssd.eps \
		pics/ssd2.eps \
		pics/tetris.eps \
		pics/three-buckets.eps \
		pics/two-buckets.eps \
		pics/two-cats-one-bucket.eps \
		pics/usb-hub.eps \
		pics/ufs-details.eps \
		pics/xraid.eps \
		pics/equation-tweet.eps \
		pics/zfs.eps \
		pics/many-cats-in-basket.eps \
		pics/numbered-cats.eps \
		pics/several-cats.eps


.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .png .gif

all:	$(FIGURES) $(TARGET).dvi

show: ${TARGET}.dvi
	xdvipresent xga ${TARGET}.dvi -paper 25.8x19.3 -geometry 1024x764-0-0
#xdvipresent vga ${TARGET}.dvi -paper 25.8x19.3 -geometry 640x480-0-0

#show: ${TARGET}.pdf
#	open ${TARGET}.pdf

slides:	fs-tree.eps #example.knuth.eps example.knuth2.eps example.knuth3.eps

.tex.dvi:
	$(LATEX) $<
	$(LATEX) $<

.fig.eps:
	fig2dev -L eps $< > $@

.png.eps:
	convert $< $@

.jpg.eps:
	convert $< $@

.gif.eps:
	convert $< $@

ps:	$(TARGET).dvi $(TARGET).ps

# PS will be upside down - add the following line after each "%%Page: "
# directive:
# 180 rotate -612 -792 translate
.dvi.ps:
	$(DVIPS) $@ $<

pdf:  $(FIGURES) $(TARGET).dvi $(TARGET).ps $(TARGET).pdf

txt: $(TARGET).dvi $(TARGET).ps $(TARGET).pdf $(TARGET).txt

html:
	latex2html $(LATEX2HTMLOPTS) $(TARGET).tex

.ps.pdf:
	$(PS2PDF) $< $@

.pdf.txt:
	$(PDFTOTEXT) $< $@

clean:
	rm -f ${TARGET}.out **.bbl *.blg *.log *.aux *.dvi *.ps *.pdf *.toc *.bak *.lof ${FIGURES}
	rm -fr $(TARGET)/
