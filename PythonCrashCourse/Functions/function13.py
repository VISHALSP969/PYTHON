from PythonCrashCourse.Strings import full_name


def get_formatted_name(first_name,last_name,middle_name=""):
    if middle_name:
        return (first_name+" "+middle_name+" "+last_name).title()
    else:
        return (first_name+" "+last_name).title()

musician=get_formatted_name("jimi","hendrix")
print(musician)

musician=get_formatted_name("john","hooker","lee")
print(musician)