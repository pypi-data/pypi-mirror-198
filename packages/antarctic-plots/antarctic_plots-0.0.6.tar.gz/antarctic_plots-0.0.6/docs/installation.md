# Installation

## Online usage (Binder)

See below for the full installation instructions. If instead you'd like to use this package online, without needing to install anything, check out our [Binder link](https://mybinder.org/v2/gh/mdtanker/antarctic_plots/c88a23c9dfe92c36f0bfdbbc277d926c2de763de), which gives full access the the package in an online environment.

This Binder environment can also be accessed by clicking the Binder icon in any of the {doc}`gallery/gallery` examples.

## Install package

### Conda / Mamba
The easiest way to install this package and it's dependencies is with conda or mamba into a new virtual environement:

    mamba create --name antarctic_plots --yes --force antarctic-plots

Activate the environemnt:

    conda activate antarctic_plots

### Pip
Instead, you can use pip to install antarctic-plots, but first you need to install a few dependencies with conda. This is because `PyGMT` `GeoPandas`, and `Cartopy` all rely on C packages, which can only be install with conda/mamba and not with pip. ere I use mamba, but conda will work as well, just replace any `mamba` with `conda`:

Create a new virtual environement:

    mamba create --name antarctic_plots --yes --force pygmt geopandas cartopy

Pip install antarctic-plots

    mamba activate antarctic_plots
    pip install antarctic_plots

If you don't have Python set up on your computer, I recommend setting up python with Miniconda. See the install instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Development version
You can use pip, with the above created environemnt, to install the lastest source from Github:

    pip install git+https://github.com/mdtanker/antarctic_plots.git

Or you can clone the repository and install:

    git clone https://github.com/mdtanker/antarctic_plots.git
    cd antarctic_plots
    pip install .

## Common errors

If you get errors related to GDAL and GMT, try reinstalling Geopandas and PyGMT with the following command:

    mamba install geopandas pygmt --force-reinstall -y

If you get errors related to the PyProj EPSG database, try the following:

    mamba install -c conda-forge proj-data --force-reinstall -y

or

    mamba remove --force pyproj -y
    pip install pyproj --force-reinstall

If you get an error related to traitlets run the following command as discussed [here](https://github.com/microsoft/vscode-jupyter/issues/5689#issuecomment-829538285):

    mamba install ipykernel --update-deps --force-reinstall -y
