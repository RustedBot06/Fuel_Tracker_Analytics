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