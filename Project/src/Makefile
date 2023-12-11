all: clean requirements analysis processing datasets modeling

clean:
	rm -rf ../data/datasets
	rm -rf ../data/processed
	rm -rf ../data/plots

requirements:
	pip3 install -r requirements.txt

analysis:
	mkdir -p ../data/plots/analysis
	python3 data_analysis.py > ../docs/data_analysis.md

processing:
	mkdir -p ../data/processed
	python3 data_processing.py

datasets:
	mkdir -p ../data/datasets
	python3 datasets_creation.py

modeling:
	mkdir -p ../data/predictions/rfc
	mkdir -p ../data/predictions/svm
	mkdir -p ../data/predictions/year_11/rfc
	mkdir -p ../data/predictions/year_11/svm
	mkdir -p ../data/plots/rfc_last_year/
	mkdir -p ../data/plots/rfc_all_years/
	mkdir -p ../data/plots/svm_last_year/
	mkdir -p ../data/plots/svm_all_years/
	python3 data_modeling.py