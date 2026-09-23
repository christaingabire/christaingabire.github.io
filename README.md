# Christa Ingabire — Personal Website

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

## Building the site locally

Clone the repository and enter the project directory:

```bash
git clone https://github.com/christaingabire/christaingabire.github.io.git
cd christaingabire.github.io
```

All commands below should be run from this directory.

Set up the Python environment:

```bash
uv sync
```

Restore the R environment:

```bash
Rscript -e 'renv::restore(prompt = FALSE)'
```

Render the website:

```bash
uv run quarto render
```

The rendered site will be created in the `docs/` directory.

To preview the site locally:

```bash
uv run quarto preview
```

## Data

The Python post uses the Palmer Penguins dataset from the `palmerpenguins`
package. The R post uses the Gapminder dataset from the `gapminder` package.
Links to the original data sources and licensing information are included in
the individual posts.

The R and Python bonus post creates its example data directly in the document.

No API keys or authentication are required. An internet connection is needed
the first time the Python and R dependencies are installed.