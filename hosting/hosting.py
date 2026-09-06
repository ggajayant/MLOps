from pathlib import Path

from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
repo_id = "gjayant/Bank-Customer-Churn"

# Create the Streamlit Space on the first workflow run; subsequent runs reuse it.
api.create_repo(
    repo_id=repo_id,
    repo_type="space",
    space_sdk="streamlit",
    exist_ok=True,
)

api.upload_folder(
    folder_path=str(Path(__file__).resolve().parents[1] / "deployment"),
    repo_id=repo_id,
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
