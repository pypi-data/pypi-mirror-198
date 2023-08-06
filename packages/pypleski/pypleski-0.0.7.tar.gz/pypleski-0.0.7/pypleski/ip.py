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

r"""This module's functions, generate PleskRequestPackets using the 'ip' Operator.

Notes:
    * Supported API Operations:
        * ADD adds an IP address to Plesk server as shared or exclusive, specifying a netmask and server network interface
        * GET retrieves the list of IP addresses available on the server
        * SET updates properties for IP addresses available on the server 
        * DEL removes an IP address from Plesk server
    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-ip-addresses.35389/
"""
from pypleski.core import PleskRequestPacket

def add_ip(
    ip_address:str,
    subnetmask:str,
    ip_type:str, 
    interface:str, 
    service_node=None, 
    public_ip:str=""
    ) ->PleskRequestPacket:
    """ This Packet adds an IP address to your Plesk server as shared or exclusive.

    Args:
        ip_address (str): _description_
        subnetmask (str): _description_
        ip_type (str): Allowed values
        interface (str): _description_
        service_node (dict, optional): _description_. Defaults to None.
        public_ip (str, optional): _description_. Defaults to None.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    request = {
        'ip_address' : ip_address,
        'netmask' : subnetmask,
        'type': ip_type,
        'interface': interface,        
    }
    if service_node:
        request["service-node"] = service_node
    if public_ip:
        request["public_ip_address"] = public_ip

    return PleskRequestPacket("ip","add", __data__ = request)

def delete_ip(ip:str) ->PleskRequestPacket:
    """ This Packet removes the specified IP address from the server.

    Args:
        ip (str): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("ip", "del", filter={'ip_address':ip})

def set_ip(
    ip:str, 
    ip_type:str,
    cert_name:str="", 
    public_ip:str="", 
    service_node=None
    ) ->PleskRequestPacket:
    """ This Packet updates properties for the specified IP address.

    Args:
        ip (str): _description_
        ip_type (str, optional): _description_
        cert_name (str, optional): _description_
        public_ip (str, optional): _description_
        service_node (dict, optional): _description_. Defaults to None.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    request = {'ip_address' : ip}
    if ip_type:
        request["type"] = ip_type

    if cert_name:
        request["certificate_name"] = cert_name

    if public_ip:
        request["public_ip_address"] = public_ip


    if service_node:
        request["service-node"] = service_node

    return PleskRequestPacket("ip","set", __data__ = request)

def get_ips() ->PleskRequestPacket:
    """ This Packet retrieves the list of IP addresses available on the server.

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("ip", "get")
 