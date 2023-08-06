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

r"""The Server Module provides functions for generating Requests addressing the 'server' endpoint.


"""

from pypleski.core import PleskRequestPacket, PleskApiClient, PleskResponsePacket


def obtain_session_token(user, password:str, plesk_ip:str, plesk_port:int=8443, user_ip:str=None) -> str:
    """ obtain_session_token function - Obtains a Plesk Session Token for the given credentials

    Args:
        user (string): Your Plesk Server Username
        password (string): Your Plesk Server Password
        plesk_ip (string): IP or URL to your Plesk Server
        plesk_port (int): The Port of the server

    Returns:
        str: Returns a Session Token. Returns an empty string if something went wrong. 

    Example: 
        >>> # Get a session token for the user alvin@acme.corp with the pwd G4nd4lf from a local Plesk instance
        >>> my_token = obtain_session_token("alvin@acme.corp", "G4nd4ld", "localhost")

    """
    request = PleskRequestPacket("server", "create_session", login=user,data={'user_ip':plesk_ip, 'source_server':''})
    api = PleskApiClient(plesk_ip)
    api.set_credentials(user,password)
    response = api.request(request)    
    return (
        ""
        if response.is_error()
        else response.to_dict()['packet']['server']['create_session']['result']['id']
    )
