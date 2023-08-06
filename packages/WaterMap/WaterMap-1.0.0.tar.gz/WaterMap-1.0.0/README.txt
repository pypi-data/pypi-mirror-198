# WaterMap Library

### Watnet and DeepWaterMap Method for Water Detection in Satellite Imagery.

This library contains Watnet and DeepWaterMap methods for the detction of surface water in satellite imagery.

## Input Image:

Input image should be a six band tif image containing the following bands: red, green, blue, near infrared, shortwave infrared 1 and shortwave infrared 2 (the band number of 2, 3, 4, 8, 11, and 12 of sentinel-2 image).

## How to use this library:

### --Step 1

Enter the following commands for installing the library, and then configure the python and deep learning environment.
The deep learning software used in this repo is Tensorflow 2.
  ~~~console
  pip install WaterMap
  ~~~

### -- Step 2

- Output in array form:
In the pytest.py file provide the input image path and run the file to get ouptut in array form array
- Output in png form:
In the pytest.py file provide input to the "out_png_path" to store the output path to a particular path.
- Output in tif form:
In the pytest.py file provide input to the "out_tif_path" to store the output path to a particular path.
- All the output can also be achieved simultaneously by providing both the png and tif output path.
- Example Code for watnet method:
~~~console
  wn.predict(img_path, out_png_path='sample_images/dwm_coastal1.png')
~~~
- Example Code for deepwatermap method:
~~~console
 dwm.predict(img_path, out_png_path='sample_images/dwm_coastal1.png')
~~~

## Thresholding Option:

There is also a option to provide the threshold to both th methods as an input:

- Example Code for deepwatermap method:
- default threshold for watnet is 0.5 and for deepwatermap is 0.35
~~~console
 dwm.predict(img_path, out_png_path='sample_images/dwm_coastal1.png',threshold='0.5')
~~~

### Downloading the Image from Google Earth Engine on Google Drive
- On google earth engine open code editor.
- Select the area of interest from the map and run the following code:
~~~console
var data = ee.ImageCollection("COPERNICUS/S2_SR")
var image= data.filterDate('2022-07-22','2022-07-23')
var dataset = image.filterBounds(aoi).select(['B2', 'B3', 'B4','B8', 'B11', 'B12']);
print(dataset);
Map.addLayer(dataset);
Export.image.toDrive({
  image:dataset.mosaic(),
  description:'sentinel',
  scale:10,
  region:aoi,
})
~~~
- Run the above code and select the task option on the left hand side.
- There a run option will popup. Click on it.
- An pop window will be open afterwards asking the folder details to save the image and the file format.
- Select the file format as tif
- A six band tif image will now be downloaded in google drive.
