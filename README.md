# AutoDock Rescore & Statistical Screening Toolkit

Automated Python pipeline for post-docking data processing, binding affinity ranking, threshold filtering, and publication-ready visualization against the Human Histamine H2 Receptor (H2R).

---

## Project Overview
This repository contains standalone Python automation scripts developed to parse, screen, and benchmark molecular docking results. It serves as an independent technical module demonstrating bioinformatics automation and data analysis skills.

---

## Key Features
- Automated Data Processing: Parses tabular docking outputs using pandas.
- Affinity Screening: Ranks ligands and filters candidates against established reference drug thresholds (e.g., Icotidine: -8.42 kcal/mol).
- Visualization: Generates high-resolution comparative bar plots (matplotlib) highlighting lead phytochemical candidates versus controls.
- Export Pipeline: Automatically outputs filtered screening hits into structured CSV reports.

---

## Repository Structure
```text
autodock-rescore-toolkit/
├── data/
│   └── docking_results.csv         # Raw docking scores and compound metadata
├── results/
│   ├── top_screened_hits.csv       # Filtered high-affinity candidate leads
│   └── docking_energy_comparison.png # Comparative visualization plot
├── docking_analyzer.py             # Main automation & analysis script
└── README.md                       # Project documentation
```

## Usage
Run the analysis pipeline directly from the terminal:
python docking_analyzer.py

----

## Project Attribution & Context
* Original Collaborative Research: The underlying molecular docking protocols and phytochemical library curation were conducted as a collaborative academic project (Anti-Reflux Drug Design).
* Sole Developer & Script Author: tabantavanmand (Sole author and developer of this independent Python automation toolkit and rescoring repository).
