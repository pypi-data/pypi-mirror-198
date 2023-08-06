import sys
sys.path.insert(0,r'D:\Jupyter\my_repos_about_rum\rumpy')
import rumpy 

from rumpy import FullNode

jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhbGxvd0dyb3VwcyI6W10sImV4cCI6MTcwNzgyODEyMSwibmFtZSI6ImxvY2FsX21zaSIsInJvbGUiOiJjaGFpbiJ9.CJNhF0dp5LL3Ka6xXzAlBt0PmVN-k1EMHCEC5_LJcjs'
api_base = 'http://82.157.65.147:62716'



def test_version():
    assert rumpy.__version__ == '1.0.0'



client = FullNode(api_base=api_base,jwt_token=jwt)

