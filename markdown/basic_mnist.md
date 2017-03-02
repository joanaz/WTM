## Basic MNIST Exercise

### Prework

During this exercise, we will run code inside a [Jupyter](https://www.jupyter.org/) (aka IPython) notebook to train a basic classifier for handwritten digits. Before getting started, please make sure you have installed and started the Docker container, either [locally](install-local.md) or on the [Cloud](install-cloud.md).

New to Jupyter notebooks?

* Try this [tutorial](https://try.jupyter.org/) (after opening the webpage, click on the "Welcome to Python" notebook) to learn the ropes.

### Step 1. Start and connect to the notebook server

Start the notebook server inside the running container, then to connect to it using a web browser. Here's how:

* If you are running the container locally, see step #6 of these [instructions](install-local.md).

* If you are running the container in a Cloud-VM, see step #7 of these [instructions](install-cloud.md).

### Step 2. Open the notebook titled "5_tf_contrib_learn.ipynb" for a high level intro

After you connect to the notebook server, click on the *notebooks* folder, then open *5_tf_contrib_learn.ipynb*.

![Token](../images/notebook_5.png?raw=true)

Once you've opened the notebook, your screen should look something like this:

![Token](../images/notebook_5_open.png?raw=true)

### Step 3. Run each cell and try to understand the code

You may want to spend 5 or 10 minutes exploring this notebook. It uses an early version of TensorFlow's high level APIs. At the end is a short exercise in which you will replace the linear classifier with a deep neural network. This should only involve changing one line of code. *Note* the code in this notebook is written for TensorFlow v0.12rc. Recently, version 1.0 was released (yay!) The author of this repo hasn't had a chance to update this code yet (for our purposes, there's not a major difference).

### Step 4. Experiment with notebooks 1 through 4 for a deeper dive in to TensorFlow

Next, open and experiment with notebooks 1 through 4. These will show you how to write a neural network to classify handwritten digits using TensorFlow's core APIs. Open each notebook and follow the instructions there. Here's a description of each notebook:

* Notebook #1: roughly follows this [tutorial](https://www.tensorflow.org/get_started/mnist/beginners). We recommend you read the tutorial, then work through the notebook to try it for yourself. This may take 20 minutes or so, there's a lot of information there if you're new to the subject.

* Notebook #2: solution to the exercise from the previous notebook.

* Notebook #3: code for a single layer hidden neural network, and an exercise to convert it into a two layer DNN.

* Notebook #4: solution to the exercise from the previous notebook.
