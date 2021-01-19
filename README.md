# Raspberry Pi for Computer Vision

## Deep Learning Frameworks

Popular deep learning frameworks include **Caffe**, **TensorFlow/Keras**, 
**PyTorch**, **MXNet**, and **CNTK**.

#### Analogy
```
Consider your house. 

Your house is built on top of a **foundation** (i.e. deep learning 
fundamentals). Without knowing the underlying **fundamentals of deep learning** 
you will struggle to train various types of model.

On top of the foundation of your house is a **frame** (i.e. **deep learning** 
**framework**). The deep learning framework helps you build a deep learning 
model. **The frame includes the wood, screws, nails, and other hardware** 
**required to build your house**. Without the frame, you won’t ever get to 
install a roof. **A deep learning framework is similar to the frame of a house**. 

**The framework allows us to put together a deep learning model, train it, and**
**perform inference**.
```

## What is Caffe?
-  developed by the **Berkeley Vision and Learning Center (BVLC)**
- based around **.prototxt** files, which are essentially plaintext configuration 
files which typically follow a **JSON-like structure**
-  allow researchers and computer vision developers to innovate, freeing them to
**focus on the model architecture itself rather than having to learn how to** 
**operate a given library**
- **extremely fast**

## What is TensorFlow?
- **open-source library to build and deploy highly scalable machine learning**
models by **Google**
- TensorFlow represents an entire ecosystem of different offerings that help 
with efficient data handling, model training, hyperparameter tuning, model 
optimization, and model deployment

## What is TensorFlow’s Relation to Keras?
- a very popular deep learning framework, is built on top of TensorFlow

## What is TensorFlow-Lite?
- "...open-source deep learning framework for on-device inference..."
- can do the heavy-lifting for us to optimize deep learning models for limited-
capability devices including smartphones, smart cameras, Raspberry Pis, Google 
Corals, NVIDIA Jetson Nanos, and more.

## What is TensorFlow Object Detection?
- TensorFlow Object Detection (TFOD) API is built on top of TensorFlow and helps 
us to quickly build and deploy object detection systems
- does not require any coding on your part to train an object detection model, 
rather it is based on configuration files
-  we will supply parameters so that the TFOD API can work with your annotated 
dataset to do the hard work for us

## How to Choose DL suitable Frameworks?
1. Compatibility
2. Documentation

```
TensorFlow/TensorFlow Lite and Caffe play nicely with the tools and libraries 
we will be using, including OpenVINO, TensorRT, and the EdgeTPU Compiler
```

3. Hardware Extensibility

```
In the near future, we think the embedded deep learning community will adopt the
following three frameworks:

• TensorFlow Lite
• OpenVINO
• PyTorch Mobile

Additionally, it’s not just about the library — it’s about the supporting tools 
that facilitate embedded optimization and deployment. TF Lite is (currently) the 
clear winner in that regard.
```

## Which Frameworks Work Best With Which Hardware and Why?
#### Embedded Hardware
1. Raspberry Pi
	1. Caffe, PyTorch, and TensorFlow
	2. Caffe, TensorFlow, and OpenCV’s DNN
	
```
OpenVINO supports optimizing TensorFlow models along with Caffe, MXNet, and PyTorch
(via ONNX). But in our experience, we have found out that the combinations of TensorFlow +
OpenVINO and Caffe + OpenVINO work better than the other combinations. Thus, Tensor-
Flow and Caffe are typically the best options.
```
	
2. Intel Movidius Neural Compute Stick (NCS)
	1. need to use OpenVINO
	2. OpenVINO supports Caffe and TensorFlow models for deployment
	
3. Google Coral Edge Tensor Processing Unit (TPU) USB Accelerator
	1. only supports TensorFlow Lite models as of the writing

4. NVIDIA Jetson Nano
	1. CUDA-capable NVIDIA
	2. supports a variety of frameworks including Caffe, TensorFlow, and PyTorch
	3. to take advantage of TensorRT for optimizing deep learning models for the Jetson
Nano, we will stick with TensorFlow.

