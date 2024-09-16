import logging

# 设置日志配置
logging.basicConfig(
    level=logging.DEBUG, # 日志的级别，有DEBUG INFO WARNING ERROR CRITICAL等级别
    format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式，此处输出时间、级别与日志消息
    handlers=[ # 配置输出到何处
        logging.FileHandler('debug.log'),  # 输出到文件
        logging.StreamHandler()  # 输出到控制台
    ]
)

# 以除法函数为例：
def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero.")
        logging.exception("Exception occurred:")  # 输出异常信息
        return None

# 主程序
if __name__ == "__main__":
    logging.info("Program started.")
    divide(10, 2)  # 正常情况
    divide(10, 0)  # 错误情况
    logging.info("Program ended.")