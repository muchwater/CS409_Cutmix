import json
import random
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

def cut_generator(idx):
    global image_id

    image_root = "/home/ubuntu/TextFuseNet/datasets/icdar2013/train_images/ICDAR2013_Train_"
    rand_ind = 99 + idx     
    # rand_ind = random.randint(100, 328)
    rand_ind2 = random.randint(100, 328)
    # rand_ind2 = 240
    image_name1 = image_root + str(rand_ind) + ".jpg"
    image_name2 = image_root + str(rand_ind2) + ".jpg"
    img1 = Image.open(image_name1)
    W1, H1 = img1.size
    img2 = Image.open(image_name2)
    W2, H2 = img2.size
    size = [W1, H1, W2, H2]

    bbx1 = 0
    bbx2 = 0
    bby1 = 0
    bby2 = 0

    with open('/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train_test.json') as f:
        bbox_data = json.load(f)
    
    initial = bbox_data["annotations"]
    for data in initial:
        if data["image_id"] == image_id:
            bbx2 = int(data["bbox"][0])
            bby2 = int(data["bbox"][1])
            break
    # bbx1, bbx2, bby1, bby2 = min(bbx1, bbx2), max(bbx1, bbx2), min(bby1, bby2), max(bby1, bby2)

    crop_img_idx = rand_ind2 - 99
    for data in initial:
        if data["image_id"] == crop_img_idx:
            cropx1 = int(data["bbox"][0])  
            cropy1 = int(data["bbox"][1])
            break
    
    cropx2 = int(cropx1 + bbx2)
    cropy2 = int(cropy1 + bby2)
    paste_img = img2.crop((cropx1, cropy1, cropx2, cropy2))
    new_img = Image.new("RGB", (W1, H1))
    new_img.paste(img1, (0, 0))
    new_img.paste(paste_img, (bbx1, bby1))

    new_img.save("/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train_images/ICDAR2013_Train_" + str(idx+99) + ".jpg")
    return rand_ind2, int(bbx1), int(bby1), int(bbx2), int(bby2), size, int(cropx1), int(cropy1)

text_id = 1
image_id = 1

def image_dict(idx, size):
    global image_id
    path = "/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train_images/ICDAR2013_Train_" + str(99+idx) + ".jpg"
    h = size[1]
    w = size[0]

    image = {}
    image["file_name"] = path
    image["height"] = h
    image["width"] = w
    image["id"] = idx
    return image

# def overwrap_check(bbox, data, rate):
    global image_id
    global text_id

    bbx1 = bbox[0]
    bby1 = bbox[1]
    bbx2 = bbox[2]
    bby2 = bbox[3]

    bbx1_i = int(math.ceil(data["bbox"][0] * 300 / rate[0]))
    bby1_i = int(math.ceil(data["bbox"][1] * 300 / rate[1]))
    bbx2_i = int(math.ceil(data["bbox"][2] * 300 / rate[0]))
    bby2_i = int(math.ceil(data["bbox"][3] * 300 / rate[1]))

    case = 0
    # x 좌표 먼저 확인
    if bbx1 < bbx1_i:
        if bbx2 < bbx1_i:
            # case 0
            x1 = bbx1_i
            x2 = bbx2_i
        elif bbx2 < bbx2_i:
            x1 = bbx2
            x2 = bbx2_i
        else:
            # case 0
            x1 = bbx1_i
            x2 = bbx2_i
    elif bbx1 < bbx2_i:
        if bbx2 <= bbx2_i:
            x1 = bbx1_i
            x2 = bbx1
            # case 1
            xx1 = bbx2
            xx2 = bbx2_i
        else:
            x1 = bbx1_i
            x2 = bbx1
    else:
        # case 0
        x1 = bbx1_i
        x2 = bbx2_i

    # y 좌표 확인후 JSON 파일 추가 or 무시
    if bby1 < bby1_i:
        if bby2 < bby1_i:
            # case 0
            y1 = bby1_i
            y2 = bby2_i
        elif bby2 < bby2_i:
            y1 = bby2
            y2 = bby2_i
        else:
            y1 = bby1_i
            y2 = bby2_i
    elif bby1 < bby2_i:
        if bby2 < bby2_i:
            y1 = bby1_i
            y2 = bby1
            # case 2
            yy1 = bby2
            yy2 = bby2_i
        else:
            y1 = bby1_i
            y2 = bby1
    else:
        y1 = bby1_i
        y2 = bby2_i
    
    text = {}
    text["bbox"] = [x1, y1, x2, y2]
    text["category_id"] = 1
    text["id"] = text_id
    text_id += 1
    text["image_id"] = image_id
    text["iscrowd"] = 0
    text["segmentation"]= [000]
    text["area"] = float((x2-x1)*(y2-y1))
    return text

