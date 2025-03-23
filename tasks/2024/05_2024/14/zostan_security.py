import hashlib
import json
import re

import requests


def parse_html_and_send():
    # first request
    # -----------------------------------------------------------------------------------------------------------------
    response = requests.get("https://task.zostansecurity.ninja/")
    match = re.search(r"step=\d+&challenge=[a-zA-Z0-9]+&timestamp=\d+", response.text)
    params_string = match.group(0)
    new_url = f"https://task.zostansecurity.ninja/?{params_string}"
    response = requests.get(new_url)
    print("First response: ", response.text)

    # second request
    # -----------------------------------------------------------------------------------------------------------------
    match_challenge = re.search(r"X-challenge: ([a-zA-Z0-9]+)", response.text)
    match_timestamp = re.search(r"X-timestamp: (\d+)", response.text)
    challenge = match_challenge.group(1)
    timestamp = match_timestamp.group(1)
    headers = {"X-challenge": challenge, "X-timestamp": timestamp}
    second_url = "https://task.zostansecurity.ninja/?step=2"
    response = requests.get(second_url, headers=headers)
    print("Second response: ", response.text)

    # third request
    # -----------------------------------------------------------------------------------------------------------------
    match_challenge = re.search(r"(?<=challenge:)(.*)(?=- t)", response.text, flags=re.DOTALL)
    match_data = re.search(r"(?<=below:)(.*)(?=Format)", response.text, flags=re.DOTALL)
    match_timestamp = re.search(r"(?<=timestamp:)(.*)(?=-)", response.text, flags=re.DOTALL)
    challenge = match_challenge.group(1).strip()
    data = json.loads(match_data.group(1))
    timestamp = str(int(match_timestamp.group(1)))
    sorted_data_str = "&".join([f"{key}={value}" for key, value in sorted(data.items())])
    hash_value = hashlib.sha256(sorted_data_str.encode()).hexdigest()
    third_url = "https://task.zostansecurity.ninja/?step=3"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    response = requests.post(
        third_url,
        headers=headers,
        data={
            "challenge": challenge,
            "timestamp": timestamp,
            "hash": hash_value,
        },
    )
    print("Third response: ", response.text)


if __name__ == "__main__":
    parse_html_and_send()
