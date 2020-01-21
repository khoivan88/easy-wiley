<<<<<<< HEAD
import xml.etree.ElementTree as ET
import os
import requests
import subprocess
import csv

ET.register_namespace('', 'http://purl.org/rss/1.0/')
ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
ET.register_namespace('prism', 'http://prismstandard.org/namespaces/basic/2.0/')
ET.register_namespace('content', 'http://purl.org/rss/1.0/modules/content/')
ET.register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')

def getxml():        
	url = 'https://onlinelibrary.wiley.com/action/showFeed?jc=15213773&type=etoc&feed=rss'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding': 'none',
                   'Accept-Language': 'en-US,en;q=0.8',
                   'Connection': 'keep-alive'}

	response = requests.get(url, headers = headers)
	if response.status_code == 200:
		root = ET.fromstring(requests.get(url, headers = headers).content)
		return root
	else:
		response.raise_for_status()

def getxmlfromfile():
	filename = 'acie.xml'
	tree = ET.parse(filename)
	root = tree.getroot()

	return root

def updaterss():
        root = getxml()

        # Read in old articles
        with open('acie_old.csv', 'rt') as fin:
                reader = csv.reader(fin)
                old_articles = list(reader)

        # Read in RSS articles and remove newer duplicates
        rss_articles = old_articles
        for paper in root[2:][::-1]:
                for doi in paper.findall('{http://prismstandard.org/namespaces/basic/2.0/}doi'):
                        doi = doi.text
                for date in paper.findall('{http://purl.org/dc/elements/1.1/}date'):
                        date = date.text

                if [doi, date] not in rss_articles:
                        if doi in [i[0] for i in rss_articles]:
                                root.remove(paper)
                                #print(paper.findall('{http://purl.org/dc/elements/1.1/}title')[0].text)
                        else:
                                rss_articles.append([doi, date])

        # Create new RSS feed
        with open('ACIE.xml', 'wb') as fout:
                fout.write(ET.tostring(root))

        # Update old article list
        with open('acie_old.csv', 'wt', newline = '') as fout:
                writer = csv.writer(fout, quoting = csv.QUOTE_ALL)
                for a in rss_articles:
                        b = fout.write((',').join(a) + '\n')

def ghpush(cdate):
        print(subprocess.check_output('git init'))
        print(subprocess.check_output('git add .'))
        subprocess.run('git commit -m "%s"' % cdate)
        subprocess.run('git push origin master')

##{http://purl.org/rss/1.0/}title {}
##{http://purl.org/dc/elements/1.1/}description {}
##{http://purl.org/dc/elements/1.1/}creator {}
##{http://purl.org/rss/1.0/}link {}
##{http://purl.org/rss/1.0/modules/content/}encoded {}
##{http://purl.org/rss/1.0/}description {}
##{http://purl.org/dc/elements/1.1/}title {}
##{http://purl.org/dc/elements/1.1/}identifier {}
##{http://purl.org/dc/elements/1.1/}source {}
##{http://purl.org/dc/elements/1.1/}date {}
##{http://prismstandard.org/namespaces/basic/2.0/}publicationName {}
##{http://prismstandard.org/namespaces/basic/2.0/}doi {}
##{http://prismstandard.org/namespaces/basic/2.0/}url {}
##{http://prismstandard.org/namespaces/basic/2.0/}copyright {}
##{http://prismstandard.org/namespaces/basic/2.0/}section {}
=======
import xml.etree.ElementTree as ET
import os
import requests
import subprocess
import csv

ET.register_namespace('', 'http://purl.org/rss/1.0/')
ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
ET.register_namespace('prism', 'http://prismstandard.org/namespaces/basic/2.0/')
ET.register_namespace('content', 'http://purl.org/rss/1.0/modules/content/')
ET.register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')

def getxml():        
	url = 'https://onlinelibrary.wiley.com/action/showFeed?jc=15213773&type=etoc&feed=rss'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding': 'none',
                   'Accept-Language': 'en-US,en;q=0.8',
                   'Connection': 'keep-alive'}

	response = requests.get(url, headers = headers)
	if response.status_code == 200:
		root = ET.fromstring(requests.get(url, headers = headers).content)
		return root
	else:
		response.raise_for_status()

def getxmlfromfile():
	filename = 'acie.xml'
	tree = ET.parse(filename)
	root = tree.getroot()

	return root

def updaterss():
        root = getxml()

        # Read in old articles
        with open('acie_old.csv', 'rt') as fin:
                reader = csv.reader(fin)
                old_articles = list(reader)

        # Read in RSS articles and remove newer duplicates
        rss_articles = old_articles
        for paper in root[2:][::-1]:
                for doi in paper.findall('{http://prismstandard.org/namespaces/basic/2.0/}doi'):
                        doi = doi.text
                for date in paper.findall('{http://purl.org/dc/elements/1.1/}date'):
                        date = date.text

                if [doi, date] not in rss_articles:
                        if doi in [i[0] for i in rss_articles]:
                                root.remove(paper)
                                #print(paper.findall('{http://purl.org/dc/elements/1.1/}title')[0].text)
                        else:
                                rss_articles.append([doi, date])

        # Create new RSS feed
        with open('ACIE.xml', 'wb') as fout:
                fout.write(ET.tostring(root))

        # Update old article list
        with open('acie_old.csv', 'wt', newline = '') as fout:
                writer = csv.writer(fout, quoting = csv.QUOTE_ALL)
                for a in rss_articles:
                        b = fout.write((',').join(a) + '\n')

def ghpush(cdate):
        print(subprocess.check_output('git init'))
        print(subprocess.check_output('git add .'))
        subprocess.run('git commit -m "%s"' % cdate)
        subprocess.run('git push origin master')

##{http://purl.org/rss/1.0/}title {}
##{http://purl.org/dc/elements/1.1/}description {}
##{http://purl.org/dc/elements/1.1/}creator {}
##{http://purl.org/rss/1.0/}link {}
##{http://purl.org/rss/1.0/modules/content/}encoded {}
##{http://purl.org/rss/1.0/}description {}
##{http://purl.org/dc/elements/1.1/}title {}
##{http://purl.org/dc/elements/1.1/}identifier {}
##{http://purl.org/dc/elements/1.1/}source {}
##{http://purl.org/dc/elements/1.1/}date {}
##{http://prismstandard.org/namespaces/basic/2.0/}publicationName {}
##{http://prismstandard.org/namespaces/basic/2.0/}doi {}
##{http://prismstandard.org/namespaces/basic/2.0/}url {}
##{http://prismstandard.org/namespaces/basic/2.0/}copyright {}
##{http://prismstandard.org/namespaces/basic/2.0/}section {}
>>>>>>> f40365329ff4e8368af6923c797429068942ebf3
