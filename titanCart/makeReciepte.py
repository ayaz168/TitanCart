def makeOrderTXT(orderNo,UserName,Price,productsList,ShippingInfo,paid):
    filename=orderNo
    filename+=".txt"
    f = open("Orders/{str1}".format(str1=filename), "w")   # 'r' for reading and 'w' for writing
    f.write("Name: "+UserName+'\n')
    f.write("Order Id: "+orderNo+'\n')
    if not paid:
        f.write("COD::TotalPrice: "+str(Price)+'\n')
    else:
        f.write("Already Paid.Just Deliver "+'\n')
    f.write("###################################--ITEMS--###################################"+'\n')
    for i in productsList:
        strX="ID: "+str(i.item.ProductId)+"  :  "+"Name: "+i.item.ProductTitle+"  :  "+"Price: "+str(i.item.Price)+"  :  "+"Qty: "+str(i.quantity)+'\n'
        f.write(strX)    # Write inside file 
    f.write("################################--Delivery Info--#############################"+'\n')
    f.write("Recievers Title: "+ShippingInfo.Title+'\n')
    f.write("Recievers Name: "+ShippingInfo.Shipping_Name+'\n')
    f.write("Recievers Number: "+ShippingInfo.Phone+'\n')
    if ShippingInfo.Alt_Phone:
        f.write("Recievers Alt. Number: "+ShippingInfo.Alt_Phone+'\n')
    f.write("Recievers Address: "+ShippingInfo.Shipping_Address+'\n')
    if ShippingInfo.Alt_Phone:
        f.write(ShippingInfo.Shipping_Address_b+'\n')
    f.write("Zip Code: "+ShippingInfo.Zip+'\n')
    if ShippingInfo.ShippingNote:
        f.write("Note : "+ShippingInfo.ShippingNote+'\n')
    f.write("This is a Computer Generated Reciept\n")
    f.write("################################--TitanCart--################################"+'\n')
    f.close()
def getOrderString(orderNo):
    filename=orderNo
    filename+=".txt"
    return filename