Feature: Purchase assistant

    Scenario: Verify that the file catalog.json loads correctly and contains the expected products
        When Diego loads the catalog.json file
        Then the catalog loads correctly and the products can be iterated over without error

    Scenario: Verify that the list of all available products is returned
        When Diego asks about the available products
        Then Diego should only see the available products