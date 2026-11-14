# Cloudfide-recruitment-task

## Setup

Clone the repository:

```bash
git clone https://github.com/marphalis/Cloudfide-recruitment-task
cd Cloudfide-recruitment-task
```

Install the dependencies:

```bash
python -m pip install pandas pytest
```

##   Implementation of operations on columns

The first part of the project was to write `add_virtual_column()` function which would allow user to create new columns in a dataset using mathematical operations on existing ones. The creation request would consist of: a `Dataframe` object, a `string` variable containing instructions about operations for the new column and the name for the new column.

As a part of the task, validation should be performed at the beginning of the function. I set up 4 validation steps as prerequisites to proceed with implementing the instructions:

- Check whether the name for the new column hadn't already been used in the Dataframe for a different column (UPDATE: this check was removed, one of the provided tests shows this is not a requirement).
- Test if the name fulfills the requirement of consisting of only letters and underscore character.
- Requirement that the instructions are non-empty and consists of lowercase column names.
- Validation of every expression in the instructions being either an existing column name, a number value or an operation character. The operands accepted for this task were +, - and *.

When it comes to `string` formatting and lower versus uppercase characters: in the task instructions there wasn't a straightforward direction for the formatting of string variables and column names. The assumption was made that the sample instructions input represents the correct formatting. That is to say, the lowercase formatting was implemented across all `string` variables and column names.

The additional fifth check was implemented using the `eval()` method. This method allows for a straightforward conversion of the instructions `string` into mathematical expression and implements it. It simultaneously validates if the expression makes mathematical sense. F.e.: if there were two separate numbers next to each other, the instructions would pass the previous tests. But when trying to use the `eval()` function, it will raise an error since this doesn't represent a valid mathematical operation. Otherwise, this implements the operations on the columns to return to the user. In the case of failing any of these tests, the function will return an empty `Dataframe` object as instructed.

## Dataset cleanup

Various data cleaning steps were implemented in the _pipeline.py_ file on the provided dataset:

- Column names were cleaned of whitespaces.
- Spaces between words in the names were replaced with underscore characters.
- Characters were converted to lowercases.
- Duplicate rows were removed (five rows).
- The row with values copied from column names was also removed.
- The row with `TOTAL` as the `order_id` value was removed.
- Commas in the `unit_price` column were substituted with dots (for the sake of consistency in symbols for decimals).
- Columns with all non-empty values being numeric (`quantity`, `unit_price` and `discount`) were converted from `string` type to respectively `int`, `float` and `float` types. The empty cells were substituted with 0.
- `order_date` column was converted to `datetime` type.
- All the cells with values of `string` type were reformatted the same way column names were.

## Running the Pipeline

Run:

```bash
python pipeline.py
```
The pipeline reads `sales.csv`, cleans the data, calculates revenue and generates `revenue_by_region.csv`.

Revenue is calculated as:

```text
revenue = quantity * unit_price
```


## Data transformation and analysis

The stated goal of this task was to use the `add_virtual_column` function to create a `revenue` column using formula _quantity * unit_price_. Next, using the new column, present the overall revenue from each region. These are the results:

| region | revenue |
|:-:| :-: |
|central|529314.3|
|east|453732.1|
|north|680466.5|
|south|513943.2|
|west|454063.7|



## Running Tests

The tests were implemented in the *test_solution.py* and *test_pipeline.py* files. Run all tests with:

```bash
pytest -v
```