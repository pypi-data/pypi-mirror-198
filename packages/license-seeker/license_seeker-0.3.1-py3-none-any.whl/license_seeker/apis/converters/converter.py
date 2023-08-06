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

from .github_converter import GithubConverter
from .pypi_converter import PypiConverter

class Converter:
    def __init__(self, converters=None):
        self.converters = converters
        if converters is None:
            self.converters = [
                GithubConverter,
                PypiConverter
            ]

    def convert(self, url:str) -> str|None:
        for c in self.converters:
            rurl = c.convert(url)
            if rurl is None:
                continue
            return (c.get_name(), rurl)
        else:
            return None

