.PHONY: clean gen serve

all: clean gen

cp_notebooks:
	mkdir -p content/notebooks
	rsync -r ../notebooks/*.ipynb ../notebooks/images content/notebooks/
	mkdir -p content/notebooks/files/images # hack to make files/images work
	rsync -r content/notebooks/images/* content/notebooks/files/images/

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
