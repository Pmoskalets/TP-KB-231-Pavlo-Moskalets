class Student:
    def __init__(self, name, phone, email, address):
        self._name = name
        self._phone = phone
        self._email = email
        self._address = address

    def modify(self, **kwargs):
        """Оновлює дані студента. Приймає ключові аргументи."""
        if 'name' in kwargs and kwargs['name']:
            self._name = kwargs['name']
        if 'phone' in kwargs and kwargs['phone']:
            self._phone = kwargs['phone']
        if 'email' in kwargs and kwargs['email']:
            self._email = kwargs['email']
        if 'address' in kwargs and kwargs['address']:
            self._address = kwargs['address']

    def details(self):
        """Повертає строкове представлення об'єкта."""
        return f"Name: {self._name}, Phone: {self._phone}, Email: {self._email}, Address: {self._address}"

    # Додаткові методи доступу до полів
    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def email(self):
        return self._email

    @property
    def address(self):
        return self._address

    @name.setter
    def name(self, value):
        if value:
            self._name = value

    @phone.setter
    def phone(self, value):
        if value:
            self._phone = value

    @email.setter
    def email(self, value):
        if value:
            self._email = value

    @address.setter
    def address(self, value):
        if value:
            self._address = value
