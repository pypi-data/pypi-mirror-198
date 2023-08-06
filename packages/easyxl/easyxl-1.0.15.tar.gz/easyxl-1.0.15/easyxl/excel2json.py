import os
import re
import mjson5
import sys
from xlwings import Sheet as Sheet_
from pathlib import Path
try:
    from .utils import *
except:
    from utils import *


json_str_reg = re.compile(r"^\[[\s\S]*\]$|^\{[\s\S]*\}$")
wrap_list_reg = re.compile(r"^\{[\w]+:\[\]\}$")
wrap_list_key_reg = re.compile(r"[\w]+")
number_reg = re.compile(r"^[0-9\.]+$")

null_tags = ['null', 'none']
convert_types = ['int', 'float', 'str', 'bool']
header_split_char = "-"
comment_char = "#"


def find_name(splitted_text):
    c0 = splitted_text[0]
    if check_str_tags(splitted_text, null_tags) or (not c0):
        rlt = None
    elif number_reg.match(c0):
        rlt = str(int(float(c0)))
    else:
        rlt = c0
    return rlt

def find_convert_type(splitted_text):
    for i in convert_types:
        if i in splitted_text:
            rlt = i
            break
    else:
        rlt = None
    return rlt
        

def first_n_last_con_occ(in_list, check_str):
    first_occ = None
    last_occ = None
    
    for idx, item in enumerate(in_list):
        if first_occ is None:
            if check_str_tags(item, check_str):
                if not str(item).startswith(comment_char):
                    first_occ = idx + 1
                else:
                    continue
            else:
                continue
        else:
            if check_str_tags(item, check_str):
                if not str(item).startswith(comment_char):
                    last_occ = idx + 1
                else:
                    continue
            else:
                continue
    
    if last_occ is None:
        last_occ = first_occ
    return first_occ, last_occ


def split_text(input):
    if type(input) is not str:
        input = str(input)
    output = [i.strip() for i in \
        re.split(header_split_char, input)]
    return output


def check_str_tags(src, tags):
    b = False

    if type(src) is str:
        src = [i.lower() for i in split_text(src)]
    elif type(src) is list:
        src = [str(i).lower() for i in src]
    elif src is None:
        src = ["none"]
    else:
        return False

    if type(src) is list:
        if type(tags) is str:
            b = tags in src
        elif type(tags) is list:
            for tag in tags:
                if tag in src:
                    b = True
                    break
    else:
        raise ValueError("src type error")

    return b


def convert_cell_value(src, convert_type=None):

    def convert(x, c_type):
        if c_type is None:
            rlt = x
        elif c_type == 'int':
            rlt = int(x)
        elif c_type == 'float':
            rlt = float(x)
        elif c_type == 'str':
            rlt = str(x)
        elif c_type == 'bool':
            rlt = bool(x)
        else:
            rlt = x
        return rlt
    
    result = src
    if type(src) is str and json_str_reg.match(src):
        result = mjson5.loads(src)
    else:
        if convert_type:
            try:
                result = convert(src, convert_type)
            except:
                print("                Fail {0}: {1}".format(convert_type, src))
    return result


def convert_cell_values(srcs, convert_type):
    if type(srcs) is list:
        rlt = [convert_cell_value(src, convert_type) for src in srcs]
    else:
        rlt = convert_cell_value(srcs, convert_type)
    return rlt


def get_header_range(ws, row, col, d=(0, 0)):
    cell = ws.range((row, col))

    if cell.merge_cells:
        address = cell.merge_area.address
        rng = convert_xlsx_addr(address)
    else:
        content = cell.value
        ss = split_text(content)
        cell_name = find_name(ss)
        if type(cell_name) is str and cell_name.startswith(comment_char):
            cell_name = cell_name[1:]
        test_len = max( (ws.ids_end_row-row)*d[0], (ws.headers_end_col-col)*d[1] )

        f_row = row
        f_col = col

        for i in range(1, test_len+1):
            test_row = row + i*d[0]
            test_col = col + i*d[1]
            test_content = ws.range((test_row, test_col)).value
            s_test_content = split_text(test_content)
            test_name = find_name(s_test_content)
            if test_name == cell_name or test_name is None or \
                (test_name.startswith(comment_char) and test_name[1:] == cell_name):
                f_row = test_row
                f_col = test_col
                continue
            else:
                break
        rng = tuple([(row, col), (f_row, f_col)])
    return rng


