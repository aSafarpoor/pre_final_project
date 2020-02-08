# -*- coding: utf-8 -*-
"""dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12bg04OFcO0I2JzCNggZTNUCVoPnEX5Sr
"""

!mkdir -p ~/.kaggle

!cp kaggle.json ~/.kaggle/

!kaggle datasets download -d paultimothymooney/breast-histopathology-images

!ls

!sudo apt-get install unzip
!unzip breast-histopathology-images.zip -d destination_folder

!ls

# Commented out IPython magic to ensure Python compatibility.
# %cd destination_folder/
!ls

# Commented out IPython magic to ensure Python compatibility.
# %cd 10253
!ls

# Commented out IPython magic to ensure Python compatibility.
# %cd 0

!ls

import cv2
img=cv2.imread("10253_idx5_x701_y951_class0.png")

from google.colab.patches import cv2_imshow
cv2_imshow(img)

# Commented out IPython magic to ensure Python compatibility.
# %cd ..

!ls

# Commented out IPython magic to ensure Python compatibility.
# %cd ..

!ls

# Commented out IPython magic to ensure Python compatibility.
# % ls -1 | wc -l

# Commented out IPython magic to ensure Python compatibility.
# %cd content
# %cd destination_folder/
!ls

# Commented out IPython magic to ensure Python compatibility.
# %cd 10253
# %cd 10253
!ls
! ls 0 | wc -l
! ls 1 | wc -l
# %cd ..

!ls

