import pandas as pd

# row to table
def rowToTable(data):
    '''
    Input: a df with multiple rows. Each row is a combination of a tag and a size

    Output: row is a tag and columns names are sizes. The values are the occurences of the tag in the size.
    '''

    # create an empty df. The columns are fixed from 220 to 300, increment by 5
    result = pd.DataFrame(columns=range(220, 305, 5))

    # loop through each row
    for index, row in data.iterrows():
        # get the tag and the sizes. Sizes are always the last 3 characters
        rowStr = str(row[0])
        tag, size = rowStr[:-3], int(rowStr[-3:])

        # check if the tag is already in the rows
        if tag in result.index:
            # if yes, increment the size. tag is a string
            result.loc[tag][size] += 1

        else:
            # if not, add a new row with the tag and increment the size
            result.loc[tag] = pd.Series(0, index=range(220, 305, 5))
            result.loc[tag][size] = 1

    # fill the NaN with 0
    result.fillna(0, inplace=True)

    # sort the index
    result.sort_index(inplace=True)

    return result




