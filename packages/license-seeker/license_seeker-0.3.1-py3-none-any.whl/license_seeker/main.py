################################################################################
# Copyright (C) 2023 Kostiantyn Klochko <kostya_klochko@ukr.net>               #
#                                                                              #
# This file is part of license-seeker.                                         #
#                                                                              #
# license-seeker is free software: you can redistribute it and/or modify it    #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# license-seeker is distributed in the hope that it will be useful, but        #
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY   #
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for  #
# more details.                                                                #
#                                                                              #
# You should have received a copy of the GNU General Public License along with #
# license-seeker. If not, see <https://www.gnu.org/licenses/>.                 #
################################################################################

import sys
from license_seeker.apis.receiver import Receiver
from license_seeker.apis.connection_config import ConnectionConfig
from license_seeker.apis.converters.converter import Converter
from license_seeker.apis.parsers.parser import Parser

def main():
    lines = get_stdin()
    conconfig = ConnectionConfig()
    receiver = Receiver(conconfig)
    converter = Converter()
    parser = Parser()
    for url in lines:
        license = get_license(url, receiver, converter, parser)
        license = dict_only_keys(license, [
            'key', 'name', 'spdx_id'
        ])
        print(f"{license=}")

def get_license(url, receiver, converter, parser) -> dict:
    """
    Return dictionary that contains information about license.
    """
    res = converter.convert(url.strip())
    if res is None:
        print("[Error] something wrong.")
    name, url = res
    url = url.strip()
    res = receiver.get(url)
    return parser.parse(name, res)

def dict_only_keys(dictionary:dict, keys:list) -> dict:
    """
    Return dictionary with the keys.
    If a key is not in keys list or not in dictionary keys list then it will be skipped.
    """
    return {k: dictionary[k] for k in keys if k in dictionary.keys()}

def get_stdin():
    return (line for line in sys.stdin)

if __name__ == "__main__":
    main()

