import sys
import json

sys.path.append("..")

def do_convert(uploadImagesModel, img_path, model):
    """
    解析图片特征并入口
    :param uploadImagesModel:
    :param img_path:
    :param model:
    :return:
    """
    try:
        return model.resnet50_extract_feat(img_path)
    except Exception as e:
        raise e
