import sys
from module_1 import raw_data_collector
from module_2 import processor

num = raw_data_collector.rdc(sys.argv)
processor.process(num)