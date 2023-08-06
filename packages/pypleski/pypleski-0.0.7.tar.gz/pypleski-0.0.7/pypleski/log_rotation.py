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
Notes: 
    * Supported Operations:    
        * GET retrieves Log Rotation settings.        
        * ENABLE enables Log Rotation service on a site
        * DISABLE disables Log Rotation service on a site
        * GET-STATUS retrieves status of Log Rotation service
        * SET changes Log Rotation settings.

    Review:
        Improve doc strings
        SET function is not very elegant.
"""

from pypleski.core import PleskRequestPacket

def enable_log_rotation(filter_name:str, filter_value:str) -> PleskRequestPacket:
    """ This Packet enables the log rotation service for the selected site or owner

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter

    
    Returns:
        PleskRequestPacket: The RequestPacket ready to use.

    Notes: 
        * Available Filters: 
            * site-id (int)
            * owner-id (int)
            * site-name (str)
            * owner-login (str)

    """
    return PleskRequestPacket("log-rotation", "enable", filter={filter_name:filter_value})

def disable_log_rotation(filter_name:str, filter_value:str) -> PleskRequestPacket:
    """ This Packet disables the log rotation service for the selected site or owner.

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter
    
    Returns:
        PleskRequestPacket: The RequestPacket ready to use.

    Notes: 
        * Available Filters: 
            * site-id (int)
            * owner-id (int)
            * site-name (str)
            * owner-login (str)

    """
    return PleskRequestPacket("log-rotation", "disable", filter={filter_name:filter_value})

def get_log_rotation_status(filter_name:str, filter_value:str) -> PleskRequestPacket:
    """ This Packet  retrieve status of Log Rotation service on sites by site or owner.

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter
  
    Returns:
        PleskRequestPacket: The RequestPacket ready to use.

    Notes: 
        * Available Filters: 
            * site-id (int)
            * owner-id (int)
            * site-name (str)
            * owner-login (str)

    """
    return PleskRequestPacket("log-rotation", "get-status", filter={filter_name:filter_value})

def get_log_rotation_settings(filter_name:str, filter_value:str) -> PleskRequestPacket:
    """ This Packet retrieves settings of Log Rotation of sites by site or owner.

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter.    

    Returns:
        PleskRequestPacket: The RequestPacket ready to use.

    Notes: 
        * Available Filters: 
            * site-id (int)
            * owner-id (int)
            * site-name (str)
            * owner-login (str)

    """
    return PleskRequestPacket("log-rotation", "get", filter={filter_name:filter_value})


def set_log_rotation_settings(
    filter_name:str, 
    filter_value:str, 
    log_by_size:int=0, 
    log_by_time:str="", 
    log_max_num_files:int=0, 
    log_compress:str="", 
    log_email:str=""
    ) -> PleskRequestPacket:
    """This Packet 

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter

        log_by_size (int, optional): _description_. Defaults to None.
        log_by_time (str, optional): _description_. Defaults to None.
        log_max_num_files (int, optional): _description_. Defaults to None.
        log_compress (str, optional): Compression on or off Allowed values: true | false. Defaults to None.
        log_email (str, optional): _description_. Defaults to None.
        
    Returns:
        PleskRequestPacket: PleskRequestPacket

    Notes: 
        * Available Filters: 
            * site-id (int)
            * owner-id (int)
            * site-name (str)
            * owner-login (str)

    """
    request = {filter_name:filter_value, 'settings':{}}
    if log_by_size:
        request["settings"]["log-condition"]["log-bysize"] = log_by_size    
    if log_by_time:
        request["settings"]["log-condition"]["log-bytime"] = log_by_time
    if log_max_num_files:
        request["settings"]["log-max-num-files"] = log_max_num_files
    if log_compress:
        request["settings"]["log-compress"] = log_compress
    if log_email:
        request["settings"]["log-email"] = log_email

    return PleskRequestPacket("log-rotation", "set", __data__ = request)
    