def crop_img_text(idx, bbox, crop, json_data):
    global image_id
    global text_id
    initial = json_data["annotations"]
    img2_id = idx - 99
    for data in initial:
        if data["image_id"] == img2_id:
            data["bbox"] = list(map(int, data["bbox"]))                                     
            if data["bbox"][0] >= crop[0] and data["bbox"][2] <= (crop[0] + bbox[2]):
                if data["bbox"][1] >= crop[1] and data["bbox"][3] <= (crop[1] + bbox[3]):   
                    for i in range(len(data["bbox"])):                                      
                        if i%2 == 0:
                            data["bbox"][i] -= min(cropx1, data["bbox"][i])
                        else:
                            data["bbox"][i] -= min(cropy1, data["bbox"][i])
                    for j in range(len(data["segmentation"])):
                        for k in range(len(data["segmentation"][j])):
                            if k%2 == 0:
                                data["segmentation"][j][k] -= min(cropx1, data["segmentation"][j][k])
                            else:
                                data["segmentation"][j][k] -= min(cropy1, data["segmentation"][j][k])
                    data["image_id"] = image_id
                    data["id"] = text_id
                    text_id += 1
                    data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                    datasets["annotations"].append(data)
                else:
                    if data["category_id"] == 1 and data["bbox"][1] <= (crop[1] + bbox[3]) and bbox[2]*bbox[3] >= data["area"] * 0.1:             
                        for i in range(len(data["bbox"])):                                  
                            if i%2 == 0:
                                data["bbox"][i] -= min(cropx1, data["bbox"][i])                                   
                            else:
                                data["bbox"][i] -= min(cropy1, data["bbox"][i])
                        for j in range(len(data["segmentation"])):
                            for k in range(len(data["segmentation"][j])):
                                if k%2 == 0:
                                    data["segmentation"][j][k] -= min(cropx1, data["segmentation"][j][k])
                                else:
                                    data["segmentation"][j][k] -= min(cropy1, data["segmentation"][j][k])
                        data["bbox"][3] = crop[1] + bbox[3]                                 
                        data["image_id"] = image_id
                        data["id"] = text_id
                        text_id += 1
                        data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                        datasets["annotations"].append(data)
                    if data["category_id"] != 1:                                            
                        if (data["bbox"][3] - (crop[1] + bbox[3])) <= (data["bbox"][3]-data["bbox"][1]) * 0.1:
                            for i in range(len(data["bbox"])):                              
                                if i%2 == 0:
                                    data["bbox"][i] -= min(cropx1, data["bbox"][i])
                                else:
                                    data["bbox"][i] -= min(cropy1, data["bbox"][i])
                            for j in range(len(data["segmentation"])):
                                for k in range(len(data["segmentation"][j])):
                                    if k%2 == 0:
                                        data["segmentation"][j][k] -= min(cropx1, data["segmentation"][j][k])
                                    else:
                                        data["segmentation"][j][k] -= min(cropy1, data["segmentation"][j][k])
                            data["bbox"][3] = crop[1] + bbox[3]
                            data["image_id"] = image_id
                            data["id"] = text_id
                            text_id += 1
                            data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                            datasets["annotations"].append(data)

            else:
                if data["bbox"][1] >= crop[1] and data["bbox"][3] <= (crop[1] + bbox[3]):
                    if data["category_id"] == 1 and data["bbox"][0] <= (crop[0] + bbox[2]) and bbox[2]*bbox[3] >= data["area"] * 0.1:             
                        for i in range(len(data["bbox"])):                                  
                            if i%2 == 0:
                                data["bbox"][i] -= min(cropx1, data["bbox"][i])
                            else:
                                data["bbox"][i] -= min(cropy1, data["bbox"][i])
                        for j in range(len(data["segmentation"])):
                            for k in range(len(data["segmentation"][j])):
                                if k%2 == 0:
                                    data["segmentation"][j][k] -= min(cropx1, data["segmentation"][j][k])
                                else:
                                    data["segmentation"][j][k] -= min(cropy1, data["segmentation"][j][k])
                        data["bbox"][2] = crop[0] + bbox[2]                                
                        data["image_id"] = image_id
                        data["id"] = text_id
                        text_id += 1
                        data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                        datasets["annotations"].append(data)
                    if data["category_id"] != 1:                                            
                        if (data["bbox"][2] - (crop[0] + bbox[2])) <= (data["bbox"][2]-data["bbox"][0]) * 0.1:
                            for i in range(len(data["bbox"])):                              
                                if i%2 == 0:
                                    data["bbox"][i] -= min(cropx1, data["bbox"][i])
                                else:
                                    data["bbox"][i] -= min(cropy1, data["bbox"][i])
                            for j in range(len(data["segmentation"])):
                                for k in range(len(data["segmentation"][j])):
                                    if k%2 == 0:
                                        data["segmentation"][j][k] -= min(cropx1, data["segmentation"][j][k])
                                    else:
                                        data["segmentation"][j][k] -= min(cropy1, data["segmentation"][j][k])
                            data["bbox"][2] = crop[0] + bbox[2]
                            data["image_id"] = image_id
                            data["id"] = text_id
                            text_id += 1
                            data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                            datasets["annotations"].append(data)
                else:
                    if data["category_id"] == 1 and data["bbox"][0] <= (crop[0] + bbox[2]) and data["bbox"][1] <= (crop[1] + bbox[3]) and bbox[2]*bbox[3] >= data["area"] * 0.1:             
                        for i in range(len(data["bbox"])):                                 
                            if i%2 == 0:
                                data["bbox"][i] -= min(cropx1, data["bbox"][i])
                            else:
                                data["bbox"][i] -= min(cropy1, data["bbox"][i])
                        for j in range(len(data["segmentation"])):
                            for k in range(len(data["segmentation"][j])):
                                if k%2 == 0:
                                    data["segmentation"][j][k] -= min(cropx1, data["segmentation"][j][k])
                                else:
                                    data["segmentation"][j][k] -= min(cropy1, data["segmentation"][j][k])
                        data["bbox"][2] = crop[0] + bbox[2]                                 
                        data["bbox"][3] = crop[1] + bbox[3]
                        data["image_id"] = image_id
                        data["id"] = text_id
                        text_id += 1
                        data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                        datasets["annotations"].append(data)
                    if data["category_id"] != 1:                                            
                        if (data["bbox"][2] - (crop[0] + bbox[2])) <= (data["bbox"][2]-data["bbox"][0]) * 0.1:
                            if (data["bbox"][3] - (crop[1] + bbox[3])) <= (data["bbox"][3]-data["bbox"][1]) * 0.1:
                                for i in range(len(data["bbox"])):                          
                                    if i%2 == 0:
                                        data["bbox"][i] -= min(cropx1, data["bbox"][i])
                                    else:
                                        data["bbox"][i] -= min(cropy1, data["bbox"][i])
                                for j in range(len(data["segmentation"])):
                                    for k in range(len(data["segmentation"][j])):
                                        if k%2 == 0:
                                            data["segmentation"][j][k] -= min(cropx1, data["segmentation"][j][k])
                                        else:
                                            data["segmentation"][j][k] -= min(cropy1, data["segmentation"][j][k])
                                data["bbox"][2] = crop[0] + bbox[2]
                                data["bbox"][3] = crop[1] + bbox[3]
                                data["image_id"] = image_id
                                data["id"] = text_id
                                text_id += 1
                                data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                                datasets["annotations"].append(data)
                    

        elif data["image_id"] > img2_id:
            break
        else:
            continue

def annotation(idx, bbx1, bby1, bbx2, bby2, cropx1, cropy1):
    global image_id
    global text_id
    bbox = [bbx1, bby1, bbx2, bby2]
    crop = [cropx1, cropy1]
    with open('/home/ubuntu/TextFuseNet/datasets/icdar2013/train.json') as f:
        json_data = json.load(f)

    initial = json_data["annotations"]
    for data in initial:
        if data["image_id"] == image_id:
            data["bbox"] = list(map(int, data["bbox"]))
            data["id"] = text_id
            text_id += 1
            datasets["annotations"].append(data)
        elif data["image_id"] > image_id:
            break
        else:
            continue
    crop_img_text(idx, bbox, crop, json_data)



for i in range(5):
    idx, bbx1, bby1, bbx2, bby2, size, cropx1, cropy1 = cut_generator(image_id)
    print("mixed image's index: " + str(idx))
    img = image_dict(image_id, size)
    datasets["images"].append(img)
    annotation(idx, bbx1, bby1, bbx2, bby2, cropx1, cropy1)
    image_id += 1

with open("/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train_pretty.json", 'w') as outfile:
    json.dump(datasets, outfile, indent=4)

with open("/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train.json", 'w') as outfile:
    json.dump(datasets, outfile)