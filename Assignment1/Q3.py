"""
3. Write a Python program to print all unique values in the following sample Data.
Sample Data : [{"A":"B001"}, {"A": "B002"}, {"AI": "B001"}, {"AI": "B005"}, {"AII":"B005"}, {"A":"B009"},{"AIII":"B007"}]
Expected Output : {'B005', 'B002', 'B007', 'B001', 'B009
"""


data = [{"A":"B001"}, {"A": "B002"}, {"AI": "B001"}, {"AI": "B005"}, {"AII":"B005"}, {"A":"B009"},{"AIII":"B007"}]

new_data = list(set(num for dic in data for num in dic.values()))

print(new_data)