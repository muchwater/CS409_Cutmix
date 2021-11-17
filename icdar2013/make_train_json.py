import glob
import os
import cv2
from cv2 import contourArea, data
import numpy as np
from tqdm import tqdm
import json
import sys

datasets = {
        "images" : [],
        "categories" :
        [
        {
            "id" : 1,
            "name" : "text",
            "supercategory" : "text"
        },

        {
            "id" : 2,
            "name" : "0",
            "supercategory" : "text"
        },

        {
            "id" : 3,
            "name" : "1",
            "supercategory" : "text"
        },

        {
            "id" : 4,
            "name" : "2",
            "supercategory" : "text"
        },

        {
            "id" : 5,
            "name" : "3",
            "supercategory" : "text"
        },

        {
            "id" : 6,
            "name" : "4",
            "supercategory" : "text"
        },

        {
            "id" : 7,
            "name" : "5",
            "supercategory" : "text"
        },

        {
            "id" : 8,
            "name" : "6",
            "supercategory" : "text"
        },

        {
            "id" : 9,
            "name" : "7",
            "supercategory" : "text"
        },

        {
            "id" : 10,
            "name" : "8",
            "supercategory" : "text"
        },

        {
            "id" : 11,
            "name" : "9",
            "supercategory" : "text"
        },

        {
            "id" : 12,
            "name" : "A",
            "supercategory" : "text"
        },

        {
            "id" : 13,
            "name" : "B",
            "supercategory" : "text"
        },

        {
            "id" : 14,
            "name" : "C",
            "supercategory" : "text"
        },

        {
            "id" : 15,
            "name" : "D",
            "supercategory" : "text"
        },

        {
            "id" : 16,
            "name" : "E",
            "supercategory" : "text"
        },

        {
            "id" : 17,
            "name" : "F",
            "supercategory" : "text"
        },

        {
            "id" : 18,
            "name" : "G",
            "supercategory" : "text"
        },

        {
            "id" : 19,
            "name" : "H",
            "supercategory" : "text"
        },

        {
            "id" : 20,
            "name" : "I",
            "supercategory" : "text"
        },

        {
            "id" : 21,
            "name" : "J",
            "supercategory" : "text"
        },

        {
            "id" : 22,
            "name" : "K",
            "supercategory" : "text"
        },

        {
            "id" : 23,
            "name" : "L",
            "supercategory" : "text"
        },

        {
            "id" : 24,
            "name" : "M",
            "supercategory" : "text"
        },

        {
            "id" : 25,
            "name" : "N",
            "supercategory" : "text"
        },

        {
            "id" : 26,
            "name" : "O",
            "supercategory" : "text"
        },

        {
            "id" : 27,
            "name" : "P",
            "supercategory" : "text"
        },

        {
            "id" : 28,
            "name" : "Q",
            "supercategory" : "text"
        },

        {
            "id" : 29,
            "name" : "R",
            "supercategory" : "text"
        },

        {
            "id" : 30,
            "name" : "S",
            "supercategory" : "text"
        },

        {
            "id" : 31,
            "name" : "T",
            "supercategory" : "text"
        },

        {
            "id" : 32,
            "name" : "U",
            "supercategory" : "text"
        },

        {
            "id" : 33,
            "name" : "V",
            "supercategory" : "text"
        },

        {
            "id" : 34,
            "name" : "W",
            "supercategory" : "text"
        },

        {
            "id" : 35,
            "name" : "X",
            "supercategory" : "text"
        },

        {
            "id" : 36,
            "name" : "Y",
            "supercategory" : "text"
        },

        {
            "id" : 37,
            "name" : "Z",
            "supercategory" : "text"
        },

        {
            "id" : 38,
            "name" : "a",
            "supercategory" : "text"
        },

        {
            "id" : 39,
            "name" : "b",
            "supercategory" : "text"
        },

        {
            "id" : 40,
            "name" : "c",
            "supercategory" : "text"
        },

        {
            "id" : 41,
            "name" : "d",
            "supercategory" : "text"
        },

        {
            "id" : 42,
            "name" : "e",
            "supercategory" : "text"
        },

        {
            "id" : 43,
            "name" : "f",
            "supercategory" : "text"
        },

        {
            "id" : 44,
            "name" : "g",
            "supercategory" : "text"
        },

        {
            "id" : 45,
            "name" : "h",
            "supercategory" : "text"
        },

        {
            "id" : 46,
            "name" : "i",
            "supercategory" : "text"
        },

        {
            "id" : 47,
            "name" : "j",
            "supercategory" : "text"
        },

        {
            "id" : 48,
            "name" : "k",
            "supercategory" : "text"
        },

        {
            "id" : 49,
            "name" : "l",
            "supercategory" : "text"
        },

        {
            "id" : 50,
            "name" : "m",
            "supercategory" : "text"
        },

        {
            "id" : 51,
            "name" : "n",
            "supercategory" : "text"
        },

        {
            "id" : 52,
            "name" : "o",
            "supercategory" : "text"
        },

        {
            "id" : 53,
            "name" : "p",
            "supercategory" : "text"
        },

        {
            "id" : 54,
            "name" : "q",
            "supercategory" : "text"
        },

        {
            "id" : 55,
            "name" : "r",
            "supercategory" : "text"
        },

        {
            "id" : 56,
            "name" : "s",
            "supercategory" : "text"
        },

        {
            "id" : 57,
            "name" : "t",
            "supercategory" : "text"
        },

        {
            "id" : 58,
            "name" : "u",
            "supercategory" : "text"
        },

        {
            "id" : 59,
            "name" : "v",
            "supercategory" : "text"
        },

        {
            "id" : 60,
            "name" : "w",
            "supercategory" : "text"
        },

        {
            "id" : 61,
            "name" : "x",
            "supercategory" : "text"
        },

        {
            "id" : 62,
            "name" : "y",
            "supercategory" : "text"
        },

        {
            "id" : 63,
            "name" : "z",
            "supercategory" : "text"
        }
    ],
    "annotations":[]
}

