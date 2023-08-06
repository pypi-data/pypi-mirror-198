import pandas as pd
import os
if __name__ == "__main__":

    # from tsfresh.examples.robot_execution_failures import download_robot_execution_failures, \
    #     load_robot_execution_failures
    # download_robot_execution_failures()
    # timeseries, y = load_robot_execution_failures()
    # timeseries = pd.read_csv("/Users/john/dataset0.4.2/radiomics-features-data-VIDEO/all/dataset/230.csv")
    # timeseries["id"] = 0

    all_path = "/Users/john/all.csv"
    root = "/Users/john/dataset0.4.2/radiomics-features-data-VIDEO/traintest/test/"
    df = pd.read_csv("/Users/john/dataset0.4.2/radiomics-features-data-VIDEO/traintest/test/labels.csv")
    labels = df["label"]
    data_paths = df["data_path"]
    for data_path, y in zip(data_paths, labels):
        path = os.path.join(root, data_path)
        ddf = pd.read_csv(path)
        ddf["id"] = data_path.replace(".csv", "")
        ddf.to_csv(all_path, mode="a", index=False, header=not os.path.exists(all_path))
    # exit()
    #
    timeseries = pd.read_csv(all_path)
    print(timeseries.head())
    print("unique(id) = ", len(timeseries["id"].unique()))

    # import matplotlib.pyplot as plt
    # timeseries[timeseries['id'] == 3].plot(subplots=True, sharex=True, figsize=(10,10))
    # plt.show()

    print("shape-1 = ", timeseries.shape)

    from tsfresh import extract_features
    extracted_features = extract_features(timeseries, column_id="id", n_jobs=4, chunksize=10)
    print("shape0 = ", extracted_features.shape)
    extracted_features.to_csv("extracted_features.csv", index=False)

    from tsfresh import select_features
    from tsfresh.utilities.dataframe_functions import impute

    impute(extracted_features)
    features_filtered = select_features(extracted_features, labels)
    print("shape0 = ", extracted_features.shape)

    features_filtered.to_csv("features_filtered.csv", index=False)






