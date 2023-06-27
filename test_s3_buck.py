#!/usr/bin/env python3

"""Download images from explore page of TikTok and upload to S3 bucket.
"""

import os

import boto3
from t2thumb import T2TClient

# Change to True to use Firefox instead of Chrome
USE_FIREFOX = False

IMGS_DIR = "imgs"
S3_BUCKET = "t2thumb-test"

def main():
    s3 = boto3.client('s3')
    if os.path.exists(IMGS_DIR):
        os.system(f"rm -rf {IMGS_DIR}")
    os.mkdir(IMGS_DIR)
    client = T2TClient(is_firefox=USE_FIREFOX)
    for i, img in enumerate(client.for_each_img()):
        out_path = os.path.join(IMGS_DIR, f"explore_img_{i}.png")
        with open(out_path, "wb") as f: f.write(img)
        s3.upload_file(out_path, S3_BUCKET, out_path)
        # rm file
        os.remove(out_path)

if __name__ == "__main__":
    main()