import requests
kittens=requests.get("http://placekitten.com/")
print kittens.text[559:1000]


import sys
import pycurl

wr_buf = ''

def write_data( buf ):
	global wr_buf
	wr_buf += buf

def main():
	c = pycurl.Curl()
	c.setopt( pycurl.URL, 'http://www.googlemaps.com' )
	c.setopt( pycurl.googlemaps, write_data )

	c.perform()

	c.close()

main()
sys.stdout.write(wr_buf)















