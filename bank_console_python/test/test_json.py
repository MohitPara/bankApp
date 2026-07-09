import json
import os
from dtos.acc_info import AccInfo


class TestJson:
    def test_json1(self, json_file_path: str):
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as f:
                json_data = f.read()
                if json_data.strip():
                    data = json.loads(json_data)
                    # Can deserialize to AccInfo objects if needed
                    return data
        return None
