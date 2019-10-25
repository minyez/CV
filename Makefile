NAME = CV

#default: cncv

all: cncv encv join #cnsite ensiteA

join: $(NAME)_cn.pdf $(NAME)_en.pdf
	join.py -o cv.pdf $^

cnsite: site_cn.pdf site_cn.html
	rm site_cn.pdf
ensite: site_en.pdf site_en.html
	rm site_en.pdf

# use join.py of Automator actions in macOS
cncv: $(NAME)_cn.pdf
encv: $(NAME)_en.pdf

%.pdf: %.tex cvcmds.sty data/common_cn.tex data/common_en.tex
	xelatex -interaction=batchmode $<
	xelatex -interaction=batchmode $<
	xelatex -interaction=batchmode $<

%.html: %.pdf
	pdf2htmlEX --zoom=1.5 $<
	python process.py $@
	mv $@ docs/	

clean:
	rm -f *.aux *.log *.out *.html
	rm -rf auto	

cleanall: clean
	rm -f *.pdf
