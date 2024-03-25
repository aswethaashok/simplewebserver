from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>
Top Companies List
</title>
</head>
<table align="center" border="4" cellspacing="5" cellpadding="10" height="100" width="800">
<caption align="center"><B>Top Companies Lists</B></caption>
<tr>
<th align="center">Rank</th>
<th align="center">Company</th>
<th align="center">Country</th>
<th align="center">Revenue</th>
<th align="center">Exchange</th>
<th align="center">Market Value</th>
</tr>
<tr>
  <td align="center">1.</td>
  <td align="center">Microsoft Corp</td>
  <td align="center">United States</td>
  <td align="center">$203.08 B</td>
  <td align="center">NASDAQ</td>
  <td align="center">$1.82 T</td>
</tr>
<tr>
  <td align="center">2.</td>
  <td align="center">Oracle Corp</td>
  <td align="center">United States</td>
  <td align="center">$46.07 B</td>
  <td align="center">New York Stock Exchange</td>
  <td align="center">$219.74 B</td>
</tr>
<tr>
  <td align="center">3.</td>
  <td align="center">SAP SE</td>
  <td align="center">Germany</td>
  <td align="center">$32.97 B</td>
  <td align="center">New York Stock Exchange</td>
  <td align="center">$122.57 B</td>
</tr>
<tr>
  <td align="center">4.</td>
  <td align="center">Salesforce Inc.</td>
  <td align="center">United States</td>
  <td align="center">$30.29 B</td>
  <td align="center">NewYork Stock Exchange</td>
  <td align="center">$130.30 B</td>
</tr>
<tr>
  <td align="center">5.</td>
  <td align="center">Adobe Inc.</td>
  <td align="center">United States</td>
  <td align="center">$17.61 B</td>
  <td align="center">NASDAQ</td>
  <td align="center">$158.71 B</td>
</tr>
</table>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()