def fill_ids(iheaders):
    for i in iheaders:
        f_type = i._data._type
        if i.is_id_h_end: # 已经到达Header的垂直结束位置，分情况进行数据填充
            if f_type == "dict":
                if i._height == 1:
                    i._data[i._index] = UnifiedData(i._type)
                    headers = Headers(i._ws, i._row, i._ws.headers_start_row, \
                        i._ws.headers_start_col, i._ws.headers_end_col, \
                            i._data[i._index], next_idx=0)
                    fill_headers(headers)
                else:
                    i._data[i._index] = UnifiedData('list')
                    for idx, row in enumerate(range(i._row, i._row + i._height)):
                        i._data[i._index][str(idx)] = UnifiedData(i._type)
                        headers = Headers(i._ws, row, i._ws.headers_start_row, \
                            i._ws.headers_start_col, i._ws.headers_end_col, \
                                i._data[i._index][str(idx)], next_idx=0)
                        fill_headers(headers)
                
            elif f_type == "list":
                if i._type == "dict":
                    if i._name:
                        if i._height == 1:
                            i._data[i._index] = UnifiedData(i._type)
                            headers = Headers(i._ws, i._row, i._ws.headers_start_row, \
                                i._ws.headers_start_col, i._ws.headers_end_col, \
                                    i._data[i._index], next_idx=0)
                            fill_headers(headers)
                        else:
                            i._data[i._index] = UnifiedData('dict')
                            i._data[i._index][i._name] = UnifiedData('list')
                            
                            for idx, row in enumerate(range(i._row, i._row + i._height)):
                                i._data[i._index][i._name][str(idx)] = UnifiedData(i._type)
                                headers = Headers(i._ws, row, i._ws.headers_start_row, \
                                    i._ws.headers_start_col, i._ws.headers_end_col, \
                                        i._data[i._index][i._name][str(idx)], next_idx=0)
                                fill_headers(headers)
                    else:
                        if i._height == 1:
                            i._data[i._index] = UnifiedData(i._type)
                            headers = Headers(i._ws, i._row, i._ws.headers_start_row, \
                                i._ws.headers_start_col, i._ws.headers_end_col, \
                                    i._data[i._index], next_idx=0)
                            fill_headers(headers)
                        else:
                            i._data[i._index] = UnifiedData('list')
                            
                            for idx, row in enumerate(range(i._row, i._row + i._height)):
                                i._data[i._index][str(idx)] = UnifiedData(i._type)
                                headers = Headers(i._ws, row, i._ws.headers_start_row, \
                                    i._ws.headers_start_col, i._ws.headers_end_col, \
                                        i._data[i._index][str(idx)], next_idx=0)
                                fill_headers(headers)
                    
                        
                elif i._type == "list":
                    i._data[i._index] = UnifiedData(i._type)
                    
                    for idx, row in enumerate(range(i._row, i._row + i._height)):
                        i._data[i._index][str(idx)] = UnifiedData('dict')
                        headers = Headers(i._ws, row, i._ws.headers_start_row, \
                            i._ws.headers_start_col, i._ws.headers_end_col, \
                                i._data[i._index][str(idx)], next_idx=0)
                        fill_headers(headers)

        else: # 如果未到达header的垂直末尾，则进行递归
            i._data[i._index] = UnifiedData(i._type)
            sub_ids = Ids(i._ws, i._col+1, i._row, i._end_row, \
                i._data[i._index], next_idx=0)
            fill_ids(sub_ids)

