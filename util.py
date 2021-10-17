import os
import random
from azure.storage.blob import BlobServiceClient

# /801/bmshj2018-factorized2/0.png
# {container}/{model}/{img_id}
def retrieve_imgs(base_url=r'https://compressrimages.blob.core.windows.net/'):
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    containers = [x.name for x in blob_service_client.list_containers()]

    ind = random.randrange(len(containers))

    # get a random container
    container_name = containers[ind]
    container_client = blob_service_client.get_container_client(container_name)

    # choose 4 random files
    files = [x.name.split("/") for x in container_client.list_blobs()]
    models = list(set([f[0] for f in files]))  # possible models
    img_id = [f[1] for f in files]  # possible image slices
    img_ind = random.randrange(len(img_id))  # random image to sample

    inds = random.sample([i for i in range(len(models))], k=4)  # get 4 models
    ret_files = [os.path.join(base_url, container_name,
                            models[i], img_id[img_ind]).replace('\\', '/') for i in inds]

    return ret_files
