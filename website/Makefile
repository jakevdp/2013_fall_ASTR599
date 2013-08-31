.PHONY: clean gen serve

all: clean gen

cp_notebooks:
	mkdir -p content/media/notebooks
	rsync ../notebooks/*.ipynb content/media/notebooks/

gen: cp_notebooks
	hyde gen

serve: clean gen
	hyde serve

clean:
	rm -rf deploy

update: gen
