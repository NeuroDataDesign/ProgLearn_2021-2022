# Random Forest Scene Segmentation Papers: Datasets

## Semantic Segmentation of an Image Using Random Forest and Single Histogram Class Model
**Rohan Jingar and Mridul Verma, mentored by Dr. Amitabha Mukarjee**

**April 2012**

- Used Microsoft Research Cambridge (MSRC) dataset for random forest model with goals of image classification, object detection, and image segmentation. 
-  **MSRC Dataset**: https://mldta.com/dataset/msrc-v1/
  -  240 images
  -  9 object classes
  -  Often used for full scene segmentation, often with 50/50 split for training and testing


## Random Forest with Learned Representations for Semantic Segmentation

**Byeongkeun Kang and Truong Q. Nguyen**

**January 2019**

- Made random forest model for scene segmentation and used "road scene dataset" and "indoor scene dataset"
- Road scene dataset source
  - https://arxiv.org/abs/1604.01685
  - Cityscapes dataset: https://paperswithcode.com/dataset/cityscapes
    - Pixel annotations for 30 classes - 8 categories (human, vehicle, construction, objects, nature, sky, void, flat surface)
    - Semantic, instance, dense annotations
    - 5,000 fine annotated; 20,000 coarse annotated images
    - Data from 50 cities
  - **COCO (Microsoft Common Objects in Context)**: https://paperswithcode.com/dataset/cityscapes
    - 328,000 images
    - 2014: 164,000 images already split into training (83,000) + validation (41,000) + test (41,000)
    - 2015: added 40,000 new images
    - 2017: changed split ratio from 83,000 and 41,000 to 118,000 and 5,000  
    - Annotations for objects (80 categories), captions, keypoints (e.g. left eye), stuff image (e.g. grass, sky), dense pose (labeled individuals)
    - More importantly for us perhaps --> panoptic (full scene segmentation, 80 thing categories and 91 stuff categories)
      - thing catgory = bike, elephant, etc. 
      - stuff category = grass, sky, road, etc.
  - CamVid (Cambridge-driving Labeled Video Database): https://paperswithcode.com/dataset/cityscapes
- Indoor scene dataset source
  - https://nyuscholars.nyu.edu/en/publications/indoor-segmentation-and-support-inference-from-rgbd-images
