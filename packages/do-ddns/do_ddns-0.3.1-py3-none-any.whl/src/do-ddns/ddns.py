#!/usr/bin/python3
import sqlite3
from pathlib import Path
from sqlite3 import Error
import urllib.request
import json
import logging
import argparse
import requests
import os
import time 
from datetime import datetime
from string import ascii_letters, digits
from rich import print
from argparse import RawTextHelpFormatter

homefilepath = Path.home()
filepath = homefilepath.joinpath('.config/ddns')
database = filepath.joinpath('ddns.db')
logfile = filepath.joinpath('ddns.log')
logging.basicConfig(filename=logfile,level=logging.INFO)
app_version = '0.3'


def get_ip():
	cursor = conn.cursor()
	cursor.execute('SELECT COUNT(ip4_server) FROM ipservers')
	count = cursor.fetchone()[0]
	if count != 0:
		cursor.execute('SELECT ip4_server from ipservers')
		server = cursor.fetchone()
		server = server[0]
		try:
			current_ip = urllib.request.urlopen(server).read().decode('utf-8')
			return current_ip
		except Exception as e:
			error = str(e)
			return error
	else:
		return None



def connect_database():
	Path(filepath).mkdir(parents=True, exist_ok=True)
	conn = None
	try:
		conn = sqlite3.connect(database)
	except Error as e:
		print(e)
	finally:
		if conn:
			c = conn.cursor()
			c.execute('''CREATE TABLE IF NOT EXISTS apikey
				(id integer NOT NULL PRIMARY KEY,
					api text NOT NULL)''')
			c.execute('''CREATE TABLE IF NOT EXISTS ipservers
			(id integer NOT NULL PRIMARY KEY,
			 ip4_server text NOT NULL,
			 ip6_server text)''')
			c.execute('''CREATE TABLE IF NOT EXISTS domains
			(id integer PRIMARY KEY,
			 name text NOT NULL)''')
			c.execute('''CREATE TABLE IF NOT EXISTS subdomains
			(id integer PRIMARY KEY,
			 main_id integer NOT NULL,
			 name text NOT NULL,
			 current_ip4 text NOT NULL,
			 current_ip6 text NULL)''')

			return conn


def get_api():
	cursor = conn.cursor()
	cursor.execute('SELECT COUNT(*) FROM apikey')
	count = cursor.fetchone()[0]
	if count == 0:
		return None
	else:
		cursor.execute('SELECT * FROM apikey')
		rows = cursor.fetchone()
		return rows[1]


def api(api_value):
	cursor = conn.cursor()
	cursor.execute('SELECT COUNT(*) FROM apikey')
	count = cursor.fetchone()[0]
	if count == 0:
		cursor.execute('INSERT INTO apikey values(?,?)', (1, api_value))
		print('Your API key has been added.')
	else:
		cursor.execute('UPDATE apikey SET api = ? WHERE id = 1',(api_value,))
		print('Your API key has been updated.')
	conn.commit()


def add_domian(domain):
	apikey = get_api()
	cursor = conn.cursor()
	cursor.execute('SELECT COUNT(*) FROM domains WHERE name like ?',(domain,))
	count = cursor.fetchone()[0]
	if count != 0:
		print('[red]Error:[/red] Domain name (%s) already in database!' % (domain))
	else:
		if apikey != None:
			headers = {'Authorization': 'Bearer ' + apikey, "Content-Type": "application/json"}
			response = requests.get('https://api.digitalocean.com/v2/domains/' + domain, headers=headers)
			response_data = response.json()

			if 'id' in response_data:
				print('[red]Error: [/red]The domain does not exist in your DigitalOcean account.\nPlease add the domain from your control panel [b]https://cloud.digitalocean.com/networking/domains/[/b]')
			else:
				cursor.execute('INSERT INTO domains values(?,?)', (None, domain,))
				print('The domain [b]%s[/b] has been added to the DB' % (domain))
				conn.commit()
	


