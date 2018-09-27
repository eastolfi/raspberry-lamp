#!flask/bin/python
import os
from app import app

app.run(host = os.getenv("IP", "0.0.0.0"), port = os.getenv("PORT", 8080))