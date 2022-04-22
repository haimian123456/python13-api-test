import logging
from common.conf import Conf



#实例化配置类
conf=Conf()
#获取日志输出格式
fmt=conf.get_str('logger','formatter')
#获取日志收集器级别
setlevel = conf.get_str('logger', 'setLevel')
#获取控制台输出渠道 级别
stream_setlevel = conf.get_str('logger', 'stream_handler_setLevel')
#获取文件输出渠道 级别
file_setlevel = conf.get_str('logger', 'file_handler_setLevel')
def get_logger(logger_name,file_name):
    #日志收集器
    logger=logging.getLogger(logger_name)
    #日志收集级别
    logger.setLevel(setlevel)

    #规定日志输出格式
    formatter=logging.Formatter(fmt)

    #输出渠道 控制台
    stream_handler=logging.StreamHandler()
    # 输出渠道 文件
    file_handler = logging.FileHandler(file_name, encoding='utf-8')

    # 控制台收集级别
    stream_handler.setLevel(stream_setlevel)
    # 文件收集级别
    file_handler.setLevel(file_setlevel)

    #设置输出格式
    stream_handler.setFormatter(formatter)
    #设置输出格式
    file_handler.setFormatter(formatter)

    #日志收集器与输出渠道对接
    logger.addHandler(stream_handler)
    # 日志收集器与输出渠道对接
    logger.addHandler(file_handler)
    return logger
if __name__ == '__main__':

    logger=get_logger(__name__,'test.text')
    logger.debug('debug')
    logger.info('info')
    logger.error('error')

    logger.critical('critical')