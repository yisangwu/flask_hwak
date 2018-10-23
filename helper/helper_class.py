# coding=utf-8

'''
Helper
@subpackage Helper_Singleton
单例模式
'''
class ObjSingleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(HelperSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def import_views(app=None, module=None, file=None):
    '''
    动态加载views
    @param app: 
    @param module:  __init__.py 文件所在目录
    @param file: __init__.py
    '''
    if not app or not module or not file:
        return False

    import os
    # __init__.py 文件所在目录
    path = os.path.dirname(os.path.realpath(file))

    # list当前目录文件
    DIR_FILE_LIST = os.listdir(path)

    # 开始导入
    if DIR_FILE_LIST:
        from werkzeug.utils import import_string
        # 遍历导入
        for py_file in DIR_FILE_LIST:
            # 目录，忽略
            if os.path.isdir(py_file):
                continue
            # __init__ 忽略
            if py_file.startswith('_'):
                continue
            # 不是 .py 后缀的。忽略
            if '.' not in py_file or py_file.split('.')[-1] != 'py':
                continue
            # 导入
            import_string('%s.%s.%s' % (app, module, py_file.split('.')[0]))

    return True