def fill_headers(headers):
    for h in headers:
        f_type = h._data._type
        if h.is_header_v_end: # 已经到达Header的垂直结束位置，分情况进行数据填充
            if f_type == "dict":
                if h._type == "dict":
                    h._data[h._index] = \
                        convert_cell_values(h._ws.range(*h._content_range).value, \
                            h._convert_type)
                elif h._type == "list":
                    if h._width == 1:
                        h._data[h._index] = \
                            [convert_cell_values(h._ws.range(*h._content_range).value, \
                                h._convert_type)]
                    else:
                        h._data[h._index] = \
                            convert_cell_values(h._ws.range(*h._content_range).value, \
                                h._convert_type)
                        
            elif f_type == "list":
                if h._type == "dict":
                    if h._name:
                        h._data[h._index] = {h._name: convert_cell_values(\
                                h._ws.range(*h._content_range).value, h._convert_type)}

                    else: # 如果list下边是空Cell或者标注null_tags的Cell，直接把数据注册到list下
                        h._data[h._index] = convert_cell_values(\
                            h._ws.range(*h._content_range).value, h._convert_type)
                        
                elif h._type == "list":
                    h._data[h._index] = convert_cell_values(\
                        h._ws.range(*h._content_range).value, h._convert_type)

        else: # 如果未到达header的垂直末尾，则进行递归
            h._data[h._index] = UnifiedData(h._type)
            sub_headers = Headers(h._ws, h._content_row, h._row+1, h._col, \
                h._end_col, h._data[h._index], next_idx=0)
            fill_headers(sub_headers)




class Ids:
    def __init__(self, ws, id_start_col, id_next_row, ids_end_row, data, next_idx=0):
        self._ws = ws

        self._col = id_start_col
        self._id_next_row = id_next_row
        self._ids_end_row = ids_end_row

        self._data = data
        self._next_idx = next_idx

        self._row = id_next_row
        self._range = None
        self._content = None
        self._height = None
        self._end_row = None
        self._idx = None
        self._name = None
        self._type = None
        self._index = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.get_id_info()
        rlt = self
        if self._id_next_row > self._ids_end_row:
            raise StopIteration
        if type(self._name) is str and self._name.startswith(comment_char):
            self._id_next_row = self._end_row + 1
            rlt = self.__next__()
        self._id_next_row = self._end_row + 1
        self._next_idx += 1
        return rlt
    
    def check_id_h_end(self):
        b = False
        if self._col == self._ws.ids_end_col:
            b = True
        else:
            b = True
            for row in range(self._row, self._end_row+1):
                cell_right = self._ws.range((row, self._col+1))
                if cell_right.value and \
                    not check_str_tags(cell_right.value, null_tags):
                    b = False
                    break
        return b

    def get_id_info(self):
        # 将row和idx更新为下一个id的col和排序
        self._row = self._id_next_row
        self._idx = self._next_idx

        # 更新id的_range、_content、_height、_end_row、_name、_type、_index
        cell = self._ws.range((self._row, self._col))
        self._range = get_header_range(self._ws, self._row, self._col, d =(1, 0))
        self._content = str(cell.value)
        range_len = len(self._range)
        if range_len == 1:
            self._height = 1
            self._end_row = self._range[0][0]
        elif range_len ==2:
            self._height = self._range[1][0] - self._range[0][0] + 1
            self._end_row = self._range[1][0]
        else:
            raise ValueError("id range error")

        # 获取header的_name和_convert_type
        ss = split_text(self._content)
        self._name = find_name(ss)
        self._convert_type = find_convert_type(ss)

        # 获取header的_type，如果有'list'，则为list，否则为dict。空的Cell默认为dict
        self._type = 'list' if 'list' in ss else 'dict'
        
        # 根据传入的data的_type（也就是父节点的_type，f_type），决定header的_index
        # 如果f_type是dict，那么index就是name，如果是list，那么index就是idx
        if self._data._type == 'list':
            self._index = str(self._idx)
        elif self._data._type == 'dict':
            self._index = str(self._name) if self._name else None
        else:
            # print(self._data._type)
            raise ValueError("data type must be 'list' or 'dict'")

        self.is_id_h_end = self.check_id_h_end()
        # print("end of update_id_info")
            

