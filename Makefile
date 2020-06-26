
FILE=thesis

build: $(FILE).tex
	pdflatex -shell-escape $(FILE)
	pdflatex -shell-escape $(FILE)
	bibtex $(FILE)
	pdflatex -shell-escape $(FILE)
	pdflatex -shell-escape $(FILE)
	pdflatex -shell-escape $(FILE)

clean:
	$(RM) *.aux *.bbl *.blg *.dvi *.idx *.log *.lol *.t1 *.toc *.bcf *~ src/*.aux
