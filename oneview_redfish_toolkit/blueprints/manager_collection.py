# -*- coding: utf-8 -*-

# Copyright (2017) Hewlett Packard Enterprise Development LP
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
import logging

# 3rd party libs
from flask import abort
from flask import Blueprint
from flask import g
from flask import Response
from flask_api import status

# own libs
from oneview_redfish_toolkit.api.errors \
    import OneViewRedfishResourceNotFoundError
from oneview_redfish_toolkit.api.manager_collection import ManagerCollection
from oneview_redfish_toolkit import multiple_oneview
from oneview_redfish_toolkit.blueprints.util.response_builder import \
    ResponseBuilder

manager_collection = Blueprint("manager_collection", __name__)


@manager_collection.route("/redfish/v1/Managers/", methods=["GET"])
def get_manager_collection():
    """Get the Redfish Manager Collection.

        Return ManagerCollection redfish JSON.
        Logs exception of any error and return
        Internal Server Error or Not Found.

        Returns:
            JSON: Redfish json with ManagerCollection.

        Exceptions:
            Exception: Generic error, logs the exception and call abort(500).
    """

    try:
        oneview_appliances = multiple_oneview.get_map_appliances()
        mc = ManagerCollection(oneview_appliances)

        # Build redfish json
        json_str = mc.serialize()
        # Build response and returns
        return Response(
            response=json_str,
            status=status.HTTP_200_OK,
            mimetype="application/json")

    except Exception as e:
        # In case of error print exception and abort
        logging.exception('Unexpected error: {}'.format(e))
        abort(status.HTTP_500_INTERNAL_SERVER_ERROR)
