from datetime import date
import mysql.connector
from mysql.connector import errorcode
import logging

LOG_FORMAT = '%(asctime)-15s %(levelname)s %(message)s'
LOG_FILE = '/Users/obumonuorah/Documents/Python_projects/log.txt' #Personalize

logger= logging.getLogger()
logger.setLevel(logging.DEBUG) 
handler = logging.FileHandler(LOG_FILE, 'a', 'utf-8')
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(handler)

query_config = {
  'user': 'root', #Personalize
  'password': 'Favour@123', #Personalize
  'host': '127.0.0.1',
  'database': 'atm',
  'raise_on_warnings': True
}

query_new_email = ("SELECT  account_number  from atm.customer where email = (%s)")
insert_account_type = ("INSERT INTO atm.account (account_type,balance) VALUES (%s,%s)")
insert_account_data_query = ("INSERT INTO atm.account (customer_id, account_number, balance, account_type) VALUES (%s, %s, %s, %s)")
insert_customer_data_query = ("INSERT INTO atm.customer (fullname, username, password, gender, email, date_of_birth) VALUES (%s, %s, %s, %s, %s,%s)")
receiver_name_query = ("SELECT fullname FROM atm.account join atm.customer on (atm.account.customer_id = atm.customer.id) where username = %s and password = %s")
balance_query = ("SELECT balance FROM atm.account WHERE account_number = %s")
login_query = ("SELECT username FROM atm.customer WHERE username = %s and password = %s")
query_login = ("SELECT username,password FROM atm.customer")

transfer_from_query = query_add = ("UPDATE atm.account SET balance = balance - %s WHERE account_number = %s")
transfer_to_query = query_add = ("UPDATE atm.account SET balance = balance + %s WHERE account_number = %s")

customer_info_query = ("SELECT account_number, balance, fullname, email FROM atm.account join atm.customer on (atm.account.customer_id = atm.customer.id) where username = %s and password = %s")
account_info_query = ("SELECT account_number, balance, fullname, email FROM atm.account join atm.customer on (atm.account.customer_id = atm.customer.id) where account_number = %s")

def query_db(query, *args):
	cnx = mysql.connector.connect(**query_config)
	cursor = cnx.cursor()
	logger.debug('Database auth successful for USER: {}'.format(query_config.get('user')))
	val = []
	for arg in args:
		val.append(arg)
	val = tuple(val)
	cursor.execute(query, val) # Must be a tuple
	logger.debug('Database Query successful for USER: {}'.format(query_config.get('user')))
	result = []
	for r in cursor:
		result.append(r)
	#cursor.fetchall()[0]
	if not result:
		cnx.commit()
	cursor.close()
	cnx.close()
	return result

query_db(insert_account_data_query,'5','8000','1500000', 'Savings')
#query_db(balance_query,'5000')
query_db(insert_customer_data_query,'Zina Onuorah', 'zina', 'zina', 'F', 'stancassica4sure@gmail.com', date(2019, 8, 20))




