TARGET	=	slides

LATEX	=	latex
DVIPS	=	dvips -o
PS2PDF	=	ps2pdf
PDFTOTEXT=	pdftotext

FIGURES=	\
	pics/das.eps \
	pics/nas.eps \
	pics/san-nas-das.eps \
	pics/cloud-storage.eps \
	pics/6platter.eps \
	pics/numbered-cats.eps \
	pics/buckets.eps \
	pics/lego.eps \
	pics/map.eps \
	pics/tetris.eps \
	pics/block.eps \
	pics/ufs-details.eps \
	pics/types-of-software.eps \
	pics/angel.eps \
	pics/thumbsup-borat.eps \
	pics/tools.eps \
	pics/rirs.eps \
	pics/internet-undersea-cable.eps \
	pics/3computers-arp.eps \
	pics/3computers-ping.eps \
	pics/dsr.eps \
	pics/traceroute4.eps \
	pics/tcpip-stack.eps \
	pics/hierarchical-dns.eps \
	pics/wireshark.eps \
	pics/resolution.eps \
	pics/www.cs.stevens.edu.eps \
	pics/csr-process.eps \
	pics/events-metrics.eps \
	pics/glass-needle.eps \
	pics/root-servers.eps \
	pics/cylinders.eps \
	pics/Room_641A.eps \
	pics/revproxy.eps \
	pics/schrodinger.eps \
	pics/wafl.eps \
	pics/host-states.eps

