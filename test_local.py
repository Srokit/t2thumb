#!/usr/bin/env python3

"""Download images from explore page of TikTok to local dir.
"""

import os

from t2thumb import T2TClient

# Change to True to use Firefox instead of Chrome
USE_FIREFOX = False

IMGS_DIR = "imgs"

def main():
    if os.path.exists(IMGS_DIR):
        os.system(f"rm -rf {IMGS_DIR}")
    os.mkdir(IMGS_DIR)
    client = T2TClient(is_firefox=USE_FIREFOX)
    for i, img in enumerate(client.for_each_img()):
        out_path = os.path.join(IMGS_DIR, f"explore_img_{i}.png")
        with open(out_path, "wb") as f: f.write(img)

if __name__ == "__main__":
    main()
