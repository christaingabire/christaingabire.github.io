# Christa Ingabire's Personal Website

This repository contains my personal website built with Quarto. It includes
blog posts and computational work in Python and R.

## Requirements

The site was built using:

- Quarto 1.10.18
- uv 0.12.7
- R 4.6.1
- Git

Python does not need to be installed separately. `uv` installs the Python
version specified in `.python-version`.

The Python environment is defined by `pyproject.toml` and `uv.lock`.
The R environment is defined by `renv.lock` and is restored using `renv`.

## Building the site locally

Clone the repository and enter the project directory:

```bash
git clone https://github.com/christaingabire/christaingabire.github.io.git
cd christaingabire.github.io
```

All commands below should be run from the top-level project directory.

### 1. Set up the Python environment

```bash
uv sync
```

This creates the project's `.venv` and installs the Python dependencies
recorded in `uv.lock`.

### 2. Restore the R environment

```bash
Rscript -e 'renv::restore(prompt = FALSE)'
```

This restores the R packages recorded in `renv.lock`, including `reticulate`,
which is used by the R and Python bonus post.

### 3. Render the website

```bash
uv run quarto render
```

The site should always be rendered through `uv run` so that Quarto and
`reticulate` use the Python environment associated with this project.

The rendered website is written to the `docs/` directory.

### 4. Preview the website locally

```bash
uv run quarto preview
```

## Computational posts

The site contains computational posts using both Python and R.

The Python post uses the Palmer Penguins dataset from the `palmerpenguins`
package. The R post uses the Gapminder dataset from the `gapminder` package.
Links to the original data sources and licensing information are included in
the individual posts.

The bonus post runs R and Python in the same Quarto document using
`reticulate`. It creates example data directly in the document, passes data
from R to Python, performs a calculation in Python, and returns the result to
R for visualization.

## Reproducibility

No API keys or authentication are required.

An internet connection is required the first time the Python and R
dependencies are installed.

To reproduce the site from a fresh clone, run the commands above in order:

```bash
uv sync
Rscript -e 'renv::restore(prompt = FALSE)'
uv run quarto render
```