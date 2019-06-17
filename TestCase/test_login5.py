from Common import Request, Assert

request = Request.Request()
assertion = Assert.Assertions()
head = {}
url="http://192.168.1.104:8080/"
class Test_yhj():

    def test_login5(self):
        login_response=request.post_request(url=url+"admin/login",
        json={'username': "admin", 'password': "123456"})
        response_dict=login_response.json()
        assertion.assert_code(login_response.status_code,200)
        assertion.assert_in_text(response_dict['message'],'成功')

        data_dict=response_dict['data']
        token=data_dict['token']
        tokenHead=data_dict['tokenHead']
        global head
        head={'Authorization':token+tokenHead}

    def test_yhj_list(self):
        json={"type":0,"name":"手机优惠劵","platform":0,"amount":20,
              "perLimit":1,"minPoint":100,"startTime":'null',"endTime":'null',
              "useType":0,"note":'null',"publishCount":20,"productRelationList":[],
              "productCategoryRelationList":[]}
        test_yhj_response=request.post_request(url=url+'coupon/create',json=json,headers=head)
        response_dict=test_yhj_response.json()
        # print(type(response_dict))
        assertion.assert_code(test_yhj_response.status_code, 200)
        assertion.assert_in_text(response_dict['message'], '成功')

    def test_cx_list(self):
        params={'pageNum':1,'pageSize':10,'name':'%E6%89%8B%E6%9C%BA%E4%BC%98%E6%83%A0%E5%8A%B5'}

        test_cx_response=request.get_request(url=url+'coupon/list',params=params,headers=head)
        response_dict=test_cx_response.json()
        json_data = response_dict['data']
        data_list = json_data['list']
        itam = data_list[0]
        global itam_id
        itam_id = itam['id']

        assertion.assert_code(test_cx_response.status_code,200)
        assertion.assert_in_text(response_dict['message'], '成功')

    def test_xg_list(self):
        json={"type":0,"name":"手机优惠","platform":0,"amount":20,
              "perLimit":1,"minPoint":100,"startTime":'null',"endTime":'null',
              "useType":0,"note":'null',"publishCount":20,"productRelationList":[],
              "productCategoryRelationList":[]}
        test_xg_response=request.post_request(url=url+'coupon/update/',params={'ids':itam_id},json=json,headers=head)
        response_dict=test_xg_response.json()
        json_data = response_dict['data']
        data_list = json_data['list']
        itam = data_list[0]
        global itam_id
        itam_id = itam['id']
        assertion.assert_code(test_xg_response.status_code,200)
        assertion.assert_in_text(response_dict['message'],'成功')
















