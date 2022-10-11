import pandas as pd

data = {'Product': ['Desktop Computer','Printer','Tablet','Monitor'],
        'Price': [1200,150,300,450]
        }

df = pd.DataFrame(data, columns = ['Product', 'Price'])
with pd.ExcelWriter("test_excel.xlsx") as writer: #xlsx file type

    df.to_excel (writer)