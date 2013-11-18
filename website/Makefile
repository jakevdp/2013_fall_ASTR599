.PHONY: clean gen serve

all: clean gen

cp_notebooks:
	mkdir -p content/notebooks
	rsync -ar ../notebooks/*.ipynb ../notebooks/images ../notebooks/fig_code content/notebooks/
	mkdir -p content/notebooks/files/images # hack to make files/images work
	rsync -ar content/notebooks/images/* content/notebooks/files/images/
	cp ../notebooks/nth_fib.html content/notebooks/nth_fib.html

clean_notebooks:
	rm content/notebooks/*.ipynb

gen: cp_notebooks
	hyde gen

serve: clean gen
	hyde serve

clean: clean_notebooks
	rm -rf deploy

update: gen

publish:
	hyde gen -c production.yaml
	rsync -e ssh -r deploy_production/ gateway.astro.washington.edu:/www/astro/users/vanderplas/html/Astr599/
