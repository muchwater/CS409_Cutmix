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
    if rand_ind == rand_ind2: 
        if rand_ind2 < 328:
            rand_ind2 += 1
        else:
            rand_ind2 = random.randint(100, 327)
            
    image_name1 = image_root + str(rand_ind) + ".jpg"
    image_name2 = image_root + str(rand_ind2) + ".jpg"
    img1 = Image.open(image_name1)
    W1, H1 = img1.size
    img2 = Image.open(image_name2)
    W2, H2 = img2.size
    size = [W1, H1, W2, H2]

    xlist = []
    ylist = []

    with open('/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train_test.json') as f:
        bbox_data = json.load(f)
    initial = bbox_data["annotations"]
    
    for data in initial:
        if data["image_id"] == image_id:
            xlist.append(data["bbox"][0])
            xlist.append(data["bbox"][2])
            ylist.append(data["bbox"][1])
            ylist.append(data["bbox"][3])
        elif data["image_id"] > image_id:
            break

    min_x = min(xlist)
    max_x = max(xlist)
    min_y = min(ylist)
    max_y = max(ylist)

    case = random.randint(1, 4)
    if case == 1:
        bbx1 = random.randint(0, min_x//3)
        bby1 = random.randint(0, H1//2)
        bbx2 = random.randint(2*min_x//3, min_x)
        bby2 = random.randint(H1//2, H1)
    elif case == 2:
        bbx1 = random.randint(0, W1//2)
        bby1 = random.randint(0, min_y//3)
        bbx2 = random.randint(W1//2, W1)
        bby2 = random.randint(2*min_y//3, min_y)
    elif case == 3:
        bbx1 = random.randint(max_x, max_x + (W1-max_x)//3)
        bby1 = random.randint(0, H1//2)
        bbx2 = random.randint(max_x + 2*(W1-max_x)//3, W1)
        bby2 = random.randint(H1//2, H1)
    else:
        bbx1 = random.randint(0, W1//2)
        bby1 = random.randint(max_y, max_y + (H1-max_y)//3)
        bbx2 = random.randint(W1//2, W1)
        bby2 = random.randint(max_y + 2*(H1-max_y)//3, H1)
    bbx1, bby1, bbx2, bby2 = min(bbx1, bbx2), min(bby1, bby2), max(bbx1, bbx2), max(bby1, bby2)

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

def translation (bbox, crop, target):
    width = bbox[0] - crop[0]
    heigh = bbox[1] - crop[1]

    for i in range(len(target)):
        if i%2 == 0:
            target[i] += width
        else:
            target[i] += heigh
    return target

def crop_img_text(idx, bbox, crop, json_data):
    global image_id
    global text_id
    initial = json_data["annotations"]
    img2_id = idx - 99
    for data in initial:
        if data["image_id"] == img2_id:
            data["bbox"] = list(map(int, data["bbox"]))
            for i in range(len(data["segmentation"])):
                data["segmentation"][i] = list(map(int, data["segmentation"][i]))
                                     
            if data["bbox"][0] >= crop[0] and data["bbox"][2] <= (crop[0] + (bbox[2]-bbox[0])):         
                if data["bbox"][1] >= crop[1] and data["bbox"][3] <= (crop[1] + (bbox[3]-bbox[1])):     # case 0
                    data["bbox"] = translation(bbox, crop, data["bbox"])
                    for i in range(len(data["segmentation"])):
                        data["segmentation"][i] = translation(bbox, crop, data["segmentation"][i])

                    data["image_id"] = image_id
                    data["id"] = text_id
                    text_id += 1
                    data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                    datasets["annotations"].append(data)
                else:
                    if data["category_id"] == 1 and bbox[2]*bbox[3] >= data["area"] * 0.1: # case 1 #data["bbox"][1] <= (crop[1] + bbox[3]) and 
                        if data["bbox"][1] < crop[1]:
                            data["bbox"][1] = crop[1]
                            if data["bbox"][3] <= crop[1]:
                                continue
                            elif data["bbox"][3] > (crop[1] + (bbox[3]-bbox[1])):
                                data["bbox"][3] = (crop[1] + (bbox[3]-bbox[1]))
                        elif data["bbox"][1] < (crop[1] + (bbox[3]-bbox[1])):
                            if data["bbox"][3] > (crop[1] + (bbox[3]-bbox[1])):
                                data["bbox"][3] = (crop[1] + (bbox[3]-bbox[1]))
                        else:
                            continue

                        data["bbox"] = translation(bbox, crop, data["bbox"])
                        for i in range(len(data["segmentation"])):
                            data["segmentation"][i] = translation(bbox, crop, data["segmentation"][i])
                            
                        data["image_id"] = image_id
                        data["id"] = text_id
                        text_id += 1
                        data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                        datasets["annotations"].append(data)
                    
                    if data["category_id"] != 1:
                        if data["bbox"][1] < crop[1]:
                            if (crop[1] - data["bbox"][1]) <= ((data["bbox"][3] - data["bbox"][1]) * 0.15):
                                data["bbox"][1] = crop[1]
                                if data["bbox"][3] > (crop[1] + bbox[3] - bbox[1]):
                                    data["bbox"][3] = (crop[1] + bbox[3] - bbox[1])
                            else:
                                continue
                        elif data["bbox"][1] < (crop[1] + bbox[3] - bbox[1]):
                            if (data["bbox"][3] - (crop[1] + bbox[3] - bbox[1])) <= ((data["bbox"][3]-data["bbox"][1]) * 0.15):
                                data["bbox"][3] = (crop[1] + bbox[3] - bbox[1])
                            else:
                                continue
                        else:
                            continue

                        data["bbox"] = translation(bbox, crop, data["bbox"])
                        for i in range(len(data["segmentation"])):
                            data["segmentation"][i] = translation(bbox, crop, data["segmentation"][i])

                        data["image_id"] = image_id
                        data["id"] = text_id
                        text_id += 1
                        data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                        datasets["annotations"].append(data)

            else:
                if data["bbox"][1] >= crop[1] and data["bbox"][3] <= (crop[1] + bbox[3]): 
                    if data["category_id"] == 1 and bbox[2]*bbox[3] >= data["area"] * 0.1:    # case 2         #and data["bbox"][0] <= (crop[0] + bbox[2]) 
                        if data["bbox"][0] < crop[0]:
                            data["bbox"][0] = crop[0]
                            if data["bbox"][2] <= crop[0]:
                                continue
                            elif data["bbox"][2] > (crop[0] + (bbox[2]-bbox[0])):
                                data["bbox"][2] = (crop[0] + (bbox[2]-bbox[0]))
                        elif data["bbox"][0] < (crop[0] + (bbox[2]-bbox[0])):
                            if data["bbox"][2] > (crop[0] + (bbox[2]-bbox[0])):
                                data["bbox"][2] = (crop[0] + (bbox[2]-bbox[0]))
                        else:
                            continue
                        
                        data["bbox"] = translation(bbox, crop, data["bbox"])
                        for i in range(len(data["segmentation"])):
                            data["segmentation"][i] = translation(bbox, crop, data["segmentation"][i])
                                                        
                        data["image_id"] = image_id
                        data["id"] = text_id
                        text_id += 1
                        data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                        datasets["annotations"].append(data)

                    if data["category_id"] != 1:
                        if data["bbox"][0] < crop[0]:
                            if crop[0] - data["bbox"][0] <= ((data["bbox"][2] - data["bbox"][0]) * 0.15):
                                data["bbox"][0] = crop[0]
                                if data["bbox"][2] > (crop[0] + bbox[2] - bbox[0]):
                                    data["bbox"][2] = (crop[0] + bbox[2] - bbox[0])
                            else:
                                continue
                        elif data["bbox"][0] < (crop[0] + bbox[2] - bbox[0]):
                            if (data["bbox"][2] - (crop[0] + bbox[2] - bbox[0])) <= ((data["bbox"][2] - data["bbox"][0]) * 0.15):
                                data["bbox"][2] = (crop[0] + bbox[2] - bbox[0])
                            else:
                                continue
                        else:
                            continue

                        data["bbox"] = translation(bbox, crop, data["bbox"])
                        for i in range(len(data["segmentation"])):
                            data["segmentation"][i] = translation(bbox, crop, data["segmentation"][i])

                        data["image_id"] = image_id
                        data["id"] = text_id
                        text_id += 1
                        data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                        datasets["annotations"].append(data)
                
                else:
                    if data["category_id"] == 1 and bbox[2]*bbox[3] >= data["area"] * 0.1: # case 3
                        if data["bbox"][0] < crop[0]:
                            data["bbox"][0] = crop[0]
                            if data["bbox"][2] < crop[0]:
                                continue
                            elif data["bbox"][2] > (crop[0] + (bbox[2]-bbox[0])):
                                data["bbox"][2] = (crop[0] + (bbox[2]-bbox[0]))
                            
                            if data["bbox"][1] < crop[1]:           
                                data["bbox"][1] = crop[1]
                                if data["bbox"][3] <= crop[1]:
                                    continue
                                elif data["bbox"][3] > (crop[1] + (bbox[3]-bbox[1])):
                                    data["bbox"][3] = (crop[1] + (bbox[3]-bbox[1]))
                            elif data["bbox"][1] < (crop[1] + (bbox[3]-bbox[1])):
                                if data["bbox"][3] > (crop[1] + (bbox[3]-bbox[1])):
                                    data["bbox"][3] = (crop[1] + (bbox[3]-bbox[1]))
                            else:
                                continue
                        elif data["bbox"][0] < (crop[0] + (bbox[2]-bbox[0])):
                            if data["bbox"][2] > (crop[0] + (bbox[2]-bbox[0])):
                                data["bbox"][2] = (crop[0] + (bbox[2]-bbox[0]))
                            
                            if data["bbox"][1] < crop[1]:
                                data["bbox"][1] = crop[1]
                                if data["bbox"][3] <= crop[1]:
                                    continue
                                elif data["bbox"][3] > (crop[1] + (bbox[3]-bbox[1])):
                                    data["bbox"][3] = (crop[1] + (bbox[3]-bbox[1]))
                            elif data["bbox"][1] < (crop[1] + (bbox[3]-bbox[1])):
                                if data["bbox"][3] > (crop[1] + (bbox[3]-bbox[1])):
                                    data["bbox"][3] = (crop[1] + (bbox[3]-bbox[1]))
                            else:
                                continue

                        else:
                            continue
                        
                        data["bbox"] = translation(bbox, crop, data["bbox"])
                        for i in range(len(data["segmentation"])):
                            data["segmentation"][i] = translation(bbox, crop, data["segmentation"][i])

                        data["image_id"] = image_id
                        data["id"] = text_id
                        text_id += 1
                        data["area"] = float((data["bbox"][2]-data["bbox"][0]) * (data["bbox"][3]-data["bbox"][1]))
                        datasets["annotations"].append(data)
                    
                    if data["category_id"] != 1:
                        if data["bbox"][0] < crop[0]:
                            if crop[0] - data["bbox"][0] <= (data["bbox"][2] - data["bbox"][0]) * 0.15:
                                data["bbox"][0] = crop[0]
                                if data["bbox"][2] > (crop[0] + bbox[2] - bbox[0]):
                                    data["bbox"][2] = (crop[0] + bbox[2] - bbox[0])
                                
                                if data["bbox"][1] < crop[1] and (crop[1] - data["bbox"][1]) <= ((data["bbox"][3] - data["bbox"][1]) * 0.15):
                                    data["bbox"][1] = crop[1]
                                    if data["bbox"][3] > (crop[0] + bbox[3] - bbox[1]):
                                        data["bbox"][3] = (crop[0] + bbox[3] - bbox[1])
                                elif data["bbox"][1] < (crop[1] + bbox[3] - bbox[1]) and (data["bbox"][3] - (crop[1] + bbox[3] - bbox[1])) <= (data["bbox"][3] - data["bbox"][1]) * 0.15:
                                    data["bbox"][3] = (crop[1] + bbox[3] - bbox[1])
                                else:
                                    continue
                            else:
                                continue
                        elif data["bbox"][0] < (crop[0] + bbox[2] - bbox[0]):
                            if (data["bbox"][2] - (crop[0] + bbox[2] - bbox[0])) <= ((data["bbox"][2] - data["bbox"][0]) * 0.15):
                                data["bbox"][2] = (crop[0] + bbox[2] - bbox[0])

                                if data["bbox"][1] < crop[1] and (crop[1] - data["bbox"][1]) <= ((data["bbox"][3] - data["bbox"][1]) * 0.15):
                                    data["bbox"][1] = crop[1]
                                    if data["bbox"][3] > (crop[0] + bbox[3] - bbox[1]):
                                        data["bbox"][3] = (crop[0] + bbox[3] - bbox[1])
                                elif data["bbox"][1] < (crop[1] + bbox[3] - bbox[1]) and (data["bbox"][3] - (crop[1] + bbox[3] - bbox[1])) <= (data["bbox"][3] - data["bbox"][1]) * 0.15:
                                    data["bbox"][3] = (crop[1] + bbox[3] - bbox[1])
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue

                        data["bbox"] = translation(bbox, crop, data["bbox"])
                        for i in range(len(data["segmentation"])):
                            data["segmentation"][i] = translation(bbox, crop, data["segmentation"][i])

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
            for i in range(len(data["segmentation"])):
                data["segmentation"][i] = list(map(int, data["segmentation"][i]))

            data["id"] = text_id
            text_id += 1
            datasets["annotations"].append(data)
        elif data["image_id"] > image_id:
            break
        else:
            continue
    crop_img_text(idx, bbox, crop, json_data)



for i in range(10):
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