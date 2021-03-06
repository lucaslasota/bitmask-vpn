#!/usr/bin/env python3

import json
import os
import sys

import configparser

from provider import getDefaultProvider
from provider import getProviderData


VERSION = os.environ.get('VERSION', 'unknown')


def writeOutput(data, outfile):

    with open(outfile, 'w') as outf:
        outf.write(json.dumps(data))


if __name__ == "__main__":
    env_provider_conf = os.environ.get('PROVIDER_CONFIG')
    if env_provider_conf:
        if os.path.isfile(env_provider_conf):
            print("[+] Overriding provider config per "
                  "PROVIDER_CONFIG variable")
            configfile = env_provider_conf

    config = configparser.ConfigParser()
    config.read(configfile)
    provider = getDefaultProvider(config)
    data = getProviderData(provider, config)

    if len(sys.argv) != 2:
        print('Usage: generate-osx.py <output_file>')
        sys.exit(1)

    outputf = sys.argv[1]

    data['applicationNameLower'] = data.get('applicationName').lower()
    data['URL'] = data.get('infoURL')
    data['version'] = VERSION
    writeOutput(data, outputf)
