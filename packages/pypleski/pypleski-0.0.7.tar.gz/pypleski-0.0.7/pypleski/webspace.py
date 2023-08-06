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

r"""This module's functions, generate PleskRequestPackets using the 'webspace' Operator.

Notes:

    * Supported API Operations:
        * ADD creates a subscription and sets general information, hosting settings, limits, preferences  
        * GET retrieves information on subscriptions from Plesk database
        * DEL removes subscriptions from Plesk database
        * GET-LIMIT-DESCRIPTOR retrieves descriptor of limits
        * GET-PERMISSION-DESCRIPTOR retrieves descriptor of permissions
        * GET-PHYSICAL-HOSTING-DESCRIPTOR retrieves descriptor of hosting settings
        * GET_TRAFFIC retrieves information on traffic spent by the site(s) between two dates
        * SWITCH-SUBSCRIPTION switches a subscription to a different service plan

    * Not yet Supported Operations:
        * SET updates subscription settings in Plesk database    
        * CFORM_BUTTONS_LIST retrieves list of buttons displayed on the subscription        
        * SET_TRAFFIC sets information on traffic spent by the specified sites(s)        
        * SYNC-SUBSCRIPTION rolls back to settings defined by associated service plan
        * ADD-SUBSCRIPTION adds a add-on plan to a subscription
        * REMOVE-SUBSCRIPTION detaches an add-on plan from a subscription
        * ADD-PACKAGE adds an application to the specified subscription
        * REMOVE-PACKAGE removes an application from the specified subscription
        * ADD-PLAN-ITEM adds custom options of service plans (additional services) to the specified subscription
        * REMOVE-PLAN-ITEM removes custom options of service plans (additional services) from the specified subscription
        * ENABLE-APS-FILTER turns on applications list for specified subscriptions and makes available only added applications, by default all applications are available
        * DISABLE-APS-FILTER turns off applications list for specified subscriptions and makes available all applications
        * GET-CHANGED
        * DB_SERVERS manages the list of database servers available within the specified subscription

    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-subscriptions.33852/


"""

from typing import Any, List, Dict
from pypleski.core import PleskRequestPacket


def add_webspace(domain: str, ip: str, owner_filter: str, owner_filter_value: str, plan_filter: str, plan_filter_value: str, external_id: str = ""):
    """Add a virtual hosting subscription. This Packet only requires a plan, owner, ip and domain name 
    to add a webhosting subscription and activates it.

    Args:
        domain (str): The domain name for the subscription.
        ip (str): _descript
        owner_filter (str): _description_
        owner_filter_value (str): _description_
        plan_filter (str): _description_
        plan_filter_value (str): _description_
        external

    Returns:
        _type_: _description_

    Notes:
        * Available Owner Filter
            * owner_id : The ID of the account the subscription will be assigned to. 
            * owner_login: The login name of the account the subscription will be assigned to. 
            * owner_guid : The GUID of the account the subscription will be assigned to.

        * Available Plan Filter
            * plan_id : _description_. 
            * plan_name: _description_.
            * plan_guid: _description_.
    """
    if external_id:
        return PleskRequestPacket("webspace", "add", __data__={
            'name': domain,
            owner_filter: owner_filter_value,
            'ip_address': ip, plan_filter: plan_filter_value,
            'external-id': external_id
        })
    return PleskRequestPacket("webspace", "add", __data__={'name': domain, owner_filter: owner_filter_value, 'ip_address': ip, plan_filter: plan_filter_value})




