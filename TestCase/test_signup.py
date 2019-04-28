from Common import Request, Assert, read_excel,Login,Tools
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
phones = Tools.phone_num()
pwds =Tools.random_str_abc(3)+Tools.random_123(6)
userNames =Tools.random_str_abc(3)+Tools.random_123(3)
npwds =Tools.random_str_abc(2)+Tools.random_123(6)



# excel_list = read_excel.read_excel_list('./document/thyunyin.xlsx')
# length = len(excel_list)
# for i in range(length):
#     idsList.append(excel_list[i].pop())

url = 'http://192.168.1.137:1811/'
head = {}
item_id = 0

@allure.feature('用户模块')
class Test_zhuce:
    @allure.story('注册')
    def test_signup(self):
        sign_resp = request.post_request(url=url + 'user/signup',
                                         json={"phone":phones,"pwd": pwds,"rePwd": pwds,"userName":userNames})

        resp_dict = sign_resp.json()
        assertion.assert_code(sign_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['respBase'], '成功')


    @allure.story("登录")
    def test_login3(self):
        sign_resp = request.post_request(url=url + 'user/login',
                                         json={'pwd': pwds, 'userName': userNames})

        resp_dict = sign_resp.json()
        assertion.assert_code(sign_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')

    @allure.story("修改密码")
    def test_xg(self):
        xg_resp = request.post_request(url=url + 'user/changepwd',
                                         json={"newPwd":npwds,"oldPwd": pwds,
                                               "reNewPwd": npwds,"userName": userNames},)
        resp_dict = xg_resp.json()
        assertion.assert_code(xg_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')

    @allure.story("冻结")
    def test_dj(self):
        dj_resp = request.post_request(url=url + 'user/lock',params ={'userName':userNames},
                                       headers={'Content-Type': 'application/x-www-form-urlencoded'})
        resp_dict = dj_resp.json()
        assertion.assert_code(dj_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')

    @allure.story(" 结冻")
    def test_jd(self):
        jd_resp = request.post_request(url=url + 'user/unLock', params={'userName': userNames},
                                       headers={'Content-Type': 'application/x-www-form-urlencoded'})
        resp_dict = jd_resp.json()
        assertion.assert_code(jd_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')

