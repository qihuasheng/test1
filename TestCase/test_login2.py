# from Common import Request, Assert, read_excel
# import allure
# import pytest
#
# request = Request.Request()
# assertion = Assert.Assertions()
# idsList=[]
# excel_list = read_excel.read_excel_list('./document/优惠券.xlsx')
# length = len(excel_list)
# for i in range(length):
#     idsList.append(excel_list[i].pop())
#
# url = 'http://192.168.1.137:8080/'
# head = {}
# item_id=0
#
# @allure.feature("优惠劵模块")
# class Test_yhq:
#
#     @allure.story("登录")
#     def test_login3(self):
#         login_resp = request.post_request(url=url + 'admin/login',
#                                           json={"username": "admin", "password": "123456"})
#         resp_text = login_resp.text
#         print(type(resp_text))
#         resp_dict = login_resp.json()
#         print(type(resp_dict))
#         assertion.assert_code(login_resp.status_code, 200)
#         assertion.assert_in_text(resp_dict['message'], '成功')
#
#         data_dict = resp_dict['data']
#         token = data_dict['token']
#         tokenHead = data_dict['tokenHead']
#         global head
#         head = {'Authorization': tokenHead + token}
#
#     @allure.story('查询优惠券列表')
#     def test_get_yhq_list(self):
#         get_yhq_list_resp = request.get_request(url=url + 'coupon/list', params={'pageNum': 1, 'pageSize': 10},
#                                                 headers=head)
#         resp_json = get_yhq_list_resp.json()
#         json_data = resp_json['data']
#         data_list = json_data['list']
#         item = data_list[0]
#         global item_id
#         item_id = item['id']
#         assertion.assert_code(get_yhq_list_resp.status_code, 200)
#         assertion.assert_in_text(resp_json['message'], '成功')
#
#     @allure.story('删除优惠券')
#     def test_del_yhq(self):
#         del_resp = request.post_request(url=url + 'coupon/delete/' + str(item_id), headers=head)
#         resp_json = del_resp.json()
#         assertion.assert_code(del_resp.status_code, 200)
#         assertion.assert_in_text(resp_json['message'], '成功')
#
#     @allure.story("添加商品优惠劵")
#     def test_add_sku(self):
#         res_json ={"type":0,"name":"苹果优惠券1","platform":0,"amount":10,"perLimit":1,"minPoint":20,"startTime":'null',"endTime":'null',"useType":0,"note":'null',"publishCount":30,"productRelationList":[],"productCategoryRelationList":[]}
#
#         add_sku_resp= request.post_request(url=url + 'coupon/create',json=res_json,headers=head)
#         resp_json = add_sku_resp.json()
#         assertion.assert_code(add_sku_resp.status_code, 200)
#         assertion.assert_in_text(resp_json['message'], '成功')
#
#
#
#     @allure.story("批量添加商品优惠劵1")
#     @pytest.mark.parametrize('name,amount,minPoint,publishCount,msg',excel_list,ids=idsList)
#     def test_add_sku(self,name,amount,minPoint,publishCount,msg):
#         res_json ={"type":0,"name":name,"platform":0,"amount":amount,"perLimit":1,
#                    "minPoint":minPoint,"startTime":'',"endTime":'',
#                    "useType":0,"note":'',"publishCount":publishCount,
#                    "productRelationList":[],"productCategoryRelationList":[]}
#
#         add_sku_resp= request.post_request(url=url + 'coupon/create',json=res_json,headers=head)
#         resp_json = add_sku_resp.json()
#         assertion.assert_code(add_sku_resp.status_code, 200)
#         assertion.assert_in_text(resp_json['message'],msg)
