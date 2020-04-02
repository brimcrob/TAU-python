def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. His email is "
    "{}.".format(fname, lname, company, email,))


application("brian","jones","a@a.com",
"big comp",8000,start_date="Jan 2020")
