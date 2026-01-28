import csv
import os
from typing import List, Dict, Any


class CSVWriter:
    """
    Utility for writing user data to a CSV file.
    """

    @staticmethod
    def write_users_to_csv(users: List[Dict[str, Any]], csv_path: str):
        if not users:
            raise ValueError("No user data to write to CSV.")

        # Ensure output directory exists
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)

        # Flatten nested fields for CSV output
        def flatten_user(user: Dict[str, Any]) -> Dict[str, Any]:
            flat = {}
            for k, v in user.items():
                if isinstance(v, dict):
                    for sub_k, sub_v in v.items():
                        if isinstance(sub_v, dict):
                            for sub2_k, sub2_v in sub_v.items():
                                flat[f"{k}.{sub_k}.{sub2_k}"] = sub2_v
                        else:
                            flat[f"{k}.{sub_k}"] = sub_v
                else:
                    flat[k] = v
            return flat

        flat_users = [flatten_user(u) for u in users]
        fieldnames = sorted({k for user in flat_users for k in user.keys()})

        with open(csv_path, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user in flat_users:
                writer.writerow(user)