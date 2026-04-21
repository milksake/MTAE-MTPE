# MTAE-MTPE
[![DOI](https://zenodo.org/badge/1133394676.svg)](https://doi.org/10.5281/zenodo.19674169)

This repository contains the code used to generate the results and figures reported in the paper:

> *Modeling the Effect of Awareness on the Spread of Misinformation*

The code implements two new rumor spreading models and runs simulations on three random graphs.

## Repository contents

- `code/` – Source code for graph generation, models, simulations and figure generation.
- `data/` – Raw data results of the simulations.
- `images/` – Output figures used in the paper.
- `requirements.txt` – Required python packages.  

## Installation and Usage

Clone the repository:

```bash
git clone https://github.com/milksake/MTAE-MTPE.git
cd MTAE-MTPE
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulations and generate figures:

```bash
python code/main.py
python code/plot.py
python code/lambert.py
python code/ws.py
```
