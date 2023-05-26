import tqdm
from pathlib import Path
import os
import tasks_helper_utils as t_utils

DATA_DIR = Path(os.getcwd() + "/task_images")

# Check if dir exists. If so ignore download.
# Just assume we have done from a prior run
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)
    print(f"downloading images ...")
    for url in tqdm.tqdm(t_utils.URLS):
        t_utils.download_images(url, DATA_DIR)
