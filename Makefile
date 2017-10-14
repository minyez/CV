all: cnsite ensite cncv encv

cnsite: site_cn.pdf site_cn.html
	-rm site_cn.pdf
ensite: site_en.pdf site_en.html
	-rm site_en.pdf

cncv: WeizhouPan_cn.pdf
encv: WeizhouPan_en.pdf

%.pdf: %.tex WeizhouPan.sty
	xelatex -interaction=batchmode $<
	xelatex -interaction=batchmode $<
	xelatex -interaction=batchmode $<

%.html: %.pdf
	pdf2htmlEX --zoom=1.5 $<
	python process.py $@
	mv $@ docs/	

clean:
	-rm -f *.aux *.log *.out *.html
	-rm -r auto	

