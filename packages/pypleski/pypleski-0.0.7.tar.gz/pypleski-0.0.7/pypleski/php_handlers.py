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
This module's functions, generate PleskRequestPackets using the 'php-handler' Operator.

Notes:
    * Supported Operations:
        * GET retrieves the specified PHP handler.
        * ENABLE enables the specified PHP handler.
        * DISABLE disables the specified PHP handler.
        * GET-USAGE displays the usage of the specified PHP handler.
    
    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-php-handlers.75313/
"""
from pypleski.core import PleskRequestPacket

def get_php_handler(id:str) -> PleskRequestPacket:
    """ This Packet retrieves information about the specified php-handler.

    Args:
        id (int): The handlers ID

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("php-handler", "get", filter={'id':id})

def enable_php_handler(id:str) -> PleskRequestPacket:
    """ This Packet enables the specified php-handler

    Args:
        id (int): The handlers ID

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("php-handler", "enable", filter={'id':id})

def disable_php_handler(id:str) -> PleskRequestPacket:
    """ This Packet disables a php-handler

    Args:
        id (int): The handlers ID

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("php-handler", "disable", filter={'id':id})
    

def get_php_handler_usage(id:str) -> PleskRequestPacket:
    """ This Packet gets usage information for the specified

    Args:
        id (int): The handlers ID

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("php-handler", "get-usage", filter={'id':id})