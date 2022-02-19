import unittest # Importing the unittest module
from details import details # Importing the account class


class Testdetails(unittest.TestCase):
    def setUp(self):
       
        self.new_details = details("Vyonna","vee","123456789","vyonna@g.com") # create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_details.details_name,"Vyonna")
        self.assertEqual(self.new_details.usr_name,"Vee")
        self.assertEqual(self.new_details.password,"123456789")
        self.assertEqual(self.new_details.email,"vyonna@g.com")

    def test_save_details(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_details.save_details() # saving the new account
        self.assertEqual(len(details.details_list),1)  


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            details.details_list = []    


    def test_save_multiple_details(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_details.save_details()
            test_details = details("Test","user","0712345678","test@user.com") # new account
            test_details.save_details()
            self.assertEqual(len(details.details_list),2)


    def test_delete_details(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_details.save_details()
            test_details = details("Test","user","0712345678","test@user.com") # account
            test_details.save_details()

            self.new_details.delete_details()# Deleting an account object
            self.assertEqual(len(details.details_list),1) 

    def test_find_details_by_details_name(self):
        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_details.save_details()
        test_details = details("Test","user","0711222333","test@user.com") # new account
        test_details.save_details()

        found_details = details.find_by_name("Test")

        self.assertEqual(found_details.email,test_details.email)  



    def test_details_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_details.save_details()
        test_details = details("Test","user","0711222333","test@user.com") # new account
        test_details.save_details()

        details_exists = details.details_exist("0711222333")
        self.assertTrue(details_exists)    
        
                       


if __name__ == '__main__':
    unittest.main()
    