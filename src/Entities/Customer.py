class Customer :
    first_name = ""
    last_name = ""
    email_address = ""
    password = ""
    data_source_name = "customer"

    def __init__(self, email_address, first_name, last_name, password):
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def get_first_name():
        return self.first_name

    def get_last_name():
        return self.last_name

    def get_email_address():
        return self.email_address

    def get_password():
        return self.password

    def get_name():
        return self.first_name + " " + self.last_name
