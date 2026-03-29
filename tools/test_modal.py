import os
from dotenv import load_dotenv

# Load credentials from .env to bypass the modal CLI login buggy state on Py3.13
load_dotenv()

import modal

app = modal.App("scraperrr-test")

@app.function()
def test_modal():
    return "Handshake successful! Modal is connected and executing functions in the cloud."

@app.local_entrypoint()
def main():
    print(test_modal.remote())
