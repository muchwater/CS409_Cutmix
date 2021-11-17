import json

# with open('/home/ubuntu/TextFuseNet/datasets/icdar2013/train.json') as f:
#     json_data = json.load(f)

# # print(type(json_data))
# # image_name = json_data['images'][0]['file_name']
# # print(image_name)

# initial = json_data["annotations"]
# for data in initial:
#     if data["image_id"] == 1:
#         print("image_id is 1")
#     elif data["image_id"] == 2:
#         continue
#     else:
#         print(data["image_id"])
#         break

# # dict 수정이 기존 파일에 영향을 미치는지 확인 완료!
# with open('/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train.json') as f:
#     json_data = json.load(f)

# datasets = {"images" : [],
#            "annotations": []
#            }

# initial = json_data["annotations"]
# for i in range(5):
#     initial[i]["id"] = initial[i]["id"] + 1
#     datasets["annotations"].append(initial[i])

# with open("/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train_pretty_check.json", 'w') as outfile:
#     json.dump(datasets, outfile, indent=4)

# with open("/home/ubuntu/TextFuseNet/datasets/icdar2013_cutmix/train_check.json", 'w') as outfile:
#     json.dump(datasets, outfile)


if 1 == 1 and 2 == 2 and 3 == 3:
    print("test")