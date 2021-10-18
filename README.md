# tap-bamboohr

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [FIXME](http://example.com)
- Extracts the following resources:
  - [FIXME](http://example.com)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

---

Copyright &copy; 2018 Stitch

## Developer Notes
Some notes to consider that are made during tap development.

**Activate environment during testing - using of tap app**
**Installed pip install PyBambooHR -  tbc if stays**

### Config.json file
      - Consists of 3x parameters: `subdomain`, `api_key` and `start_date`
      - Get `api_key` from BambooHR website when logged in as user, create the key and copy key code
      - The `subdomain` is the first part of the web url
        eg. https://<subdomain>.bamboohr.com/home
      - Specify the `start_date` value as required with format <2017-01-01T00:00:00Z>

### Get stream working
Start with testing single stream - Employee Directory. Also imported package PyBambooHR.
1. Added code for it
2. Create empty schema json file employee_directory.json - {}

###  Fixing metadata
Need to use Singer tool get_standard_metadata to retrieve the standard metadata and write it to the catalog file during discovery mode.
