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

r"""This Module's Function use the "locale" Operator.

Notes:
    * Supported Operations:
        * GET retrieves info on the language packs installed on Plesk server
        * GET-MESSAGE retrieves the message specified by a key from resource files of the language pack
        * ENABLE enables the language pack on the server       
        * DISABLE disables the language pack on the server

    **All Language Codes**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-locales/locale-codes.39382/
    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-locales.40658/
   
"""
from pypleski.core import PleskRequestPacket

def get_installed_language_packs(locale_id:str="en-US") -> PleskRequestPacket:
    """This Packet retrieves info on the language packs installed for the specified language.

    Args:
        local_id (str, optional): _description_. Defaults to "en-US".

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("locale", "get", filter={'id':locale_id})

def get_localized_message(key:str, locale_id:str="en-US") -> PleskRequestPacket:
    """This Packet retrieves the message specified by a key from resource files of the language pack.

    Args:
        key (str): _description_
        local_id (str, optional): _description_. Defaults to "en-US".

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("locale", "get-message", filter={'key', key}, id = locale_id)

def enable_language_pack(locale_id:str) -> PleskRequestPacket:
    """This Packet enables the language pack on the server.

    Args:
        locale_id (str): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("locale", "enable", filter={'id': locale_id})

def disable_language_pack(locale_id:str) -> PleskRequestPacket:
    """This Packet disables the language pack on the server.

    Args:
        locale_id (str): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("locale", "disable", filter={'id': locale_id})