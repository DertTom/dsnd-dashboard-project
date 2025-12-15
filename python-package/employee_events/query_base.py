# Import any dependencies needed to execute sql queries
# YOUR CODE HERE
import pandas as pd
from .sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase(QueryMixin):
    def __init__(self):
        self.name = ""
    # Define a `names` method that receives
    # no passed arguments
    def names(self): 
        # Return an empty list
        return []
    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE
    def event_counts(self, id)->pd.DataFrame:
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        sql_query = f"""SELECT 
                        SUM(positive_events) AS 'sum_pos_evt',
                        SUM(negative_events) AS 'sum_neg_evt',
                        event_date
                        FROM {self.name}
                        JOIN employee_events USING({self.name}_id)
                        WHERE {self.name}.{self.name}_id = {id}
                        GROUP BY event_date
                        ORDER BY event_date
                        """
        return self.pandas_query(sql_query)

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE
    def notes(self, id)->pd.DataFrame:  
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        sql_query = f"""SELECT note_date, note
                        FROM 'notes'
                        WHERE {self.name}'_id' = {id}
                        GROUP BY event_date
                        ORDER BY event_date
                        """
        return pd.DataFrame()   # ToDo: IMPLEMENT ME !!! 

