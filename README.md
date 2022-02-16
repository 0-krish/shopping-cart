
## shopping-cart

### How do I run the game?
- Open the command line interface
- Activate game-specific conda environment with Python 3.8:
  - ```conda create -n shopping-env Python=3.8```
  - ```conda activate shopping-env```
- Install required packages using pip and "requirements.txt" file:
  - ```pip install -r requirements.txt```
- Run game using command:
  - ```python shopping_cart.py```

### Testing

To run tests on the logic that decides the winner of
the game, type the following command into the command
line interface:
- ```pytest```
