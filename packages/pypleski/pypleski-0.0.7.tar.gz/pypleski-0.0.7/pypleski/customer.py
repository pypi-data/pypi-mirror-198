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
This module's functions, generate PleskRequestPackets using the 'customer' Operator.

Examples:

    Import the module to play with it: 


    >>> from pypleski.customer import as customer


    Or import only the functions you want really want to use::

        from pypleski.customer import get_customer_by_login, delete_customer_by_login, add_customer

        # To craft a PleskRequestPacket simply call the function for the appropriate packet generator
        # and save the output to a variable for further. 

        # Create a Package to request the creation of a new customer and print the package. 
        create_alvin = add_customer(cname="ACME Corp.", pname="Alvin", login="alvin@acme.corp"))
        print(get_alvin)

        # Create a Package to request Alvins information and print the request XML. 
        get_alvin = get_customer_by_login('alvin@acme.corp')
        print(get_alvin)

        # Create a Package to delete Alvin from Plesk. 
        delete_alvin = delete_customer_by_login('alvin@acme.corp')
        print(delete_alvin)

Notes:
    * Currently Supported API Operations:
        * ADD creates new customer account to Plesk database.
        * GET retrieves the list of customer accounts from Plesk database.
        * DEL deletes the specified customer accounts from Plesk database.
        * SET updates/ modifies certain information about the specified customer accounts in Plesk database.
        * CONVERT-TO-RESELLER upgrades customer accounts to reseller accounts.
        * CHANGE-OWNER transfers customer accounts to a new owner (provider).
        * GET-DOMAIN-LIST retrieves information about all the customer's domains.
    
    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-customer-accounts.28788/ 
