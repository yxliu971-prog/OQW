"""
 defines class _DbConnect_, for abstracting connections to databases

"""
from __future__ import annotations
from rdkit.Dbase import DbInfo
from rdkit.Dbase import DbModule
from rdkit.Dbase import DbUtils
__all__: list[str] = ['DbConnect', 'DbError', 'DbInfo', 'DbModule', 'DbUtils']
class DbConnect:
    """
      This class is intended to abstract away many of the details of
        interacting with databases.
    
        It includes some GUI functionality
    
      
    """
    def AddColumn(self, tableName, colName, colType):
        """
         adds a column to a table
        
            **Arguments**
        
              - tableName: the name of the table to manipulate
        
              - colName: name of the column to insert
        
              - colType: the type of the column to add
        
            
        """
    def AddTable(self, tableName, colString):
        """
         adds a table to the database
        
            **Arguments**
        
              - tableName: the name of the table to add
        
              - colString: a string containing column definitions
        
            **Notes**
        
              - if a table named _tableName_ already exists, it will be dropped
        
              - the sqlQuery for addition is: "create table %(tableName) (%(colString))"
        
            
        """
    def Commit(self):
        """
         commits the current transaction
        
            
        """
    def GetColumnNames(self, table = '', join = '', what = '*', where = '', **kwargs):
        """
         gets a list of columns available in the current table
        
              **Returns**
        
                  a list of column names
        
              **Notes**
        
               - this uses _DbInfo.GetColumnNames_
        
            
        """
    def GetColumnNamesAndTypes(self, table = '', join = '', what = '*', where = '', **kwargs):
        """
         gets a list of columns available in the current table along with their types
        
              **Returns**
        
                  a list of 2-tuples containing:
        
                    1) column name
        
                    2) column type
        
              **Notes**
        
               - this uses _DbInfo.GetColumnNamesAndTypes_
        
            
        """
    def GetColumns(self, fields, table = '', join = '', **kwargs):
        """
         gets a set of data from a table
        
              **Arguments**
        
               - fields: a string with the names of the fields to be extracted,
                 this should be a comma delimited list
        
              **Returns**
        
                  a list of the data
        
              **Notes**
        
                - this uses _DbUtils.GetColumns_
        
            
        """
    def GetCursor(self):
        """
         returns a cursor for direct manipulation of the DB
              only one cursor is available
        
            
        """
    def GetData(self, table = None, fields = '*', where = '', removeDups = -1, join = '', transform = None, randomAccess = 1, **kwargs):
        """
         a more flexible method to get a set of data from a table
        
              **Arguments**
        
               - table: (optional) the table to use
        
               - fields: a string with the names of the fields to be extracted,
                 this should be a comma delimited list
        
               - where: the SQL where clause to be used with the DB query
        
               - removeDups: indicates which column should be used to recognize
                 duplicates in the data.  -1 for no duplicate removal.
        
              **Returns**
        
                  a list of the data
        
              **Notes**
        
                - this uses _DbUtils.GetData_
        
            
        """
    def GetDataCount(self, table = None, where = '', join = '', **kwargs):
        """
         returns a count of the number of results a query will return
        
              **Arguments**
        
               - table: (optional) the table to use
        
               - where: the SQL where clause to be used with the DB query
        
               - join: the SQL join clause to be used with the DB query
        
        
              **Returns**
        
                  an int
        
              **Notes**
        
                - this uses _DbUtils.GetData_
        
            
        """
    def GetTableNames(self, includeViews = 0):
        """
         gets a list of tables available in a database
        
              **Arguments**
        
              - includeViews: if this is non-null, the views in the db will
                also be returned
        
              **Returns**
        
                  a list of table names
        
              **Notes**
        
               - this uses _DbInfo.GetTableNames_
        
            
        """
    def InsertColumnData(self, tableName, columnName, value, where):
        """
         inserts data into a particular column of the table
        
            **Arguments**
        
              - tableName: the name of the table to manipulate
        
              - columnName: name of the column to update
        
              - value: the value to insert
        
              - where: a query yielding the row where the data should be inserted
        
            
        """
    def InsertData(self, tableName, vals):
        """
         inserts data into a table
        
            **Arguments**
        
              - tableName: the name of the table to manipulate
        
              - vals: a sequence with the values to be inserted
        
            
        """
    def KillCursor(self):
        """
         closes the cursor
        
            
        """
    def __init__(self, dbName = '', tableName = '', user = 'sysdba', password = 'masterkey'):
        """
         Constructor
        
              **Arguments**  (all optional)
        
                - dbName: the name of the DB file to be used
        
                - tableName: the name of the table to be used
        
                - user: the username for DB access
        
                - password: the password to be used for DB access
        
            
        """
class DbError(RuntimeError):
    pass
