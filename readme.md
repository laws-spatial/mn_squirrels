# Setup

### Clone the repo

Clone the repo using

```
git clone https://github.com/alaws-USGS/mn_squirrels.git
```

### Set up conda environment
Open a conda CLI and change directory into mn_squirrels. Create the environment from the
environment.yml.

```
cd mn_squirrels
conda create -f environment.yml
```

### Data
The data was created using the data_prep.ipynb notebook found in the /data folder. However, using [dask-geopandas](https://dask-geopandas.readthedocs.io/en/stable/) allows the shapefiles to be read from the web service and manipulated when an internet connection is present.

# mn_squirrels