def add_subdomain(domain):
	if set(domain).difference(ascii_letters + '.' + digits):
		print('[red]Error:[/red] Give the domain name in simple form e.g. [b]test.domain.com[/b]')
	else:
		parts = domain.split('.')
		sub = parts[0]
		top = parts[1] + '.' + parts[2]
		apikey = get_api()
		if apikey == None:
			print("[red]Error:[/red] Missing APIkey. Please add one!")
		else:
			ip = get_ip()
			if ip == None or 'urlopen error' in ip:
				print('[red]Error:[/red] Failed to get public IP. Do you have a typo in your URI? [red]Error %s.[/red]' % (ip))
			else:
				cursor = conn.cursor()
				cursor.execute('SELECT COUNT(*) FROM domains WHERE name like ?',(top,))
				count = cursor.fetchone()[0]
				if count == 0:
					print('[red]Error:[/red] Top domain [bold]%s[/bold] does not exist in the DB. Please add it with [i]ddns -t %s[/i].' % (top,top))
				else:
					cursor.execute('SELECT id FROM domains WHERE name LIKE ?',(top,))
					topdomain_id = cursor.fetchone()
					topdomain_id = topdomain_id[0]
					cursor.execute('SELECT count(*) FROM subdomains WHERE main_id LIKE ? AND name like ?',(topdomain_id,sub,))
					count = cursor.fetchone()[0]
					if count != 0:
						print('[red]Error:[/red] [bold]%s[/bold] already exists.' % (domain))
					else:
						data = {'name': sub,'data': ip,'type': "A",'ttl': 3600}
						headers = {'Authorization': 'Bearer ' + apikey, "Content-Type": "application/json"}
						response = requests.post('https://api.digitalocean.com/v2/domains/' + top + '/records',
												data=json.dumps(data), headers=headers)
						if str(response) == '<Response [201]>':
							if response != 'Fail':
								response_data = response.json()
								domainid = str(response_data['domain_record']['id'])
								cursor.execute('INSERT INTO subdomains values(?,?,?,?,?)',(domainid,topdomain_id,sub,ip,None,))
								conn.commit()
								print('The domain %s has been added.' % (domain))
						else:
							return '[red]Error: %s [/red]' % (str(response))


def remove_subdomain(domain):
	if set(domain).difference(ascii_letters + '.' + digits):
		print('[red]Error:[/red] Give the domain name in simple form e.g. [b]test.domain.com[/b]')
	else:
		parts = domain.split('.')
		sub = parts[0]
		top = parts[1] + '.' + parts[2]
		cursor = conn.cursor()
		cursor.execute('SELECT COUNT(*) FROM domains WHERE name like ?',(top,))
		count = cursor.fetchone()[0]
		if count == 0:
			print('[red]Error:[/red] Top domain [bold]%s[/bold] does not exist in the DB. So I\'m giving up!.' % (top))
		else:
			cursor.execute('SELECT COUNT(*) FROM subdomains WHERE name like ? and main_id=(SELECT id from domains WHERE name=?)',(sub,top,))
			count = cursor.fetchone()[0]
			if count == 0:
				print('[red]Error:[/red] Domain [bold]%s[/bold] does not exist in the DB. So I\'m giving up!.' % (domain))
			else:
				apikey = get_api()
				if apikey == None:
					print("[red]Error:[/red] Missing APIkey. Please add one!")
				else:
					cursor.execute('SELECT id FROM subdomains WHERE name like ? and main_id=(SELECT id from domains WHERE name=?)',(sub,top,))
					subdomain_id = str(cursor.fetchone()[0])
					headers = {'Authorization': 'Bearer ' + apikey, "Content-Type": "application/json"}
					response = requests.delete('https://api.digitalocean.com/v2/domains/'+top+'/records/' + subdomain_id, headers=headers)
					if str(response) == '<Response [204]>':
						cursor.execute('DELETE from subdomains where id=?',(subdomain_id,))
						conn.commit()
					else:
						print('[red]Error: [/red]An error occurred! Please try again later!')



def show_all_top_domains():
	cursor = conn.cursor()
	apikey = get_api()
	if apikey != None:
		req = urllib.request.Request('https://api.digitalocean.com/v2/domains/?per_page=200')
		req.add_header('Content-Type', 'application/json')
		req.add_header('Authorization', 'Bearer ' + apikey)
		current = urllib.request.urlopen(req)
		remote = current.read().decode('utf-8')
		remoteData = json.loads(remote)
		print('Domains in database are marked with a [*]')
		print('================================================')
		for k in remoteData["domains"]:
			cursor.execute('SELECT COUNT(*) FROM domains WHERE name like ?',(k['name'],))
			count = cursor.fetchone()[0]
			if count != 0:
				print('Name : [bold]'+k['name']+ ' [*][/bold]')
			else:
				print('Name : '+k['name'])

	else:
		print("[red]Error:[/red] Missing APIkey. Please add one!")
	


