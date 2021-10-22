# tap-bamboohr

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [BambooHR](https://www.bamboohr.com/homepage-customer/)
- Extracts the following resources:
  - [BambooHR API documentation](https://documentation.bamboohr.com/reference#get-employees-directory-1)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

---

Copyright &copy; 2018 Stitch

## Developer Notes
Some notes to consider that are made during tap development.

**Activate environment during testing - using of tap app**
**Installed pip install PyBambooHR -  tbc if stays**
**Singer tools infer schema - include part of that environment or not

### Config.json file
      - Consists of 3x parameters: `subdomain`, `api_key` and `start_date`
      - Get `api_key` from BambooHR website when logged in as user, create the key and copy key code
      - The `subdomain` is the first part of the web url
        eg. https://<subdomain>.bamboohr.com/home
      - Specify the `start_date` value as required with format <2017-01-01T00:00:00Z>

### Get singer tap template working
Start with testing single stream - Employee Directory. Also imported package PyBambooHR.
1. Added code for it
2. Create empty schema json file employee_directory.json - {}
3. Tried discover mode and dit not work
4. Copied existing catalog file and then run tap
5. Got stream data but not in Singer format
6 Used script file format and developed tap from scratch

###  Fixing metadata
Need to use Singer tool get_standard_metadata to retrieve the standard metadata and write it to the catalog file during discovery mode.

### Tap from scratch:
1. Used copied schema and discovered catalog - got data out, worked.
2. Process for each stream:
  - Make empty schema and use singer infer schema
  - Run tap in discovery mode to get catalog
    ` ~/.virtualenvs/tap-bamboohr/bin/tap-bamboohr --config ~/tap-bamboohr/config.json --discover > new_catalog.json`
  - Add to catalog metadata `"selected": true`
  - Run tap and output stream data to json file:
  `~/.virtualenvs/tap-bamboohr/bin/tap-bamboohr --config ~/tap-bamboohr/config.json --catalog ~/tap-bamboohr/new_catalog.json > ~/tap-bamboohr/empl_dir.json`
  - Use singer tool infer schema on data json file to get schema:
  `~/.virtualenvs/singer-tools/bin/singer-infer-schema < empl_dir.json > empl_schema.json`
  - Copy schema output into schemas folder in file
  - Run tap with new schema file and in discovery mode to get final catalog file
  - Run tap with new schema file and new catalog file (after adding selected:true) and output data


### State file tests:
~/.virtualenvs/<tap-foo>/bin/<tap-foo> --config tap_config.json --catalog catalog.json | ~/.virtualenvs/<target-bar>/bin/<target-bar> --config target_config.json >> state.json

tail -1 state.json > state.json.tmp && mv state.json.tmp state.json

