class Customer :
    firstName = ""
    lastName = ""
    emailAddress = ""
    password = ""
    dataSourceName = "customer"

    def __init__(self, emailAddress, firstName, lastName, password):
        self.emailAddress = emailAddress
        self.firstName = firstName
        self.lastName = lastName
        self.password = password

    def getFirstName():
        return self.firstName

    def getLastName():
        return self.lastName

    def getEmailAddress():
        return self.emailAddress

    def getPassword():
        return self.password

    def getName():
        return self.firstName + " " + self.lastName
