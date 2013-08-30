.PHONY: clean gen serve

all: clean gen

gen:
	hyde gen

serve: clean gen
	hyde serve

clean:
	rm -rf deploy

update: gen
