"""
Add LabeledList and Table classes
"""

import csv

# helper function for repr/str
def truncate(input):
    str_ = str(input)
    if len(str_) > 20:
        return str_[:17] + '..'
    else: return str_

class LabeledList:

    # data and index assumed to be the same length
    def __init__(self, data=None, index=None):
        self.values = data
        self.index = index if index != None else range(len(data))

        # create an internal dict to store k/v pairs:
        self.internal_dict = dict(zip(self.index, data))
        
    def __repr__(self):
        output = ""
        for k, v in self.internal_dict.items():
            # TODO: check format output w/ dynamic width
            output += f'{k:<5} {v}\n'
        # strip last newline chr
        return output[:-1]

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, key_list):
        # handle each case based on type of key_list:
        if isinstance(key_list, LabeledList):
            # should (hopefully) preserve order and keep k/v pairs intact
            vals = [self.internal_dict[k] for k in key_list.index]
            return LabeledList(vals, key_list.index)      

        elif isinstance(key_list, list):

            if all(isinstance(n, bool) for n in key_list):
                keys = [self.index[i] for i in range(len(key_list))
                if key_list[i] == True]
                vals = [self.values[i] for i in range(len(key_list))
                if key_list[i] == True]
                return LabeledList(vals, keys)
            else:
                try:
                    vals = [self.internal_dict[k] for k in key_list]
                except KeyError:
                    raise KeyError("Value not in LabeledList.")
                return LabeledList(vals, key_list)

        else: return None

    def __iter__(self):
        return self.values

    def __eq__(self, scalar):
        truth_vals = [self.values[i] == scalar
        for i in range(len(self.values))]
        return LabeledList(truth_vals, self.index)

    def __ne__(self, scalar):
        truth_vals = [self.values[i] != scalar
        for i in range(len(self.values))]
        return LabeledList(truth_vals, self.index)

    def __gt__(self, scalar):
        truth_vals = [self.values[i] > scalar
        for i in range(len(self.values))]
        return LabeledList(truth_vals, self.index)
    
    def __lt__(self, scalar):
        truth_vals = [self.values[i] < scalar
        for i in range(len(self.values))]

        return LabeledList(truth_vals, self.index)

    def map(self, f):
        vals = [f(v) for v in self.values]
        return LabeledList(vals, self.index)


class Table:

    def __init__(self, data, index=None, columns=None):

        try:
            len(data[0])
            self.values = data
        except:
            self.values = [data]
        # data is passed as a list of lists, each nested list
        # being a row and the len of each list

        # TODO: what happens if the length of each row isn't equal?

        if index == None:

            if isinstance(data[0], list): self.index = range(len(data))

            else: self.index = [0]

        else: self.index = index

        if columns == None:
            # alternatively could do 'if len(data) == 1'
            try:
                self.columns = range(len(data[0]))
            except:
                self.columns = range(len(data))

        else: self.columns = columns


    def __repr__(self): # check!
            
        # print col names:
        output = f'{self.columns[0]:>23}'
        for c in self.columns[1:]:
            c_ = truncate(c)
            output+= f'{c_:>20}'
        output += '\n'
        
        # print index + data for each row:
        for i in range (len(self.index)): # 
            output += f'{self.index[i]:<3}'

            for val in self.values[i]:
                val_ = truncate(val)
                output += f'{val_:>20}'

            output += '\n'
        return output

    def __str__(self):
        return self.__repr__()

    # TODO: TEST!!!
    def __getitem__(self, col_list):

        if isinstance(col_list, LabeledList):
            return self.__getitem__(col_list.values)
            # recursive call will treat the input as a list, which
            # is handled by the next statement
        
        elif isinstance(col_list, list):
            
            if all(c in self.columns for c in col_list):

                # if called with a 1-item list, treat as a single col
                if (len(col_list) == 1): self.__getitem__(col_list[0])

                col_indices = [self.columns.index(c) for c in col_list]

                ret_values = []
                for row in self.values:
                    ret_values.append([row[c] for c in col_indices])

                return Table(ret_values, self.index, col_list)
                

            elif all(isinstance(c, bool) for c in col_list):

                # assume length of list is same size as each row
                if len(col_list) != len(self.values):
                    raise IndexError("Length of Boolean list does not equal" +
                    " number of rows in Table")

                rows = [self.values[i] for i in range(len(col_list)) if col_list[i]]
                index = [self.index[i] for i in range(len(col_list)) if col_list[i]]
                    
                return Table(rows, index, self.columns)

            else: raise KeyError("One or more column(s) not in Table.")

        else:

            try:
                i = self.columns.index(col_list)
                vals = [row[i] for row in self.values]
            except: 
                raise KeyError(f"'{col_list}' is not in Table")

            return LabeledList(vals, self.index)


    # TODO:
    def head(self, n):
        
        return Table(self.values[:n], self.index[:n], self.columns)

    def tail(self, n):
        
        return Table(self.values[-n:], self.index[-n:], self.columns)

    def shape(self):
        
        rows = len(self.values)

        try:
            cols = len(self.values[0])
        except IndexError:
            cols = 1

        return (rows, cols)
                
def read_csv(fn):
    with open (fn, newline='') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
            # .keys() -> col names
            # .values() -> row contents
            # each index in data corresponds to 1 row in Table

    # convert numeric vals to float64:
    for row in data:
        
        for k, v in row.items():
            try:
                new_val = float(v)
                row[k] = new_val
            except ValueError:
                pass


    columns = list(data[0].keys())
    index = range(len(data))
    values = []
    
    # using loop instead of list comp to get rid of dict.values obj
    for row in data:
        values.append(list(row.values()))

    return Table(values, index, columns)
    
            
if __name__ == '__main__':
    
    t = read_csv('occupations-truncated.csv')

    # TODO: annotations
    

    
