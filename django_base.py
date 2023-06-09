# import urllib.request
#
# url = 'https://www.google.com'
#
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
#
# html = response.read()
#
# print(html)
#
# import http.client
# from urllib.parse import urlunparse, urljoin
# from urllib.request import urlopen, urlretrieve
# from html.parser import HTMLParser
# from pathlib import Path
#
#
# class ImagePaser(HTMLParser):  # HTMLParser를 상속
# 	def __init__(self):
# 		super().__init__()
# 		self.result = []
#
# 	def handle_starttag(self, tag, attrs):
# 		if tag != 'img':
# 			return
# 		if not hasattr(self, 'result'):
# 			self.result = []
# 		for name, value in attrs:
# 			if name == 'src':
# 				self.result.append(value)
#
#
# def parse_image(data):
# 	parser = ImagePaser()
# 	parser.feed(data)
# 	data_set = set(x for x in parser.result)
# 	return data_set
#
#
# def download_image(url, data):
# 	download_dir = Path("DOWNLOAD")
# 	download_dir.mkdir(exist_ok=True)
#
# 	parser = ImagePaser()
# 	parser.feed(data)
# 	data_set = set(x for x in parser.result)
# 	for x in sorted(data_set):
# 		image_url = urljoin(url, x)
# 		basename = Path(image_url).name
# 		target_file = download_dir / basename
# 		print(target_file)
#
# 		print("Downloading...", image_url)
# 		urlretrieve(image_url, target_file)
#
# 	return data_set
#
#
# def main():
# 	# url = 'https://google.com'
# 	# with urlopen(url) as f:
# 	# 	charset =f.headers.get_params('charset')[1][1]
# 	# 	data = f.read().decode(charset)
# 	# 위와 같은 방법
# 	host = "www.google.co.kr"
# 	conn = http.client.HTTPConnection(host)
# 	conn.request('GET', "")
# 	resp = conn.getresponse()
#
# 	charset = resp.msg.get_param("charset")
# 	print('charset:', charset)
# 	data = resp.read().decode(charset)
# 	conn.close()
#
# 	print("\n >>>>> 다운로드중..", host)
# 	url = urlunparse(('http', host, '', '', '', ''))
#
# 	data_set = parse_image(data)
# 	print("\n >>>> Fetcch Images from", url)
# 	print("\n".join(sorted(data_set)))
#
# 	download_image(url, data)
#
#
# if __name__ == '__main__':
# 	main()

# # 서버 실습
# from http.server import HTTPServer, BaseHTTPRequestHandler
#
#
# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
# 	def do_GET(self):
# 		self.send_response(200, "OK")
# 		self.send_header('Content-Type', 'text/plain')
# 		self.end_headers()
# 		self.wfile.write(b"Hello World")
#
#
# server = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
# server.serve_forever()

# 서버를 작동시키고 어플을 얹는것
from wsgiref.simple_server import make_server


def application(environ, start_response):
	response_body = b"Hello World"
	status = "200 OK"
	headers = [("Content-Type", "text/plain")]

	start_response(status, headers)
	return [response_body]


if __name__ == '__main__':
	httpd = make_server("", 8000, application)
	print("Running..")
	httpd.serve_forever()