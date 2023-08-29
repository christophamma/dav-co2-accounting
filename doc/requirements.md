# Requirements

## User stories

1. As a user I want to see the scanned bill and enter the data in the form planetly expects
2. As a user I want to mark a bill as finished when I have entered all data of this bill
3. As a user I want to see all unfinished and finished bills
4. As a user I want to work sequentially through all unfinished bills
5. As a user I want all entered data to be persistent without triggering persistency explicitly
6. As a user I want to be able to mark a bill as incomplete and save a comment with it
7. As a user I want to be able to see the entered data as a summary according to the data categories
8. As a user I want to be able to export the entered data together with the summary to a human readable text file
9. As a user I want to be able to load different bills with identical file names (file names should not be an identifier)

## System context

Planetly: provides categories and requirements how to collect data
Accounting: provides bills

## Functional requirements

1. Categorize data: All bill positions must be categorized into a category.
In addition to the price, there is a detailed category, where positions are optionally given in a special unit (e.g. kg).
That means each position belongs to one and only one category, has a price/amount in euro and optionally a detailed unit.

2. Available categories are likely subject to change.
It can be assumed that new categories will be added in the future and existing ones are changed in terms of special
unit and the scope of the category. The system should allow adding and changing of categories easily.
Caveat: It is unclear what happens with already present data, when a category is changed.
Idea: Allow adding easily through a config file containing categories, postpone changing categories or model it as
defining new ones and deactivate obsolete ones

3. Each category has an optional detail unit, a description that describes the scope of the category and might be part
of a group of categories.


## Architecture

Business Logic:
PdfStore: Provides access to the pdfs of the individual bills
Bill: Central class that stores all data entered for one bill (maybe pure dataclass)
BillId: Identifies one Bill
BillStore: Provides (filtered) access to the BillData instances
BillFilter: Maybe have filters as extra classes instead of methods in BillDataStore
SummaryGenerator: Provides a summary of the data
Exporter: Can save the entered data with the summary
Category: 
CategoryProvider: Provides all available categories to the application
CvsCategoryImporter: Reads Categories from cvs files and add them to a CategoryProvider

User Interface:
TBD
