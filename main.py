'''This program takes an xlsx file as input and allows for the upload of bulk products on a Woocommerce store as well as
the upload of images on your server.

Written By Simone Onorato
Kingston,Ontario
support: simon.onorato@queensu.ca
all right reserved.'''

import product_upload


runProgram=True

print('Welcome to the Woocommerce Bulk Uploader')
while runProgram is True:
    print()
    print()
    print('Chose an option from the following menu:')
    print()
    print('-----------------------------------------')
    print('Bulk Upload Products - 1')
    print('Gerate Input File ---- 2')
    print('Exit ----------------- 0')
    choice=input('Enter Your Choice: ')

    if choice == '1':
        print('Product Upload')
        inputFile=str(input('Drag and drop the input file here and press Enter: '))
        productData=product_upload.readData(inputFile)
        product_upload.checkFile(productData)
        print(productData)
        product_upload.uploadProducts(productData)
        print('Uploads Complete \n')
    elif choice == '2':
        runProgram = False
        print()
        print('Bye Bye!')
    elif choice == '0':
        runProgram = False
        print()
        print('Bye Bye!')
    else:
        print('\n-------------Invalid Choice')
