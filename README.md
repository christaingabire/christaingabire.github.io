# Christa Ingabire — Personal Website

This repository contains my personal website built with Quarto. It includes my
blog posts and computational work in Python and R

## Requirements

I built the site using:

- Quarto 1.10.18
- uv 0.12.7
- R 4.6.1
- Git

## Building the site locally

Clone the repository and enter the project directory:

```bash
git clone git@github.com:christaingabire/christaingabire.github.io.git
cd christaingabire.github.io
```

The commands below should be run from this directory

Set up the Python environment:

```bash
uv sync
```

Start R and restore the R packages:

```bash
R
```

Then, in the R console:

```r
renv::restore()
q()
```

If R asks whether to save the workspace image, choose `n`.

Once both environments are set up, render the website:

```bash
uv run quarto render
```

The rendered site will be created in the `docs/` directory.

To preview it locally:

```bash
uv run quarto preview
```

## Data

The Python post uses the Palmer Penguins dataset from the `palmerpenguins`
package. The R post uses the Gapminder dataset from the `gapminder` package.
Links to the original data sources are included in each post.

No API keys or authentication are required. An internet connection is needed
the first time the Python and R dependencies are installed.