class Headers:
    def __init__(self, ws, content_row, header_start_row, \
        header_next_col, headers_end_col, data, next_idx=0):
        ## sheet info
        self._ws = ws
        self._content_row = content_row

        self._row = header_start_row
        self._header_next_col = header_next_col
        self._headers_end_col = headers_end_col

        self._data = data
        self._next_idx = next_idx

        # info updated by update_header_info
        self._col = header_next_col
        self._range = None
        self._content = None
        self._width = None
        self._end_col = None
        self._idx = None
        self._name = None
        self._type = None
        self._index = None
        
    def __iter__(self):
        return self

    def __next__(self):
        rlt = self
        self.update_header_info()
        if self._header_next_col > self._headers_end_col:
            raise StopIteration
        # 跳过以#开头的非空header
        if type(self._name) is str and self._name.startswith(comment_char):
            self._header_next_col = self._end_col + 1
            rlt = self.__next__()
        self._header_next_col = self._end_col + 1
        self._next_idx += 1
        return rlt

    def check_header_v_end(self):
        b = False
        if self._row == self._ws.headers_end_row:
            b = True
        else:
            b = True
            for col in range(self._col, self._end_col+1):
                cell_below = self._ws.range((self._row + 1, col))
                if cell_below.value and \
                    not check_str_tags(cell_below.value, null_tags):
                    b = False
                    break
        return b
            
    def update_header_info(self):
        # 将col和idx更新为下一个header的col和排序
        self._col = self._header_next_col
        self._idx = self._next_idx

        # 获取header的_range、_content、_content_range、_width、_end_col
        cell = self._ws.range(self._row, self._col)
        self._range = get_header_range(self._ws, self._row, self._col, d=(0, 1))
        self._content_range = tuple((self._content_row, self._range[i][1]) \
            for i in range(len(self._range)))
        self._content = str(cell.value)

        range_len = len(self._range)
        if range_len == 1:
            self._width = 1
            self._end_col = self._range[0][1]
        elif range_len == 2:
            self._width = self._range[1][1] - self._range[0][1] + 1
            self._end_col = self._range[1][1]
        else:
            raise ValueError("header range error")

        # _name: 如果header的内容中包含%，则取%前面的内容作为name
        # 如果%拆分后得到name==’’，或者content包含null_tags，则name为None
        ss = split_text(self._content)
        self._name = find_name(ss)
        self._convert_type = find_convert_type(ss)

        # 获取header的_type，如果有'list'，则为list，否则为dict。空的Cell默认为dict
        self._type = 'list' if 'list' in ss else 'dict'
        
        # 根据传入的data的_type（也就是父节点的_type，f_type），决定header的_index
        # 如果f_type是dict，那么index就是name，如果是list，那么index就是idx
        if self._data._type == 'list':
            self._index = str(self._idx)
        elif self._data._type == 'dict':
            self._index = str(self._name) if self._name else None
        else:
            raise ValueError("data type must be 'list' or 'dict'")

        self.is_header_v_end = self.check_header_v_end()
    

class Sheet(Sheet_):
    def __init__(self, ws, json_folder=None, OneFilePerId=False, \
        IgnoreNull=True, Dumpformat=None, impl=None):
        super().__init__(ws)
        self._ws = ws
        self.json_folder = json_folder
        self.OneFilePerId = OneFilePerId
        self.IgnoreNull = IgnoreNull
        self.Dumpformat = Dumpformat
        self.update_sheet_info()

    def update_sheet_info(self):
        # 获取headers的起始行、终止行
        self.content_end_row = self._ws.range('1:1').end('down').row
        vertical_notes = self._ws.range(1, 1).expand('down').value

        self.headers_start_row, self.headers_end_row = \
            first_n_last_con_occ(vertical_notes, 'h')
        self.content_start_row = self.headers_end_row + 1

        # 获取headers的起始列、终止列
        col = 1
        first_headers = []
        while self._ws.range(self.headers_start_row, col).value or \
            self._ws.range(self.headers_start_row, col).merge_cells:
            first_headers.append(self._ws.range(self.headers_start_row, \
                col).value)
            col += 1
            
        self.headers_end_col = len(first_headers)
        self.ids_start_col, self.ids_end_col = first_n_last_con_occ(first_headers, 'id')
        self.headers_start_col = self.ids_end_col + 1
        self.ids_end_row = self.content_end_row
    
    def process_sheet(self):
        if not os.path.exists(self.json_folder):
            os.mkdir(self.json_folder)

        init_cell_name = split_text(self._ws.range(1, 1).value)[0]
        if wrap_list_reg.match(init_cell_name) and not self.OneFilePerId:
            data = UnifiedData('list')
        else:
            data = UnifiedData('dict')
        ids = Ids(self, self.ids_start_col, self.content_start_row, \
            self.content_end_row, data, next_idx=0)
        fill_ids(ids)
        if self.IgnoreNull:
            tag_data(data)
            prune_data(data)

        if self.OneFilePerId:
            self.json_folder = os.path.join(self.json_folder, self._ws.name)
            if not os.path.exists(self.json_folder):
                os.mkdir(self.json_folder)
            keys = remove_keys(data, keys_to_remove)
            for key in keys:
                if type(data[key]) is UnifiedData:
                    result = render_unified_data(data[key])
                    file_path = os.path.join(self.json_folder, key + '.json')
                    with open(file_path, 'w', encoding='utf-8') as f:
                        mjson5.dump(result, f, **self.Dumpformat)
                else:
                    print("failed to dump data {0}: {1}".format(self._ws.name, key))
        else:
            if wrap_list_reg.match(init_cell_name):
                wrap_key_name = wrap_list_key_reg.findall(init_cell_name)[0]
                wrap_data = UnifiedData('dict')
                wrap_data[wrap_key_name] = data
                data = wrap_data

            result = render_unified_data(data)
            file_path = os.path.join(self.json_folder, self._ws.name + '.json')
            with open(file_path, 'w', encoding='utf-8') as f:
                mjson5.dump(result, f, **self.Dumpformat)

    
