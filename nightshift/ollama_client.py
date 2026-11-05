"""One Ollama call. Thinking stays off. Context stays inside 32,768 tokens."""

import json
import urllib.request

from nightshift.textutil import chunk_text

MODEL = "qwen3.8:27b"


def chat(prompt, system=""):
    pieces = []
    tokens_in = 0
    tokens_out = 0
    for index, part in enumerate(chunk_text(prompt), start=1):
        text = part
        if index > 1:
            text = "Continue from the previous chunk. Use only this chunk plus what you already wrote.\n\n" + part
        body = {
            "model": MODEL,
            "stream": False,
            "think": False,
            "messages": [
                {"role": "system", "content": system or "You write plain text for David Johnson. No AI wording."},
                {"role": "user", "content": text},
            ],
            "options": {"num_ctx": 32768, "temperature": 0.2},
        }
        request = urllib.request.Request(
            "http://127.0.0.1:11434/api/chat",
            data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request, timeout=600) as response:
            payload = json.loads(response.read().decode())
        message = (payload.get("message") or {}).get("content") or ""
        pieces.append(message.strip())
        tokens_in += int(payload.get("prompt_eval_count") or 0)
        tokens_out += int(payload.get("eval_count") or 0)
    return {"text": "\n\n".join(piece for piece in pieces if piece), "tokens_in": tokens_in, "tokens_out": tokens_out}
