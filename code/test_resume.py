import pandas as pd
import pytest
import numpy
import re

data = pd.read_csv('D:/Jobs_Scrapped.csv', skip_blank_lines=True)
data.dropna(how="all", inplace=True)
# print(data.shape)

duplicateRowsDF = data[data.duplicated()]

def isValid(s):
    print (s)
    if s.isnull():
        return "Invalid"
    else:
        pattern = re.compile("(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$")
        result = pattern.search(s)
        print(result.group())
        if result.group() :
            return "Valid"
        else:
            return "Invalid"
# s = " "
# isValid(s)

@pytest.mark.parametrize("value", data['Job Date Posted'])
def test_date_limit(value):
    assert value.count("30") == 0, "{} is greater than to {}".format(value, 30)


def test_redundant_scraped():
    assert len(duplicateRowsDF.index) == 0, "Duplicates exist"

@pytest.mark.parametrize("value",isValid(data['Job Phone No']))
def test_valid_phone_no(value):
     assert value == "Valid" ,"Not a valid phone number"
