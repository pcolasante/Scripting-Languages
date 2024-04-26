# Based on: https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
# and: https://api.mongodb.com/python/current/

import pprint as pp
from pymongo import MongoClient

# Get a client connection
def init_connection(user, passwd):
    client = MongoClient('mongodb://' + user + ':' + passwd + '@167.99.118.99/test')
    return client

# Find a sample doc
def get_one_doc(coll):
    result = coll.find_one()
    pp.pprint(result)

def or_example(col):
    orExample = col.find({ '$or': [{'desc' : 'FELONY DRUGS'}, {'desc' : 'CRIMINAL MISCHIEF'}]})
    for m in orExample:
        pp.pprint(m)

def and_example(col):
    andExample = col.find({'$and': [{'desc':'FIRE'}, {'sector': 4}]})
    for a in andExample:
        pp.pprint(a)

def get_distinct_crimes(col):
    for d in col.distinct('desc'):
        pp.pprint(d)

def aggregate_example(col):
    number = col.aggregate(
        [
            { '$group':
            {
                '_id': "$desc",
                "count" : { '$sum': 1}

            }}
        ]
    )
    print(number)

def main():
    # Change this to your assigned student user
    user = 'student16'

    # default password for all student users
    passwd = 'mongo_is_fun'

    # Try to connect to the cloud instance of Mongodb
    client = init_connection(user, passwd)

    # Select the database
    db = client.test

    # Select the collection within the database
    col = db['ocso_out']

    # find one example doc/crime
    try:         
        get_one_doc(col)
    except Exception as e:
        print("find_one failed")
        print(e)

    # Get a list of all crimes in the collection
    print( "***Distinct Crimes***")
    try:
        get_distinct_crimes(col)
    except Exception as e:
        print("distinct failed")
        print(e)

    # Find all the documents in the collection for a particular type of crime report   
    print("***Particular Crime: HIT AND RUN***")
    specific = {'desc': 'HIT AND RUN'}
    for x in col.find(specific):
        print(x)

    # Test OR
    print( "***OR Example: FELONY DRUGS OR CRIMINAL MISCHIEF***")
    try:
        or_example(col)
    except Exception as e:
        print("or failed")
        print(e)

    # Test AND
    print( '***AND Example: FIRE AND SECTOR 4***')
    try:
        and_example(col)
    except Exception as e:
        print("and failed")
        print(e)



    # Aggregate pipeline example
    print( '***Aggregate Example***' )
    try:
        aggregate_example(col)
    except Exception as e:
        print("and failed")
        print(e)

# Execution starts here
if __name__ == "__main__":
    main()
