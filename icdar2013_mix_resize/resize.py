import json
import math
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

with open('/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train.json') as f:
        json_data = json.load(f)

images = json_data["images"]
annotations = json_data["annotations"]

for img in images:
    img_name = img["file_name"]
    img_id = img["id"]
    width = img["width"]
    height = img["height"]

    img1 = Image.open(img_name).resize((300, 300))
    img1.save("/home/ubuntu/EfficientNet/datasets/icdar2013/train_images/ICDAR2013_Train_" + str(img_id+99) + ".jpg")

    img["file_name"] = "/home/ubuntu/EfficientNet/datasets/icdar2013/train_images/ICDAR2013_Train_" + str(img_id+99) + ".jpg"
    img["width"] = 300
    img["height"] = 300
    datasets["images"].append(img)

    for data in annotations:
        if data["image_id"] == img_id:
            for i in range(len(data["bbox"])):
                if i%2 == 0:
                    data["bbox"][i] = int(math.ceil(data["bbox"][i] * 300 / width))
                else:
                    data["bbox"][i] = int(math.ceil(data["bbox"][i] * 300 / height))
            
            for j in range(len(data["segmentation"])):
                for k in range(len(data["segmentation"][j])):
                    if k%2 == 0:
                        data["segmentation"][j][k] = int(math.ceil(data["segmentation"][j][k] * 300 / width))
                    else:
                        data["segmentation"][j][k] = int(math.ceil(data["segmentation"][j][k] * 300 / height))
            
            data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))

            datasets["annotations"].append(data)

with open("/home/ubuntu/EfficientNet/datasets/icdar2013/train_pretty.json", 'w') as outfile:
    json.dump(datasets, outfile, indent=4)

with open("/home/ubuntu/EfficientNet/datasets/icdar2013/train.json", 'w') as outfile:
    json.dump(datasets, outfile)