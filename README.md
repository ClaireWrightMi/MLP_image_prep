# Mountain Legacy Project Image Prep
__Python script for perparing MLP images for use in the field__ 

[![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![GNU License](https://img.shields.io/badge/License-GNU-green.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Requirements (QGIS 3.28.1) 

- [numpy](https://numpy.org/) >=1.18.5
- 

## Intructions for Running

### STEP 1 : Download the code
1. Press the green button that says Code and select download as zip.
2. Unzip the folder and move to the location of choice (usually better to keep it on the local drive rather than anywhere on the cloud)
3. Keep the name MLP_img_prep for the folder (and make sure it’s not nested)

### STEP 2: Install Python
1. Check whether Python is installed (instructions [here] (https://www.datacamp.com/blog/how-to-install-python))
2. If Python is not installed, install it from the Python website (instructions [here](https://www.datacamp.com/blog/how-to-install-python))


### STEP 3: Set Up Virtual Environment
*The virtual environment will allow you to install Python libraries without risking conflict with other projects.*
1. Open File Explorer or Finder and navigate to the folder with your code.
2. Open Command Line or Terminal (from start, type Command Line for Windows or Terminal for Mac and open the first result)
3. Type the following:
	Windows:
	```console
	py -m venv MLP_img_prep
	```
	Mac:
	```console
	python3 -m venv MLP_img_prep
	```

### STEP 4: Activate the Virtual Environment
1. Open Command Line or Terminal (from start, type Command Line for Windows or Terminal for Mac and open the first result)
2. Type the following using the name of the folder holding the code
Windows:	MLP_img_prep\Scripts\activate
Mac:	source MLP_img_prep/bin/activate
Your command prompt should now have the name of your folder in brackets before the cursor.


## Installation

### Windows Users
Install the latest version of QGIS through the OSGeo4W installer from [here](https://qgis.org/en/site/forusers/alldownloads.html#osgeo4w-installer). From the OSGeo4W installer, select Express install. Choose QGIS LTR, GDAL, and GRASS GIS from the option menu. 

### MacOS Users
Install the latest version of QGIS [here](https://qgis.org/en/site/forusers/download.html).

### Dependencies
MIAS relies on some Python packages that do not come installed with QGIS and has conflicts with the existing versions of opencv and numpy. From the Plugins menu on QGIS, open the Python console and type the following commands:
```python
import pip
pip.main(['uninstall','-y','opencv-contrib-python'])
pip.main(['install','opencv-python'])
pip.main(['install','--upgrage','numpy'])
pip.main(['install','torch'])
pip.main(['install','scikit-image'])
```

### Installing the Plugin
From the Code menu (green button) on the [GitHub page](https://github.com/ClaireWrightMi/MLP_IA_Suite), select Download ZIP.  
From the Plugins menu in QGIS, choose Manage and Install Plugins, then Install from ZIP. Upload the ZIP file that you just downloaded from GitHub.

## Usage
A video tutorial for MIAS is available [here](URL).
A written tutorial and corresponding test data can be downloaded [here](URL).


