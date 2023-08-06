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


r"""This module's functions, generate PleskRequestPackets using the 'session' Operator.

Notes:
    * Supported API Operations:
        * GET retrieves list of currently opened sessions and information on each opened session
        * TERMINATE closes a specified session

    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-sessions.40398/
"""
from pypleski.core import PleskRequestPacket

def get_sessions() -> PleskRequestPacket:
    """ This Packet retrieves a list of active sessions.

    Returns:
        PleskRequestPacket: The RequestPacket ready to use. 
    """
    return PleskRequestPacket("session", "get")

def terminate_session(session:str) -> PleskRequestPacket:
    """ This Packet terminates the specified session. 

    Args:
        session (str): The sessions id. 

    Returns:
        PleskRequestPacket: The RequestPacket ready to use.
    """
    return PleskRequestPacket("session", "terminate", session_id = session)