# Learn.py 2024 - OpenCV for Art!

* OpenCV Art [Slides](https://docs.google.com/presentation/d/1_0k0E2MFRdN7fAwwIF3nqAq3M0N6kd25J1XH1Hk6khc/edit?usp=sharing)
* ACM Hack [Website](https://hack.uclaacm.com/)
* ACM Hack [Discord](https://discord.gg/3GSPECbCnE)

## Intro to OpenCV
OpenCV describes itself as the "World's biggest computer vision library". As an open source library with interfaces in C++, Python, Java, and MATLAB, OpenCV has emerged as a powerful tool for industry leaders. Specifically, OpenCV provides pre-written code to do the following
* Image Thresholding
* Affine Transformations (Rotation, Translation, etc.)
* Edge Detection
* Contour Detection
* Image Processing
* Image Segmentation
* Object Detection

### Running OpenCV Locally

Moving forward, we'll be using the OpenCV's python interface (we're learn.py after all). Below is a simple snippet of code also included under the `opencv-demo/` folder 

```python
import cv2
img = cv2.imread("learn_py.png")
img = cv2.rectangle(img, (10, 270), (140, 100),
                    (255, 0, 0), 2)

cv2.imshow("Display window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Notably, this code will read an image called `learn_py.png` in the same directory as the python code, then proceed to overlay a rectangle on the image and display it.

To run this script, take the following steps
1. Open a new folder in your text editor of choice (VS Code)
2. Open a new terminal (Terminal -> New Terminal)
3. Run the command `python -m venv ./.venv` to create a new Python virtual environment for our project
4. **Mac**: Run the command: `./.venv/bin/activate` to use the environment
**Windows**: Run the command: `./.venv/Scripts/activate.ps1` to use the environment
5. Navigate into the `opencv-demo/` folder by running the command `cd opencv-demo`
6. In your terminal, run the command to `pip install -r requirements.txt` install our current dependencies*
7. Run your python script either by running `python demo.py` in the terminal
8. Finally, add the code above to `demo.py` to draw a rectangle around the python!


*Note: We could have run `pip install opencv-python opencv-contrib-python` to achieve the same thing

## Argparse and Command Line Tools
Although most operating systems provide a way to interact through a graphical user interface (GUI - think the "Desktop" of a Mac or Windows PC), most also provide an alternative of interacting through a command line (think Linux/SEASnet). Although working with the Command Line Interface (CLI) usually has a steeper learning curve, there are numerous advantages of using a CLI over a GUI:
* Streamline automation (error handling, dependent task, etc.)
* Faster running time
* High customizability/control

Below is a common example of a CLI tool on UNIX systems. The `ls` command is used to list files in a particular folder.

```shell
$ ls -a
fileA.txt
fileB.txt
...
```

### Intro to Argparse

Python’s argparse module is a tool for streamlining CLI tool development (although not the only way to do it). As the name implies, it's used to parses arg(ument)s - argparse supports positional arguments, named arguments, and flags. Argparse also supports highly customizable usage and help messages.

Below is an example of the output of running an Argparse python script `main.py` that accepts a list of integers and either takes the sum or max and an optional number of times to repeat.

```shell
$ python main.py 1 2 3 4 --sum --repeat 3
10
10
10
```
In the above code we note we have three types of arguments
* Named Arguments: Arguments that require both a name and a value (like `--repeat 3` above). Named Arguments can come in long or short form (ex: `--option val` or `-o val`)
* Flags: Arguments that are either present or absent (like `--sum` above). Flags can come in long or short form (ex: `--option` or `-o`)
* Positional Arguments: Arguments that do not require a name, just a value (ex: `1 2 3 4` above). Since they don't have a name, these arguments are expected to come in a particular order. We generally use this for the command's payload.

We also recommend checking out this [document](https://docs.google.com/document/d/1mHGHozBAD04BsOavnUFRSdIbcxmFPx7hCPUJ8PUccoM/edit?usp=sharing) with more details about using argparse
    

### Running Argparse locally

Below is the code under the `argparse-demo/` folder that implements the `main.py` command above.

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('integers', type=int, nargs='+')
parser.add_argument('--sum', dest='op', action='store_const', const=sum, default=max)

args = parser.parse_args()
print(args.op(args.integers))
```

After importing argparse, we create an instance of an `ArgumentParser()`, the object that will store our intended arguments and map them when running. We use the `add_argument()` on our ArgumentParser to add new arguments. Finally, we use the `parser_args()` function to interpret the arguments provided to the script. It returns the results in a namespace/dictionary. 

## Creating a OpenAI Art CLI Tool
Now that we've got an understanding of the fundamentals, let's apply our skills building an OpenAI Art CLI Tool. We are providing a template under the `cli-art-template/` folder. This template leverages the OpenCV built-in functionality to stylize an image like an oil painting, as well as starter scripts for deep frying an image `cli-art-template/fried/fried.py` and creating pop art `cli-art-template/pop/pop.py`. To build off of the template, take a look at the following:

* Art techinques: [Watercolor](https://towardsdatascience.com/painting-and-sketching-with-opencv-in-python-4293026d78b#Watercolor%20Effect), [Oil Painting](https://towardsdatascience.com/painting-and-sketching-with-opencv-in-python-4293026d78b#Watercolor%20Effect), [Sketching](https://towardsdatascience.com/painting-and-sketching-with-opencv-in-python-4293026d78b#Watercolor%20Effect), [Pointillism](https://github.com/matteo-ronchetti/Pointillism), [Pop Art](https://www.analytics-link.com/post/2019/07/11/creating-pop-art-using-opencv-and-python), [ASCII Art](https://github.com/sjqtentacles/Image-to-Ascii-Art-with-OpenCV/blob/master/image-to-ascii-art-a-demo-using-opencv.ipynb), [Blurring](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html), [Sharpening](https://www.geeksforgeeks.org/image-enhancement-techniques-using-opencv-python/), [Cartoon](https://github.com/jumralia/Cartoonify-Image-with-OpenCV), [Pixel Art](https://jrtechs.net/data-science/creating-pixel-art-with-open-cv), [Contrast Booster](https://www.geeksforgeeks.org/image-enhancement-techniques-using-opencv-python/), [Aligner](https://www.geeksforgeeks.org/image-registration-using-opencv-python/), [Low Poly](https://github.com/tasercake/lowpolypy), [Titling](https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/)

* Argparse extensions: [Robust parameter validation (with subparsers)](https://dev.to/taikedz/ive-parked-my-side-projects-3o62), [Help/Usage messages](https://docs.python.org/3/library/argparse.html#help), [Parameter Sweep Option](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), Output File Names Option, Folder of Images Option, Add loading bars ([tqdm](https://www.geeksforgeeks.org/python-how-to-make-a-terminal-progress-bar-using-tqdm/) or [progressbar2](https://medium.com/pythoniq/progress-bars-in-python-with-progressbar2-da77838077a9))
