import os
import json
import time
import random
import string
import requests

url_alphabet = "useandom-26T198340PX75pxJACKVERYMINDBUSHWOLF_GQZbfghjklqvwyzrict"

def nanoid(size=21):
    random_values = [random.SystemRandom().randint(0, 255) for _ in range(size)]
    return "".join(
        [
            url_alphabet[byte & 63]
            if byte & 63 < 36
            else url_alphabet[(byte & 63) - 26].upper()
            if byte & 63 < 62
            else "-"
            if byte & 63 == 62
            else "_"
            for byte in random_values
        ]
    )

EVENTS_API = "https://us-central1-get-fast-dev.cloudfunctions.net/events"

class Session:
    def __init__(self, key, event_id, session_id, completed):
        self.key = key
        self.event_id = event_id
        self.session_id = session_id
        self.completed = completed

    @classmethod
    async def init(cls, key, event_id, session_id, completed):
        return cls(key, event_id, session_id, completed)

    async def start(self):
        if self.completed:
            raise ValueError("Session already completed")

        data = {
            "apiKey": self.key,
            "start": True,
            "event_id": self.event_id,
            "session_id": self.session_id,
            "timestamp": int(time.time() * 1000),
        }
        response = requests.post(
            EVENTS_API,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data),
        )
        response.raise_for_status()
        return response

    async def checkpoint(self, checkpoint=None):
        if self.completed:
            raise ValueError("Session already completed")

        data = {
            "apiKey": self.key,
            "checkpoint": checkpoint,
            "event_id": self.event_id,
            "session_id": self.session_id,
            "timestamp": int(time.time() * 1000),
        }
        response = requests.post(
            EVENTS_API,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data),
        )
        response.raise_for_status()
        return response

    async def stop(self):
        if self.completed:
            raise ValueError("Session already completed")

        data = {
            "apiKey": self.key,
            "stop": True,
            "event_id": self.event_id,
            "session_id": self.session_id,
            "timestamp": int(time.time() * 1000),
        }
        response = requests.post(
            EVENTS_API,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data),
        )
        response.raise_for_status()
        self.completed = True

        return response

class GetFast:
    def __init__(self, key: str):
        self.key = key or os.environ.get("GETFAST_API_KEY")

    @classmethod
    async def init(cls, key=None):
        return cls(key)

    def session(self, event_id, session_id=None):
        session_id = session_id or nanoid()
        return Session(self.key, event_id, session_id, False)