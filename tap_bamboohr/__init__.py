#!/usr/bin/env python3
import singer
from singer import utils
# Import discover script from current directory
from .discover import discover
# Import sync script from current directory
from .sync import sync

REQUIRED_CONFIG_KEYS = ["start_date", "subdomain", "api_key"]
LOGGER = singer.get_logger()

@utils.handle_top_exception(LOGGER)
def main():
    # Parse command line arguments
    args = utils.parse_args(REQUIRED_CONFIG_KEYS)
    
    # If discover flag was passed, run discovery mode and dump output to stdout
    if args.discover:
        LOGGER.info("Starting discovery mode")
        catalog = discover()
        catalog.dump()
    # Otherwise run in sync mode
    else:
        LOGGER.info("Starting sync mode")
        if args.catalog:
            catalog = args.catalog
        else:
            catalog = discover()
        sync(args.config, args.state, catalog)


if __name__ == "__main__":
    main()
