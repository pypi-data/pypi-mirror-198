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

r"""This module's functions, generate PleskRequestPackets using the 'site-alias' Operator.

Notes:
    * Not Yet Supported Operations:
        * ADD creates a subdomain.
        * GET retrieves information on a specified subdomain from Plesk database.
        * SET changes subdomain settings.
        * DEL removes a specified subdomain.
        * RENAME renames a specified subdomain.

    **Status:** _planning_
"""
from pypleski.core import PleskRequestPacket

