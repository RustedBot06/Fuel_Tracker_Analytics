# Fuel Tracker

A Python-based fuel tracking application that stores refueling records in an SQLite database and provides mileage statistics and graphical analysis using Matplotlib.

## Features

- Store fuel logs with:
  - Date
  - Odometer reading
  - Fuel volume
  - Fuel cost

- View stored records

- Calculate:
  - Mileage per refill
  - Overall average mileage
  - Fuel price trends

- Generate graphs:
  - Date vs Mileage
  - Date vs Fuel Rate
  - Date vs Fuel Price

## Technologies Used

- Python
- SQLite
- Matplotlib

## Project Structure

```
FuelTracker/
│
├── main.py
├── functions.py
├── mileage.py
├── graphs.py
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

Run:

```bash
python main.py
```

## What I Learned

Through this project I learned:

- Modular Python programming
- SQLite database operations
- SQL queries and parameterized queries
- Data processing with lists and comprehensions
- Tuple unpacking
- Using zip()
- Building menu-driven applications
- Data visualization with Matplotlib
- Debugging real-world software issues

## Future Improvements

- Export data to CSV
- Better graph customization
- GUI version using Tkinter or PyQt
- Mobile application version
- Cloud backup support

## Known Limitations

- Input validation is limited.
- Odometer rollback checks are not yet implemented.
- Fuel volume must be entered correctly by the user.

## Author

Saptashwa