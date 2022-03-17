# Homework 02

## 4 List Comprehensions

1. [Technically, these are four separate list comprehensions in themselves, but since they all effectively perform the same operation, I've lumped them into one.

The __eq__, __ne__, __gt__, and __lt__ methods in the LabeledList class each employ a list comprehension to loop over the "values" property of the LabeledList and create a new list of boolean variables. The value of each boolean at each index corresponds to its truth value relative to the scalar passed to the method; for example, in __eq__, the value at each index will correspond to whether the element at that index in "values" is equal to the scalar.]

(https://github.com/nyu-csci-ua-0479-001-spring-2022/homework02-ericsson-c/blob/315a4b0484bdc41a4f4f8cd8923a242fbd2412e9/nelta.py#L62-L81)

2. [The underlying data structure in my implementation of the LabeledList is a dictionary, where the keys correspond to the LL's indices and the values correspond to the LL's values. In the __getitem__ method of the LabeledList class, a list comprehension is used to retrieve the values of the underlying dict based on the keys passed into the function.]

(https://github.com/nyu-csci-ua-0479-001-spring-2022/homework02-ericsson-c/blob/315a4b0484bdc41a4f4f8cd8923a242fbd2412e9/nelta.py#L39)

(https://github.com/nyu-csci-ua-0479-001-spring-2022/homework02-ericsson-c/blob/315a4b0484bdc41a4f4f8cd8923a242fbd2412e9/nelta.py#L52)

3. [In the __getitem__ method of the Table class, a list comp is used to make a new "row" of items only in the specified columns.]

(https://github.com/nyu-csci-ua-0479-001-spring-2022/homework02-ericsson-c/blob/315a4b0484bdc41a4f4f8cd8923a242fbd2412e9/nelta.py#L162)

4. [In the read_csv method, a list comp is used in conjunction with the DictReader object from the csv library to read the file data into a data structure that can be accessed after the file is closed.]

(https://github.com/nyu-csci-ua-0479-001-spring-2022/homework02-ericsson-c/blob/315a4b0484bdc41a4f4f8cd8923a242fbd2412e9/nelta.py#L215)