def add_custom_webspace_subscription(domain_name: str, ip_address: str,
                   owner_id=0,
                   owner_login: str = "",
                   owner_guid: str = "",
                   hosting_type: str = "vrt_hst",

                   status: int = 0,
                   external_id: str = "",
                   hosting: Dict[str, str] = None,
                   limits: Dict[str, str] = None,
                   prefs: Dict[str, str] = None,
                   plan_id: int = 0, plan_name: str = "", plan_guid: str = "") -> PleskRequestPacket:
    """ This Packet will add a Webspace Subscription with more complex settings. It is a chunky peace of banana pie and will mostlikely break things.
    Do not touch yet. 

    More technical speaking, the PleskRequestPacket class, uses dicts which are nice but won't allow for 2 keys with the same name on the same level. 
    We are curretly working on a solution for this problem involving the use of typed lists, new types or a mix of both. 

    Args:
        domain_name (str): The name of the subscription
        ip_address (str): The IP from the servers pool this subscription
            will be assigned
        owner_id (int, optional): The ID of the account the subscription will be assigned to. Defaults to 0.
        owner_login (str, optional): The login name of the account the subscription will be assigned to. Defaults to "".
        owner_guid (str, optional): The GUID of the account the subscription will be assigned to.. Defaults to "".
        hosting_type (str, optional): The hosing type. Defaults to "vrt_hst".
        status (int, optional): The Status of the subscripton. Defaults to 0.
        external_id (str, optional): An external identifier for the subscription. Defaults to "".
        hosting (Dict, optional): This is not fully tested and almost guaranteed to brake.  Defaults to None.
        limits (Dict, optional): This is not fully tested and almost guaranteed to brake. Defaults to None.
        prefs (Dict, optional): This is not fully tested and almost guaranteed to brake. Defaults to None.
        plan_id (int, optional): _description_. Defaults to 0.
        plan_name (str, optional): _description_. Defaults to "".
        plan_guid (str, optional): _description_. Defaults to "".

    Returns:
        PleskRequestPacket: _description_
    """
    packet = PleskRequestPacket("webspace", "add", name=domain_name)

    if owner_id:
        packet.add_data_to_node(packet.operation, owner_id=owner_id)
    elif owner_login:
        packet.add_data_to_node(packet.operation, owner_login=owner_login)
    elif owner_guid:
        packet.add_data_to_node(packet.operation, owner_guid=owner_guid)
    # if no owner is given the subscriptio will be assigned to the sender of

    # hosting type is set anyways so we'll add to the package
    packet.add_data_to_node(packet.operation, htype=hosting_type)
    # The ip_address node is required by the function call so for now no check for it here
    packet.add_data_to_node(packet.operation, ip_address=f"{ip_address}")

    # More optional nodes being added here
    if status:
        packet.add_data_to_node(packet.operation, status=f"{status}")

    if external_id:
        packet.add_data_to_node(packet.operation, external_id=f"{external_id}")

    if hosting:
        # Set might not keep the order so we iterate
        packet.add_data_to_node(packet.operation, hosting={d for d in hosting})

    if limits:
        packet.add_data_to_node(packet.operation, limits={d for d in limits})

    if prefs:
        packet.add_data_to_node(packet.operation, pref={d for d in prefs})

    if plan_id:
        packet.add_data_to_node(packet.operation, plan_id=f"{plan_id}")
    elif plan_guid:
        packet.add_data_to_node(packet.operation, plan_guid=f"{plan_guid}")
    elif plan_name:
        packet.add_data_to_node(packet.operation, plan_name=f"{plan_name}")

    return packet


def get_webspace(filter_name: str = "", filter_value: str = "", datasets: List[str] = None) -> PleskRequestPacket:
    """ This Packet will get information for the specified subscription. Get's general information 
    on all available Subscription by default. Set a Filter and/or specifie a list of datasets 
    you want to retrieve.

    Args:
        filter_name (str): The filter to use. Defaults to "". 
        filter_value (str): The value to use with the filter. Defaultes to "".
        datasets (List[str]): Specify the Datasets you want to retrieve. Defaults to None.

    Returns:
        PleskRequestPacket: Plesk API Response     

    Notes:
        * Available Filter:  
            * id: The ID of the webspace. 
            * owner-id: The ID of the owner.
            * owner-login: The login name of the owner.
            * guid: The GUID of the webspace.
            * owner-guid: The owners GUID.    
            * external-id: The webspace's external identifier. 
            * owner-external-id: The owner's external identifier. 

        * Available Datasets:
            * gen_info: General Information
            * hosting: Hosting Settings (complete)
            * hosting-basic: Hosting Settings (limited)
            * limits: Subscripton Limits 
            * stat: Statistics
            * prefs: Webspace Preferences
            * disk_usage: Disk Usage
            * performance: Performance Settings
            * subscriptions: Lock- & Sync-Status and Addon Plans 
            * permissions: Webspace Permissions
            * plan-items: Additional Service Items
            * php-settings: PHP Server Settings
            * resource-usage: Webspace Ressource Usage
            * mail: Mail Settings
            * aps-filter: Application Filter
            * packages: Available Applications

    Examples: 
        Without a Filter set, this packet will retrieve all available webspace subscriptions under the senders account.
        Not setting the datasets List will result into retrieving the gen_info dataset.


        >>> # This will return all webspace subscriptions 
        >>> # with only their general information dataset
        >>> client.request(get_webspace()) 


        To get information on a specific user use a filter.

        >>> # This will return all webspace subscriptions for the owner-id 1
        >>> # with only their general information dataset
        >>> client.request(get_webspace('owner-id','1'))


        If you want to retrieve a specific or multiple datasets use the datasets keyword with a List. 

        >>> # This will return all webspace subscriptions 
        >>> # with only their hosting settings.
        >>> client.request(get_webspace(datasets = ['hosting']))   

        >>> # This will return all webspace subscriptions 
        >>> # with their general information and hosting settings.
        >>> client.request(get_webspace(datasets = ['gen_info', 'hosting'])) 

    """
    if datasets is None:
        datasets = ["gen_info"]
    if filter_name:
        # the second arguments value will create <dataset><[dataset] /> </dataset>
        return PleskRequestPacket("webspace", "get", filter={filter_name: filter_value}, datasets={d: '' for d in datasets})
    # the second arguments value will create <dataset><[dataset] /> </dataset>
    return PleskRequestPacket("webspace", "get", filter="", dataset={d: '' for d in datasets})


