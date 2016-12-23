#encoding=utf8
import json
if __name__=='__main__':
    # 获取输入数据
    input_file = raw_input('csvFileName:')
    lines = open(input_file, "r").readlines()
    lines = [line.strip() for line in lines]
    # 获取键值
    keys = lines[0].split(',')
    line_num = 1
    total_lines = len(lines)
    parsed_datas = []
    while line_num < total_lines:
            # 按情况修改
            values = []
            for item in lines[line_num].split(',"'):
                values.append(item.strip('"'))
            values.append(list(values[3].split('",')[1].split(',')))
            values[3] = values[3].split('",')[0]

            parsed_datas.append(dict(zip(keys, values)))
            line_num = line_num + 1

    json_str = json.dumps(parsed_datas, ensure_ascii=False, indent=4)
    output_file = input_file.replace("csv", "json")

    # write to the file
    f = open(output_file, "w")
    f.write(json_str)
    f.close()

    print("解析结束！")