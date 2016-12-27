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

def find_matching_bills(keywords):
	keywords = quote(keywords)
	click.echo(keywords)

	url='https://congress.api.sunlightfoundation.com/bills/search?query=%22{}%22&history.enacted=true'.format(keywords)
	dataurl = urllib.request.urlopen(url).read()
	data = dataurl
	json_obj = str(data, 'utf-8')
	poldata = json.loads(json_obj)

	for obj in poldata['results']:
		print(obj['official_title'])
		bill_id_text = 'Bill id is: {}'.format(obj['bill_id'])
		click.echo(click.style(bill_id_text,bg='green'))
		print(obj['introduced_on'],'\n')



def find_my_legis(zipcode):
	url = 'https://congress.api.sunlightfoundation.com/legislators/locate?zip={}'.format(zipcode)
	print(url)

@click.command()
@click.option('--zipcode', prompt='What is your zipcode?')
@click.option('--keywords',prompt='What would you like to search for?')
def main (zipcode,keywords):
	print('This application is used for finding bills which contain certain keywords then enabling the user to gather more details about the bill \n')
	if zipcode:
		find_my_legis(zipcode)
		return

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