"""

import re
from typing import List
import warnings
from pypleski.core import PleskRequestPacket

GEN_INFO_REQUIRED_FIELDS = ['cname', 'pname', 'login', 'passwd', 'status', 'phone', 'fax', 'email', 'address', 'city', 'state', 'pcode', ]

def add_customer(**data) -> PleskRequestPacket:    
    r"""This Packet adds a new customer to plesk. 
    
    Keyword Args:
        cname(str, optional): Company Name
        pname(str, optional): Person Name
        login(str): Login Name
        passwd(str): Password
        status(int, optional): The Status of the Account in Plesk
        phone(str, optional): Phone Number
        fax(str, optional): Fax Number 
        email(str, optional): e-Mail Address
        address(str, optional):Address
        city(str, optional): Address City
        state(str, optional): Address State
        pcode(str, optional): Address Post Code
        country(str, optional): Address Country
        external_id(int, optional): Customers External Identifier
        description(str, optional): Additional Description in Plesk

    Returns:    
        PleskRequestPacket: The RequestPacket ready for use.
    
    Example:
    
        >>> # Create a new Customer with name Garry, login name garry1 and the Password T0pS3crt.P4$$w0Rd.    
        >>> request = add_customer(pname="Garry", login = "garry1", passwd = "T0pS3crt.P4$$w0Rd" )
    
    """           
    return PleskRequestPacket("customer", "add", gen_info = {key: data.get(key, '') for key in GEN_INFO_REQUIRED_FIELDS})

def delete_all_customers() -> PleskRequestPacket:
    r""" This Packet deletes customer accounts available to the Sender.
   
    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        This function only exists to avoid accidental deletion of all customers
        with the delete_customer() function.
        If you are absolutely sure you want to do this, use this function instead.


    Example:     
        >>> # Create a Packet with the request to delete ALL customer accounts
        >>> # available to the Sender.
        >>> request = delete_all_customers()
    
    """  

    return PleskRequestPacket("customer","del", filter = "")



def delete_customer(filter_name:str, filter_value:str) -> PleskRequestPacket:
    r""" This Packet deletes the specified customer.

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (str): The Value for the selected Filter.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    
    Notes:        
        *Available Filter: 
            * id: The customer's ID.
            * login: The customers Login Name.
            * guid: The customers GUID.
            * external-id: The customers external identifier.

        If you want to delete all accounts, use the delete_all_customers() function.
        
    Example:     
        >>> Create a Packet with the request to delete the customer with the id 12.
        >>> request = delete_customer('id', 12)    
    """
    if not filter_name:
        warnings.warn("Pypleski will introduce an intentional error to fail validation on the Server.To delete all accounts, use delete_all_accounts() instead.")
        filter_name = "Error"
        filter_value = "To delete all accounts, use delete_all_accounts() instead."

    return PleskRequestPacket("customer","del", filter = { filter_name: filter_value })


def delete_customer_by_login(login:str) -> PleskRequestPacket:
    r""" This Packet deletes the customer with the specified login name.
    Args:
        login(str): the users login name

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Example:     
        >>> # Create a Packet with the request to delete the customer
        >>> # with the login name 'alvin@acme.corp'.
        >>> request = delete_customer_by_login('alvin@acme.corp')
    
    """
    return PleskRequestPacket("customer","del", filter = { 'login': login })

def delete_customer_by_guid(guid:str) -> PleskRequestPacket:
    r""" This Packet deletes the customer with the specified GUID.
    Args:
        guid (str): The users GUID in Plesk.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    
    Example: 
        >>> # Delete the customer with the GUID f35187a8-8edf-11ed-a1eb-0242ac120002
        >>> request = delete_customer_by_guid('f35187a8-8edf-11ed-a1eb-0242ac120002')
    """


    return PleskRequestPacket("customer","del", filter = { 'guid': guid })

def delete_customer_by_id(user_id:int) -> PleskRequestPacket:
    r""" This Packet deletes the customer with the specified id.
    Args:
        user_id (int): the users 

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    
    Example:
    
        >>> # Create a Packet with the request to delete the customer with the id 12.
        >>> request = delete_customer_by_id(12)
    
    """
    return PleskRequestPacket("customer","del", filter = { 'id': user_id })

def get_customer_info(filter_name:str="", filter_value:str="", datasets: List[str] = None) -> PleskRequestPacket:
    r"""This Packet gets information on the specified customer. If no Filter is used, all

    Args:
        filter_name (str, Optional): The Filter used to select the customer.
        filter_value (str, Optional): The Value for the selected Filter.        
        datasets (List[str], Optional): The datasets node. Defaults to None.
    
    Returns:
        PleskRequestPacket: The PleskRequestPacket ready to use.

    Notes: 
        * Available Filter: 
            * id: The customer's ID.
            * login: The customers Login Name.
            * guid: The customers GUID.
            * external-id: The customers external identifier.

        * Available Datasets:
            * gen_info: General Information
            * stat: Statistics

    Examples: 
        Without a Filter set, this packet will retrieve all available customer accounts available to the Sender.
        Not setting the datasets List will result into retrieving the gen_info dataset.                
        >>> # This will return all customer with only their general information dataset
        >>> client.request(get_customer_info()) 
        
        To get information on a specific user use a filter.            
        >>> # This will return the customer with id 1 with only their general information dataset
        >>> client.request(get_customer_info('id','1'))        

        If you want to retrieve a specific or multiple datasets use the datasets keyword with a List.         
        >>> # This will return all customers with only their statistics.
        >>> client.request(get_customer_info(datasets = ['stat']))         
    
        If you want to retrieve multiple datasets, make sure the order is correct. 
        
        >>> # This will return an error packet
        >>> client.request(get_customer_info(datasets = ['stat', 'gen_info'])) 
        >>> # out: {"packet": {"@version": "1.6.7.0", "system": {"status": "error", "errcode": "1014", "errtext": "Parser error: Request is invalid. Error in line 1: Element 'gen_info': This element is not expected."}}}


        >>> # This will return all customers with their general information and statistics.
        >>> client.request(get_customer_info(datasets = ['gen_info', 'stat'])) 
           
    """         
    if datasets is None:
        datasets = ["gen_info"]
    # the second arguments value will create <dataset><[dataset] /> </dataset>
    if filter_name:
        return  PleskRequestPacket("customer", "get", filter={filter_name: filter_value}, dataset={d:'' for d in datasets})
    return  PleskRequestPacket("customer", "get", filter='', dataset={d:'' for d in datasets}) 

def get_customer_by_login(login:str, datasets: List[str] = None) -> PleskRequestPacket:
    r"""This Packet retrieves the specified dataset for the specified login name.

    Args:
        login (str): The customers login name.                    
        dataset (str): The dataset node. Valid values: "gen_info", "stat". Defaults to "gen_info".

    Returns:
        PleskRequestPacket: The Plesk Request Packet ready to use.

    Notes:    
        * Available Datasets:
            * gen_info: General Information
            * stat: Statistics

    Examples:    
        >>> # Get general info about carl@acme.corp    
        >>> request = get_customer_by_login('alvin@acme.corp')

        >>> # Get the statistics for alvin@acme.corp    
        >>> request = get_customer_by_login('alvin@acme.corp',['stat'])
    
    """         
    if datasets is None:
        datasets = ["gen_info"]
    # the second arguments value will create <dataset><[dataset] /> </dataset>
    return get_customer_info('login', login, datasets) 

def get_customer_by_id(user_id:int, datasets: List[str] = None) -> PleskRequestPacket:
    """This Packet retrieves the specified dataset for the specified customer's id.

    Args:
        user_id (int): The customer's id.                    
        datasets (List[str]): The dataset node. Defaults to None.

    Returns:
        PleskRequestPacket: The Plesk Request Packet ready to use.

    Notes:
        * Available Datasets:
            * gen_info: General Information
            * stat: Statistics

    Examples:
    
    >>> # Create a Request Package that requests only general information for the user with id 12      
    >>> request = get_customer_by_id(12)

    >>> # Create a Request Packege that reqests only the statistics for the user with the id 12.
    >>> request = get_customer_by_id(12,['stat'])

    >>> # Create a Request Packege that reqests the statistics and general information for the user with the id 12.
    >>> request = get_customer_by_id(12,['gen_info', 'stat'])
    
    """            
    return get_customer_info('id', str(user_id), datasets) 

def get_customers(datasets: List[str] = None) -> PleskRequestPacket:     
    """This Packet gets informatino about all customers available to the Sender.

    Args:
        datasets (List[str]): The dataset node. Defaults to None.        
    
    Returns:
        PleskRequestPacket: The Plesk Request Packet ready to use.
    
    Notes:
        If no Dataset is given, gen_info will be used by default.

        * Available Datasets:
            * gen_info: General Information
            * stat: Statistics

    Examples:
    
        >>> # Create a Request Package that requests only general information
        >>> # for all customers available to the Sender.   
        >>> request = get_customers()

        >>> # Create a Request Packege that reqests only the statistics
        >>> # for all customers available to the Sender.
        >>> request = get_customers(['stat'])

        >>> # Create a Request Package that requests the statistics and general information
        >>> # for all customers available to the Sender.
        >>> request = get_customers(['gen_info', 'stat'])
    
    """         
    # the second arguments value will create <dataset><[dataset] /> </dataset>
    return get_customer_info("", "", datasets)

def set_customer_info(filter_name:str, filter_value:str, **data) -> PleskRequestPacket:
    """This Packet changes the selected fields (keywords) for the specified customer

    Args:
        filter_name (str): The Filter Name to select the customer. 
        filter_value (str): The Filter Value.   

    Keyword Args:
        cname(str): Company Name
        pname(str): Person Name
        login(str): Login Name
        passwd(str): Password
        status(int): The Status of the Account in Plesk
        phone(str): Phone Number
        fax(str): Fax Number 
        email(str): e-Mail Address
        address(str):Address
        city(str): Address City
        state(str): Address State
        pcode(str): Address Post Code
        country(str): Address Country
        external_id(int): Customers External Identifier
        description(str): Additional Description in Plesk

    Returns:
        PleskRequestPacket: The Plesk Request Packet ready to use.
    
    Notes:
        *Available Filter: 
            * id: The customer's ID.
            * login: The customers Login Name.
            * guid: The customers GUID.
            * external-id: The customers external identifier.

    Examples:

        >>> # Create a packet that request the change of the company name
        >>> # for the customer with id 12 to "ACME CORP.". 
        >>> request = set_customer_info('id', 12, cname="ACME CORP.")


    """       
    return PleskRequestPacket("customer", "set", filter={filter_name:filter_value}, gen_info = data)

def change_owner(filter_name:str, filter_value:str, new_owners_login:str, ip:str="", ip_addresses:List[str]= None, plan:str="") -> PleskRequestPacket:
    """This Packet changes the owner of a customer. Currently only one ip address supported.

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (str): The Value for the selected Filter. 
        new_owners_login (str): The login name of the future owner.
        ip (str, optional): The ip that should be assigned to the customer.
        ip_addresses (List[str], optional):  The List of IP addresses to assigned to the customer from the IP pool of the new owner.
        plan: The name of the new plan defined by the new owner. 

    Returns:
        PleskRequestPacket: The Plesk Request Packet ready to use.

    Notes:
        * Available Filter: 
            * id: The customer's ID.
            * login: The customers Login Name.
            * guid: The customers GUID.
            * external-id: The customers external identifier.
    
        * Changes:
            * You can now set more then one IP address with one packet.

    Example:
        
        >>> # Change the ownership of the user carl@acme.corp to faceless.manager@acme.corp 
        >>> # and assign the IP addresses 10.10.10.2 and 11.10.10.5
        >>> request = change_owner(
        >>>     'login', 
        >>>     'carl@acme.corp', 
        >>>     'faceless.manager@acme.corp, 
        >>>     ip_addresses=['10.10.10.2','11.10.10.5']
        >>>     )
        
    """
   
    if ip_addresses is None:
        ip_addresses = [ip]
    ipv4 = re.compile(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.){3}(25[0-5]|(2[0-4]|1\d|[1-9]|)\d)$") 

    packet = PleskRequestPacket("customer","change-owner", filter={filter_name: filter_value},new_owner_login = new_owners_login )

    for ip in ip_addresses:
        if ipv4.match(ip): #Match IpV4
            packet.add_data_to_node(packet.operation, ipV4_address = ip)
        else: 
            # otherwise try as ipV6  
            # TODO: add regex for this one
            packet.add_data_to_node(packet.operation, ipV6_address = ip)
    if plan:
        packet.add_data_to_node(packet.operation, plan_name = plan)            
   
    return packet


def convert_to_reseller(filter_name:str, filter_value:str) -> PleskRequestPacket:
    r""" This Packet converts the selected customer's account to a reseller account in Plesk

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (any): The Value for the selected Filter.     

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    
    Notes:
        * Available Filter: 
            * id: The customer's ID.
            * login: The customers Login Name.
            * guid: The customers GUID.
            * external-id: The customers external identifier.

    Example:
    
        >>> # Convert the customer with login carl@acme.corp 
        >>> # into a reseller account
        >>> request = convert_to_reseller('login', 'carl@acme.corp')
    
    """
    return PleskRequestPacket("customer", "convert-to-reseller", filter={filter_name:filter_value})

def get_domain_list(filter_name:str, filter_value:str) -> PleskRequestPacket:
    r""" This Packet gets the selected customer's domain list.

    Args:
    * filter_name (str): The Filter used to select the customer.
    * filter_value (any): The Value for the selected Filter. 
       
    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        * Available Filter: 
            * id: The customer's ID.
            * login: The customers Login Name.
            * guid: The customers GUID.
            * external-id: The customers external identifier.

    Example:
        >>> # Get the domain list for the customer with login name carl@acme.corp. 
        >>> request = get_domain_list('login', 'carl@acme.corp')

    """
    return PleskRequestPacket("customer", "get-domain-list", filter={filter_name,filter_value})

