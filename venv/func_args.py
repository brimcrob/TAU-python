def user_info(name, age="No age given", city="No City entered"):

    ''' this function prints name, age and city
    an argument provided to the function '''

    print("{} is {} years old, from {} ".format(name, age, city))

user_info("Brian", 51, "Edinburgh")
user_info("john")
