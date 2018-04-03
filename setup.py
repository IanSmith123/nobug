from setuptools import setup

try:
    unicode
    def u8(s):
        return s.decode('unicode-escape').encode('utf-8')
except NameError:
    def u8(s):
        return s.encode('utf-8')

setup(name='nobug',
      version='0.0.2',
      description=u8('nobug nobug nobug'),
      author = 'Les1ie',
      author_email = 'iansmith@qq.com',
      packages=['nobug'],
      )

