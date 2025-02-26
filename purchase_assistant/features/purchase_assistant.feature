Feature: Purchase assistant

    Scenario: Verify that the file catalog.json loads correctly and contains the expected products
        When Diego loads the catalog.json file
        Then the catalog loads correctly and the products can be iterated over without error