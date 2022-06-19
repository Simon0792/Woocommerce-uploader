'''This module contains constant data that has to be changed by the user. fill out the fields with the data to allow
for server access and Woocommerce API keys.

Written by Simone Onorato
Kingston,Ontario
support: simon.onorato@queensu.ca'''


class constantData:

    #Autentication Data
    shop_url=''
    consumer_key=''
    consumer_secret=''
    version=''

    #Woocommerce store data
    shopCategories = {'category name':'category id'}
    shopBrands = {'key1': 'value1'}

    #Server Data
    serverIp = 'SERVER IP'
    serverUser = 'SERVER USERNAME'
    serverPass = 'SERVER PASSWORD'
    serverPort = '22' #ssh port
    remote_image_directory = 'REMOTE IMAGE DIRECTORY'
    remote_image_link = 'REMOTE IMAGE HTTPS LINK'