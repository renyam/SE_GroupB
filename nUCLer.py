class User:

    _all_users = []

    def __init__(self, name):
        """
        Constructor of the user class
        Parameters: name
        Returns: an instance of the class User
        """
        self._name = name
        self._type=None
        self._information = []
        self._email = None
        self._password = None
        self._status=False


        User._all_users.append(self) 

    def get_name(self):
        return self._name

    def set_name(self, name):
        """
        We need to make sure that name is a string
        """
        assert isinstance(name, str)
        self._name = name

    def changeUserInformation(tp,email,password):
        self._type=tp
        self._email=email
        self._password=password
        _information.append(tp,email,password)

    def get_userInformation(self):
        return self._information

    def get_login(self):
        self._status=True
    

