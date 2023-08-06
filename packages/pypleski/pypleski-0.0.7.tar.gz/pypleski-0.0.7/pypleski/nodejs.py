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

r"""This module's functions, generate PleskRequestPackets using the 'extension' Operator
to make calls to the nodejs Extension.

Notes: 
    This is not core functionality. Node.js is available as an extension.

    * Supported API Operations:
        * VERSIONS retrieves the list of Node.js versions available on the server.
        * ENABLE enables Node.js on the server or on a domain.
        * DISABLE disables a Node.js on the server or on a domain.
        * SET-VERSION sets a particular Node.js version on a domain.
        * GET retrieves a Node.js version on a domain.  
    
    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-nodejs-versions.77394/
"""
from pypleski.core import PleskRequestPacket

def get_available_nodejs_versions() -> PleskRequestPacket:
    """_summary_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("extension", "call", nodejs={'versions':''})

def enable_nodejs(domain:str="", version:str="") -> PleskRequestPacket:
    """ enable a Node.js version on the server (domain=None available to Administrator only) or on a domain.

    Args:
        domain (str, optinal): specifies the domain name. Defaults to None.
        version (str, optional): specifies the Node.js version. Defaults to None.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    request = {}
    if version:
        request["version"] = version
    if domain:
        request["domain"] = domain

    return PleskRequestPacket("extension", "call", nodejs={'enable':request})

def disable_nodejs(domain:str="", version:str="") -> PleskRequestPacket:
    """ disable a Node.js version on the server ( domain=None available to Administrator only) or on a domain.

    Args:
        domain (str, optional): specifies the domain name. Defaults to None.
        version (str, optional): specifies the Node.js version. Defaults to None.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    request = {}
    if version:
        request["version"] = version
    if domain:
        request["domain"] = domain

    return PleskRequestPacket("extension", "call", nodejs={'disable':request})

def set_nodejs_version(domain:str, version:str) -> PleskRequestPacket:
    """ set a Node.js version on a domain.

    Args:
        domain (str): specifies the domain name. Defaults to None.
        version (str): specifies the Node.js version. 
    Returns:
        PleskRequestPacket: PleskRequestPacket
    """    
    return PleskRequestPacket("extension", "call", nodejs={"enable":{"domain":domain, "version": version}})


def get_nodejs_versions(domain:str) -> PleskRequestPacket:
    """_summary_
    Args:
        domain (str): specifies the domain name. Defaults to None.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("extension", "call", nodejs={"get-versions": {"domain": domain}})