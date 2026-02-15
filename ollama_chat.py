#!/usr/bin/env python3
"""Simple Ollama API wrapper for local LLM inference."""
import sys, json, urllib.request, urllib.error

DEFAULT_URL, DEFAULT_MODEL = "http://localhost:11434/api/generate", "llama3.2"

def chat(prompt, model=DEFAULT_MODEL, url=DEFAULT_URL, system=None):
    payload = {"model": model, "prompt": prompt, "stream": False}
    if system: payload["system"] = system
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as r:
            result = json.loads(r.read().decode('utf-8'))
            return {"response": result.get("response", ""), "done": result.get("done", True)}
    except urllib.error.URLError as e:
        return {"error": f"Connection failed: {e}"}

if __name__ == "__main__":
    model, url, prompt, system = DEFAULT_MODEL, DEFAULT_URL, None, None
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        if a in ('-m', '--model'): model, i = sys.argv[i + 1], i + 2
        elif a in ('-s', '--system'): system, i = sys.argv[i + 1], i + 2
        elif not a.startswith('-'): prompt, i = a, len(sys.argv)
        else: i += 1
    if not prompt: print("Usage: ollama_chat.py <prompt> [-m model]"); sys.exit(1)
    result = chat(prompt, model, url, system)
    if "error" in result: print(f"Error: {result['error']}"); sys.exit(1)
    print(result['response'])
