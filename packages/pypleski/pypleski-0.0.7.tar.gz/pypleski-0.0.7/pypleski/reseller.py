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
This module's functions, generate PleskRequestPackets using the 'reseller' Operator.


Notes:

    *Supported API Operations
        * CONVERT-TO-CUSTOMER converts a reseller account into a customer account.

    *Not Yet Supported Operations:
        * ADD creates a reseller account.
        * SET updates reseller account settings.
        * GET retrieves information on reseller accounts.
        * DEL removes reseller accounts.

        * IPPOOL-ADD-IP adds IP addresses to a reseller’s IP pool.
        * IPPOOL-DEL-IP removes IP addresses from a reseller’s IP pool.
        * IPPOOL-SET-IP changes type of IP addresses (shared/exclusive) in a reseller’s IP pool.

        * CFORM-BUTTONS-LIST displays a buttons list for a reseller’s home page.
        * GET-LIMIT-DESCRIPTOR retrieves reseller limit descriptor.
        * GET-PERMISSION-DESCRIPTOR retrieves reseller permission descriptor.

        * SWITCH-SUBSCRIPTION operation changes a reseller plan for a reseller account.
        * SYNC-SUBSCRIPTION operation rolls reseller account settings back to the values defined in an associated reseller plan.
        * ADD-PACKAGE includes an app in the specified reseller account.
        * REMOVE-PACKAGE excludes an app from the specified reseller account.
        * ENABLE-APS-FILTER excludes all apps from the specified reseller account.
        * DISABLE-APS-FILTER includes all available apps in the specified reseller account.
        * GET-DOMAIN-LIST retrieves information about all the reseller’s domains.

    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-reseller-accounts.60289/
"""
from pypleski.core import PleskRequestPacket

"""The id node is optional. It specifies the reseller ID. Data type: id_type (common.xsd).
The login node is optional. It specifies the reseller login. Data type: string.
The guid node is optional. It specifies the reseller GUID. Data type: none.
The all node is optional. It is used for applying an operation for all resellers. Data type: none.
The external-id node is optional. It specifies a reseller GUID in the Panel components (for example, Business Manager). Data type: string.
"""

GEN_INFO_REQUIRED_FIELDS = ['cname', 'pname', 'login', 'passwd', 'status', 'phone', 'fax', 'email', 'address', 'city', 'state', 'pcode', 'country', 'external-id', 'description', 'power-user']

def add_reseller_account(**data) -> PleskRequestPacket:
    """This Packet adds a new reseller account     

    Keyword args:
        cname (str): Company Name
        pname (str): Person Name
        login (str) : Login Name
        passwd (str): Password
        status (int): 
        phone (str):
        fax (str):
        email (str):
        address (str):
        city (str):
        state (str):
        pcode (str):
        country (str): 
        external_id (int):
        description (str):
        power_user (bool):

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """       
    return PleskRequestPacket("reseller", "add", gen_info = {key: data.get(key, '') for key in GEN_INFO_REQUIRED_FIELDS})

def set_reseller_settings() -> PleskRequestPacket:
    return PleskRequestPacket("reseller", "add")

def get_reseller(reseller_id:str="") -> PleskRequestPacket:
    return PleskRequestPacket("reseller", "get")

def delete_reseller(filter_name:str,filter_value:str) -> PleskRequestPacket:
    """ Delete a reseller.

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (any): The Value for the selected Filter.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        * Available Filter: 
            * id (int): 
            * login (str):
            * guid (str):        
            * external-id (int):
    """
    return PleskRequestPacket("customer","del", filter = { filter_name: filter_value })
    
def add_ip_to_pool() -> PleskRequestPacket:
    return PleskRequestPacket("reseller", "ippool-add-ip")

def set_ip_type_for_pool() -> PleskRequestPacket:
    return PleskRequestPacket("reseller", "ippool-set-ip")

def delete_ip_from_pool() -> PleskRequestPacket:
    return PleskRequestPacket("reseller", "ippool-del-ip")



def convert_to_customer(filter_name:str, filter_value:str, all:bool=False) -> PleskRequestPacket:
    """ This Packet converts the selected resellers's account to a customer account in Plesk

     Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (any): The Value for the selected Filter. 
        all (bool): Coverts all Reseller Accounts to Customer accounts.       
   
    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        * Available Filter: 
            * id (int): 
            * login (str):
            * guid (str):        
            * external-id (int):

    """
    if all:
        return PleskRequestPacket("customer", "convert-to-reseller", filter="all")
    return PleskRequestPacket("customer", "convert-to-reseller", filter={filter_name:filter_value})