categories = {'w': 60, '8': 10, 'z': 63, 'T': 31, 'Z': 37, 'J': 21, '6': 8, 'K': 22, 'L': 23, 'text': 1, 'H': 19, '9': 11, '5': 7, 'f': 43, 'u': 58, '0': 2, 'p': 53, 'j': 47, 'x': 61, 'y': 62, 'q': 54, 'D': 15, 'G': 18, '7': 9, 'P': 27, 'm': 50, 'Y': 36, 'o': 52, 'e': 42, 't': 57, 'E': 16, 'a': 38, 'c': 40, 'k': 48, 'O': 26, 'r': 55, '4': 6, 'n': 51, 'U': 32, 'Q': 28, 'h': 45, 'S': 30, 'l': 49, 'g': 44, 'R': 29, 'I': 20, 'B': 13, '3': 5, 'W': 34, 'X': 35, 'C': 14, 'v': 59, 'd': 41, 'b': 39, 'F': 17, 'i': 46, '1': 3, 'N': 25, 'V': 33, 'M': 24, '2': 4, 'A': 12, 's': 56}

text_id = 1
image_id = 1
def text_dict(x_min, y_min, x_max, y_max, image_id):
    global text_id
    text = {}
    text["bbox"] = [x_min, y_min, x_max, y_max]
    text["category_id"] = 1
    text["id"] = text_id
    text_id += 1
    text["image_id"] = image_id
    text["iscrowd"] = 0
    text["segmentation"] = [[x_min, y_min, x_max, y_min, x_max, y_max, x_min, y_max]]
    text["area"] = float((x_max-x_min)*(y_max-y_min))
    return text

def image_dict(path):
    global image_id
    img = cv2.imread(path)
    h,w,_ = img.shape
    image = {}
    image["file_name"] = path
    image["height"] = h
    image["width"] = w
    image["id"] = image_id
    image_id += 1
    return image

def segmentation_dict(gt, gt_img, image_id):
    global text_id
    seg = {}
    seg["bbox"] = [gt["left"],gt["top"], gt["right"],gt["bottom"]]
    seg["category_id"] = categories[gt["label"]]
    seg["id"] = text_id
    text_id += 1
    seg["image_id"] = image_id
    seg["iscrowd"] = 0

    #segmentation
    img = gt_img.copy()
    idx = np.any(img!=(gt["B"],gt["G"],gt["R"]), axis=-1)
    img[idx] = [255,255,255]
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image, 254, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    segmentation = []

    for contour in contours:
        segmentation.append(contour.reshape((-1,)).astype('float').tolist())
    seg["segmentation"] = segmentation

    # area
    area = 0.0
    if(len(hierarchy)>1):
        print(hierachy)
        print(image_id)
    for i,(_, _, _, outside) in enumerate(hierarchy[0]):
        contour_area = cv2.contourArea(contours[i])
        if outside == -1: # outline
            area += contour_area
        else: # inline
            area -= contour_area
    if(area<0):
        print(area)
        print(image_id)
    seg["area"] = area
    return seg

for gt_path in tqdm(sorted(glob.glob("./Task1_GT/*"))):
    idx = os.path.basename(gt_path)[3:].split('.')[0]
    img_path = "/home/ubuntu/TextFuseNet/datasets/icdar2013/train_images/ICDAR2013_Train_"+idx+".jpg"
    gt_img_path = "/home/ubuntu/TextFuseNet/datasets/icdar2013/Challenge2_Training_Task2_GT/"+idx+"_GT.bmp"
    gt_seg_path = "/home/ubuntu/TextFuseNet/datasets/icdar2013/Challenge2_Training_Task2_GT/"+idx+"_GT.txt"

    img = image_dict(img_path)
    gt_img = cv2.imread(gt_img_path)
    datasets["images"].append(img)

    with open(gt_path,'r') as f:
        for line in f:
            line = line.strip().split()
            if len(line) < 5:
                continue
            line = [float(x) for x in line[:4]]
            text = text_dict(*line, img["id"])
            datasets["annotations"].append(text)

    with open(gt_seg_path,'r') as f:
        for line in f:
            line = line.strip().split()
            if len(line) < 10:
                continue
            if line[0].startswith("#"):
                continue
            gt = {"R":int(line[0]),"G":int(line[1]),"B":int(line[2]),"Cx":int(line[3]),"Cy":int(line[4]),
                    "left":int(line[5]),"top":int(line[6]),"right":int(line[7]),"bottom":int(line[8]),
                    "label":line[9][1:-1],}
            if gt["label"] not in categories:
                continue
            seg = segmentation_dict(gt, gt_img, img["id"])
            datasets["annotations"].append(seg)

with open("./train_pretty.json", 'w') as outfile:
    json.dump(datasets, outfile, indent=4)

with open("./train.json", 'w') as outfile:
    json.dump(datasets, outfile)
