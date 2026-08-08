## v0.2 Graph Improvements

Problem:
- Mileage was earlier plotted against a single date(higher) despite representing an interval.
- The whole graph system was heard to read.

Investigation:
- Researched matplotlib histogram/step visualizations.
- Learned about stairs(), range(), subplot(), xticks(), show(), grid(), text(), just use cases solely in the project.
- Lack of refernce lines and data values on markers made it hard to read.
- Difficulty in comparison of graphs

Solution:
- Converted mileage graph to interval-based step graph.
- Added reference lines (y axis only using grid(), majors) 
- Added data point values using text()
- Ensured same window graph showcase for easier and effective viewing and comparison at a glance.

Observations:
- More accurate representation of data.
- Subplot layout became crowded.
- show() blocks execution until window closes.

Future Ideas:
- Dashboard layout redesign.
- Interactive graph selection.
- Better annotations.

## v0.3 Input Validation

Problem:
- Invalid user inputs could enter the system and compromise data quality.
- Negative fuel prices, negative fuel volumes, invalid refill flags, and incorrect odometer readings were not adequately handled.
- Failed validation attempts could still propagate invalid values into later parts of the program.
- The application lacked a structured way to communicate validation failures.

Investigation:
- Use of custom exceptions and the difference between built-in exceptions and application-specific exceptions.
- Studied raise, exception propagation, and try-except handling within the context of the project.
- Considered different validation architectures, including direct if-else handling versus dedicated validation functions.
- Evaluated edge cases such as an empty database and first-time application usage.

Solution:
- Created a dedicated validation.py module to centralize validation logic.
- Implemented a custom ValidationError exception for application-specific validation failures.
- Added validation for:

  - Fuel price (> 0)
  - Fuel volume (> 0)
  - Odometer reading (> 0)
  - Odometer progression (current reading must exceed previous reading)
  - Refill flag (must be either 0 or 1)
- Added retrieval of the previous odometer reading from the database to enforce mileage consistency.
- Handled first-entry scenarios by providing a default previous odometer value when no records exist.
- Prevented database writes when validation fails.

Observations:
- Separating validation from business logic improved readability and maintainability.
- Custom exceptions produced clearer and more meaningful error messages.
- Validation failures highlighted the importance of handling None returns correctly.
- The current approach of re-entering all fields after a validation failure is acceptable due to the small number of inputs.
- Validation rules based on existing database state are fundamentally different from simple value checks.

Future Ideas:
- Field-specific retry loops instead of re-entering the entire entry.
- Validation logging for debugging and auditing purposes.
- Date validation during modification by user.
- Additional warning-based validations for unusually large odometer jumps.
- Expand validation coverage as new features are introduced.

## v0.4 Data Backup Export

Problem:

- Fuel data was stored only inside the SQLite database.
- Accidental database corruption or migration to another system could result in data loss.
- There was no user-accessible backup mechanism.

Investigation:

- Python's csv module for exporting tabular data.
- Reviewed file handling using with-open context managers.
- Investigated how database query results could be serialized into CSV format.

Solution:
- Added a Backup Data option to the application menu.
- Queried all records from the LOGS table.
- Exported the records into a CSV file with descriptive column headers.
- Configured the export process to overwrite the previous backup file, ensuring a simple and predictable backup workflow.

Observations:
- SQLite query results can be written directly to CSV with minimal transformation.
- The csv module handles row formatting automatically.
- Context managers simplify file handling and ensure files are closed correctly.
- A single backup file is sufficient for the current personal-use scope of the project.

Future Ideas:
- Timestamped backup files.
- JSON export format.
- Data import functionality.
- User-selectable export locations.
- Automatic scheduled backups.

01/08/2026
Feature: A latest entry summary and comparison with avg metrics after new log.

