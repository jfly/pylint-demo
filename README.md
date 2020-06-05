## pylint checker naming issue

This is a simple demonstration that Pylint 2.5+ got stricter than Pylint 2.4
about the names of checkers. See relevant issue: https://github.com/PyCQA/pylint/issues/3666

# Setup
1. Clone this repo and `cd` into it.
2. Create and activate a virtual environment.
    `python3 -m venv .venv && source .venv/bin/activate`

# To reproduce the issue using Pylint 2.5.0

    ```
    $ pip install pylint==2.5.0
    $ pylint --version
    pylint 2.5.0
    astroid 2.4.1
    Python 3.8.3 (default, May 17 2020, 18:15:42)
    [GCC 10.1.0]
    $ PYTHONPATH=./custom_checker pylint --load-plugins=no_jfly demo.py
    ************* Module demo
    demo.py:5:0: E0012: Bad option value '-no-jfly' (bad-option-value)
    demo.py:5:4: W5000: Has a variable named 'jfly' (j3-no-jfly)

    -------------------------------------------------------------------
    Your code has been rated at -2.00/10 (previous run: 0.00/10, -2.00)
    ```

# Proof that it works under Pylint 2.4.4

    ```
    $ pip install pylint==2.4.4
    $ pylint --version                                                 
    pylint 2.4.4
    astroid 2.3.3
    Python 3.8.3 (default, May 17 2020, 18:15:42) 
    [GCC 10.1.0]
    $ PYTHONPATH=./custom_checker pylint --load-plugins=no_jfly demo.py

    ---------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: -2.00/10, +12.00)
