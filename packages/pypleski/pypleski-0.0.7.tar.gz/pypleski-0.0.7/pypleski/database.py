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

This module's functions, generate PleskRequestPackets using the 'database' Operator.

Examples:

    Import the module to play with it: 

    >>> from pypleski import database as db

    Or import only the functions you want really want to use::

        from pypleski.database import get_customer_by_login, delete_customer_by_login, add_customer

        # To craft a PleskRequestPacket simply call the function for the appropriate packet generator
        # and save the output to a variable. 

        # Add a new mysql database with name db3 for the domain with id 3
        new_database = add_database(3,"db3", "mysql")
        print(new_database)

        # Create a Package to request Alvins information and print the request XML. 
        get_alvin = get_customer_by_login('alvin@acme.corp')
        print(get_alvin)

        # Create a Package to delete Alvin from Plesk. 
        delete_alvin = delete_customer_by_login('alvin@acme.corp')
        print(delete_alvin)
    
Notes:
    * Supported API Calls
        * ADD-DB creates database entry of the specified type, defining the subscription that will use it.
        * DEL-DB removes database entry; If a database is used by an application installed on the server, it cannot be removed.
        * GET-DB retrieves database parameters by the ID, subscription name or subscription ID.
        * ASSIGN-TO-SUBSCRIPTION moves a database to another subscription.
        * SET-DEFAULT-USER specifies a default database user that Plesk uses for accessing the database.
        * GET-DEFAULT-USER retrieves ID of administrator of a specified database.
        * ADD-DB-USER creates a database user account for a specified database.
        * DEL-DB-USER removes a database user account from a specified database.
        * GET-DB-USERS retrieves the list of users of a specified database and information about access control records for MySQL databases.
        * SET-DB-USER changes credentials of a database user and specifies hosts or IP addresses from which database users are allowed to connect to
    
    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-database-servers.35174/
"""
from pypleski.core import PleskRequestPacket

def add_database(webspace_id:int, database_name:str, database_type:str, db_server_id:int=0) -> PleskRequestPacket:
    """This Packet adds a new database to a webspace subscription

    Args:
        webspace_id (int): The webspace subscription that will hold the new Database
        database_name (str): The name for your Database
        database_type (str): The type of Database you want to create
        db_server_id (int, optional): Only required for admin on unix. Defaults to None. Specifies the ID of the database server on which the database will be created. If the node is not used, the default database server of the corresponding type will be used for the database creation. Data type: integer.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    
    Notes: 
        * Available database types:
            * mysql
            * mssql
            * postgre    
    
    Example:        
        >>> # Add a new mysql database with name db3 for the domain with id 3
        >>> request = add_database(3, "db3", "mysql")   

   
    """
    if db_server_id: # If Server ID is not 0 return with db server id tag
        return PleskRequestPacket("database","add-db", webspace_id = webspace_id, name = database_name, type = database_type , db_server_id = db_server_id)
    return PleskRequestPacket("database","add-db", webspace_id = webspace_id, name = database_name, type = database_type)


def delete_database(database_id:int) -> PleskRequestPacket:
    """ This Packet deletes the specified database

    Args:
        database_id (int): The id of the database to delete

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("database","del-db", filter={'id':database_id})


def get_databases(filter_name:str, filter_value:str) -> PleskRequestPacket:
    """ This Packet will get informataion about the datbases within a subscription
    or for a single database with the id filter.

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter    
    
    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    Notes:
        * Available Filter:
            * id: specifies the ID of a database. Data type for filter_value: int.
            * webspace-id: specifies the ID of the subscription. Data type for filter_value: int.
            * webspace-name: specifies the name of the subscription (domain). Data type for filter value: str.

    Example:    

        >>> # Get the databases associated with the domain acme.corp
        >>> request = get_databases('webspace-name', 'acme.corp')
    
    """
    return PleskRequestPacket("database","get-db", filter={filter_name:filter_value})


def assign_to_subscription(filter_name:str,filter_value:str, webspace_id:int)-> PleskRequestPacket:
    """This packet will assign a database to another subscription.

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    
    Notes:
        *Available Filter:
            *id: specifies the ID of a database. Data type for filter_value: int. \n
            *webspace-id: specifies the ID of the subscription. Data type for filter_value: int. \n     
            *webspace-name:specifies the name of the subscription (domain). Data type for filter value: str. \n    
    """
    return PleskRequestPacket("database","assign-to-subscription", filter={filter_name:filter_value}, webspace_id= webspace_id)

def get_database(db_id:str) -> PleskRequestPacket:
    """ This Packet will get information about the specified database

    Args:
        db_id(int): The id of the database.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Example:    
        >>> # Get information about the database with id 14
        >>> request = get_database(14)        
    """
    return get_databases(filter_name = 'id', filter_value = db_id)



