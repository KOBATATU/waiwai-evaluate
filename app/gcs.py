import os
from google.cloud import storage
from google.auth.exceptions import DefaultCredentialsError
import pandas as pd

def getGcsBucket():
    BUCKET = os.getenv("GCS_BUCKET", "bucket")
    return BUCKET

def get_file_from_gcs(bucket_name: str, object_path: str):

    try:
        client = storage.Client()
        bucket = client.bucket(getGcsBucket())
        blob = bucket.blob(object_path)
        file_data = blob.download_as_text()
        return file_data

    except DefaultCredentialsError:
        return None
    except Exception as e:
        print(f"error: {e}")
        return None


def read_csv_from_gcs(object_path: str):
    bucket_name = getGcsBucket()
    file_data = get_file_from_gcs(bucket_name, object_path)

    if file_data is not None:
        from io import StringIO
        df = pd.read_csv(StringIO(file_data), encoding='utf-8')

        return df
    else:
        return None
