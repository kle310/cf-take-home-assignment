#### How to set up the project:
```bash
pip install pytest-playwright
playwright install
```

#### How to execute the tests:
```bash
pytest
```

# Test Plan

Create a test plan ensuring the following is covered:
o happy path verifying the functionality of the password generator 

(default is 6 + lowercase + uppercase)

1. 12 characters, all options enabled
2. copy to clipboard works, both buttons
3. re-generate button works
4. options can be toggled on/off

with any edge cases / negative test cases as seen fit
1. min == 6, max == 32
2. min option == 1 


