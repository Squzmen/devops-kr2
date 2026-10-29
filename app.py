# KR2: Pshenichnov
import os
import socket

import redis
from flask import Flask, request

app = Flask(__name__)

STUDENT = os.getenv("STUDENT", "unknown")

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)


@app.route("/health")
def health():
    return "ok\n"


@app.route("/")
def index():
    hits = r.incr("hits")
    return f"KR2 | {STUDENT} | container {socket.gethostname()} | hits: {hits}\n"


@app.route("/whoami")
def whoami():
    scheme = request.headers.get("X-Forwarded-Proto", "none")
    client = request.headers.get("X-Real-IP", "none")
    host = request.headers.get("Host", "none")
    return f"scheme: {scheme}\nclient: {client}\nhost: {host}\n"
