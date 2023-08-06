# python-supporter

https://pypi.org/project/python-supporter
<pre>
pip install python-supporter
</pre>

```
'''
import python_supporter

#python_supporter.logging.basicConfig(python_supporter.logging.ERROR)
#python_supporter.logging.basicConfig(python_supporter.logging.INFO)
python_supporter.logging.basicConfig(python_supporter.logging.DEBUG)
#python_supporter.logging.basicConfig(python_supporter.logging.ERROR, filename='log.txt')
#python_supporter.logging.basicConfig(python_supporter.logging.INFO, filename='log.txt')
#python_supporter.logging.basicConfig(python_supporter.logging.DEBUG, filename='log.txt')

python_supporter.logging.error('This is error message') #2023-03-19 22:36:47: DEBUG: This is debug message
python_supporter.logging.info('This is info message') #2023-03-19 22:36:47: INFO: This is info message
python_supporter.logging.debug('This is debug message') #2023-03-19 22:36:47: ERROR: This is error message
'''
from python_supporter import logging

#logging.basicConfig(logging.ERROR)
#logging.basicConfig(logging.INFO)
logging.basicConfig(logging.DEBUG)
#logging.basicConfig(logging.ERROR, filename='log.txt')
#logging.basicConfig(logging.INFO, filename='log.txt')
#logging.basicConfig(logging.DEBUG, filename='log.txt')

logging.error('This is error message') #2023-03-19 22:36:47: DEBUG: This is debug message
logging.info('This is info message') #2023-03-19 22:36:47: INFO: This is info message
logging.debug('This is debug message') #2023-03-19 22:36:47: ERROR: This is error message
```
