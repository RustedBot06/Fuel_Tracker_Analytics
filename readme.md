# Fuel Tracker

A Python-based fuel tracking application that stores refueling records in an SQLite database and provides mileage statistics, graphical analysis, input validation, and backup functionality.

## Features

### Fuel Log Management

* Add fuel entries with:

  * Date
  * Odometer reading
  * Fuel volume
  * Fuel cost
  * Full / partial refill status

* View stored records

* Update existing records

* Delete records

### Statistics

* Mileage per refill
* Average mileage
* Total fuel consumed
* Total number of entries
* Fuel Tracker summary dashboard

### Data Visualization

* Mileage interval step graph
* Fuel price trend graph
* Fuel rate trend graph
* Mileage histogram

### Reliability Features

* Input validation
* Odometer progression checks
* Custom validation exceptions
* SQLite database initialization safeguards

### Backup

* Export all fuel records to CSV format

## Technologies Used

* Python
* SQLite
* Matplotlib
* CSV

## Project Structure

```text
FuelTracker/
│
├── main.py
├── functions.py
├── validation.py
├── mileage.py
├── graphs.py
├── DEVLOG.md
├── fuel_logs.db
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd FuelTracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Usage

1. Add fuel refill records after each visit to the fuel station.
2. View statistics and mileage calculations.
3. Analyze trends using the graphing tools.
4. Export records to CSV for backup purposes.

## What I Learned

Through this project I learned:

* Modular Python programming
* SQLite database design and operations
* SQL queries and parameterized queries
* Input validation and exception handling
* Custom exception classes
* Data processing with lists and comprehensions
* File handling and CSV export
* Git branching, merging, tagging, and releases
* Data visualization with Matplotlib
* Debugging and maintaining a growing codebase
* Basic software project documentation

## Future Improvements

* Android-friendly version for personal use
* Configuration file support
* Enhanced reporting and analytics
* Data import functionality
* Improved graph customization
* Optional GUI version

## Known Limitations

* Console-based interface
* Manual data entry
* CSV export currently overwrites the previous backup file

## Author

Saptashwa Ghosh
