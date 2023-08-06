"""
MIT License

Copyright (c) 2023 Galaxy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import requests as r
import json
import time as t


"""
    sends a PublishAsync to the specified topic
    @param      data        Data to be sent to the "message" parameter of SubscribeAsync
    @param      api_key     Your api-key (create api-key here: https://create.roblox.com/docs/reference/cloud/managing-api-keys)
    @param      topic       Topic to send data
    @param      universeId      the set to send the data (more info here: https://create.roblox.com/docs/reference/cloud/messaging-service)
"""


def Publish(data: any, api_key: str, topic: str, universeId: str, _printResponse: bool = False) -> str:
    if not data:
        data = "Hello, CLOUD-APY!"

    _URL = f"https://apis.roblox.com/messaging-service/v1/universes/{universeId}/topics/{topic}"
    response = r.post(_URL, headers={
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }, json={"message": json.dumps(data)})

    if _printResponse:
        print(f"CLOUD-APY -> {api_key}: ", response)


if __name__ == "__main__":
    Publish({"User": {"a": 1, "b": 20}},
            "dev-key", "Test", "...", True)
