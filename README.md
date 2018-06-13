# Convolutional Networks for image recognition

In this repository, I have implemented different convolutional networks for image recognition applied on the MNIST and the CIFAR-10 datasets.

## The Datasets
### MNIST

MNIST is one of the oldest and most used dataset to benchmark image recognition models. 
It has 60000/10000 training/testing images of handwritten digits, in black and white and of 28 by 28 pixels.

![Alt text](https://raw.githubusercontent.com/ArthMx/ConvNet/master/MNIST_examples.png)

It is a really easy dataset for CNNs, LeNet-5 (LeCun et al., 1998) was already able to reach an accuracy higher than 99 %, 20 years ago ! Because of the very limited room for improvement left, it's less and less used as a benchmark for image recognition.

### CIFAR-10

CIFAR-10 is a dataset of 50000/10000 training/testing color images of 32 by 32 pixels. 
The images corresponds to 10 different classes :

![Alt text](https://raw.githubusercontent.com/ArthMx/ConvNet/master/CIFAR10_examples.png)

The diversity, coupled with the low resolution of the images, makes this dataset much harder to classify than MNIST. 
That is why CIFAR-10 is much more used today as a benchmark than MNIST. Today's best models are able to do around 95 % accuracy.

## The Models
### Models for MNIST

- **MNIST_ConvNet_1.ipynb** : Exercise in Tensorflow on the MNIST dataset, from the book *Hands-On Machine Learning with Scikit-Learn and TensorFlow*, Aurélien Géron, 2017, O'Reilly Media
- **Keras_MNIST.ipynb** : A small VGG-like model applied to MNIST using Keras (99 % accuracy). 

### Models for CIFAR-10

A collection of neural networks inspired by the most successful CNNs.
- **CIFAR-10 LeNet-5.ipynb** : Y. LeCun et al., 1998, Gradient-Based Learning Applied to Document Recognition
- **CIFAR-10 VGG.ipynb** : Karen Simonyan, Andrew Zisserman, 2015, Very Deep Convolutional Networks for Large-Scale Image Recognition
- **CIFAR-10 ALL-CNN.ipynb** : J. T. Springenberg et al., 2015, Striving for Simplicity: The All Convolutional Net
- **CIFAR-10 ResNet.ipynb** : Kaiming He et al., 2015, Deep Residual Learning for Image Recognition
- **CIFAR-10 WideResNet.ipynb** : Sergey Zagoruyko & Nikos Komodakis, 2017, Wide Residual Networks

Model|Accuracy
---|---
LeNet-5|79.8 %
VGG|88.1 %
ALL-CNN|90.3 %
ResNet|91.0 %
WideResNet|92.2 %

All models have been saved in the folder **Model_trained/**.
