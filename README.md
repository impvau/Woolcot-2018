# Woolcot 2018

Replication of Woolcot's Relative Fat Mass [work in 2018](https://doi.org/10.1038/s41598-018-29362-1)

Please cite as
```
@misc{Ciezak-Woolcot-2024,
    author      = {Andrew Ciezak},
    title       = {Relative Fat Mass Replication},
    series      = {},
    year        = {2024},
    pages       = {},
    numpages    = {},
    url         = {},
    doi         = {},
    isbn        = {},
    publisher   = {},
    address     = {},
}
```

## Purpose

This work attempts to:
- Replicate Woolcot's work
- Detail errors and issues of replication in depth
- Explicitly communicate the exact procedure for replication, including the specific indicies and calculations used

## Data Generation

Data is generated from the NHANES repository using the [NHANES Interface](https://github.com/impvau/nhanes) which is also bundled within this code.

## Project Structure

The `out\rep` dir contains replicated output
The `src\replicate\tbl` dir contains a file for the replication of each table within the primary paper for comparison with our data
The `src\replicate\fig` dir contains a file for the replication of each figure within the primary paper for comparison with our data
The `src\replicate\sup_tbl` dir contains a file for the replication of each figure within the supplimentary material for comparison with our data
The `src\replicate\sup_fig` dir contains a file for the replication of each figure within the supplimentary material for comparison with our data

## Output
The `out\rep` dir produces the following key files
- `FIG2.md` replicates Figure 2 from Woolcots work
- `SUP_TABLEN.md` replicates the Nth table in Woolcots Suplementary material
- `TABLE1.md` replicates Table 1 from Woolcots work

Each of the tables includes a comparison when data is filtered using the additional steps outline in the paper.

# Execution

## Exact reproduction

A reproduction container with all required packages etc. with VS Code line-by-line debuging availble here:
```
docker pull impvsol.azurecr.io/240626-woolcot-2018
```

## Execution in VS Code
After downloading the appropriate repos and versions, Trigger F5 in VS Code to run `.vscode/launch.json` configuration in debug mode

## For the masochist

Run `python src/main.py` after configing everything manually

# Further Documetation

For use of VS Code, debugging, reproduction, containers, registries etc. see [procedures](https://github.com/impvau/proc).
