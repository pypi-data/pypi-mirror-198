#!/usr/local/bin/python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
'''
------------------------------------------------------------------------

 Description:

 Module to provide class hierachy to simplify access to the Netskope APIs

 Date Last Updated: 20230321

 Todo:

    api_key format verification upon inifile read.

 Copyright (c) 2023-2023 John Neerdael, Netskope

 Redistribution and use in source and binary forms,
 with or without modification, are permitted provided
 that the following conditions are met:

 1. Redistributions of source code must retain the above copyright
 notice, this list of conditions and the following disclaimer.

 2. Redistributions in binary form must reproduce the above copyright
 notice, this list of conditions and the following disclaimer in the
 documentation and/or other materials provided with the distribution.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

------------------------------------------------------------------------
'''
import logging
import configparser
import requests
import os
import re

# ** Global Vars **
__version__ = '0.0.1'
__author__ = 'John Neerdael'
__email__ = 'jneerdael@netskope.com'
__doc__ = 'https://python-netskope.readthedocs.io/en/latest/'
__license__ = 'BSD'


# Custom Exceptions
class IniFileSectionError(Exception):
    '''
    Exception for missing section in ini file
    '''
    pass

class IniFileKeyError(Exception):
    '''
    Exception for missing key in ini file
    '''
    pass

class APIKeyFormatError(Exception):
    '''
    Exception for API key format mismatch
    '''
    pass

# ** Facilitate ini file for basic configuration including API Key

def read_nss_ini(ini_filename):
    '''
    Open and parse ini file

    Parameters:
        ini_filename (str): name of inifile

    Returns:
        config (dict): Dictionary of Netskope configuration elements

    Raises:
        IniFileSectionError
        IniFileKeyError
        APIKeyFormatError
        FileNotFoundError

    '''
    # Local Variables
    cfg = configparser.ConfigParser()
    config = {}
    ini_keys = ['url', 'api_key']
 
    # Check for inifile and raise exception if not found
    if os.path.isfile(ini_filename):
        # Attempt to read api_key from ini file
        try:
            cfg.read(ini_filename)
        except configparser.Error as err:
            logging.error(err)

        # Look for Netskope section
        if 'Netskope' in cfg:
            for key in ini_keys:
                # Check for key in Netskope section
                if key in cfg['Netskope']:
                    config[key] = cfg['Netskope'][key].strip("'\"")
                    logging.debug('Key {} found in {}: {}'
                                 .format(key, ini_filename, config[key]))
                else:
                    logging.error('Key {} not found in Netskope section.'
                                 .format(key))
                    raise IniFileKeyError('Key "' + key + '" not found within' 
                        '[Netskope] section of ini file {}'.format(ini_filename))
                    
        else:
            logging.error('No Netskope Section in config file: {}'
                         .format(ini_filename))
            raise IniFileSectionError('No [Netskope] section found in ini file {}'
                                     .format(ini_filename))
        
    else:
        raise FileNotFoundError('ini file "{}" not found.'.format(ini_filename))

    return config


def verify_api_key(apikey):
    '''
    Verify format of API Key
    
    Parameters:
       apikey (str): api key

    Returns:
        bool: True is apikey passes format validation
    '''
    if re.fullmatch('[a-z0-9]{32}|[a-z0-9]{64}', apikey, re.IGNORECASE):
        status = True
    else:
        status = False

    return status