def list_sub_domains(domain):
	apikey = get_api()
	cursor = conn.cursor()
	if apikey == None:
		print("[red]Error:[/red] Missing APIkey. Please add one!")
	else:
		cursor.execute('SELECT COUNT(*) FROM domains WHERE name LIKE ?',(domain,))
		count = cursor.fetchone()[0]
		if count == 0:
			print("[red]Error: [/red]No such domain. Check spelling or use ddns -d to show all top domains.")
		else:
			print('\n\nCurrent sub domains for [b]%s[/b]' % (domain))
			print('=====================================================================')
			cursor.execute('SELECT id FROM domains WHERE name LIKE ?', (domain,))
			topdomain_id = cursor.fetchone()[0]
			cursor.execute('SELECT COUNT(*) FROM subdomains WHERE main_id LIKE ?',(topdomain_id,))
			count = cursor.fetchone()[0]
			if count == 0:
				print('[red]Error:[/red] No sub domains for [b]%s[/b]' % (domain))
			else:
				cursor.execute('SELECT name,last_updated FROM subdomains WHERE main_id LIKE ?',(topdomain_id,) )
				subdomains = cursor.fetchall()
				for i in subdomains:
					topdomain = i[0]+'.'+domain
					topdomain = "{:<25}".format(topdomain)
					print(topdomain+'\tLast updated : '+i[1])
			print('\n')


def list_do_sub_domains(domain):
	apikey = get_api()
	cursor = conn.cursor()
	if apikey == None:
		print("[red]Error:[/red] Missing APIkey. Please add one!")
	else:
		req = urllib.request.Request('https://api.digitalocean.com/v2/domains/'+domain+'/records?type="A"/?per_page=200')
		req.add_header('Content-Type', 'application/json')
		req.add_header('Authorization', 'Bearer ' + apikey)
		current = urllib.request.urlopen(req)
		remote = current.read().decode('utf-8')
		remoteData = json.loads(remote)
		print('Domains in your DigitalOcean account not in ddns DB for [b]%s[/b]' % (domain))
		print('===================================================================')
		for k in remoteData["domain_records"]:
			if k['type'] == 'A':
				cursor.execute('SELECT COUNT(*) FROM subdomains WHERE id like ?',(str(k['id']),))
				count = cursor.fetchone()[0]
				if count == 0:
					print(k['name']+'.'+domain+'\t\tID : '+str(k['id']))





def domaininfo(domain):
	apikey = get_api()
	local_ip = get_ip()
	cursor = conn.cursor()
	if set(domain).difference(ascii_letters + '.'):
		print('[red]Error:[/red]. Give the domain name in simple form e.g. [bold]test.domain.com[/bold]')
	else:
		parts = domain.split('.')
		topdomain = parts[1]+'.'+parts[2]
		cursor.execute('SELECT id FROM domains WHERE name like ?', (topdomain,))
		domainid = cursor.fetchone()[0]
		cursor.execute('SELECT * FROM subdomains WHERE main_id like ?', (domainid,))
		domains = cursor.fetchall()
		if local_ip != domains[0][3]: 
			localip = '[red]%s[/red]' % (local_ip) 
		else:
			localip = local_ip
		print ('The domain [bold]%s[/bold] has the IP [bold]%s[/bold]. Your public IP is [bold]%s[/bold]' % (domain,domains[0][3],localip))



def show_current_info():
	ipserver = None
	API = get_api()
	cursor = conn.cursor()
	cursor.execute('SELECT COUNT(ip4_server) FROM ipservers')
	count = cursor.fetchone()[0]
	if count == 0:
		ipserver = '[red]Error:[/red] No IP resolvers in DB'
	else:
		cursor.execute('SELECT * FROM ipservers')
		ipserver = cursor.fetchall()[0][1]

	if API == None:
		API = '[red]Error:[/red] API key not stored in DB'

	cursor.execute('SELECT COUNT(*) FROM domains')
	topdomains = cursor.fetchone()[0]
	cursor.execute('SELECT COUNT(*) FROM subdomains')
	subdomains = cursor.fetchone()[0]


	print('[b]ddns[/b] - a DigitalOcean dynamic DNS solution.')
	print('===================================================')
	print('API key 	: [b]%s[/b]' % (API))
	print('IP v4 resolver 	: [b]%s[/b]' % (ipserver))
	print('IP v6 resolver 	: [b]N/A[/b]')
	print('Logfile 	: [b]%s[/b]' % (logfile))
	print('Top domains 	: [b]%s[/b]' % (topdomains))
	print('sub domains 	: [b]%s[/b]' % (subdomains))
	print('')
	print('App version 	: [b]%s[/b] (https://gitlab.pm/rune/ddns)' % (app_version))
	print('')
	print('[i]IPv6 is not supported and not listed here.[/i]')	


