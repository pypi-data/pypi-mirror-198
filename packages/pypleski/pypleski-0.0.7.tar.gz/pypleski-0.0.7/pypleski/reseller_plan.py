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

r"""
This module's functions, generate PleskRequestPackets using the 'reseller-plan' Operator.

Notes:
    * Not Yet Supported Operations:
        * ADD creates a reseller plan
        * GET retrieves information on reseller plans from Plesk database
        * DEL removes reseller plans
        * SET updates preferences, limits, permissions and IP pool settings for a reseller plan
        * ADD-PACKAGE adds an application to the specified reseller plan
        * REMOVE-PACKAGE removes an application from the specified reseller plan
        * ENABLE-APS-FILTER excludes all apps from the specified reseller plan. You can add apps with the add-package operation
        * DISABLE-APS-FILTER includes all apps in the specified reseller plan
        * DUPLICATE creates a copy of the specified reseller plan

    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-reseller-plans.60460/
"""

from pypleski.core import PleskRequestPacket

def add_reseller_plan() -> PleskRequestPacket:
    return PleskRequestPacket("reseller-plan", "add")

def get_reseller_plan() -> PleskRequestPacket:
    return PleskRequestPacket("reseller-plan", "get")

def delete_reseller_plan(reseller_id:str="") -> PleskRequestPacket:
    return PleskRequestPacket("reseller-plan", "delete")

def set_reseller_plan_settings() -> PleskRequestPacket:
    return PleskRequestPacket("reseller-plan", "set")

def add_pkg_to_plan() -> PleskRequestPacket:
    return PleskRequestPacket("reseller-plan", "add-package")

def remove_pkg_from_plan() -> PleskRequestPacket:
    return PleskRequestPacket("reseller-plan", "remove-package")

def enable_aps_filter() -> PleskRequestPacket:
    return PleskRequestPacket("reseller-plan", "enable-aps-filter")

def duplicate_reseller_plan() -> PleskRequestPacket:
    return PleskRequestPacket("reseller-plan", "duplicate")
