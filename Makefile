FTP_DIR=cv

all: chinesecv englishcv

chinesecv: WeizhouPan_cn.pdf docs/WeizhouPan_cn.html
englishcv: WeizhouPan_en.pdf docs/WeizhouPan_en.html

%.pdf: %.tex WeizhouPan.sty
	xelatex -interaction=batchmode $<
	xelatex -interaction=batchmode $<

docs/%.html: %.pdf
	pdf2htmlEX --zoom=1.5 $<

clean:
	-rm -f *.aux *.log *.out
	-rm -r auto