#
#	pics/20th-and-C.eps \
#	pics/2computers-nic.eps \
#	pics/2computers.eps \
#	pics/3computers-1.eps \
#	pics/3computers-2.eps \
#	pics/3computers.eps \
#	pics/4layer-encapsulation.eps \
#	pics/BIOS.eps \
#	pics/ComputerChainedDown.eps \
#	pics/DES-f-function.eps \
#	pics/FireWire_4_6Pin.eps \
#	pics/IRIX.filesystem.eps \
#	pics/Installer_edit_partitions.eps \
#	pics/Killchain.eps \
#	pics/Lb101.eps \
#	pics/OSI_Model.eps \
#	pics/One-armed-inbound.eps \
#	pics/One-armed-outbound.eps \
#	pics/Public_key_encryption.eps \
#	pics/S50JBOD.eps \
#	pics/SFF_8086.eps \
#	pics/SFF_8087.eps \
#	pics/SFF_8088.eps \
#	pics/SFF_8470.eps \
#	pics/SFF_8484_angled.eps \
#	pics/Sata_host_expansor_en.eps \
#	pics/Time_Machine.eps \
#	pics/USB_Connector_End.eps \
#	pics/USB_types.eps \
#	pics/WhitneyHouston.eps \
#	pics/adapters.eps \
#	pics/angel-devil.eps \
#	pics/animal_farm.eps \
#	pics/anonymous-tweet.eps \
#	pics/anonymous.eps \
#	pics/anonymous.eps \
#	pics/apache.eps \
#	pics/arpanet1.eps \
#	pics/backdoor-trojans.eps \
#	pics/bandaid.eps \
#	pics/barrel_of_donkey.eps \
#	pics/beastie.eps \
#	pics/bert-ernie.eps \
#	pics/big-tool.eps \
#	pics/bmonkey.eps \
#	pics/bobby-tables.eps \
#	pics/bower.eps \
#	pics/broken-safe.eps \
#	pics/broken-windows.eps \
#	pics/bucket.eps \
#	pics/bugs.eps \
#	pics/build-automation.eps \
#	pics/busted-disk.eps \
#	pics/cable-layer.eps \
#	pics/cable_scsi.eps \
#	pics/car-duct-tape.eps \
#	pics/car_radio-applications.eps \
#	pics/cards.eps \
#	pics/cat-in-bucket.eps \
#	pics/cdn.eps \
#	pics/cell-phone.eps \
#	pics/chain-reaction.eps \
#	pics/chicken-egg.eps \
#	pics/chocolate.eps \
#	pics/chrome-tools.eps \
#	pics/classfull.eps \
#	pics/cloud.eps \
#	pics/cloud.eps \
#	pics/cold-boot-attack.eps \
#	pics/complexity.eps \
#	pics/computer_in_safe.eps \
#	pics/computerwithworld.eps \
#	pics/controlpanel.eps \
#	pics/controlpanel2.eps \
#	pics/cpu-12h.eps \
#	pics/cpu-30day.eps \
#	pics/cpu-7day.eps \
#	pics/crypto-accelerator.eps \
#	pics/daily-tapes.eps \
#	pics/das-nas-san.eps \
#	pics/das-versions.eps \
#	pics/dashboard-system-software.eps \
#	pics/datatransfer.eps \
#	pics/ddos.eps \
#	pics/ddrdrive.eps \
#	pics/delete.eps \
#	pics/devices.eps \
#	pics/dice-combinations.eps \
#	pics/directory.eps \
#	pics/disaster1.eps \
#	pics/disaster2.eps \
#	pics/disk-io-12h.eps \
#	pics/disk-io-30day.eps \
#	pics/disk-io-7day.eps \
#	pics/disk-structure.eps \
#	pics/disk.partition.eps \
#	pics/dlt-library.eps \
#	pics/dns-space.eps \
#	pics/dogfood.eps \
#	pics/dolly.eps \
#	pics/donkey.eps \
#	pics/donkey_too_small_for_load.eps \
#	pics/drive-by.eps \
#	pics/drown.eps \
#	pics/dual-stack.eps \
#	pics/duck_tape.eps \
#	pics/dumb-user.eps \
#	pics/elevator_buttons-reverse.eps \
#	pics/engine-kernel.eps \
#	pics/engine-os.eps \
#	pics/equation-tweet.eps \
#	pics/escalation.eps \
#	pics/exponential_growth.eps \
#	pics/fc-connector.eps \
#	pics/fc-connectors.eps \
#	pics/fc-optical.eps \
#	pics/fc-switch.eps \
#	pics/fc-switched.eps \
#	pics/fc-topologies.eps \
#	pics/feeping.eps \
#	pics/fhs.eps \
#	pics/file.eps \
#	pics/filesystem-tree-mountpoints.eps \
#	pics/firebug.eps \
#	pics/fishing.eps \
#	pics/flux-capacitor.eps \
#	pics/flux-capacitor2.eps \
#	pics/friedlander_revolving_door.eps \
#	pics/fs-layout.eps \
#	pics/fs-layout1.eps \
#	pics/fs-layout2.eps \
#	pics/fs-layout3.eps \
#	pics/fw.eps \
#	pics/fw.eps \
#	pics/fw1.eps \
#	pics/fw2.eps \
#	pics/fw3.eps \
#	pics/github-unicorn.eps \
#	pics/gollum.eps \
#	pics/groups-machines.eps \
#	pics/grub.eps \
#	pics/hacker.eps \
#	pics/hammer-screw.eps \
#	pics/hammer.eps \
#	pics/hard-drive.eps \
#	pics/headcrash-closeup.eps \
#	pics/headless.eps \
#	pics/headwall.eps \
#	pics/http-proposal-detail.eps \
#	pics/http-proposal-figure.eps \
#	pics/http-proposal.eps \
#	pics/ide-drive.eps \
#	pics/ignition-firmware.eps \
#	pics/install-method.eps \
#	pics/ipv4-exhausted-stats.eps \
#	pics/ipv4-exhausted-tweet.eps \
#	pics/ipv4-exhausted.eps \
#	pics/ipv6-launch.eps \
#	pics/iran.eps \
#	pics/irix-install.eps \
#	pics/iscsi-host-bus.eps \
#	pics/jbod-front.eps \
#	pics/jbod-inside.eps \
#	pics/kane.eps \
#	pics/kernel-dmesg.eps \
#	pics/kernel.eps \
#	pics/kfc1.eps \
#	pics/kids_fighting.eps \
#	pics/kinder-surprise.eps \
#	pics/labels.eps \
#	pics/leaking-bucket.eps \
#	pics/leftshark.eps \
#	pics/libraries.eps \
#	pics/link.eps \
#	pics/linksys.eps \
#	pics/livesofothers.eps \
#	pics/load-average-12h.eps \
#	pics/load-average-30day.eps \
#	pics/load-average-7day.eps \
#	pics/logo_oracle.eps \
#	pics/logs.eps \
#	pics/ls-l.eps \
#	pics/magic_hat.eps \
#	pics/manual.eps \
#	pics/manual2.eps \
#	pics/many-cats-in-basket.eps \
#	pics/map-of-internet.eps \
#	pics/memory-12h.eps \
#	pics/memory-30day.eps \
#	pics/memory-7day.eps \
#	pics/monkey.eps \
#	pics/mounting.filesystem.eps \
#	pics/mounting.eps \
#	pics/muppets.eps \
#	pics/mysql.eps \
#	pics/nails.eps \
#	pics/natural-stack-boxes-l.eps \
#	pics/netapp.eps \
#	pics/netbsd-install.eps \
#	pics/one-bucket-full.eps \
#	pics/os-screenshot.eps \
#	pics/os.eps \
#	pics/osi-encapsulation.eps \
#	pics/osi.eps \
#	pics/paranoid.eps \
#	pics/partition.eps \
#	pics/peered-networks.eps \
#	pics/phonebook.eps \
#	pics/php-logo.eps \
#	pics/pip.eps \
#	pics/pipe.eps \
#	pics/pki.eps \
#	pics/post.eps \
#	pics/power-tools.eps \
#	pics/python.eps \
#	pics/raid-0.eps \
#	pics/raid-1.eps \
#	pics/raid-5.eps \
#	pics/remote.eps \
#	pics/root-servers.eps \
#	pics/roots.eps \
#	pics/routed.eps \
#	pics/san.eps \
#	pics/sata-ide_lg.eps \
#	pics/satavide.eps \
#	pics/satavpata.eps \
#	pics/scsi-disk.eps \
#	pics/scsi-disk2.jpeg \
#	pics/scsi-disk2.eps \
#	pics/scsi-many.eps \
#	pics/scsi-terminator.eps \
#	pics/scsicard.eps \
#	pics/security-usability.eps \
#	pics/security.eps \
#	pics/several-cats.eps \
#	pics/sharing.eps \
#	pics/sign.eps \
#	pics/simple-reaction.eps \
#	pics/sledgehammer.eps \
#	pics/snowden.eps \
#	pics/social_engineering.eps \
#	pics/socket.eps \
#	pics/solaris-install.eps \
#	pics/spamhaus.eps \
#	pics/ssd-open.eps \
#	pics/ssd.eps \
#	pics/ssd2.eps \
#	pics/stage1.eps \
#	pics/sun-firmware.eps \
#	pics/superman.eps \
#	pics/switch.eps \
#	pics/symmetric-key-crypto.eps \
#	pics/syria-disappears.eps \
#	pics/sysadmin_infosec.eps \
#	pics/system-software.eps \
#	pics/tar.eps \
#	pics/teamwork.eps \
#	pics/test-ipv6-6.eps \
#	pics/test-ipv6.eps \
#	pics/three-buckets.eps \
#	pics/traceroute1.eps \
#	pics/traceroute2.eps \
#	pics/traceroute3.eps \
#	pics/tubes.eps \
#	pics/turbolift_access_denied.eps \
#	pics/two-buckets.eps \
#	pics/two-cats-one-bucket.eps \
#	pics/two-questions.eps \
#	pics/uncle-ben.eps \
#	pics/unplug.eps \
#	pics/unplugged.eps \
#	pics/usb-hub.eps \
#	pics/user-sets0.eps \
#	pics/user-sets1.eps \
#	pics/user-sets2.eps \
#	pics/vanilla.eps \
#	pics/waffles.eps \
#	pics/wafl-snapshot.eps \
#	pics/wafl.eps \
#	pics/wafl0.eps \
#	pics/wafl1.eps \
#	pics/wafl2.eps \
#	pics/waste.eps \
#	pics/wateringhole.eps \
#	pics/wolfram.eps \
#	pics/xdvipresent.1.ps \
#	pics/xdvipresent.2.ps \
#	pics/xdvipresent.3.ps \
#	pics/xdvipresent.4.ps \
#	pics/xdvipresent.graphviz.ps \
#	pics/xraid.eps \
#	pics/xsa.eps \
#	pics/zfs.eps

.SUFFIXES: .tex .dvi .ps .pdf .txt .fig .eps .jpg .png .gif

all:	$(FIGURES) $(TARGET).dvi

show: ${TARGET}.dvi
	xdvipresent xga ${TARGET}.dvi -paper 25.8x19.3 -geometry 1024x764-0-0
#xdvipresent vga ${TARGET}.dvi -paper 25.8x19.3 -geometry 640x480-0-0

#show: ${TARGET}.pdf
#	open ${TARGET}.pdf

slides:	

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
