# Mountain Legacy Project Image Prep
__Python script for preparing MLP images for use in the field__ 

[![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![GNU License](https://img.shields.io/badge/License-GNU-green.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Requirements

- [numpy](https://numpy.org/) >=1.26.4
- [pillow](https://pypi.org/project/pillow/) >=10.3.0
- [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter) >= 0.1.0

## Intructions for Running

### STEP 1 : Download the code
1. Press the green button that says Code and select download as zip.
2. Unzip the folder and move to location of choice (usually better to keep it on the local drive rather than anywhere on the cloud)
3. Keep the name MLP_img_prep for the folder (and make sure it’s not nested from unzipping it)

### STEP 2: Install Python
1. Check whether Python is installed (instructions [here](https://www.datacamp.com/blog/how-to-install-python))
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
2. Type the following:
	
	Windows:
	```console
	MLP_img_prep\Scripts\activate
	```
	Mac:
	```console
	source MLP_img_prep/bin/activate
	```

Your command prompt should now have MLP_image_prep in brackets before the cursor.


### STEP 5: Install Dependencies
1. Upgrade pip (type the following in command line)
	
	Windows:
	```console
	py -m pip install --upgrade pip
	```
	Mac:
	```console
	Python3 -m pip install --upgrade pip
	```

2. Install numpy

	Windows:
	```console
	py -m pip install numpy
	```
	Mac:
	```console
	Python3 -m pip install numpy
	```

3. Install pillow

	Windows:
	```console
	py -m pip install pillow
	```
	Mac:
	```console
	Python3 -m pip install pillow
	```

4. Install tkinter

	Windows:
	```console
	py -m pip install tk
	```
	Mac:
	```console
	Python3 -m pip install tk
	```

### STEP 6: Set up the image folder
1. Download all images from Explorer
2. Edit in Affinity Photo
3. Store all images from **one station** in a folder, each station should have its own folder
4. Images should be named to correspond to their name in Explorer (e-copy number is best)

### STEP 7: Run the program

**MAKE SURE YOUR ENVIRONMENT IS ACTIVE BEFORE DOING THIS, IF NOT, RETURN TO STEP 4.**

1. In the command line, navigate to the directory for the code (notice the different slashes on Windows vs Mac). Replace the words Folder with the correct path to your MLP_image_prep folder.

	* To find the path on Windows, navigate to the MLP_image_prep.py file in File Explorer, right click, choose properties, and check the File location under details

	* To find the path on Mac, navigate to the MLP_image_prep.py file in Finder, right click, choose Get Info, and check Where

	Windows:
	```console
	cd C:\Folder\Folder\MLP_img_prep
	```
	Mac:
	```console
	cd /Folder/Folder/MLP_img_prep
	```

2. Run the script

	Windows:
	```console
	py MLP_image_prep.py
	```
	Mac:
	```console
	Python3 MLP_image_prep.py
	```

3. Fill in the surveyor name, survey year, and station name when prompted
4. A window will pop up: Navigate to the folder containing your images
5. After a minute, a second window will pop up: Navigate to the folder where you want to save the completed PDF