def ip_server(ipserver, ip_type):
	cursor = conn.cursor()
	if ip_type == '4':
		cursor.execute('SELECT COUNT(ip4_server) FROM ipservers')
		count = cursor.fetchone()[0]
		if count == 0:
			cursor.execute('INSERT INTO ipservers values(?,?,?)', (None, ipserver,None))
			conn.commit()
			print('New IP resolver (%s) for ipv%s added.' % (ipserver, ip_type))
		else:
			cursor.execute('UPDATE ipservers SET ip4_server = ? WHERE id = 1',(ipserver,))
			print('IP resolver (%s) for ipv%s updated.' % (ipserver, ip_type))
			conn.commit()
	elif ip_type == '6':
		cursor.execute('SELECT COUNT(ip6_server) FROM ipservers')
		count = cursor.fetchone()[0]
		if count == 0:
			cursor.execute('INSERT INTO ipservers values(?,?,?)', (None, None,ipserver))
			conn.commit()
			print('New IP resolver (%s) for ipv%s added. \n\r This IP version is not supported.' % (ipserver, ip_type))
		else:
			cursor.execute('UPDATE ipservers SET ip6_server = ? WHERE id = 1',(ipserver,))
			print('IP resolver (%s) for ipv%s updated. \n\r This IP version is not supported.' % (ipserver, ip_type))
			conn.commit()



def updateip(force):
	apikey = get_api()
	current_ip = get_ip()
	cursor = conn.cursor()
	cursor.execute('SELECT COUNT(*) FROM subdomains')
	count = cursor.fetchone()[0]
	now = datetime.now()
	if count == 0:
		print('[red]Error: [/red]There are no dynamic domains active.'\
			' Start by adding a new domain with [i]ddns -s test.example.com[/i]')
	else:
		cursor.execute('SELECT id FROM subdomains')
		rows = cursor.fetchall()
		for i in rows:
			cursor.execute('SELECT name FROM domains WHERE id like (SELECT main_id from subdomains WHERE id = ?)',(i[0],))
			domain_name = str(cursor.fetchone()[0])
			subdomain_id = str(i[0])
			# Chek if an update is required
			req = urllib.request.Request('https://api.digitalocean.com/v2/domains/' + domain_name + '/records/' + subdomain_id)
			req.add_header('Content-Type', 'application/json')
			req.add_header('Authorization', 'Bearer ' + apikey)
			current = urllib.request.urlopen(req)
			remote = current.read().decode('utf-8')
			remoteData = json.loads(remote)
			remoteIP4 = remoteData['domain_record']['data']
			if remoteIP4 != current_ip or force == True:
				data = {'type': 'A', 'data': current_ip}
				headers = {'Authorization': 'Bearer ' + apikey, "Content-Type": "application/json"}
				response = requests.patch('https://api.digitalocean.com/v2/domains/'+domain_name+'/records/' + subdomain_id, data=json.dumps(data), headers=headers)
				if str(response) != '<Response [200]>':
					logging.error(time.strftime("%Y-%m-%d %H:%M")+' - Error : ' + str(response.json))
				else:
					cursor.execute('UPDATE subdomains SET current_ip4=? WHERE id = ?',(current_ip,subdomain_id,))
					cursor.execute('UPDATE subdomains SET last_updated=? WHERE id = ?',(now.strftime("%d/%m/%Y %H:%M:%S"),subdomain_id,))
					conn.commit()



