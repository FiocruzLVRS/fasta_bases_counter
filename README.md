# Bases Counter

This is a simple python script to analyze a group of gene sequences in Fasta format and provide a counting on their nitrogenous bases.
The objective was to compare which bases in a group of genes changed the most.

Suppose you have a group of genes where they all have 100 nitrogenous bases. The idea is to count for each "position" (from position 0 to position 99) whats is the occurrence of each nitrogenous base: absolute and percentual.

# Executing

## Requirements

- Python3
- Numpy (`pip install numpy` should suffice)

## Run it!

The simplest way to execute the script it to download the `bases_counter.py`, then run in the terminal:
```bash
python bases_counter.py <file.fasta>
```

The output will be two files:
- residue_report.csv (includes headers)
  - Report where each line represents a position and each column the nitrogenous base. Each cell represents the absolute number or percentual of each nitrogenous base in that position.
- log.txt
  - Logs the unknown nitrogenous bases and their position

--------
Any suggestion and pull requests are very welcome!

