import os
import boto3
import pymysql
import MySQLdb.cursors

try:
    mysql=MySQLdb.connect('localhost','root','22Million$','usertesting')
    print('connected')
except:
    print("nope")
try:
    cursor=mysql.cursor()
    print('cursor made')
except:
    print("nope")
try:
    cursor.execute('SELECT * FROM usertable WHERE users =\''+'jennifer'+'\' AND passwords =\''+'artiscool1'+'\'')
    account=cursor.fetchone()
    print(account)
except:
    print("nope")


'''
ENDPOINT="rvacdevdb.cfuwauqqmeg3.us-east-2.rds.amazonaws.com"
PORT=3306
USER="rvacdbconnect"
REGION="us-east-2"
DBNAME="rvacdev"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn =  pymysql.connect(host=ENDPOINT, user=USER, password=token, port=PORT, database=DBNAME, ssl_ca='C:\\Users\\pjf08\\Downloads\\us-east-2-bundle.pem')
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))
'''