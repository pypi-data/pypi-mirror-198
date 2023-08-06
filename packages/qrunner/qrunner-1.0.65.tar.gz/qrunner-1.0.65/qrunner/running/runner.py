import inspect
import os

import pytest
from adbutils import adb

from qrunner.running.config import Qrunner
from qrunner.utils.config import config
from qrunner.utils.log import logger
from qrunner.core.android.driver import AndroidDriver
from qrunner.core.ios.driver import IosDriver
from qrunner.utils.exceptions import ConnectInfoIsNull


class TestMain(object):
    """
    Support for app、web、http
    """
    def __init__(self,
                 device_id: str = None,
                 device_sonic: str = None,
                 pkg_name: str = None,
                 pkg_url: str = None,
                 browser: str = None,
                 path: str = None,
                 rerun: int = 0,
                 speed: bool = False,
                 host: str = None,
                 headers: dict = None,
                 login: dict = None,
                 visit: dict = None,
                 timeout: int = 10,
                 env: str = None,
                 screen: bool = False,
                 errors: list = None
                 ):
        """
        @param device_id: 设备id，针对安卓和ios
        @param device_sonic: sonic远程真机
        @param pkg_name: 应用包名，针对安卓和ios
        @param pkg_url: 应用安装包，针对安卓和ios
        @param browser: 浏览器类型，chrome、firefox、edge、safari
        @param path: 用例目录，默认代表当前文件、.代表当前目录
        @param rerun: 失败重试次数
        @param speed: 是否并发执行，针对接口
        @param host: 域名，针对接口和web
        @param headers: 登录和游客请求头，针对接口和web，格式: {
            "login": {},
            "visit": {}
        }
        @param login: 登录请求头，针对接口和web，以字典形式传入需要的参数即可
        @param visit: 游客请求头，有的接口会根据是否登录返回不一样的数据
        @param timeout: 超时时间，针对接口和web
        @param env: 测试数据所属环境
        @param screen: APP和Web操作是否截图（定位成功），默认不截图
        @param errors: 异常弹窗，报错会自动处理异常弹窗
        """
        # app driver 初始化
        if device_id:
            if device_id and '-' in device_id:
                Qrunner.driver = IosDriver(device_id, pkg_name)

            else:
                Qrunner.driver = AndroidDriver(device_id=device_id, pkg_name=pkg_name)
        elif device_sonic:
            if 'http' in device_sonic:
                Qrunner.driver = IosDriver(remote_addr=device_sonic, pkg_name=pkg_name)
            else:
                Qrunner.driver = AndroidDriver(remote_addr=device_sonic, pkg_name=pkg_name)
        else:
            raise ConnectInfoIsNull('device_id和remote_addr不能都为空')

        # if pkg_url is not None:
        #     Qrunner.driver.install_app(pkg_url)

        # 接口默认请求头设置
        if headers is not None:
            headers_template = {
                "login": "",
                "visit": ""
            }
            if 'login' not in headers.keys():
                raise KeyError(f"请设置正确的headers格式:\n{headers_template}\n或者使用login参数")
            if 'visit' not in headers.keys():
                raise KeyError(f"请设置正确的headers格式:\n{headers_template}\n或者使用visit参数")
            login_ = headers.pop('login', {})
            config.set_common('login', login_)
            visit_ = headers.pop('visit', {})
            config.set_common('visit', visit_)
        if login is not None:
            config.set_common('login', login)
        if visit is not None:
            config.set_common('visit', visit)

        # 其它参数保存
        config.set_common('timeout', timeout)
        config.set_common('env', env)
        config.set_common('screenshot', screen)
        config.set_app('errors', errors)
        config.set_web('browser', browser)
        config.set_common('base_url', host)

        # 执行用例
        logger.info('执行用例')
        if path is None:
            stack_t = inspect.stack()
            ins = inspect.getframeinfo(stack_t[1][0])
            file_dir = os.path.dirname(os.path.abspath(ins.filename))
            file_path = ins.filename
            if "\\" in file_path:
                this_file = file_path.split("\\")[-1]
            elif "/" in file_path:
                this_file = file_path.split("/")[-1]
            else:
                this_file = file_path
            path = os.path.join(file_dir, this_file)
        logger.info(f'用例路径: {path}')
        cmd_list = [
            '-sv',
            '--reruns', str(rerun),
            '--alluredir', 'report', '--clean-alluredir'
        ]
        if path:
            cmd_list.insert(0, path)
        if speed:
            """仅支持http接口测试和web测试，并发基于每个测试类，测试类内部还是串行执行"""
            cmd_list.insert(1, '-n')
            cmd_list.insert(2, 'auto')
            cmd_list.insert(3, '--dist=loadscope')
        logger.info(cmd_list)
        pytest.main(cmd_list)

        # 配置文件恢复默认
        config.set_app('device_id', None)
        config.set_app('pkg_name', None)
        config.set_web('browser', None)
        config.set_common('base_url', None)
        config.set_common('login', {})
        config.set_common('visit', {})
        config.set_common('timeout', None)
        config.set_common('env', None)

        # 清理远程连接
        if device_sonic and not device_sonic.startswith('http'):
            logger.info(f'清理sonic连接: {device_sonic}')
            adb.disconnect(device_sonic)


main = TestMain


if __name__ == '__main__':
    main()

