import numpy as np
import tensorflow as tf
# from watnet.geotif_io import readTiff, writeTiff
import matplotlib.pyplot as plt
from WaterMap.watnet.imgPatch import imgPatch
import gdown
import os
import tifffile as tiff
from PIL import Image


class WatNet:
    def __init__(self):
        model_dir = 'model/watnet'
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        if not os.path.exists(model_dir + '/watnet.h5'):
            model_name = 'watnet'
            out_path = 'model/watnet/watnet.h5'
            self.fetch_pretrained_models(model_name=model_name, out_path=out_path)
        self.load_path = model_dir + '/watnet.h5'
        self.model = tf.keras.models.load_model(self.load_path, compile=False)

#  Fetch pretrained model weights
    def fetch_pretrained_models(self, model_name, out_path):
        if model_name == 'watnet':
            url = 'https://drive.google.com/uc?export=download&id=1A-BDt1JGqSirKcr9KAigxSdu_BwEwPf7'
            gdown.download(url, out_path, quiet=False)

#   Input image array(normalized)/ Output water_map array
    def infer(self, rsimg, threshold):
        imgPatch_ins = imgPatch(rsimg, patch_size=512, edge_overlay=80)
        patch_list, start_list, img_patch_row, img_patch_col = imgPatch_ins.toPatch()
        result_patch_list = [self.model(patch[np.newaxis, :]) for patch in patch_list]
        result_patch_list = [np.squeeze(patch, axis=0) for patch in result_patch_list]
        pro_map = imgPatch_ins.toImage(result_patch_list, img_patch_row, img_patch_col)
        water_map = np.where(pro_map > threshold, 1, 0)
        return water_map, pro_map


#   Input img_path, out_png and Output water_map array and image(png or tiff)
    def predict(self, img_path, out_png_path="", out_tif_path="", threshold=0.5):
        print("WatNet model is predicting on img {} threshold {}.".format(img_path, threshold))
        sen2_img = tiff.imread(img_path)
        sen2_img = np.float32(np.clip(sen2_img / 10000, a_min=0, a_max=1))
        water_map, pro_map = self.infer(rsimg=sen2_img, threshold=threshold)
        water_map = np.squeeze(water_map)
        water_map = 1. / (1 + np.exp(-(16 * (water_map - 0.5))))
        water_map = np.clip(water_map, 0, 1)
        # rgb_image = water_map.convert('RGB')
        if out_png_path != "":
            plt.imsave(out_png_path, water_map, format='png', cmap='gray')
        if out_tif_path != "":
            tiff.imsave(out_tif_path, data=water_map)
        return np.squeeze(pro_map)
