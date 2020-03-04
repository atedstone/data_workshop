# Intro to Python for data analysis

https://software-carpentry.org/
http://chris35wills.github.io/courses/


## Other methods of installing ...

Miniconda
Anaconda

Use of conda-forge



## Python

http://swcarpentry.github.io/python-novice-inflammation/

### Data structures

Lists: http://chris35wills.github.io/courses/Intermediate_python/lists/
Dictionaries: http://chris35wills.github.io/courses/Intermediate_python/dictionaries/


### Functions

Are we familiar with these? If not:
http://chris35wills.github.io/courses/Intermediate_python/modules/


### Packages/classes/modules

Cover imports and 'dot' notation


### argparse


### numpy

It's a building block, but let's not spend too long on it!
http://chris35wills.github.io/courses/PythonPackages_numpy/README_numpy/


### matplotlib

http://chris35wills.github.io/courses/PythonPackages_matplotlib/README_matplotlib/

Bonus: seaborn


### pandas

http://chris35wills.github.io/courses/PythonPackages_pandas/

Mention: reading in excel files

Bonus: statsmodels


### xarray
https://github.com/atedstone/Bristol_Geography_Python/tree/master/xarray


### Plotting maps

A bit beyond the scope of this session, but have a look at:

cartopy

(basemap module is deprecated so should not be used in new scripts)



## Unix

### Logging on to server


### .bashrc and bash scripts

Code in your `.bashrc` file executes automatically on login.

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



## Git

http://chris35wills.github.io/courses/Intro_github/README/
http://swcarpentry.github.io/git-novice/guide/index.html
Git and Github are not the same thing!!

## Data management


## People

Nicolas
Nicole
Tamara
Dominik
Marlene
Christin


## To do

### data

Some netcdf files, e.g. MAR model outputs or perhaps albedo

### examples

argparse
generic file opening
data structures:
    - tuples
    - lists
    - dicts
    - [arrays]