def set_database_default_user(database_id:int, user_id:int) -> PleskRequestPacket:
    """ set the default user for the database

    Args:
        database_id (int): the id of the database
        user_id (int): the default admin user 

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("database","set-default-user", database_id = database_id, default_user_id = user_id )

def get_database_default_user(database_id:int) -> PleskRequestPacket:
    """ This Packet will get the default user for the specified database. 

    Args:
        database_id (int): The id of the database.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Example: 
        >>> # Get the default user for the database with id 76.
        >>> request = get_database_default_user(76)
     
    """
    return PleskRequestPacket("database","get-default-user", filter={'db-id':database_id})

def add_database_user(database_filter_name:str, database_filter_value:str, login_name:str, login_pwd:str, **data) -> PleskRequestPacket:
    """You can create user accounts for a certain database or create universal users with access to all databases within a subscription:

    Args:
        database_filter_name (str): The name of the filter to select a database. See Available Filters. 
        database_filter_value (any): The value for the selected filter.
        login_name (str): The login name for the new user 
        login_pwd (str): The login password for the new user 
        

    Keyword arguments:
        password_type (str): Optional. Is the password plain or encrypted? Allowed values: "plain" | "crypt". Defaults to "plain" 
        role (str): Optional. Specifies the database user role. Data type: string. Allowed values: "readWrite", "readOnly", "writeOnly".
        SPECIAL CASE acl (str): Optional. Specifies the hosts from which a database user is allowed to connect to a database.        
        SPECIAL CASE allow_access_from :node is optional. It specifies the IP addresses from which access to a database is allowed. Data type:DatabaseUserRemoteAccessRulesType, which consists of ip-address elements of the string data type

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        * Availabe Filters:
            * db-id: Used to create a user with access to the specified database.
            * webspace-id: Used to create a universal user with access to all databases within the specified subscription.
            * db-server-id: Used to create a universal user with access to all databases within the specified database server. 
    """
    
    request = {database_filter_name: database_filter_value, 'login': login_name, 'password': login_pwd} 
    request.update(data)
    return PleskRequestPacket("database", "add-db-user", __data__={ key: request.get(key, '') for key in request})

def set_database_user(user_id:int, **data) -> PleskRequestPacket:
    """ This Packet sets the data of the specified user

    Args:
        user_id (int): The id of the user to modify.
        **data (keywoards): more keyword arguments

    Keyword arguments:
        id (int): specifies the ID of the database user whose preferences are to be changed. Data type: integer.
        login (str): specifies new login name for the database user. Data type: string.
        password (str): specifies new password for the database user. Data type: string (length should be more than five digits).
        password_type (str): specifies whether it is a plain or encrypted password. Data type:string. Allowed values: plain | crypt.
        ! SPECIAL CASE acl (dict) example: acl = {'host':'127.0.0.1'}: specifies the hosts from which a database user is allowed to connect to a database. Data type:DatabaseUserAclType, which consists of host elements of the string data type.
        ! SPECIAL CASE allow_access_from :node is optional. It specifies the IP addresses from which access to a database is allowed. Data type:DatabaseUserRemoteAccessRulesType, which consists of ip-address elements of the string data type
        role node is optional. It specifies the database user role. Data type:string. Allowed values: readWrite, readOnly, writeOnly.
    
    Returns:
        PleskRequestPacket: The Packet ready to use.
    """
    
    # https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-databases/changing-credentials-access-rules-and-user-roles.34709/
    
    return PleskRequestPacket("database","set-db-users", id=user_id, **data)




def delete_database_user(user_id:int) -> PleskRequestPacket:
    """ This packet deletes the specified database user

    Args:
        user_id (int): The id of the user zou want to delete      
    
       

    !!! Something is off with the documentation on this one. The examples are confusing as they are
    probably supposed different.
    
    So this needs testing and where possible confirmation by research. 
    !!! 
    
    src: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-databases/deleting-database-users.34677/


    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("database","del-db-user",filter={'id':user_id})


def delete_all_users_from_database(database_id:int) -> PleskRequestPacket:
    """!!! This one does not make sense. !!! Supposedly, this packet deletes all users from the specified database

    Args:
        database_id (int): The id of the database   
       

    !!! Something is off with the documentation on this one. The examples are confusing as they are
    probably supposed different.
    
    So this needs testing and where possible confirmation by research. 
    !!! 
    
    src: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-databases/deleting-database-users.34677/


    Returns:
        PleskRequestPacket: PleskRequestPacket
    """    
    ## we expected to do something like this 
    # return PleskRequestPacket("database","del-db-user", filter={'id':database_id})
    # but the reference says we should do this: 
    return PleskRequestPacket("database","del-db-user", id = database_id)

def delete_all_database_users() -> PleskRequestPacket:
    """ !WARNING! This packet will delete all users from all databases the sender has access to
    
    Returns:
        PleskRequestPacket or None: The Packet ready for use. 
    """
    return PleskRequestPacket("database","del-db-user", __data__={'filter':''})
    

def get_database_users(database_id:int) -> PleskRequestPacket:
    """ This Packet retrieves information on users of the specified database

    Args:
        database_id (int): The id of the database.

    Returns:
        PleskRequestPacket: The Packet ready to use.
    """
    # https://docs.plesk.com/en-US/12.5/api-rpc/reference/managing-databases/retrieving-database-users-info.34695/
    return PleskRequestPacket("database","get-db-users", filter={'db-id':database_id})