class nss:
    '''
    Parent Class to simplify access to the Netskope APIs for subclasses
    Can also be used to genericallly access the API

    Raises:
        IniFileSectionError
        IniFileKeyError
        APIKeyFormatError
        FileNotFoundError
    '''

    def __init__(self, cfg_file='config.ini', 
                       api_key='', 
                       url=''):
        '''
        Read ini file and set attributes

        Parametrers:
            cfg_file (str): Override default ini filename
            api_key (str): Use API Key instead of ini
            url (str): Override URL, applies only if api_key specified
            api_version (str): API version, applies only if api_key specified

        '''

        self.cfg = {}

        if api_key:
            self.api_key = api_key
            # Create base URLs
            self.base_url = url
            
        else:
            # Read ini file
            self.cfg = read_nss_ini(cfg_file)
            self.api_key = self.cfg['api_key']
        
            # Create base URLs
            self.base_url = self.cfg['url']

        # Verify format of API Key
        if verify_api_key(self.api_key):
            logging.debug('API Key passed format verification')
        else:
            logging.debug('API Key {} failed format verification'
                          .format(self.api_key))
            raise APIKeyFormatError('API Key {} failed format verification'
                                    .format(self.api_key))

        # Define generic header
        self.headers = ( {'content-type': 'application/json',
                        'Netskope-Api-Token': self.api_key} )
        

        # Netskope URLs
        self.privateapps_url = self.base_url + '/api/v2/steering/apps/private'

        # List of successful return codes
        self.return_codes_ok = [200, 201, 204]

        return


    def _add_params(self, url, first_param=True, **params):
        # Add params to API call URL
        if len(params):
            for param in params.keys():
               if first_param:
                   url = url + '?'
                   first_param = False
               else:
                   url = url + '&'
               url = url + param + '=' + params[param]
        
        return url


    def _apiget(self, url):    
     # Call Netskope API
        try:
            response = requests.request("GET",
                                        url,
                                        headers=self.headers)
        # Catch exceptions
        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.debug("url: {}".format(url))
            raise

        # Return response code and body text
        # return response.status_code, response.text
        return response


    def _apipost(self, url, body, headers=""):    
        # Set headers
        if not headers:
            headers = self.headers
     
        # Call Netskope API
        try:
            response = requests.request("POST",
                                        url,
                                        headers=headers,
                                        data=body)
        # Catch exceptions
        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.debug("url: {}".format(url))
            logging.debug("body: {}".format(body))
            raise

        # Return response code and body text
        return response

 
    def _apidelete(self, url, body=""):    
     # Call Netskope API
        try:
            response = requests.request("DELETE",
                                        url,
                                        headers=self.headers,
                                        data=body)
        # Catch exceptions
        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.debug("URL: {}".format(url))
            logging.debug("BODY: {}".format(body))
            raise

        # Return response code and body text
        return response


    def _apiput(self, url, body):    
     # Call Netskope API
        try:
            response = requests.request("PUT",
                                        url,
                                        headers=self.headers,
                                        data=body)
        # Catch exceptions
        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.debug("url: {}".format(url))
            logging.debug("body: {}".format(body))
            raise

        # Return response code and body text
        return response

 
    def _apipatch(self, url, body):    
        # Call Netskope API
        try:
            response = requests.request("PATCH",
                                        url,
                                        headers=self.headers,
                                        data=body)
        # Catch exceptions
        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.debug("url: {}".format(url))
            logging.debug("body: {}".format(body))
            raise

        # Return response code and body text
        return response


    def _use_obj_id(self, url, id="", action=""):
        '''
        Update URL for use with object id
        
        Parameters:
            id (str): Netskope Object id
            action (str): e.g. nextavailableip

        Returns:
            string : Updated url
        '''
        # Check for id and next available IP
        if id:
            url = url + '/' + str(id)
            if action:
                url = url + '/' + action
        else:
            if action:
                logging.debug("Action {} not supported without " 
                              "a specified object id.")
        
        return url
    
    
    def _not_found_response(self, b1object='object'):
        '''
        Generate a response object without an API call

		Parameters:
            b1object (str): Name of object to use in error

        Returns:
            requests response object
        
        '''
        err_msg = f'{{"error":[{{"message":"{b1object} not found"}}]}}'
        response = requests.Response()
        response.status_code = 400
        response._content = str.encode(err_msg)

        return response


    # Public Generic Methods
    def get(self, url, id="", action="", **params):
        '''
        Generic get object wrapper 

        Parameters:
            url (str):      Full URL
            id (str):       Optional Object ID
            action (str):   Optional object action
        
        Returns:
            response object: Requests response object
        '''
        # Build url
        url = self._use_obj_id(url, id=id, action=action)
        url = self._add_params(url, **params)
        logging.debug("URL: {}".format(url))

        response = self._apiget(url)

        return response


    def post(self, url, id="", action="", body="", **params):
        '''
        Generic Post object wrapper 

        Parameters:
            url (str):      Full URL
            id (str):       Optional Object ID
            action (str):   Optional object action
            
        Returns:
            response object: Requests response object
        '''
        # Build url
        url = self._use_obj_id(url, id=id, action=action)
        url = self._add_params(url, **params)
        logging.debug("URL: {}".format(url))

        response = self._apipost(url, body)

        return response


    def create(self, url, body=""):
        '''
        Generic create object wrapper 

        Parameters:
            url (str):  Full URL
            body (str): JSON formatted data payload

        Returns:
            response object: Requests response object
        '''
        # Build url
        logging.debug("URL: {}".format(url))

        # Make API Call
        response = self._apipost(url, body)

        return response


    def delete(self, url, id="", body=""):
        '''
        Generic delete object wrapper

        Parameters:
            url (str):  Full URL
            id (str):   Object id to delete
            body (str):     JSON formatted data payload

        Returns:
            response object: Requests response object
        '''
        # Build url
        if id:
            url = self._use_obj_id(url,id=id)
        logging.debug("URL: {}".format(url))

        # Make API Call
        response = self._apidelete(url, body=body)

        return response


    def update(self, url, id="", body=""):
        '''
        Generic create object wrapper 

        Parameters:
            url (str):  Full URL
            body (str): JSON formatted data payload

        Returns:
            response object: Requests response object
        '''
        # Build url if needed
        url = self._use_obj_id(url, id=id)
        logging.debug("URL: {}".format(url))

        # Make API Call
        response = self._apiput(url, body)

        return response


    def replace(self, url, id="", body=""):
        '''
        Generic create object wrapper 

        Parameters:
            url (str):  Full URL
            body (str): JSON formatted data payload

        Returns:
            response object: Requests response object
        '''
        # Build url
        url = self._use_obj_id(url, id=id)
        logging.debug("URL: {}".format(url))

        # Make API Call
        response = self._apipatch(url, body)

        return response