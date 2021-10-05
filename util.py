import os
import random
from azure.storage.blob import BlobServiceClient


def retrieve_imgs(base_url=r'https://compressrimages.blob.core.windows.net/'):
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    containers = [x.name for x in blob_service_client.list_containers()]
    
    ind = random.randrange(len(containers))

    # get a random container
    container_name = containers[ind]
    container_client = blob_service_client.get_container_client(container_name)

    # choose 4 random files
    files = [x.name for x in container_client.list_blobs()]
    inds = random.sample([i for i in range(len(files))], k=4)
    ret_files = [os.path.join(base_url, container_name,
                            files[i]).replace('\\', '/') for i in inds]
    
    return ret_files
