import singer
from .client import BamboohrClient

LOGGER = singer.get_logger()

def sync(config, state, catalog):
    client = BamboohrClient(config["api_key"], config["subdomain"])
    subdomain = config["subdomain"]
    api_key = config["api_key"]

