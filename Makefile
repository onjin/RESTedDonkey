.PHONY: run
run:
	python server.py

.PHONY: install
install:
	hatch env create default
