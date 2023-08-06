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

r"""This module's functions, generate PleskRequestPackets using the 'mail' Operator.

Notes:
    * Supported API Operations:
        * CREATE creates a mail account on a specified site and sets a collection of settings for it
        * UPDATE serves to update mail account settings. It is specially designed to operate lists of mail group members, repository files, and automatic reply messages set for the mail account
        * GET_INFO serves to retrieve various information about the specified mail accounts from Plesk database
        * REMOVE removes the specified mail account and all its settings from Plesk database
        * ENABLE turns on the mail service on the specified site
        * DISABLE turns off the mail service on the specified site
        * GET_PREFS gets mail service preferences set for the specified sites            
        * SET_PREFS sets mail service preferences for the specified sites
        * RENAME renames the specified mail box

    **Plesk Reference Link**: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-mail.34477/
"""
from pypleski.core import PleskRequestPacket

def add_account(site_id:int, name:str, **account_settings) -> PleskRequestPacket:
    """ This Packet creates a new email account from the given name for the domain with the given site_id with the provided account_settings

    Args:
        site_id (int): The id of the site the email account should be created for. 
        name (str): 

        account_settings: Account Settings as keyword = value pairs

    Available keywords:

        

    Returns:
        PleskRequestPacket: The Request Packet ready to use.
    """
    return PleskRequestPacket("mail", "create", filter={'site-id': site_id, 'name': name}, **account_settings)

def update_account(site_id:int, name:str, **account_settings) -> PleskRequestPacket:
    """This Packet updates the account settings for the selected account. 

    Args:
        site_id (int): The ID of the site that holds the account.
        name (str): The name of the account
        
        account_settings: Account Settings as keyword = value pairs

    Available keywords:

        

    Returns:
        PleskRequestPacket: The Request Packet ready to use.
    """
    return PleskRequestPacket("mail", "set", filter={'site-id': site_id, 'name': name}, **account_settings)

def get_account_settings(site_id:int, name:str) -> PleskRequestPacket:
    """This Packet retrieves the settings of an account.

    Args:
        site_id (int): The ID of the site that holds the account.
        name (str): The name of the account

    Returns:
        PleskRequestPacket: The Request Packet ready to use.
    """
    return PleskRequestPacket("mail", "get_info", filter={'site-id': site_id, 'name': name})

def get_all_accounts_settings(site_id:int, name:str) -> PleskRequestPacket:
    """_summary_

    Args:
        site_id (int): _description_
        name (str): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("mail", "get_info", filter={'site-id': site_id, 'name': name})

def delete_account(site_id:int, name:str) -> PleskRequestPacket:
    """This Packet deletes the specified account

   Args:
        site_id (int): The ID of the site that holds the account.
        name (str): The name of the account

    Returns:
        PleskRequestPacket: The Request Packet ready to use.
    """
    return PleskRequestPacket("mail", "delete", filter={'site-id': site_id, 'name': name})

def delete_all_accounts(site_id:int) -> PleskRequestPacket:
    """This Packet deletes all accounts for the selected site.

   Args:
        site_id (int): The ID of the site that holds the accounts.
        

    Returns:
        PleskRequestPacket: The Request Packet ready to use.
    """
    return PleskRequestPacket("mail", "delete", filter={'site-id': site_id})

def rename_account(site_id:int, name:str, new_name:str) -> PleskRequestPacket:
    """This Packet renames an account.

    Args:
        site_id (int): The ID of the site that holds the account.
        name (str): The name of the account.
        new_name (str): The new name of the account

    Returns:
        PleskRequestPacket: The Request Packet ready to use.        
    """
    return PleskRequestPacket("mail", "rename", __data__={'site-id': site_id, 'name': name, 'new-name': new_name})

def enable_mail(site_id:int) -> PleskRequestPacket:
    """_summary_

    Args:
        site_id (int): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("mail", "enable", __data__ = {'site-id': site_id})

def disable_mail(site_id:int) -> PleskRequestPacket:
    """_summary_

    Args:
        site_id (int): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("mail", "disable", __data__ = {'site-id':site_id})

def get_mail_settings(site_id:int) -> PleskRequestPacket:
    """_summary_

    Args:
        site_id (int): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("mail", "get_prefs", filter={'site-id':site_id})

def set_mail_settings(site_id:int, **mail_settings)-> PleskRequestPacket:
    """_summary_

    Args:
        site_id (int): _description_

    Returns:
        PleskRequestPacket: PleskRequestPacket
    """
    return PleskRequestPacket("mail", "set_prefs", filter={'site-id':site_id}, **mail_settings)



