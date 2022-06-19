# Woocommerce-uploader
This Python app facilitates the bulk upload of product on your woocommerce store through restAPI calls.

Created by Simone Onorato
Kingston, Ontario.
For questions and support email simon.onorato@queensu.ca
all right reserved.

-----------------------------------------------------------------------------------------------------------
1-How to install and setup
Download all files to your computer, you will need to also download a few dependancies.
A file called requirements.txt lists them but for the sake of simplicity i am going to list them here as well.
The dependencies you need are:

#woocommerce
#openpyxl
#paramiko

#pyinstaller (optional)

Once these are installed, you can open the 'constants.py' file and insert the required data (your server information, your shop information, your categories information).

Optionally,once you have finished the previous steps, you can create an executable version (.exe) using py installer. Installing the dependencies and creating the executable file requires PIP installed. If you do not have PIP installed or if you have trouble creating the executable, this is a great tutorial that helped me along the way:
https://www.youtube.com/watch?v=UZX5kH72Yx4&ab_channel=TechWithTim

2-How to use
In the folder 'Templates' you are going to find 2 xlsx files. One was used for testing and one is a virgin files. You can copy any of these files to any directory you like in order to create listings. You will have to complete them inserting your own information. Once you run the program, the program will check for fatal errors that could result in unwanted upload or unwanted behaviours. If a mistake was made while entering the product information on these xlsx file, please follow the error output instruction to correct your file.

Once you have completed your file, run the 'main.py' file and chose option 1. The program will ask you to drag and drop the file into the terminal. If you are running the program to pycharm (or other software that do not support drag and drop into the terminal, you will have to enter the directory by hand).

This program will in order
1. Read the xlsx file provided
2. Check the file for errors
3. Ask you for the image directory in order to upload your images to the server (images must be reachable by a url)
4. Upload the products to your shop.

This is a beta version of the program, if you run into problems or would like to ask me questions please contact me at
simon.onorato@queensu.ca

Thank you :):):):)
