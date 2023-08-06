#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Seeplus API
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Seeplus API.
#
# Hive Seeplus API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Seeplus API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Seeplus API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import order

BASE_URL = "https://api.seeplus.inovretail.com/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """

class API(
    appier.API,
    order.OrderAPI
):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("SEEPLUS_BASE_URL", BASE_URL)
        self.token = appier.conf("SEEPLUS_TOKEN", None)
        self.base_url = kwargs.get("base_url", self.base_url)
        self.token = kwargs.get("token", self.token)

    def build(
        self,
        method,
        url,
        data = None,
        data_j = None,
        data_m = None,
        headers = None,
        params = None,
        mime = None,
        kwargs = None
    ):
        auth = kwargs.pop("auth", True)
        if auth: headers["Authorization"] = "Bearer %s" % self.token
        kwargs["api-version"] = "1"
