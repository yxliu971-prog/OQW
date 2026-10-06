"""
 a set of functions for interacting with databases

 When possible, it's probably preferable to use a _DbConnection.DbConnect_ object

"""
from __future__ import annotations
from _io import StringIO
from rdkit.Dbase import DbInfo
from rdkit.Dbase import DbModule
from rdkit.Dbase.DbResultSet import DbResultSet
from rdkit.Dbase.DbResultSet import RandomAccessDbResultSet
import sys as sys
__all__: list[str] = ['DatabaseToDatabase', 'DatabaseToText', 'DbInfo', 'DbModule', 'DbResultSet', 'GetColumns', 'GetData', 'GetTypeStrings', 'RandomAccessDbResultSet', 'StringIO', 'TextFileToDatabase', 'TypeFinder', 'sys']
def DatabaseToDatabase(fromDb, fromTbl, toDb, toTbl, fields = '*', join = '', where = '', user = 'sysdba', password = 'masterkey', keyCol = None, nullMarker = 'None'):
    """
    
    
         FIX: at the moment this is a hack
    
        
    """
def DatabaseToText(dBase, table, fields = '*', join = '', where = '', user = 'sysdba', password = 'masterkey', delim = ',', cn = None):
    """
     Pulls the contents of a database and makes a deliminted text file from them
    
          **Arguments**
            - dBase: the name of the DB file to be used
    
            - table: the name of the table to query
    
            - fields: the fields to select with the SQL query
    
            - join: the join clause of the SQL query
              (e.g. 'join foo on foo.bar=base.bar')
    
            - where: the where clause of the SQL query
              (e.g. 'where foo = 2' or 'where bar > 17.6')
    
            - user: the username for DB access
    
            - password: the password to be used for DB access
    
          **Returns**
    
            - the CSV data (as text)
    
        
    """
def GetColumns(dBase, table, fieldString, user = 'sysdba', password = 'masterkey', join = '', cn = None):
    """
     gets a set of data from a table
    
          **Arguments**
    
           - dBase: database name
    
           - table: table name
    
           - fieldString: a string with the names of the fields to be extracted,
              this should be a comma delimited list
    
           - user and  password:
    
           - join: a join clause (omit the verb 'join')
    
    
          **Returns**
    
           - a list of the data
    
        
    """
def GetData(dBase, table, fieldString = '*', whereString = '', user = 'sysdba', password = 'masterkey', removeDups = -1, join = '', forceList = 0, transform = None, randomAccess = 1, extras = None, cn = None):
    """
     a more flexible method to get a set of data from a table
    
          **Arguments**
    
           - fields: a string with the names of the fields to be extracted,
                this should be a comma delimited list
    
           - where: the SQL where clause to be used with the DB query
    
           - removeDups indicates the column which should be used to screen
              out duplicates.  Only the first appearance of a duplicate will
              be left in the dataset.
    
          **Returns**
    
            - a list of the data
    
    
          **Notes**
    
            - EFF: this isn't particularly efficient
    
        
    """
def GetTypeStrings(colHeadings, colTypes, keyCol = None):
    """
      returns a list of SQL type strings
        
    """
def TextFileToDatabase(dBase, table, inF, delim = ',', user = 'sysdba', password = 'masterkey', maxColLabelLen = 31, keyCol = None, nullMarker = None):
    """
    loads the contents of the text file into a database.
    
          **Arguments**
    
            - dBase: the name of the DB to use
    
            - table: the name of the table to create/overwrite
    
            - inF: the file like object from which the data should
              be pulled (must support readline())
    
            - delim: the delimiter used to separate fields
    
            - user: the user name to use in connecting to the DB
    
            - password: the password to use in connecting to the DB
    
            - maxColLabelLen: the maximum length a column label should be
              allowed to have (truncation otherwise)
    
            - keyCol: the column to be used as an index for the db
    
          **Notes**
    
            - if _table_ already exists, it is destroyed before we write
              the new data
    
            - we assume that the first row of the file contains the column names
    
        
    """
def TypeFinder(data, nRows, nCols, nullMarker = None):
    """
    
    
          finds the types of the columns in _data_
    
          if nullMarker is not None, elements of the data table which are
            equal to nullMarker will not count towards setting the type of
            their columns.
    
        
    """
def _AddDataToDb(dBase, table, user, password, colDefs, colTypes, data, nullMarker = None, blockSize = 100, cn = None):
    """
     *For Internal Use*
    
          (drops and) creates a table and then inserts the values
    
        
    """
def _AdjustColHeadings(colHeadings, maxColLabelLen):
    """
     *For Internal Use*
    
          removes illegal characters from column headings
          and truncates those which are too long.
    
        
    """
def _insertBlock(conn, sqlStr, block, silent = False):
    ...
def _take(fromL, what):
    """
     Given a list fromL, returns an iterator of the elements specified using their
        indices in the list what 
    """
