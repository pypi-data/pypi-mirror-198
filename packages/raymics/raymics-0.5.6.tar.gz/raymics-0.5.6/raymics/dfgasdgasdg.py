from raymics.extract_radiomics_features import extract

dataset_dir = "./raw_data"                       # 原始数据文件夹，需要根据数据集文件夹的实际路径进行修改
result_dir = "./radiomics_feature_data"          # 用来放置特征数据文件夹，根据自己所希望的实际路径进行修改
config_path = "./radiomics.yaml"                 # radiomics配置文件，根据实际文件的路径进行修改

dataset_dir = "/Users/john/dataset0.4.2/original-2D/full/original"                       # 原始数据文件夹，需要根据数据集文件夹的实际路径进行修改
result_dir = "/Users/john/dataset0.4.2/original-2D/full/original-ttt"          # 用来放置特征数据文件夹，根据自己所希望的实际路径进行修改
config_path = "/Users/john/PycharmProjects/raymics-python/raymics/radiomics_settings/radiomics_2d_params.yaml"                 # radiomics配置文件，根据实际文件的路径进行修改

processes = 2
if __name__ == "__main__":
    extract(dataset_dir=dataset_dir, config=config_path, result_dir=result_dir, processes=processes)
