from bs4 import BeautifulSoup
import urllib.request
import json
from urllib.parse import quote
import click
#from pyDictionary import pyDictionary


'''Get data from sunlight and govtrack api 
allow users to key term search for a past bill, upcoming bill, and current bill
allow users to select bill and provide summary of what that bill entails
find supporters of bill and their info integrate ability to donate to sponsers
explain how the bill will progress forward'''



def Main_Screen():
	click.echo(click.style('\nMain Menu', bg='blue'))
	click.echo('1: Find your legislator \n')
	click.echo('2: Find a bill by keyword/s \n')
	click.echo('3: Get info on process \n')
	click.echo('4: Exit Program \n')
	selection = click.prompt('Enter number to make selection \n', type=int)

	if(selection == 1): 
		zipcode = click.prompt('\nWhat is your zipcode? \n') 
		find_my_legis(zipcode)
	if(selection == 2):
		keywords = click.prompt('\n Search for?')
		find_matching_bills(keywords)


def find_matching_bills(keywords):
	keywords = quote(keywords)
	click.echo(keywords)

	url='https://congress.api.sunlightfoundation.com/bills/search?query=%22{}%22&history.enacted=true'.format(keywords)
	dataurl = urllib.request.urlopen(url).read()
	data = dataurl
	json_obj = str(data, 'utf-8')
	poldata = json.loads(json_obj)
	click.echo('Data on bills goes back to 2009')
	print(poldata['results'])

	for obj in poldata['results']:
		print(obj['official_title'])
		bill_id_text = 'Bill id is: {}'.format(obj['bill_id'])
		click.echo(click.style(bill_id_text,bg='green'))
		print(obj['introduced_on'],'\n')


def find_my_legis(zipcode):
	url = 'https://congress.api.sunlightfoundation.com/legislators/locate?zip={}'.format(zipcode)
	data = urllib.request.urlopen(url).read()
	json_obj = str(data, 'utf-8')
	data = json.loads(json_obj)
	click.echo('Your Legislators Are:')
	
	for obj in data['results']:
		idnum = str(obj['bioguide_id'])
		print('\nName: {} {}'.format(obj['first_name'],obj['last_name']))
		print('Party Affiliation/Chamber: {} {}'.format(obj['party'], obj['chamber']))
		print('Email Address: {}'.format(obj['oc_email']))
		print('Phone Number: {}'.format(obj['phone']))
		print('Website: {}'.format(obj['website']))
		print('Twitter: @{}'.format(obj['twitter_id']))
		print('Facebook: https://www.facebook.com/{}'.format(obj['facebook_id']))
		click.echo(click.style(('ID: '+ idnum), bg ='red'))
		click.echo(click.style('='*50, fg='blue'))

	choice = int(click.prompt('1. Detailed View 2. Main Menu'))
	if(choice == 1): 
		idnum = click.prompt('Enter ID')
		detailed_view(idnum)
	if(choice == 2): Main_Screen()

def detailed_view(data_id):
	url = 'https://congress.api.sunlightfoundation.com/legislators/?bioguide_id={}'.format(data_id)
	data = urllib.request.urlopen(url).read()
	json_obj = str(data, 'utf-8')
	data = json.loads(json_obj)

	for obj in data['results']:
		print('\nName: {} {}'.format(obj['first_name'],obj['last_name']))
		print('Middle Name: {}'.format(obj['middle_name']))
		print('Gender: {}'.format(obj['gender']))
		print('Birthday: {}'.format(obj['birthday']))
		print('Term Start: {} | Term End: {}'.format(obj['term_start'], obj['term_end']))
		print('Party Affiliation/Chamber: {} {}'.format(obj['party'], obj['chamber']))
		print('Office: {}'.format(obj['office']))
		print('Email Address: {}'.format(obj['oc_email']))
		print('Phone Number: {}'.format(obj['phone']))
		print('Fax Number: {}'.format(obj['fax']))
		print('Website: {}'.format(obj['website']))
		print('Contact Form: {}'.format(obj['contact_form']))
		print('Twitter: @{}'.format(obj['twitter_id']))
		print('Facebook: https://www.facebook.com/{}'.format(obj['facebook_id']))
		print('YouTube: {}'.format(obj['youtube_id']))

		choice = int(click.prompt('\n1. Main Menu   2. Exit Application'))
		if(choice == 1): Main_Screen()  #turn this into function!!!!!!!!!!!
		if(choice == 2): break




@click.command()
#@click.option('--zipcode', prompt='What is your zipcode?')
#@click.option('--keywords',prompt='What would you like to search for?')
def main():
	
	Main_Screen()
	

	#url='https://congress.api.sunlightfoundation.com/bills/search?query=%22{}%22&history.enacted=true'.format(keywords)
	


	'''bill_id = 's3055-114'
	bill_summary_url = 'https://congress.api.sunlightfoundation.com/bills?bill_id={}&fields=last_action,cosponsors_count,committees'.format(bill_id)

	bill_summary_rough = urllib.request.urlopen(bill_summary_url).read()

	bill_summary_obj = str(bill_summary_rough, 'utf-8')

	summary_data = json.loads(bill_summary_obj)


	bill_status_text = summary_data['results'][0]['last_action']['text']
	bill_action_date = summary_data['results'][0]['last_action']['acted_at']

	print('This bill {} on {}'.format(bill_status_text,bill_action_date))

	for objz in summary_data['results']:
	print(objz['summary_short'])'''
	

if __name__ == '__main__':
	main()

