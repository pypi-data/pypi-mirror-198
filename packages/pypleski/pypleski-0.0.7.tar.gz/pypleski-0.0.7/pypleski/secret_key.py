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

r"""This module's functions, generate PleskRequestPackets using the 'secret_key' Operator.

Notes:
    *Supported API Operations:
        * CREATE creates a secret key.
        * GET_INFO retrieves a secret key.
        * DELETE deletes a secret key.

    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-secret-keys.37121/
"""
from pypleski.core import PleskRequestPacket


def create_secret_key(login:str="", ip_address:str="", description:str="") -> PleskRequestPacket:
    """ This Packet creates and retrieves a secret key. If login is None the administrators login will be used.

    Args:
        login (str, optional): specifies the login name of the customer or reseller.Defaults to None.
        ip_address (str, optional):  Specifies the IP address that will be assigned to the secret key. If value is None, Plesk will use the request senders IP. Defaults to None.
        description (str, optional): The description for the secret key. Defaults to None.

    Returns:
        PleskRequestPacket: The PleskRequestPacket ready to use.
    """
    request = {}
    if ip_address:
        request['ip_address'] = ip_address
    if description:
        request['description'] = description
    if login:
        request['login'] = login
    
    return PleskRequestPacket("secret-key", "create", __data__ = request)

def get_secret_key_info(key:str='') -> PleskRequestPacket:
    """ This Packet retrieves information on the specified secret key (or all available keys?).

    Args:
        key (str | int): The secret key or its id.

    Returns:
        PleskRequestPacket: The PleskRequestPacket ready to use.
    """
    if key:
        return PleskRequestPacket("secret-key", "get_info", filter={'key': key})
    # this should retrieve all keys. the space is important to get this output: ...<filter> </filter>...
    return PleskRequestPacket("secret-key", "get_info", filter=' ') 

def delete_secret_key(key:str) -> PleskRequestPacket:
    """This Packet deletes the selected secret key.

    Args:
        key (str): The secret key to delete. 

    Returns:
        PleskRequestPacket: The PleskRequestPacket ready to use.
    """
    return PleskRequestPacket("secret-key", "delete", filter={'key': key})


