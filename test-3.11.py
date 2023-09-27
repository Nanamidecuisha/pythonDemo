import cgi
import urllib.parse as parse
import platform
import html




if __name__ == '__main__':
    # 查询字符串示例
    query_string = "name=John&age=30&city=New+York"
    # 需要进行转义的文本
    user_input = "<script>alert('Hello, XSS!');</script>"

    # 使用 parse_qs 解析查询字符串
    parsed_data = parse.parse_qs(query_string)
    # 使用 parse_qsl 解析查询字符串
    parseqsl_data = parse.parse_qsl(query_string)
    # 使用 escape 进行转义
    escaped_text = html.escape(user_input)
    print(f'python version is ,{platform.python_version()}')
    # 打印解析后的数据
    print(f'parse_qs data,{parsed_data}')
    print(f'parse_qsl data,{parseqsl_data}')
    print(f'escaped_text data,{escaped_text}')