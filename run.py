# coding:utf--8

"""
静态服务器
"""
import sys
if sys.version_info[0] == 2:
    print('请使用 Python3 启动服务器')
    exit()

from wsgiref.simple_server import make_server
import mimetypes
import os


class WSGIHandler(object):
    def get_response(self, path):
        fpath = os.path.abspath(os.path.join(self.root, path))
        if os.path.isfile(fpath):
            content_type, encoding = mimetypes.guess_type(str(fpath))
            content_type = content_type or 'application/octet-stream'
            header = [('Content-Type', content_type)]
            if encoding:
                header.append(("Content-Encoding", encoding))

            with open(fpath, 'rb') as rf:
                content = rf.read()
                return '200 OK', header, [content]
        else:
            return '404 Not Found', [('Content-Type', 'text/html;charset=utf-8')], ['<h1>404 文件不存在</h1>'.encode('utf-8')]

    def __init__(self,  root):
        self.root = os.path.abspath(root)

        print('载入网站路径', self.root)

    def __call__(self, environ, start_response):
        url = environ.get('PATH_INFO', '/')
        if url == '/':
            url = 'index.html'
        status_code, header, response = self.get_response(url.lstrip('/'))
        start_response(status_code, header)
        return response


if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) > 1 else 8000
    site_path = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()
    print(site_path)
    httpd = make_server('', int(port), WSGIHandler(site_path))
    print(f"启动服务器 http://0.0.0.0:{httpd.server_port}")
    # 开始监听HTTP请求:
    httpd.serve_forever()
