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
    print("here 1")
    
    # If discover flag was passed, run discovery mode and dump output to stdout
    if args.discover:
        print('here 2 - discover explicitly selcted')
        catalog = discover()
        catalog.dump()
        print("discover complete")
    # Otherwise run in sync mode
    else:
        if args.catalog:
            catalog = args.catalog
        else:
            print("here 2.1 - discover forced")
            catalog = discover()
            print("forced discover complete")
        sync(args.config, args.state, catalog)


if __name__ == "__main__":
    main()
