import json
import random
import numpy as np
from PIL import Image

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

def cut_generator(idx):
    image_root = "/home/ubuntu/TextFuseNet/datasets/icdar2013/train_images/ICDAR2013_Train_"

    # rand_ind = random.randint(100, 328)
    rand_ind = 100 + idx -1
    rand_ind2 = random.randint(100, 328)

    bbx1 = random.randint(0, 130)
    bbx2 = random.randint(170, 300)
    bby1 = random.randint(0, 130)
    bby2 = random.randint(170, 300)
    bbx1, bbx2, bby1, bby2 = min(bbx1, bbx2), max(bbx1, bbx2), min(bby1, bby2), max(bby1, bby2)

    image_name1 = image_root + str(rand_ind) + ".jpg"
    image_name2 = image_root + str(rand_ind2) + ".jpg"

    img1 = Image.open(image_name1).resize((300, 300))
    img2 = Image.open(image_name2).resize((300, 300))
    paste_img = img2.crop((bbx1, bby1, bbx2, bby2))

    new_img = Image.new("RGB", (300, 300))
    new_img.paste(img1, (0, 0))
    new_img.paste(paste_img, (bbx1, bby1))

    new_img.save("/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train_images/ICDAR2013_"  + str(idx+100) + ".jpg")
    return rand_ind2, bbx1, bby1, bbx2, bby2

text_id = 1
image_id = 1

def image_dict(idx):
    global image_id
    path = "/home/ubuntu/TextFuseNet/datasets/icdar2013/train_images/ICDAR2013_Train_" + str(100+idx) + ".jpg"
    h = 300
    w = 300
    image = {}
    image["file_name"] = path
    image["height"] = h
    image["width"] = w
    image["id"] = idx
    image_id += 1
    return image

def annotation(idx, bbx1, bby1, bbx2, bby2):
    global image_id
    global text_id
    with open('/home/ubuntu/TextFuseNet/datasets/icdar2013/train.json') as f:
        json_data = json.load(f)

    initial = json_data["annotations"]
    for data in initial:
        if data["image_id"] == image_id:
            x1 = data["bbox"][0]
            y1 = data["bbox"][1]
            x2 = data["bbox"][2]
            y2 = data["bbox"][3]

            if bbx1 > x1 and bbx1 < x2:
                if bby1 > y1 and bby1 < y2:
                    pass
            text = {}
            text["bbox"] = []
            text["category_id"] = 1
            text["id"] = text_id
            text_id += 1
            text["image_id"] = image_id
            text["iscrowd"] = 0
            text["segmentation"] = []
            # text["area"] = float((x_max-x_min)*(y_max-y_min))

            datasets["annotations"].append(text)

        elif data["image_id"] > image_id:
            break

for i in range(5):
    idx, bbx1, bby1, bbx2, bby2 = cut_generator(image_id)
    img = image_dict(image_id)
    datasets["images"].append(img)

    text = annotation(idx, bbx1, bby1, bbx2, bby2)

with open("/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train_pretty.json", 'w') as outfile:
    json.dump(datasets, outfile, indent=4)

with open("/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train.json", 'w') as outfile:
    json.dump(datasets, outfile)