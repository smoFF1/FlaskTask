import sys


def sum_columns(csv_file: str,col_num:int):
    sum_col=0
    with open(csv_file, 'r') as file:
        header = next(file, None)
        if header:
            cols = header.split(',')
            column_name = cols[col_num].strip().replace('"', '')
        for line in file:
            columns = line.split(',')
            try:
                sum_col+=float(columns[col_num])
            except (ValueError, IndexError):
                continue
    return sum_col, column_name

filename = sys.argv[1]
col_index = int(sys.argv[2])
total, name = sum_columns(filename, col_index)  
print(f"The total '{name}' is {total}")