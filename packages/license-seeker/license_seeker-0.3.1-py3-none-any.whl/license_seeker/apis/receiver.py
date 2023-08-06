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

import requests

class Receiver:
    """The handler of response."""
    def __init__(self, config):
        self.config = config

    def get(self, url) -> dict:
        headers = self.config.get_headers()
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None
        return response.json()
