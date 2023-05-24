from datasets import load_dataset

SMALL_DATA = False
DATASET_NAME = "scene_parse_150"

# Load data from the Hugging Face datasets repository.
if SMALL_DATA:
    train_dataset = load_dataset(DATASET_NAME, split="train[:160]")
else:
    train_dataset = load_dataset(DATASET_NAME, split="train")
