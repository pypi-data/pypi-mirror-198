# icon-nmltools

This package provides command line tools (written in python) to deal with namelist files of the **ICON** numerical weather prediction model of DWD/MPI.

## nmldiff

Displays differences between two ICON namelists. It is also possible to provide an ICON namelist logfile to read the default values and consider them in the comparison. Output and Meteogram namelists are excluded from the comparison. Report bugs and missing features on https://gitlab.physik.uni-muenchen.de/Tobias.Selz/icon-nmltools or via email.


### Example usage

To see the available options:

    nmldiff -h
    nmldiff --help

Display the differences between two namelist files (nmlfile1 and nmlfile2):

    nmldiff nmlfile1 nmlfile2

Display the differences, but with defaults values filled:

    nmldiff -d nml.log nmlfile1 nmlfile2

Show all namelist parameters that are set in either file (differences will be highlighted in red) and consider the defaults. Also ignore namelist parameters that contain file or path in their name:

    nmldiff -vi -d nml.log nmlfile1 nmlfile2

# Installation

The tools can easily installed via pip. A Python-version >=3.6 is required.

    pip install icon-nmltools