def delete_webspace(filter_name: str, filter_value: int) -> PleskRequestPacket:
    """Delete a subscription

    Args:
        login (str): customers login name

    Returns:
         PleskRequestPacket: Response from Plesk
    """
    return PleskRequestPacket("webspace", "del", filter={filter_name: filter_value})


def delete_all_webspaces() -> PleskRequestPacket:
    """ This Packet delets all Webspace Subscriptions the Sender can access. 

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("webspace", "del", filter='')


def get_cform_buttons(filter_name: str, filter_value: str) -> PleskRequestPacket:
    return PleskRequestPacket("webspace", "cform_buttons_list", filter={filter_name: filter_value})


def get_traffic(filter_name: str = "", filter_value: str = "", since_date: str = "", to_date: str = "") -> PleskRequestPacket:
    """ This packet retrieves the traffic usage statistics. By default it will set the request for all 
    webspace subscriptions available to the sender with their full traffic usage history since creation.
    You can set a filter if you're looking for a particular webspace's traffic usage statistics.

    If you want to see only a certain time frame, specify the since_date and/or to_date in Format YYYY-MM-DD.

    Args:
        filter_name (str, optional): The Filter used to select the customer.
        filter_value (str), optional: The Value for the selected Filter.
        since_date (str, optional): The start date of the requested timeframe
            in Format YYYY-MM-DD
        to_date (str, optional): The end date of the requested timeframe
            in Format YYYY-MM-DD


    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        * Available Filter:  
                * id: The ID of the webspace. 
                * owner-id: The ID of the owner.
                * owner-login: The login name of the owner.
                * guid: The GUID of the webspace.
                * owner-guid: The owners GUID.    
                * external-id: The webspace's external identifier. 
                * owner-external-id: The owner's external identifier. 

    Example:     
        >>> # Create a Packet with the request the traffic 
        >>> # usage statistics for the webspace subscription 
        >>> # with the id 29.
        >>> request = get_traffic('id', 29)        
    """
    request = {'filter': {filter_name: filter_value} if filter_name else ''}

    if since_date:
        request['since-date'] = since_date

    if to_date:
        request['to-date'] = to_date

    return PleskRequestPacket("webspace", "get-traffic", __data__=request)


def set_traffic(filter_name: str, filter_value: str, max_traffic) -> PleskRequestPacket:
    return PleskRequestPacket("webspace", "set-traffic", filter={filter_name: filter_value})


def get_limit_descriptor(filter_name: str = "", filter_value: Any = None) -> PleskRequestPacket:
    """ This packet retrieves the descriptor of limits. By default it will set the request for all 
    webspace subscriptions available to the sender. You can set a filter if you're looking for a
    particular webspace's limit descriptor.

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (str): The Value for the selected Filter.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        * Available Filter:  
                * id: The ID of the webspace. 
                * owner-id: The ID of the owner.
                * owner-login: The login name of the owner.
                * guid: The GUID of the webspace.
                * owner-guid: The owners GUID.    
                * external-id: The webspace's external identifier. 
                * owner-external-id: The owner's external identifier. 

    Example:     
        >>> # Create a Packet with the request to retrieve the Limits Descriptor
        >>> # for the webspace subscription with the id 29.
        >>> request = get_limit_descriptor('id', 29)        
    """
    #     GET-LIMIT-DESCRIPTOR retrieves descriptor of limits
    if filter_name:
        return PleskRequestPacket("webspace", "get-limit-descriptor", filter={filter_name, filter_value})
    return PleskRequestPacket("webspace", "get-limit-descriptor", filter='')


def get_permission_descriptor(filter_name: str = "", filter_value: Any = None) -> PleskRequestPacket:
    """ This packet retrieves the descriptor of permissions. By default it will set the request for all 
    webspace subscriptions available to the sender. You can set a filter if you're looking for a
    particular webspace's limit descriptor.

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (str): The Value for the selected Filter.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        * Available Filter:  
                * id: The ID of the webspace. 
                * owner-id: The ID of the owner.
                * owner-login: The login name of the owner.
                * guid: The GUID of the webspace.
                * owner-guid: The owners GUID.    
                * external-id: The webspace's external identifier. 
                * owner-external-id: The owner's external identifier. 

    Example:     
        >>> # Create a Packet with the request to retrieve the Permissions Descriptor
        >>> # for the webspace subscription with the id 29.
        >>> request = get_permission_descriptor('id', 29)        
    """

    #   GET-PERMISSION-DESCRIPTOR retrieves descriptor of permissions
    if filter_name:
        return PleskRequestPacket("webspace", "get-permission-descriptor", filter={filter_name, filter_value})
    return PleskRequestPacket("webspace", "get-permission-descriptor", filter='')


def get_physical_hosting_descriptor(filter_name: str = "", filter_value: Any = None) -> PleskRequestPacket:
    """ This packet retrieves the descriptor of the physical hosting settings. By default it will set the request for all 
    webspace subscriptions available to the sender. You can set a filter if you're looking for a
    particular webspace's physical hosting settings descriptor.

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (str): The Value for the selected Filter.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        * Available Filter:  
                * id: The ID of the webspace. 
                * owner-id: The ID of the owner.
                * owner-login: The login name of the owner.
                * guid: The GUID of the webspace.
                * owner-guid: The owners GUID.    
                * external-id: The webspace's external identifier. 
                * owner-external-id: The owner's external identifier. 

    Example:     
        >>> # Create a Packet with the request to retrieve the Physical Hosting
        >>> # Descriptor for the webspace subscription with the id 29.
        >>> request = get_physical_hosting_descriptor('id', 29)        
    """

    if filter_name:
        return PleskRequestPacket("webspace", "get-physical-hosting-descriptor", filter={filter_name, filter_value})
    return PleskRequestPacket("webspace", "get-physical-hosting-descriptor", filter='')


def switch_subscription(filter_name: str, filter_value: Any, new_plan_guid: str = "", new_plan_external_id: str = "") -> PleskRequestPacket:
    """ This packet switches the plan for the specified subcsription. By default it will remove the current plan,
    without applying a new plan. The plan's GUID prioritizes over the plan's external id if both are given.

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (str): The Value for the selected Filter.
        new_plan_guid (str, optional): The GUID of the future plan.
        new_plan_external_id (str, optional): The external identifier of the plan.

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    Notes:
        * Available Filter:  
                * id: The ID of the webspace. 
                * owner-id: The ID of the owner.
                * owner-login: The login name of the owner.
                * guid: The GUID of the webspace.
                * owner-guid: The owners GUID.    
                * external-id: The webspace's external identifier. 
                * owner-external-id: The owner's external identifier. 

    Example:     
        >>> # Create a Packet with the request to change the
        >>> # plan for the webspace subscription with the id 29
        >>> # to the plan with GUID dd4a0d71-ddeb-4a96-9ae1-bcaf0e71731c
        >>> request = switch_subscription('id', 29, new_plan_guid = 'dd4a0d71-ddeb-4a96-9ae1-bcaf0e71731c')        
    """
    #    SWITCH-SUBSCRIPTION switches a subscription to a different service plan
    request = PleskRequestPacket(
        "webspace", "switch-subscription", filter={filter_name: filter_value})

    if not new_plan_guid and not new_plan_external_id:
        request.add_data_to_node(request.operation, no_plan='')
        return request

    if new_plan_guid:
        request.add_data_to_node(request.operation, plan_guid=new_plan_guid)
        return request

    # If a new_plan_guid was not provided but a new_plan_external_id
    request.add_data_to_node(
        request.operation, plan_external_id=new_plan_external_id)
    return request


def sync_subscription(id, domain, package, **data) -> PleskRequestPacket:
    #    SYNC-SUBSCRIPTION rolls back to settings defined by associated service plan

    return PleskRequestPacket("webspace", "sync-subscription")


def add_subscription_addon_plan():
    # ADD-SUBSCRIPTION adds a add-on plan to a subscription
    pass


def remove_subscription_addon_plan():
    # REMOVE-SUBSCRIPTION detaches an add-on plan from a subscription
    pass


def add_plan_item():
    # ADD-PLAN-ITEM adds custom options of service plans (additional services) to the specified subscription
    pass


def remove_plan_item():
    # REMOVE-PLAN-ITEM removes custom options of service plans (additional services) from the specified subscription
    pass


def enable_aps_filter():
    # ENABLE-APS-FILTER turns on applications list for specified subscriptions and makes available only added applications, by default all applications are available
    pass


def disable_aps_filter():
    # DISABLE-APS-FILTER turns off applications list for specified subscriptions and makes available all applications
    pass


def __get_changed():
    # GET-CHANGED ????????
    pass


def set_billing_info():
    pass


def add_db_servers():
    # https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-subscriptions/managing-database-servers-available-in-a-subscription/adding-available-databases-servers.72631/
    pass


def remove_db_servers():
    pass


def list_db_servers():
    pass
