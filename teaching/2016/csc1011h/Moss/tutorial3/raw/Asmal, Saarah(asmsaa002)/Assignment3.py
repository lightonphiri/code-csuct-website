# Assignment 3
# ASMSAA002 - Saarah Asmal

import sqlite3
from PyQt4 import QtGui, QtCore

class PointOfSale:
    
    def __init__(self,db=None):
        db = sqlite3.connect("PointOfSale.db")
        
        db.execute()
        
        db.commit()
        
        db.close()
        
    
    
    
    