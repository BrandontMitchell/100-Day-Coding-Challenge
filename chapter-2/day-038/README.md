# Day 038 - Face detection

Computer vision is a very controversial topic, but one of the most useful paths in computer science. Here we explore `opencv`, a very common object recognition/computer vision modules. We will be creating a project that recognizes faces from a given image!

### Guide
1. This is a complex module, so we will need to implement the specifics first. Many of that is in the starter code
2. We need something called `haarcascade`s, which do most of the face defining features for us. This is just a fat xml file, feel free to look through it (and understand if you're a genius)

### Your Task:

1. After you finish reading through this guide, visit the documentation to get an understanding how to use things

2. Install all dependencies:
    ```
    pip install opencv2
    https://pip.pypa.io/en/stable/installing/
    ^ if you do not have pip installed on machine
    ```

3. Define `faces` -- a variable that uses `faceCascade.detectMultiScale()` and pass the correct parameters for converting the image to grayscale, with a certain scalefactor, minNeighbors, and minSize.

4. Write a loop that detects all faces in image

5. Print how many faces were found, and display the image.

6. Refer to: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html if you get lost at any point! This is a hard task, but very cool!

Good luck and happy coding!