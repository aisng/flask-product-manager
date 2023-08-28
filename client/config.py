import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "5413889438bb0885393262ce91db503a"
    API_URL = "http://localhost:5000/product"
