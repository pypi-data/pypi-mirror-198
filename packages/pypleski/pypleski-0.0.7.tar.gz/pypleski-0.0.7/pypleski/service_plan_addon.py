# Copyright (C) 2023  Uli Toll
# 
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

r""" This module's functions, generate PleskRequestPackets using the 'service-plan-addon' Operator.

Notes:
    * Not Yet Supported Operations:
        * ADD creates an add-on plan
        * GET gets the information about specified add-on plans from the server
        * DEL deletes specified add-on plans
        * SET updates settings for specified add-on plans.
        * ADD-PACKAGE includes an app in the specified add-on plan.
        * REMOVE-PACKAGE excludes an app from the specified add-on plan.
        * GET-LIMIT-DESCRIPTOR retrieves add-on plan limit descriptor
        * GET-PERMISSION-DESCRIPTOR retrieves add-on plan permission descriptor
        * GET-PHYSICAL-HOSTING-DESCRIPTOR retrieves descriptor of hosting settings
        * DUPLICATE creates a copy of the specified add-on plan.

    **Plesk Reference Link** https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-addon-plans.66420/
"""
from pypleski.core import PleskRequestPacket


def add_plan_addon() -> PleskRequestPacket:
    return PleskRequestPacket("service-plan-addon", "add")

def get_plan_addon() -> PleskRequestPacket:
    return PleskRequestPacket("service-plan-addon", "get")

def delete_plan_addon(reseller_id:str="") -> PleskRequestPacket:
    return PleskRequestPacket("service-plan-addon", "delete")

def set_plan_addon_settings() -> PleskRequestPacket:
    return PleskRequestPacket("service-plan-addon", "set")

def add_pkg_to_plan() -> PleskRequestPacket:
    return PleskRequestPacket("service-plan-addon", "add-package")

def remove_pkg_from_plan() -> PleskRequestPacket:
    return PleskRequestPacket("service-plan-addon", "remove-package")
