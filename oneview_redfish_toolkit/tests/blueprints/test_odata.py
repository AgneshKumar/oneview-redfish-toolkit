# -*- coding: utf-8 -*-

# Copyright (2017-2018) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# Python libs
import json

# 3rd party libs
from flask_api import status

# Module libs
from oneview_redfish_toolkit.blueprints.odata import odata
from oneview_redfish_toolkit.tests.base_flask_test import BaseFlaskTest


class TestOdata(BaseFlaskTest):
    """Tests for Odata blueprint"""

    @classmethod
    def setUpClass(self):
        super(TestOdata, self).setUpClass()

        self.app.register_blueprint(odata)

    def test_get_odata(self):
        """Tests Odata blueprint result against know value """

        response = self.client.get("/redfish/v1/odata")

        result = json.loads(response.data.decode("utf-8"))

        with open(
            'oneview_redfish_toolkit/mockups/redfish/Odata.json'
        ) as f:
            odata_mockup = json.load(f)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual("application/json", response.mimetype)
        self.assertEqual(odata_mockup, result)
