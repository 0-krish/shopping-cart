# OPIM-243: Project 3
## Shopping Cart Program

### How do I run the program?
- Open the command line interface
- Activate a conda environment specific to the shopping-cart program with Python 3.8:
  - ```conda create -n shopping-env Python=3.8```
  - ```conda activate shopping-env```
- Install required packages using pip and "requirements.txt" file:
  - ```pip install -r requirements.txt```
- Run the program using command:
  - ```python shopping_cart.py```


### How do I customize the tax rate?

To customize the tax rate to your store's location:
- Create a file with the following name: ".env"
- In the file, enter your desired tax rate as shown in the example below:
  - ```TAX_RATE = 0.085```
  - Ensure you use the exact format as prescribed above
  - Enter your tax rate as a decimal number between 0 and 1
  - The default tax rate is 8.75%
  - Ensure the ".env" file is in the same directory as the rest of these files


### How do I setup and select the Google Sheet for my data?

#### Setup Google Sheet
- Setup instructions adapted from Prof. Rossetti's [instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/gspread.md).
- On the [Google Developer Console](https://console.developers.google.com/cloud-resource-manager):
  - Create a new project. 
  - Click on your project
    - Then search for the "Google Sheets API" and enable it
    - Next, search for the "Google Drive API" and enable it
- From the [API Credential](https://console.developers.google.com/apis/credentials) page, create and download your credentials to use Google's APIs:
  - Click "Create Credentials" for a "Service Account"
    - Follow the prompt to create a new service account named something like "spreadsheet-service", and add a role of "Editor".
  - Click on the newly created service account from the "Service Accounts" section, and click "Add Key" to create a new "JSON" credentials file for that service account
    - Download the resulting .json file (this will likely happen automatically)
  - Move a copy of the credentials file into your project repository.
    - Name the .json file "google-credentials.json" 
    - Put this in a file in a folder named "auth" in the program folder
    - Note the file path: "auth/google-credentials.json"

#### Select Google Sheet 
- Add a variable named GOOGLE_SHEET_ID to the .env file 
  - instructions to create this file can be found above in the documentation to customize the tax rate 
- Find the ID for your Google Sheet on it's URL
  - The centralized Google Sheet for this company has the following ID:
    - 1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpIs
  - If you create your own Google Sheet, it must follow the exact same format as the [centralized sheet](https://docs.google.com/spreadsheets/d/1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI/edit#gid=1014123801)
- The code on your .env file should look as below:
  - ```GOOGLE_SHEET_ID = 1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpIs```

### How do I select the csv file for my data?

- There is a folder named "data" in the program folder
- Add a file named "products.csv" with the data to that folder
- Find a file named "default_products.csv" in the data folder
  - Your products.csv file must follow the **exact** format as this file
- You are now able to update your product list as required

### How do I setup this program's email capabilities? 
- Setup instructions adapted from Prof. Rossetti's [instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md).
- Sign up for a [SendGrid account](https://signup.sendgrid.com/)
  - Complete "Single Sender Verification"
- Create a [SendGrid API](https://app.sendgrid.com/settings/api_keys) key with "full access" permissions
  - Store this key in an environment variable called SENDGRID_API_KEY in the .env file
    - .env file approach explained in the customized tax rate documentation 
  - Set another environment variable called SENDER_ADDRESS in the .env file
    - This must be the same as the email associated with your single sender account on SendGrid
- After completing these steps, you will be ready to send email receipts to your customers!

