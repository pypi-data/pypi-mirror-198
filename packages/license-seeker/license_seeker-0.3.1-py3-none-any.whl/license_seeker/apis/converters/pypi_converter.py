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

import re

class PypiConverter:
    @staticmethod
    def get_name() -> str:
        return "pypi.org"

    @staticmethod
    def convert(url:str) -> str|None:
        pattern = r'//pypi.org/project/'
        api_base_url = "//pypi.org/pypi/"
        if re.search(pattern, url) is None:
            return None
        if url[-1] != "/":
            url += "/"
        return re.sub(pattern, api_base_url, url) + "json"
