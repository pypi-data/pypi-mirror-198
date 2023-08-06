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
This module's functions, generate PleskRequestPackets using the 'ftp-user' Operator.

Notes:
    * Supported API Operations:
        * DEL deletes FTP account from a specified site
        * GET retrieves information on properties of specified FTP accounts on particular sites
        * ADD creates FTP account on a site specified by its name or ID    
        * SET changes properties of a specified FTP account

    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-ftp-accounts.35213/
"""
from pypleski.core import PleskRequestPacket

def add_ftp_user(name:str, password:str, webspace:str,  home:str='', create_non_existent:bool=False, quota:int=0, permissions:str="rw") -> PleskRequestPacket:    
    """ This Packet creates a new FTP user for the specified webspace. 
    
    Args:
        name (str, required): the name under which the FTP account will be known in Plesk, and the account login.   
        password (str, required): the FTP account password.
        webspace: (str or int, required): The site name or webspace id where the user should be created. 
        home (str, optional): the home directory of the account. Leave empty to use default directory. Defaults to: ''.
        create-non-existent (bool, optional): if the home directory should be created or not. This node with value true is required if the home directory defined by the home node does not exist on the site.
        quota (int, optional): the maximum total size of files and folders (in bytes) that the FTP account user can create in or upload to the home directory.
        permissions (str, optional): the FTP account permissions for home directory. Allowed values rw|r|w. Defaults to: rw.

    Notes:    
        Differences to documented XML API Calls         
        ---------------------------------------
            webspace translates to either:
                webspace-id (int, required): the ID of the site on which the FTP account is created.
            or:
                webspace-name (str, required): the name of the site (in unicode) on which the FTP account is created.

            permissions translates to up to 2 subnodes (read/ and write/)

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """

    request = {"name": name, "password": password, "home":home, "create-non-existent": create_non_existent}

    # only add quota if it set to create FTP account with unlimited quota, specify value “-1” in the quota node
    if quota:
        request["quota"] = quota

    # it is not exactly needed 
    request["permissions"] = {}
    if "r" in permissions:
            request["permissions"]["read"] = ""
    if "w" in permissions:
            request["permissions"]["write"] = ""

    # webspace-name or webspace-id should be the last node
    request['webspace-id'] = webspace
    if type(webspace) == str:       
        del request['webspace-id']    
        request['webspace-name'] = webspace              

    return PleskRequestPacket("ftp-user", "add", __data__ = request)

def set_ftp_user(filter_name:str, filter_value:str, name:str='', password:str='', home:str='', create_non_existent = False, quota:int=0, permissions:str="") -> PleskRequestPacket:
    """ This Packet is used to change the selected users.

    Args:
        filter_name (str): _description_
        filter_value (str): _description_
        name (str, optional): _description_. Defaults to None.
        password (str, optional): _description_. Defaults to None.
        home (str, optional): _description_. Defaults to ''.
        create_non_existent (bool, optional): _description_. Defaults to False.
        quota (int, optional): _description_. Defaults to None.
        permissions (str, optional): _description_. Defaults to None.
    
    Returns:
        PleskRequestPacket: PleskRequestPacket

    Notes:
        * Available Filters:
            * id  (int) : Specifies the FTP account ID in Plesk database.
            * name (str): Specifies the name of FTP account. Data type: string.
            * webspace-id (int): Specifies the unique identifier of the site on which the FTP account exists. Data type: integer.
            * webspace-name (str): Specifies the name of the site (in Unicode) on which the FTP account exists. Data type: string.

    """
    
    request={"filter":{filter_name:filter_value}}
    
    # make sure the nodes are added in the right order if used
    if name:
        request["name"] = name
    if password:
        request["password"] = password    
    request["home"] = home

    if create_non_existent:
        request["create-non-existent"] = "True"
        
    if quota:
        request["quota"] = quota
    
    if permissions:
        request["permissions"] = {}
        if "r" in permissions:
                request["permissions"]["read"] = ""
        if "w" in permissions:
                request["permissions"]["write"] = ""
        
    
    return PleskRequestPacket("ftp-user", "set", __data__ = request)




def delete_ftp_user(filter_name:str, filter_value:str) -> PleskRequestPacket:
    """ This Packet delets the selected user or all users from the selected webspace. 
    
    Args:
        filter_name (str): _description_
        filter_value (str): _description_    
   
    Returns:
        PleskRequestPacket: PleskRequestPacket

    Notes:
        * Available Filters:
            * id  (int) : Specifies the FTP account ID in Plesk database.
            * name (str): Specifies the name of FTP account. Data type: string.
            * webspace-id (int): Specifies the unique identifier of the site on which the FTP account exists. Data type: integer.
            * webspace-name (str): Specifies the name of the site (in Unicode) on which the FTP account exists. Data type: string.

    """
    return PleskRequestPacket("ftp-user", "del", filter={filter_name:filter_value})



def get_ftp_user(filter_name:str, filter_value:str) -> PleskRequestPacket:
    """ This Packet gets information on  the selected user or all users from the selected webspace.

    Args:
        filter_name (str): _description_
        filter_value (any): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket

    Notes:
        * Available Filters:
            * id  (int) : Specifies the FTP account ID in Plesk database.
            * name (str): Specifies the name of FTP account. Data type: string.
            * webspace-id (int): Specifies the unique identifier of the site on which the FTP account exists. Data type: integer.
            * webspace-name (str): Specifies the name of the site (in Unicode) on which the FTP account exists. Data type: string.

    """
    return PleskRequestPacket("ftp-user", "get", filter={filter_name:filter_value})    


