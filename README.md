# SMDF
Demand Forecasting

# If you want do project from scratch you follow this step
1. Create github repository
2. Clone new Github repository
    a. open your terminal like cmd, gitbash and run run
    ```
    git clone "here you paste your git repository path"
    ```
    b. open vs code
    ```
    code .
    ```
    c. In VS code open terminal
    
2. Create virtual environment And Activate
    ```
    conda create -p venv python==3.8.0 -y
    ```
    ```
    conda activate venv/
    ```
3. First create template.py folder for Make folder structure
    ```
    touch template.py
    ```
    copy code of template.py
    ```
    run template.py
    ```
    Folder structure created

4. After Complete Each Module you should update the git hub repo
    a. add
        ````
        git add .
        ````
    b. commit
        ```
        git commit -m "write message which module complete
        ```
    c. push
        ```
        git push origin main
        ```
5. You should write some code inside setup.py for made local package Also made
 ```
 __init__.py
 ```
    in all file
6. Write some installation library inside the requirement.txt
7. Also in requirement.txt write below 
      ```
      -e .
      ```
8. Install package
    ```
    pip install -r requirement.txt
    ```
9. You write some code for logger for track project inside src/SMDF/logging 
10. You also made custom exception And Also write common code inside utill.py

11. Experiment in each module in notebook file then you write modular          programming for that you should flow the work flow which write below.

12. After this finally your project ready.




# Work Flow

1. Update Config.yaml
2. Update Params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the component
6. Update the pipeline
7. Update the main.py
8. Update the app.py

# To Run

1. Clone The Repository
```
git clone https://github.com/bishwajyotichaudhary46/SMDF.git
``` 

2. Create Virtual Environment
```
conda create -p venv python==3.10 -y
```
3. Install requirement.txt
```
pip install -r requirement.txt
```
4. first run main.py for data collection to trainig pipeline
```
python main.py
``` 
5. Run Project for forecasting
```
python app.py
```
