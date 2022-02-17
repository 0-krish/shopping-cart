
## shopping-cart

### How do I run the system?
- Open the command line interface
- Activate a conda environment specific to the shopping-cart system with Python 3.8:
  - ```conda create -n shopping-env Python=3.8```
  - ```conda activate shopping-env```
- Install required packages using pip and "requirements.txt" file:
  - ```pip install -r requirements.txt```
- Run system using command:
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
