from pathlib import Path

from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path=str(Path(__file__).resolve().parents[1] / "deployment"),
    repo_id="gjayant/Bank-Customer-Churn",
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
