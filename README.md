# Dice Game - Python

## Python program that simulates a simple dice game:

1. The program should draw two random numbers from 1 to 6.

   - Rules: 
   - a. If any number other than 1 or 6 is drawn, return the result immediately.
   - b. If 6 occurs twice, draw again and return all results up to 3 times. 
   - c. If 1 occurs twice, draw again and return only the next valid draw (not including double 1's), up to 3 attempts total. 
   - d. If after 3 draws no valid result is obtained, return an empty list.

 2. Write unit tests code.    

 3. Create a command-line interface that allows the user to specify the number of times to run the simulation.

 4. Log each run's results to a file.

 ## How to use

 1. Clone the repository.
 ```
 git clone https://gitlab.com/MCKY0822/simpledicegame-python.git
 ```

 2. Navigate to the directory.
```
cd "location of directory".
```

3. Create virtual environment and activate.
```
python3 -m venv venv
source venv/bin/activate
```

4. Install dependency.
```
pip install pytest
```

5. Run the script.
```
python dice_game.py (number of times to run)
python dice_game.py 1000
```

6. Application will save log results.
```
log_file.txt
```

7. Test the code if the conditions are working.
```
pytest
```
