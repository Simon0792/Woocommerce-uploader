'''This module allows for server communication, while uploading files to your woocommerce store, you will have to
provide images reachable through url, this module allows for easy upload of images from your local machine to your server.

Written by Simone Onorato
Kingston,Ontario
support: simon.onorato@queensu.ca'''

from paramiko import SSHClient, AutoAddPolicy
import getpass
import platform
import requests
import os
from constants import constantData


#declaring global variables
myDir = os.getcwd()
serverIp=constantData.serverIp
serverUser=constantData.serverUser
serverPass=constantData.serverPass
serverPort=constantData.serverPort
remote_image_directory= constantData.remote_image_directory
currentDirectory=os.getcwd()
softwareDirectory=os.path.dirname(os.getcwd())
platformOs = platform.system()

#this function gets the user id on windows platforms
def getUserId():
    #opsys = platform.platform()
    username = getpass.getuser()
    return username

#this function uploads images to the server that are needed temporarily for the wordpress upload
def uploadTempFiles():
    print('Image upload process started..\n')
    local_image_director=input('Please drag and drop here your local image folder: ')
    print()
    #create ssh connection
    client = SSHClient()
    #load host keys
    username=getUserId()
    client.load_host_keys(f'\\Users\\{username}\\.ssh\\known_hosts')
    client.load_system_host_keys()
    #Known host policy - not sure what this does
    client.set_missing_host_key_policy(AutoAddPolicy())

    #Declare host, username, password and port
    client.connect(serverIp, username=serverUser, password=serverPass, port=serverPort)
    print('successfully connected via SSH')
    #establish sftp connection for secure file transfer
    sftpConnection=client.open_sftp()
    print('succesfully connected via SFTP')
    print()
    print('Starting images upload')
    print()
    for img in os.listdir(local_image_director):
        print()
        print(f'Uploading: {img}')
        sftpConnection.put(f'{local_image_director}{img}', f'{remote_image_directory}{img}')

    sftpConnection.close()
    client.close()
    print()
    print('All upload complete, All connection closed')

    sftpConnection.close()
    client.close()
    print()
    print('Connection Closed')

'''-----------------------------------------------------------------------'''

#this function clears the image folder on the server when the images are not anymore needed
def clearTemp():
    #create ssh connection
    client = SSHClient()
    #load host keys
    username=getUserId()
    client.load_host_keys(f'\\Users\\{username}\\.ssh\\known_hosts')
    client.load_system_host_keys()
    #Known host policy - not sure what this does
    client.set_missing_host_key_policy(AutoAddPolicy())

    #Declare host, username, password and port
    client.connect(serverIp, username=serverUser, password=serverPass, port=serverPort)
    print('successfully connected via SSH')
    #establish sftp connection for secure file transfer
    sftpConnection=client.open_sftp()
    print('succesfully connected via SFTP')
    print()
    print('Checking Temporary Directory for Files...')
    print()
    temp_dir=constantData.remote_image_directory
    open_dir=sftpConnection.listdir(path=temp_dir)
    total_files=0
    for img in open_dir:
        total_files+=1

    print('Total Files in Temporary Directory:', total_files)
    userInput=input(f'Remove {total_files} files? (y or n) ')
    if userInput == 'y' or userInput =='Y':
        for img in open_dir:
            print(f'Removing: {img}')
            sftpConnection.remove(temp_dir + img)
            print()
        print(f'{total_files} files removed.')
    else:
        print('Files not removed.')

    sftpConnection.close()
    client.close()
    print()
    print('Connection Closed')

#check if an image has been uploaded on server
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True

