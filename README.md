## Prerequisites

1. Clone this repository.  
2. Open the repository in your preferred IDE (I recommend VSCode) inside the `salesgenioai` folder.  
3. Create and activate a virtual environment:
    ```sh
    python -m venv env
    env\Scripts\Activate.ps1
    ```
4. Install dependencies:
    ```sh
    pip install -r config/requirements.txt
    ```
5. Install [Allure Report](https://allurereport.org/docs/install/)

## Running Automated Tests

- To execute the tests:
    ```sh
    allure generate --clean --output allure_report; pytest --alluredir allure_report/
    ```
- To generate the report:
    ```sh
    allure generate -c allure_report/ -o report; allure-combine report
    ```
- To view the report, there are two options:
    - Open the `report/complete.html` file in your preferred browser.  
    - Start a local server with the report using:
      ```sh
      allure serve allure_report
      ```

## Video

A video is also attached, showing the previous setup and the execution of the tests.
