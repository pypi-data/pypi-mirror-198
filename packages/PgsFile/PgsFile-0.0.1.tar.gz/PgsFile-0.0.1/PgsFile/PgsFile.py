# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 23:44:04 2021

@author: Petercusin
"""



def get_data_text(path):
    import chardet
    path=path.replace("\n","")
    #path=r'C:\Users\Petercusin\Desktop\123.txt'
    f=open(path,'rb')  # 先用二进制打开
    data=f.read()  # 读取文件内容
    f.close()
    file_encoding=chardet.detect(data).get('encoding')  # 得到文件的编码格式
    f1=open(path,'r', encoding=file_encoding, errors='ignore')  # 使用得到的文件编码格式打开文件
    text=f1.read().replace("’","'")
    f1.close()
    return text
            
def get_data_lines(path):
    import chardet
    path=path.replace("\n","")
    #path=r'C:\Users\Petercusin\Desktop\123.txt'
    f=open(path,'rb')  # 先用二进制打开
    data=f.read()  # 读取文件内容
    f.close()
    file_encoding=chardet.detect(data).get('encoding')  # 得到文件的编码格式
    f1=open(path,'r', encoding=file_encoding, errors='ignore')  # 使用得到的文件编码格式打开文件
    lines=f1.readlines()
    lines=[l.replace("’","'") for l in lines if len(l.strip()) !=0]
    f1.close()
    return lines

def write_to_txt(file_path,text,mode=None,encoding=None):
    '''
    Parameters
    ----------
    file_path : TYPE string
        DESCRIPTION.
    text : TYPE
        DESCRIPTION. string
    mode : TYPE, optional # w;a+
        DESCRIPTION. The default is None.
    encoding : TYPE, optional # utf-8
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    '''
    if mode is None:
        mode="w"
    else:
        mode=mode
    if encoding is None:
        encoding="utf-8"
    else:
        encoding=encoding    
    f=open(file_path,mode=mode,encoding=encoding)
    f.write(text.strip()+"\n")
    f.close()

def get_data_excel(excel_path,column_id,sheet_name=None):
    '''
    Parameters
    ----------
    excel_path : TYPE
        DESCRIPTION. D://data_python.xlsx
        
    column_id : TYPE Int 0,1,2,3
        DESCRIPTION. 0 means the first column, 1 means the second.
        
    sheet_name : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    TYPE list
        DESCRIPTION. return a list of data.
    '''
    
    import pandas as pd
    if sheet_name is None:
        sheet_name=0
    else:
       sheet_name=sheet_name  
    df=pd.read_excel(excel_path,keep_default_na=False, sheet_name=sheet_name,header=None) 
    inter=df.iloc[0:,column_id] #提取第二列所有行  
    return list(inter)

def write_to_excel(excel_path,dic_of_list,sheet_name=None,index=None):
    '''
    Parameters
    ----------
    excel_path : TYPE
        DESCRIPTION. D://results.xlsx
        
    dic_of_list : TYPE
        DESCRIPTION. {"col":["a","b","c","d"],"freq":[1,2,3,4]}
        
    sheet_name : TYPE, optional
        DESCRIPTION. The default is None.
        
    index : TYPE, optional
        DESCRIPTION. The default is None.
        
    Returns
    -------
    None.

    '''
    import pandas as pd
    if sheet_name is None:
        sheet_name="sheet1"
    else:
       sheet_name=sheet_name
    if index is None:
        index=False
    else:
        index=True        
        
    df=pd.DataFrame(dic_of_list)
    df.style.to_excel(excel_path, sheet_name=sheet_name,startcol=0, index=index)
    
 
def get_data_json(json_path):
    '''
    Parameters
    ----------
    json_path : TYPE D://data.json
        DESCRIPTION.

    Returns
    -------
    load_dict : TYPE dict
        DESCRIPTION. return a dict of data.

    '''
    import json
    try:
        f=open(json_path,"r",encoding="utf-8")
        load_dict=json.load(f)    
        return load_dict            
    except:
        f=open(json_path,"r",encoding="utf-8-sig")
        load_dict=json.load(f)    
        return load_dict

def write_to_json(json_path,my_dic):
    '''

    Parameters
    ----------
    json_path : TYPE string
        DESCRIPTION. D://data.json
        
    my_dic : TYPE dict or list
        DESCRIPTION. 
        type1: {"pans":1}
        type2: {"word":["a","b","c"]}
        type3: [{"pans":1},{"glenna":2}]
        type4: [{"word":["a","b","c"]},{"freq":[1,2,3,4,5,6]}]

    Returns
    -------
    None.

    '''
    import json
    f2 = open(json_path, "w", encoding="utf-8", errors="ignore")
    f2.write(json.dumps(my_dic,ensure_ascii=False)) #ensure_ascii=False 让中文不再乱码
    f2.close() 
    



    