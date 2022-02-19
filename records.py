class details:
    """
    Class that generates new instances of users.
    """
    details_list = [] #empty details list

    def __init__(self,details_name,usr_name,password,email):
        self.details_name = details_name
        self.usr_name = usr_name
        self.password = password
        self.email = email    

    def save_details(self):

        '''
        save_details method saves details objects into details_list
        '''

        details.details_list.append(self)    


    def delete_details(self):

        '''
        delete_details method deletes a saved details from the details_list
        '''

        details.details_list.remove(self)   


    @classmethod
    def find_by_name(cls,name):
        for details in cls.details_list:
            if details.details_name == name:
                return details  


    @classmethod
    def details_exist(cls,name):
        '''
        Method that checks if a details exists from the details list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the details exists
        '''
        for details in cls.details_list:
            if details.password == name:
                    return details

        return False      


    @classmethod
    def display_details(cls):  #check this line later
        '''
        method that returns the details list
        '''
        return cls.details_list
        