def local_add_subdomain(domain,domainid):
	if set(domain).difference(ascii_letters + '.' + digits + '-'):
		print('[red]Error:[/red] Give the domain name in simple form e.g. [b]test.domain.com[/b]')
	else:
		parts = domain.split('.')
		sub = parts[0]
		top = parts[1] + '.' + parts[2]
		apikey = get_api()
		if apikey == None:
			print("[red]Error:[/red] Missing APIkey. Please add one!")
		else:
			ip = get_ip()
			if ip == None or 'urlopen error' in ip:
				print('[red]Error:[/red] Failed to get public IP. Do you have a typo in your URI? [red]Error %s.[/red]' % (ip))
			else:
				cursor = conn.cursor()
				cursor.execute('SELECT COUNT(*) FROM domains WHERE name like ?',(top,))
				count = cursor.fetchone()[0]
				if count == 0:
					print('[red]Error:[/red] Top domain [bold]%s[/bold] does not exist in the DB. Please add it with [i]ddns -t %s[/i].' % (top,top))
				else:
					cursor.execute('SELECT id FROM domains WHERE name LIKE ?',(top,))
					topdomain_id = cursor.fetchone()
					topdomain_id = topdomain_id[0]
					cursor.execute('SELECT count(*) FROM subdomains WHERE main_id LIKE ? AND name like ?',(topdomain_id,sub,))
					count = cursor.fetchone()[0]
					if count != 0:
						print('[red]Error:[/red] [bold]%s[/bold] already exists.' % (domain))
					else:
						cursor.execute('INSERT INTO subdomains values(?,?,?,?,?)',(domainid,topdomain_id,sub,ip,None,))
						conn.commit()
						print('The domain %s has been added.' % (domain))



def updatedb():
	# Update DB with new column 20.03.23
	# Add last updated field for subdomains
	new_table = 'last_updated'
	info = conn.execute("PRAGMA table_info('subdomains')").fetchall()
	if not any(new_table in word for word in info):
		add_column = "ALTER TABLE subdomains ADD COLUMN last_updated text default 'N/A'"
		conn.execute(add_column)
		conn.commit()	



# Commandline arguments
conn = connect_database()
updatedb()
parser = argparse.ArgumentParser(prog='ddns',
								description='Application to use domains from DigitalOcean account as dynamic '\
								'DNS domain(s).\nThe app only supports IP4. IPv6 is planned for a later release!'\
								'\nYou\'ll always find the latest version on https://gitlab.pm/rune/ddns',
								formatter_class=RawTextHelpFormatter,
								epilog='Making Selfhosting easier...')

parser.add_argument('-a', '--api', help='Add/Change API key.', 
	nargs=1, metavar=('APIkey'), required=False, action="append")

parser.add_argument('-f', '--force', help='Force update of IP address for all domains.', 
	required=False, action="store_true")

parser.add_argument('-l', '--list', help='List subdomains for supplied domain.', 
	nargs=1, metavar=('domain'), required=False, action="append")

parser.add_argument('-o', '--serverdomains', help='List subdomains for supplied domain not in ddns DB.', 
	nargs=1, metavar=('domain'), required=False, action="append")

parser.add_argument('-d', '--domains', help='List top domains in your DigitalOcean account.', 
	required=False, action="store_true")

parser.add_argument('-c', '--current', help='List the current IP address for the sub-domain given',
					required=False, nargs=1, action="append")

parser.add_argument('-t', '--top', help='Add a new domain from your DigitalOcean account to use as a dynamic DNS domain',
					required=False, nargs=1, metavar=('domain'), action='append')

parser.add_argument('-s', '--sub', help='Add a new subdomain to your DigitalOcean account and use as dynamic DNS.\n',
					required=False, nargs=1, metavar=('domain'), action='append')

parser.add_argument('-k', '--local', help='Add an existing DigitalOcean subdomain to your ddns DB and use as dynamic DNS.',
					required=False, nargs=2, metavar=('domain','domainid'), action='append')

parser.add_argument('-r', '--remove', help='Remove a subdomain from your DigitalOcean account and ddns.',
					required=False, nargs=1, metavar=('domain'), action='append')

parser.add_argument('-v', '--version', help='Show current version and config info',
					required=False, action='store_true')

parser.add_argument('-p', '--ipserver', help='Set IP server lookup to use. Indicate 4 or 6 for IP type.',
					required=False, nargs=2, metavar=('ip4.iurl.no', '4'), action="append")
args = vars(parser.parse_args())

if args['list']:
	list_sub_domains(args['list'][0][0])
elif args['domains']:
	show_all_top_domains()
elif args['serverdomains']:
	list_do_sub_domains(args['serverdomains'][0][0])
elif args['current']:
	domaininfo(args['current'][0][0])
elif args['top']:
	add_domian(args['top'][0][0])
elif args['sub']:
	add_subdomain(args['sub'][0][0])
elif args['version']:
	show_current_info()
elif args['force']:
	updateip(True)
elif args['ipserver']:
	ip_server(args['ipserver'][0][0],args['ipserver'][0][1])
elif args['api']:
	api(args['api'][0][0])
elif args['remove']:
	remove_subdomain(args['remove'][0][0])
elif args['local']:
	local_add_subdomain(args['local'][0][0],args['local'][0][1])
else:
	updateip(None)










