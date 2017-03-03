# Status: Drafting #

## Basic MNIST Exercise

### Prework

Before starting this exercise, please make sure you have installed and started the Docker container, either [locally](install-local.md) or on the [Cloud](install-cloud.md).

**Learn how to use a Jupyter Notebook**

During this exercise, you will edit and run code inside [Jupyter](https://www.jupyter.org/) notebooks. Jupyter notebooks are handy: they enable you to interactive execute code, and to display output and instructions in-line. If you're new to Jupyter, try this quick [tutorial](https://try.jupyter.org/) to learn the ropes before continuing (after following the link, click on the "Welcome to Python" notebook). Here are the key concepts you should know:

* A notebook is a bit like an IDE that runs inside your web browser. It's connected to a Python backend (during this exercise, the backend will be running inside the Docker container) that's responsible for executing the code, and returning results to the browser.

* A notebook is made up of cells. There are two types. A *markdown* cell contains, well, markdown. This is useful for providing instructions, or notes. A *code* cell contains, you guessed it, code. 

* Cells can be *executed*. To execute a sell, select it and press *shift + enter*, or click the "Play" button on the notebook's toolbar.

* Cells can be *edited*. To edit a cell, select it, and start typing.

* You can *reset* a notebook. This is useful if you want to restore everything to a clean slate. To reset a notebook, click on the *Kernel* menu, then select *Restart*.

**Ok, let's get started.**

In this exercise, we will write TensorFlow code to train a basic classifier to recognize handwritten digits, using the classic MNIST dataset.

### Step 1. Start and connect to the notebook server

Start the notebook server inside the running container, then to connect to it using a web browser. Here's how:

* If you are running the container locally, see step #6 of these [instructions](install-local.md).

* If you are running the container in a Cloud-VM, see step #7 of these [instructions](install-cloud.md).

### Step 2. Open the first notebook 

After you connect to the notebook server, click on the *notebooks* folder, then open *1_tf_contrib_learn.ipynb*.

![Token](../images/notebook_1.png?raw=true)

Once you've opened the notebook, your screen should look something like this:

![Token](../images/notebook_1_open.png?raw=true)

### Step 3. Run each cell and try to understand the code

This notebook contains step by step instructions. 

You may want to spend 5 or 10 minutes exploring this notebook. It uses an early version of TensorFlow's high level APIs. At the end is a short exercise in which you will replace the linear classifier with a deep neural network. This should only involve changing one line of code. 

*Note* the code in this notebook is written for TensorFlow v0.12rc. Recently, version 1.0 was released (yay!) The author of this repo hasn't had a chance to update this code yet (for our purposes, there's not a major difference).

### Step 4. Experiment with notebooks 2 through 5 for a deeper dive in to TensorFlow

Next, open and experiment with notebooks 2 through 5. These will show you how to write a neural network to classify handwritten digits using TensorFlow's core APIs. Open each notebook and follow the instructions there. Here's a description of each notebook:

* Notebook #2: roughly follows this [tutorial](https://www.tensorflow.org/get_started/mnist/beginners). To begin, we **recommend** you read the tutorial, then work through the notebook and try it for yourself. This may take about 20 minutes.

* Notebook #3: solution to the exercise from the previous notebook.

* Notebook #4: code for a single layer hidden neural network, and an exercise to convert it into a two layer DNN.

* Notebook #5: solution to the exercise from the previous notebook.