def process_wb(wb_path, app, wb):
    cmd_ws = wb.sheets['cmd']
    parent_folder = os.path.dirname(wb_path)
    task_end_row = cmd_ws.range('1:1').end('down').row
    header_end_col = cmd_ws.range('1:1').end('right').column
    header_cols = {h: idx for idx, h in \
        enumerate(cmd_ws.range(1, 1).expand('right').value)}
    for row in range(2, task_end_row+1):
        if str(cmd_ws.range(row, 1).value).startswith(comment_char):
            continue
        else:
            row_content = cmd_ws.range((row, 1), (row, header_end_col)).value

            Task = row_content[header_cols['Task']]
            SheetName = row_content[header_cols['SheetName']]
            Export = row_content[header_cols['Export']]
            OneFilePerId = True if row_content[header_cols['OneFilePerId']] \
                else False

            stem = Path(wb_path).stem
            OutputFolder = os.path.join(parent_folder, stem)

            QuoteKeys = row_content[header_cols['QuoteKeys']]
            SortKeys = row_content[header_cols['SortKeys']]
            Indent = row_content[header_cols['Indent']]
            IgnoreNull = row_content[header_cols['IgnoreNull']]

            DumpFormat = dict(
            quote_keys = True if QuoteKeys else False,
            sort_keys = True if SortKeys else False,
            indent = int(Indent) if str(Indent).isdigit() else 4,
            trailing_commas = False,
            ensure_ascii = False,
            )

            print("\n>>> Task: {0}".format(Task))
            if Export:
                ws = wb.sheets[SheetName]
                sh = Sheet(ws, OutputFolder, OneFilePerId, IgnoreNull, DumpFormat)
                sh.process_sheet()
    wb.close()
    app.kill()


def excel2json(wb_path, mode=None):
    app, wb = xw_open(wb_path)

    if mode=='dev':
        print('dev mode')
        print(sys.argv)
        process_wb(wb_path, app, wb)
    else:
        try:
            process_wb(wb_path, app, wb)
        except:
            wb.close()
            app.kill()
    print('\n')


def main():
    TestHeader = False
    mode = 'dev'
    if TestHeader:
        wb_path = r"D:\GIT\Github\easyxl\xlsx\test.xlsx"
        if len(sys.argv) > 2:
            mode = sys.argv[2]
        if len(sys.argv) > 1:
            wb_path = sys.argv[1]
        excel2json(wb_path, mode)
    
    TestId = True
    if TestId:
        wb_path = r"D:\GIT\Github\easyxl\xlsx\test.xlsx"
        excel2json(wb_path, 'dev') 

    

if __name__ == "__main__":
    main()