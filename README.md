# Sales taxes problem
This solution solves the **Sales Taxes Problem** using *Python 3*. 
The problem requires to compute the taxes on the products in a basket and return their final 
price together with the total taxes that the client must pay.

## Problem

**Basic sales tax** is applicable at a rate of **10%** on all goods, 
**except** books, food, and medical products that are exempt. 
**Import duty** is an additional sales tax applicable on all imported goods at a rate of 5%, 
with no exemptions.

## Test Cases

```
INPUT:

Input 1:
2 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85

Input 2:
1 imported box of chocolates at 10.00
1 imported bottle of perfume at 47.50

Input 3:
1 imported bottle of perfume at 27.99
1 bottle of perfume at 18.99
1 packet of headache pills at 9.75
3 box of imported chocolates at 11.25

OUTPUT

Output 1:
2 book: 24.98
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 42.32

Output 2:
1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15

Output 3:
1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
3 imported box of chocolates: 35.55
Sales Taxes: 7.90
Total: 98.38
```

## Pre Requisites
The solution is written in *Python 3.7*, 
hence you need *Python 3* installed on your OS. 
To install *Python 3* on your OS, check this website:
https://www.python.org/downloads/

In order to run the tests, you need to install the *Python3* library: **pytest**.
To install *pytest*, check this website:
https://docs.pytest.org/en/latest/getting-started.html

If you prefer, you can use **venv** to keep the *pytest* library bounded to the project directory,
 without interfering with other libraries.

## File Structure
The code is structured in the following way:
- **lib**: Contains all classes used by *app.py*.
- **app.py**: The main file to run this solution.
- **text_taxes_sales_problem.py**: The tests that can be executed through *pytest*.
- **files**: Contains examples of input and categories files.
- **files/categories.csv**: It maps the products with their categories (goods / food / books / medical products / ...). 
If the category contains *book*, *medical* or *food*, then the script will consider the product free of taxes. 
In the other cases, a tax of 10% will be added to the final price.
- **file/input_X.txt**: The input file which corresponds to the basket with all products to buy. 
The lines must be formatted in the following way: 
<*numerical quantity*> <*imported/empty*> <*name of the product*> at <*price*>. 
If the file is formatted in this way, the solution is able to parse it and return the price and taxes. 
The name of the product must be present in the CSV file, 
otherwise it will be considered as general goods with 10% of taxes. 
The *imported* must be present only if the product is imported, otherwise it can be omitted.

All *files/input_X.txt* files are examples of possible input files which are the same as the test cases shown 
in this README.md.

#### Lib Structure
The library contains different files, one for each class generated to solve the problem.
- **orders.py**: Handles the selected products in the basket of a customer. 
It is possible to add *products* for each order and retrieve the total price and taxes that the customer has to pay 
in order to buy these products.
- **parser.py**: Parses the input file and generates an order with all products in the file.
- **product.py**: Handles one single type of product. 
- **categories.py**: Defines the categories of products. Taxes are computed based on the product category.
- **taxescalculator.py**: Based on the input, it returns the taxes rounded to 2 decimals. 
It is possible to compute the importation taxes, category taxes or the sum of both taxes.

## How to Run
There are 2 ways to run the code:
- *Hardcoded cases*: The main script runs these cases if both the input filename and the categories filename are not specified. 
It just run the test cases defined before.
```
python3 app.py
```
- *Input cases*: It is required to specify the input filename and the categories filename.
```
python3 app.py --input <input filename> --categories <categories filename>
```

## Tests
If you want to test the code, just run:
```
pytest
```
It will start all the test automatically.

