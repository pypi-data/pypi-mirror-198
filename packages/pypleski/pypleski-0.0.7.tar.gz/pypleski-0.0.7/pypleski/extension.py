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

r"""This Module's functions generate requests to talk to the Plesk Extension Endpoint.

Notes:
    * Supported API Calls: 
        * INSTALL installs an extension from the specified URL.
        * CALL calls an XML API operation specific to a particular extension.
        * GET retrieves information on installed extensions.
        * UNINSTALL uninstalls an extension with the given ID.
    
    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-plesk-extensions.76730/

"""

from pypleski.core import PleskRequestPacket

def install_extension(install_from_url:str="", install_by_id:str="") -> PleskRequestPacket:
    """This Packet installs a packet either from the given url or by id. 
        If both options are provided, install install_by_id will be used.

    Args:
        install_from_url (str, optional): URL as source for installation. Defaults to None.
        install_by_id (str, optional): Id of the extension to install. Defaults to None.

    

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    if install_from_url:
        return PleskRequestPacket("extension", "install", url = install_from_url)
    return PleskRequestPacket("extension", "install", id = install_by_id)
    

def uninstall_extension(extension_id:str) -> PleskRequestPacket:
    """ This Packet unbinstalls the specified extension. 

    Args:
        extension_id (str): Id of the extension to uninstall.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("extension", "uninstall", id = extension_id)

def call_to_extension(**call) -> PleskRequestPacket:
    """This Packet sends the specified call to the extension. The Format of calls depend on the extension. 

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("extension", "call", **call)

def get_extensions(extension_id:str="") -> PleskRequestPacket:
    """This Packet retrieves information on installed extensions. Gets all if extension_id is None

    Args:
        extension_id (str, oprional): Id of the extension you may want to specifie

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    if extension_id:
        return PleskRequestPacket("extension", "get", filter = {"id": extension_id})
    return PleskRequestPacket("extension", "get")
