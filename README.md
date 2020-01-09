# Neuro-Pic

Making E-commerce Immersive and Swifter through Neural Networks


## Getting Started

This repository provides a foundation for Team Neuropic E-Commerce Tech course project that includes image processing deep learning frameworks and a user interface. The instructions in this readme file will get you a copy of the project up and running on your local machine for testing purposes.

### Prerequisites

Python 3 should be installed in the system.

All the prerequisites are comprised of the python libraries leveraged to build neural network and perform clustering. Following is the list of libraries that are needed to be installed -
```
1. keras
2. numpy
3. pandas
4. glob
5. imageio
6. shutil
7. os

```

### Installing

To install the above libraries write the following command for each library -
```
pip install packagename

E.g. pip install keras

for cv2 please use the command: python -m pip install opencv-python
```

Do the same for all the packages

```
To verify whether the packages have installed properly, try import packagename command in your python IDE
```

### Categorizing Product Images

1. The Raw Data for different apparal categories was fetched from open-source website - http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html
2. This Raw Data is stored in Data folder of the project
3. The Data_Train_Valid_Split.py code is used to fetch the required images (with flat in their name) and divide them into Train and Validation sets (in Data\Model Data)
4. Categories that lack images or don't differ much in visuals are manually removed. Images that doesn't meet the requirement (e.g. with human in them) are manually removed
5. The Train and Valid images currently present in the folder are the result of the above steps
6. Then Test images folder is created (in Data\Model Data) and uncategorized images are added to them. These images can be changed as per requirements
7. Now we can run the Categorizing_Apparel.py code to predict the categories for the images in the Test folder
8. The above code creates a 'Predict' folder in the working directory with Test images categorized in folders according to their predictions

Note - Change the current working directory in Data_Train_Valid_Split.py and Categorizing_Apparel.py codes (in the beginning) to the directory they are stored in


## Acknowledgments

* Keras documentation
* https://medium.com/@arindambaidya168/https-medium-com-arindambaidya168-using-keras-imagedatagenerator-b94a87cdefad

