import unittest
from post import getResponse,getToken,fillDict, getPost


class TestFileName(unittest.TestCase):
    def test_getPost(self):
        CLIENT_ID = '19c1eccd1f02498faad82917e19d5042'
        CLIENT_SECRET = 'be9c7e5056fc460cb1d2af8d121efce3'
        auth_url = 'https://accounts.spotify.com/api/token'
        data2 = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
        response = getPost(auth_url,data2)        
        self.assertTrue(len(auth_url)>0)
        self.assertTrue(len(data2)>0)
        self.assertEqual(response.status_code, 200)
    def test_getResponse(self):
        CLIENT_ID = '19c1eccd1f02498faad82917e19d5042'
        CLIENT_SECRET = 'be9c7e5056fc460cb1d2af8d121efce3'
        auth_url = 'https://accounts.spotify.com/api/token'
        data2 = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
        self.assertTrue(len(getResponse(auth_url, data2)) > 0)
        


    

if __name__ == '__main__':
    unittest.main()
