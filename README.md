# Password Locker

## By Vyonna Njenga.

## Description
On Average, a person has at least 7 different accounts he or she has signed into, be it email, social media, entertainment or job portal accounts.
It becomes really hard to remember all those passwords and even create new ones.
Password Locker will help manage our passwords and even generate new passwords for us.

## User Stories
These are the features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./passwordlocker.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: CA** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: LN** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, su - Sign Up, ex - exit |
| Display prompt for creating a credential | **Enter: CA** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: DC** | Prints a list of saved credentials |
| Exit application | **Enter: EX** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* pyperclip
* xclip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/vyonna6519/Password-locker.git
        $ cd Password-Locker
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 accounts_test.py
        
## Technologies Used
* Python3.6

## License
MIT &copy;2022 [LICENSE.md]()
