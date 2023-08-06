from WaterMap.dwm import deepwatermap
import tifffile as tiff
import matplotlib.pyplot as plt
import numpy as np
from WaterMap.dwm import utils
import gdown
import os
import zipfile
import warnings
warnings.filterwarnings('ignore')


class DWM:
    def __init__(self):
        model_dir = 'model/dwm/'
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        if not os.path.exists(model_dir + '/checkpoints/cp.135.ckpt.data-00000-of-00001'):
            model_name = 'dwm'
            self.out_path = model_dir + 'checkpoints.zip'
            self.fetch_pretrained_models(model_name=model_name, out_path=self.out_path)
            with zipfile.ZipFile(self.out_path, 'r') as zip_ref:
                zip_ref.extractall(model_dir)
            os.remove(self.out_path)
        # load the model
        self.model = deepwatermap.model()
        self.model.load_weights(model_dir + 'checkpoints/cp.135.ckpt')

    def fetch_pretrained_models(self, model_name, out_path):
        if model_name == 'dwm':
            url = "https://drive.google.com/uc?export=download&id=1c_rXB8KY_pM1oFdwDs-lguK-TGGu_oUS"
            gdown.download(url, out_path, quiet=False)

    def predict(self, img_path, out_png_path="", out_tif_path="", threshold=0.3):
        print("DWM model is predicting on img {} threshold {}.".format(img_path, threshold))
        # load and preprocess the input image
        image = tiff.imread(img_path)
        pad_r = utils.find_padding(image.shape[0])
        pad_c = utils.find_padding(image.shape[1])
        image = np.pad(image, ((pad_r[0], pad_r[1]), (pad_c[0], pad_c[1]), (0, 0)), 'reflect')
        # solve no-pad index issue after inference
        if pad_r[1] == 0:
            pad_r = (pad_r[0], 1)
        if pad_c[1] == 0:
            pad_c = (pad_c[0], 1)
        image = image.astype(np.float32)
        # remove nans (and infinity) - replace with 0s
        image = np.nan_to_num(image, copy=False, nan=0.0, posinf=0.0, neginf=0.0)
        image = image - np.min(image)
        image = image / np.maximum(np.max(image), 1)
        # run inference
        image = np.expand_dims(image, axis=0)
        dwm = self.model.predict(image)
        dwm = np.squeeze(dwm)
        dwm = dwm[pad_r[0]:-pad_r[1], pad_c[0]:-pad_c[1]]
        # soft threshold
        dwm = 1. / (1 + np.exp(-(16 * (dwm - 0.5))))
        dwm = np.clip(dwm, 0, 1)
        dwm_out = np.where(dwm > threshold, 1, 0)
        # save the output water map
        if out_png_path != "":
            plt.imsave(out_png_path, dwm_out*255, format='png', cmap='gray')
        if out_tif_path != "":
            tiff.imsave(out_tif_path, data=dwm_out)
        return dwm
