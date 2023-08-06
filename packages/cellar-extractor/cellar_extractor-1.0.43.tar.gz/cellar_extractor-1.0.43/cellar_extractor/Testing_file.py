"""

This file is purely a testing file for trying out separate parts of code, testing if everything works and such.
Can be also used to develop future code.



"""
from nodes_and_edges import get_nodes_and_edges
from os.path import join
from json_to_csv import read_csv
import time
from eurlex_scraping import *
from cellar import *
from sparql import *

if __name__ == '__main__':
    username = "n00ac9w5"
    password = "XUtjyPDrl1c"
    base_query = "SELECT DN,CI WHERE DN = %s"
    input = " OR ".join(['62004CJ0292'])
    query = base_query % (str(input))
    response = run_eurlex_webservice_query(query, username, password)
    b=2