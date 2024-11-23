def build_profile(first_name,last_name,**kwargs):
    profile = {}
    profile['first_name']=first_name
    profile['last_name']=last_name
    for key,value in kwargs.items():
        profile[key]=value
    return profile


user_info=build_profile('John','Doe',age=25,qualification='bachelors',job='Software Developer')
print(user_info)