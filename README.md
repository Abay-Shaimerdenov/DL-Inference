# DL-Inference
This is a replication project. The paper can be found [here](https://arxiv.org/pdf/1805.04252.pdf). The original source code can be found [here](https://zenodo.org/record/1242583#.WvAmFXUvz80).  
## Requirements to run this project
*Python 2 - 3.7*  
*Tensorflow 1.3 - 1.15*  
*MySQL*  
*sklearn, numpy*  
*Pyro4*  
## Setup
Here, the **images** and **model_data** folders should be created.  
Images should be placed inside the **images** folder which should be like this: _images/val/images/ILSVRC2012_val_00000001.JPEG_.  
Image dataset (ImageNet LSVRC 2012) can be downloaded [here](https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5)  
Inside of the **model_data** folder, the nested folder structure is like this: _model_data/tensorflow/checkpoints/inception_v4/inception_v4.cpkt, the same for others dnn models:
/resnet_v1_152/, /mobilenet_v1_1.0_224_/.
Inside these folders, checkpoints should be placed respectively.  
Checkpoints couls be downloaded from [here](https://github.com/tensorflow/models/tree/master/research/slim)  
## Running the project
First, the Database Tutorial.ipynb file should be run, and then the CSV Tutorial.ipynb file. After the CSV file is generated (it is provided here, but only with 15k entries), Testing the premodel.ipynb file should be run.
