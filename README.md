# jsonx

CN: 替代默认JSON.parse, 将大整数替换为字符串格式保留精度
EN: suport bigint in json, parse bingint to str


useage: 
let json_str = '{"num": 1234567890123456789}'
let jsonx = new JSONX(json_str)
let obj = jsonx.parse()

开启测试服务器
on linux:
python3 run.py 9000
