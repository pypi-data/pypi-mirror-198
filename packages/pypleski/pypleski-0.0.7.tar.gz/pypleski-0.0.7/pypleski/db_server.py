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
This module's functions, generate PleskRequestPackets using the 'db_server' Operator.


Notes:
    * Supported API Operations:
        * ADD creates a database server entry of the specified type, specifying the login and password of the database administrator.
        * SET updates properties of the specified database server.
        * DEL removes a database server entry. Only remote database servers can be specified. The default database server cannot be removed.
        * SET-DEFAULT sets a remote database server entry as default for its DBMS type. Only remote database servers can be specified.
        * GET-DEFAULT retrieves ID of a default database server.
        * GET retrieves the database server info by the server ID.
        * GET-SUPPORTED-TYPES get the DBMS types supported by the Plesk.
        * GET-LOCAL retrieves ID of a local database server.
    
    Plesk Reference Link: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-database-servers.35174/
"""

from pypleski.core import PleskRequestPacket

def add_db_srv(host:str,port:int, admin:str, password:str="", db_type:str="mysql") -> PleskRequestPacket:
    """This Packet creates a database server entry of the specified type, specifying the login and password of the database administrator.

    Args:
        host (str): IP address or name of the database server you want to add. 
        port (int): port of the database server.         
        admin (str): The admin login name for the server.
        password (str, optional): The admins password. Defaults to: None.
        db_type (str): database server type. Allowed values: mysql | postgresql | mssql. Defaults to: mysql.
    """
    keywords = {'host':host,'port':port, 'type': db_type, 'admin':admin}
    if password:
        keywords['password']=password
    return PleskRequestPacket("db-server","add",__data__ = keywords)


def delete_db_srv(id:int) -> PleskRequestPacket:
    """ This Packet removes a database server entry. Remote database servers only. Default database server cannot be removed.

    Args:
        id (int): The ID of the database server to detach from plesk.

    Returns:
        _type_: _description_
    """
     
    return PleskRequestPacket("db-server","add", filter = {'id':id})


def __delete_db_srvrs(ids:list) -> None:
    """ This Packet removes the given database server entries. Remote database servers only. Default database server cannot be removed.

    Args:
        ids (list): _description_

    
    Example 
        >>> delete_sb_srvrs([1,67,34]) 

    TODO:
        DOES NOT WORK WITH CURRENT USE OF DICT AS MULTIPLE KEYS WITH THE SAME NAME ARE REQUIRED. WE NEED TO BUILD THIS PACKET SLIGHTLY DIFFERENT THAN OTHERS!
    """
   
    pass
    

def set_db_srv(srv_id:int, host:str, port:int, admin:str, password:str="", db_type:str="mysql") -> PleskRequestPacket:
    """This Packet updates properties of the specified database server.

    Args:
        srv_id (int): The id of the server to update with the given settings
        host (str): IP address or name of the database server you want to add. 
        port (int): port of the database server.         
        admin (str): The admin login name for the server.
        password (str, optional): The admins password. Defaults to: None.
        db_type (str): database server type. Allowed values: mysql | postgresql | mssql. Defaults to: mysql.
    
    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    
    keywords = {'host':host,'port':port, 'type': db_type, 'admin':admin}
    if password:
        keywords['password']=password
    keywords['id'] = srv_id
    return PleskRequestPacket("db-server","add",__data__ = keywords)

def get_db_srv(srv_id:int) -> PleskRequestPacket:
    """This Packet retrieves the database server info by the server ID.

    Args:
        srv_id (int): The server id

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """    
    return PleskRequestPacket("db-server","get", filter={'id':srv_id})

def set_default_srv(filter_name:str,filter_value:str) -> PleskRequestPacket:
    """This Packet sets a remote database server entry as default for its DBMS type. Only remote database servers can be specified._summary_

    Args:
        filter_name (str): _description_
        filter_value (any): _description_
    
    Returns:
        PleskRequestPacket: The RequestPacket ready for use.


    Notes: 
        * Available Filters:
            * id (int): The id of the remote database server to be used as default server.
            * type (str):  The type of local database server to be used as default. Allowed values: mysql | postgresql | mssql.

    """   
    return PleskRequestPacket("db-server","set-default", filter = {filter_name:filter_value})

def get_default_srv(db_type:str='mysql') -> PleskRequestPacket:
    """This Packet retrieves ID of a default database server.

    Args:
        db_type (str, optional): The DBMS type. Defaults to 'mysql'.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("db-server","set-default", filter = {'type':db_type})


def get_supported_types() -> PleskRequestPacket:
    """This packet gets the DBMS types supported by the Plesk.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use. 
    """
    
    return PleskRequestPacket("db-server","get-supported-types")

def get_local(DBMS_type:str="") -> PleskRequestPacket:
    """This Packet retrieves ID of a local database server.

    Args:
        DBMS_type (str, optional): The DBMS type. Leave empty to get all default database servers. Defaults to None. Allowed values: mysql | postgresql | mssql | None.


    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """    
    if DBMS_type:
        return PleskRequestPacket("db-server","get-local", filter={'type':DBMS_type})
    return PleskRequestPacket("db-server","get-local", filter={'':''})



