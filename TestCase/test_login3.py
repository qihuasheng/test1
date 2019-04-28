from Common import Request, Assert, read_excel,Login
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
idsList=[]

excel_list = read_excel.read_excel_list('./document/thyunyin.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())

url = 'http://192.168.1.137:8080/'
head = {}
item_id = 0

@allure.feature("退货订单设置")
class Test_th:

    @allure.story("登录")
    def test_login3(self):
        login_resp = request.post_request(url=url + 'admin/login',
                                          json={"username": "admin", "password": "123456"})
        resp_text = login_resp.text
        print(type(resp_text))
        resp_dict = login_resp.json()
        print(type(resp_dict))
        assertion.assert_code(login_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['message'], '成功')

    @allure.story('查询删除列表')
    def test_dele_list(self):
        test_dele_list = request.get_request(url=url + 'returnReason/list', params={'pageNum': 1, 'pageSize': 5},
                                                headers=head)
        resp_json = test_dele_list.json()
        json_data = resp_json['data']
        data_list = json_data['list']
        item = data_list[0]
        global item_id
        item_id = item['id']
        assertion.assert_code(test_dele_list.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

    @allure.story('删除订单')
    def test_dele(self):
        global head
        head =Login.Login().get_token()
        del_resp = request.post_request(url=url + 'returnReason/delete',params={'ids':item_id}, headers=head)
        resp_json = del_resp.json()
        assertion.assert_code(del_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')



    @allure.story("批量添加订单")
    @pytest.mark.parametrize('name,sort,status,msg',excel_list,ids=idsList)
    def test_add_th(self,name,sort,status,msg):
        res_json ={"name":name,"sort":sort,"status":status,"createTime":''}

        add_th_resp= request.post_request(url=url + 'returnReason/create',json=res_json,headers=head)
        resp_json = add_th_resp.json()
        assertion.assert_code(add_th_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'],msg)
    #
