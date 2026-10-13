.PHONY: setup convert test

setup:
	python -m pip install -r requirements.txt

convert:
	python -m src.convert --raw data/raw --out data/processed

test:
	python -m pytest -q
