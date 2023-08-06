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

from .github_parser import GithubParser
from .pypi_parser import PypiParser

class Parser:
    def __init__(self, parsers=None):
        self.parsers = {}
        if parsers is None:
            parsers = [
                GithubParser,
                PypiParser
            ]
        for parser in parsers:
            self.add_parser(parser)

    def add_parser(self, parser):
        self.parsers[parser.get_name()] = parser

    def parse(self, name:str, response:str) -> str|None:
        parser = self.parsers.get(name, None)
        if parser is None:
            return None
        return parser.parse(response)

