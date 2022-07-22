import json

with open('custom_config.json', 'r+') as file:
    custom_config = json.loads(file.read())
if custom_config['environment'] == 'kaggle':
    base_path = "/kaggle/working/"
    if custom_config["dataset"] == "loveda":
        data_root = "/kaggle/input/loveda-makan/data/"
    elif custom_config["dataset"] == "vaihingen":
        data_root = "/kaggle/input/vaihingenmakan/"

elif custom_config['environment'] == 'colab':
    base_path = "/content/drive/MyDrive/segmentation/" 
    data_root = "/content/drive/MyDrive/segmentation/"
else:
    base_path = ""
    data_root = ""