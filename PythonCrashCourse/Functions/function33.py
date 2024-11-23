def make_car(manufacturer,model,**kwargs):
    my_car={}
    my_car['manufacturer']=manufacturer
    my_car['model']=model
    for key,value in kwargs.items():
        my_car[key]=value
    return my_car

car_details=make_car('Subaru','outback',color='Blue',tow_package=True)
print(car_details)