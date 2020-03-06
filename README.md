# Intro to Python for data analysis

## Introduction

http://chris35wills.github.io/courses/pydata_stack/

Make sure that everyone's environments are working.


## Other methods of installing ...

Miniconda
Anaconda

Use of conda-forge



## Python

The Software Carpentry basic introduction is here:

http://swcarpentry.github.io/python-novice-inflammation/

However, this begins with numPy as the main building block, which we are skipping today in favour of more stuff on Pandas.

Some tips:

* Use iPython, the interactive shell for Python. These tips below only apply to iPython and not plain Python.
* You can request help by typing the command plus a question mark afterwards, e.g. `print?`
* There are a variety of 'magic' commands, which begin with a %. One of the most useful is `%run <name_of_file.py>`.
* To see a list of variables currently in memory, type `whos`.


### Data structures

Lists: http://chris35wills.github.io/courses/Intermediate_python/lists/

Dictionaries: http://chris35wills.github.io/courses/Intermediate_python/dictionaries/

An example of dictionaries in use:

https://github.com/atedstone/ebmodel/blob/master/run_ebmodel_Samplemet.py

This script runs a glacier surface energy balance model for some timesteps. It uses two dictionaries to store (1) the energy fluxes and (2) the melt fluxes. Each of these two dictionaries uses date/time keys to store the data for each timestep. Each timestep contains a nested dictionary with the fluxes for that timestep.

Looping through lists and building dictionaries:

```python
a = {}
b = ['column1', 'column2']

# The 'matlab'-like way
for i in range(0,len(b)):
    a[b[i]] = 0

# The Pythonic way
for item in b:
    a[item] = 1
```


### Functions

Are we familiar with these? If not:

http://chris35wills.github.io/courses/Intermediate_python/functions/


### Packages/classes/modules

Cover imports and 'dot' notation

Cover imports `as`

Writing your own modules: 

http://chris35wills.github.io/courses/Intermediate_python/modules/


### numpy

It's a building block, but let's not spend too long on it!
http://chris35wills.github.io/courses/PythonPackages_numpy/README_numpy/


### pandas

http://chris35wills.github.io/courses/PythonPackages_pandas/

Series and DataFrames

Mention: reading in excel files

Mention: `datetime` library

Bonus: statistical data visualization...seaborn, http://seaborn.pydata.org/

Bonus: statsmodels, http://www.statsmodels.org/stable/index.html

Bonus: geopandas, used for geographic (vector) features, https://geopandas.org


### matplotlib

This package plots figures from various data sources - numpy arrays, pandas DataFrames, images ...

http://chris35wills.github.io/courses/PythonPackages_matplotlib/README_matplotlib/


### Putting our first analysis script together

Work through calibrate_ec.py step by step.



### NetCDF files and xarray

https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f

https://github.com/atedstone/Bristol_Geography_Python/tree/master/xarray

Sample data: https://www.dropbox.com/sh/ztxewjjmya3t246/AAAV2rYIiN8mqCV8M-WJOc4Ga?dl=0

First you may want to take a look at the contents of the file. Use the `ncdump` command at the command line (or other visual options like Panopoly can be downloaded from elsewhere):

```bash
$ ncdump -h MOD10A1.2000.006.MAR_GRo.nc
```


### Specialist GIS and remote sensing packages

Beyond the scope of today. In particular, look at:

* rasterio (for raster data)
* (GDAL) (for raster data)
* geopandas (for vector data), plus shapely, fiona
* scikit-image (for raster data)
* cartopy (map plotting)


### Python Style Guide

https://www.python.org/dev/peps/pep-0008

Describes how to lay out code so that it is readable and maintainable - 'best practises'.


## Unix

Good starting point for a full tutorial: 

http://swcarpentry.github.io/shell-novice


### Logging on to a server

Use PuTTY to open an SSH ('Secure Shell') session. You will need an account, for example on the UniFr beo cluster.

Files can be transferred between the server and your computer using SCP ('Secure Copy Protocol'). This can either be done on the command line or using a client such as FileZilla, https://filezilla-project.org/ or WinSCP, https://winscp.net/eng/download.php.

To open graphical windows such as figure plots, matlab etc you will also need to install the XMing client onto your computer and configure your PuTTY installation to use it:

http://laptops.eng.uci.edu/software-installation/using-linux/how-to-configure-xming-putty


### .bashrc and bash scripts

Code in your `~/.bashrc` file runs automatically when you log on to a Unix server.

You can also write bash scripts to automate your environment. E.g.

```bash
# setup_rivers.sh
export OMP_NUM_THREADS=12
export PROCESS_DIR=/home/geoscience/nobackup_cassandra/river_detection
export PYTHONPATH=/home/tedstona/scripts/landsat_ingestor/:$PYTHONPATH
```

```

```bash
$ source setup_rivers.sh
$ echo $PROCESS_DIR
/home/geosciences/nobackup_cassandra/river_detection/
$
```


### beo cluster

Use an SSH client, e.g. on the Ubuntu command line, or PuTTY for Windows.

When you login you are initially given a terminal on a login node. Login nodes can be used for copying files and for installing software but should not be used for data processing.

For processing, there are two approaches:

1.  Batch/queued processing
2.  Interactive session on a compute node.

To use an interactive session, execute the following command at the login node terminal. Note that you can change the resources that you require if you like - this command requests 10 threads/cores with 2 Gb RAM per core (therefore using 20 Gb RAM in total):

    qrsh -l h_vmem=2G -q new.q -pe smp 10


### File storage

By default, all files on beo05 are backed up. However, prepending 'nobackup_' to a folder prevents its contents from being backed up, which we have been asked to do where possible in order to reduce strain on the backup resources.

Each user has their own home space of ~1 Tb quota, e.g. 
/home/tedstona/

CASSANDRA people: we have read-only access to our BigData store from the login nodes only (not the processing nodes). If you need to work with BigData files, use a login node terminal to copy the files from BigData to the cluster's local storage.

CASSANDRA people: we also have a shared home space:

    /home/geoscience/cassandra/
    /home/geoscience/nobackup_cassandra/


'Generic'/system-wide packages can be used:
    
    module avail

Then
    
    module load XX/XX

Differentiate between login and compute nodes.




## Git

http://chris35wills.github.io/courses/Intro_github/README/

http://swcarpentry.github.io/git-novice/guide/index.html

Git and Github are not the same thing! Git is the version control software which you install on your computer. GitHub is a web service which runs Git. You can push local repositories up to GitHub and clone/pull repositories from GitHub onto your computer.


## Data management

A course about proper scientific data management: https://datatree.org.uk/

For CASSANDRA people: `switchdrive/computing_info.md`


### Data archive

Use BigData. This store is backed up and so is suitable for storing irreplacable data, especially field data, and final processed datasets. It is quite slow to access and so not recommended to work directly with data stored here.


### 'Scratch' space

For working with relatively small datasets locally, placing them on your hard drive will suffice. Always make sure that a backup is available, for instance if working with field data, or that the data can be re-created easily, for instance if working with remote sensing products.

For data-intensive processing, use the 'beo05' computing cluster. 


### Code

All code/scripts should be version-controlled using Git. Repositories should be synchronised with a Git service such as Github or Bitbucket, which provides collaboration and backup.

Repositories associated with published papers should be set to open and a specific release created. Mint a DOI for the release with Zenodo.


### External hard drives, USB sticks

Only to be used as a supplementary store of irreplaceable data such as field data. Take care if maintaining multiple copies of datasets.


### Data lineage

This is especially important in the case of irreplacable field data.

Generally, field data can be split into (1) its raw, as-collected format, and (2) a post-processed format.

Raw, as-collected files must be preserved exactly as the data were downloaded from the logger or keyed-in, without further modification, including to header rows. They should be set as read-only where possible.

There may be multiple post-processed formats. All post-processed files must contain adequate metadata to enable lineage to be traced back to the original raw data files.


## A note on GDAL/OGR

http://www.gdal.org.  A comprehensive set of tools/utilities for working with georeferenced raster and vector data, mainly on the command line.

A package to use GDAL/OGR from within Python scripts is available (also known as an API or bindings). It can have quite a steep learning curve to get it to work. Increasingly the preference in the community is to use the rasterio package, which does a variety of similar things. 

A few years ago I wrote a package called georaster which uses GDAL to simplify use of GDAL in Python. http://georaster.readthedocs.io.



## Main useful resources

https://software-carpentry.org/

http://chris35wills.github.io/courses/



