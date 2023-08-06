import socket
import re
import logging
import platform
import subprocess
import sys


logging.basicConfig(format="%(asctime)s:%(filename)s:%(levelname)s:%(message)s", level=logging.INFO)


try:
    from retrying import retry
except ModuleNotFoundError as e:
    logging.warning(e)
    logging.warning("\033[1;34mInstalling dependent libraries: retrying\033[0m")
    completed_process = subprocess.run("{} -m pip install retrying".format(sys.executable))
    if completed_process.returncode:
        raise
    from retrying import retry


_IS_LESS_THEN_PY39 = float(".".join(platform.python_version_tuple()[:-1])) < 3.9
if _IS_LESS_THEN_PY39:
    import typing
    List = typing.List
    del typing
else:
    List = list


# 'Linux', 'Darwin', 'Java', 'Windows'
OS_NAME = platform.system()


def _get_domain(url: str) -> str:
    try:
        _m = re.search(r"//(.*?)/", url.strip())
        return _m.group(1)
    except AttributeError:
        _m = re.search(r"//(.*)", url.strip())
        if _m:
            return _m.group(1)

    raise ValueError("please enter a valid url")


def get_ip(url: str = None, domain: str = None) -> List[str]:
    """
    get url or domain ip
    :param url: can be url or domain
    :param domain: website domain
    :return: list[str]
    """
    if url:
        url = url.strip()
        if "/" not in url:
            _domain = url
        else:
            _domain = _get_domain(url)
        try:
            (hostname, alias_list, ipaddr_list) = socket.gethostbyname_ex(_domain)
            return ipaddr_list
        except socket.gaierror as e:
            logging.error("please enter valid url")
            logging.error(e)

    if domain:
        domain = domain.strip()
        try:
            (hostname, alias_list, ipaddr_list) = socket.gethostbyname_ex(domain)
            return ipaddr_list
        except socket.gaierror as e:
            logging.error("please enter valid domain")
            logging.error(e)

    raise ValueError("please enter valid parameters")


@retry(stop_max_attempt_number=3, wait_random_min=1000, wait_random_max=2000)
def _install_requires(cmd):
    subprocess.run(cmd)


def _run_cmd(cmd):
    completed_p = subprocess.run(cmd)
    if not completed_p.returncode:
        logging.info("\033[1;34mThe dependent library is already installed\033[0m")
    else:
        _install_requires(cmd)
    try:
        import requests
    except ModuleNotFoundError as e:
        logging.error("Dependency library installation failed. Please check your network")
        logging.error("Failure Reason: {}".format(e))
    else:
        return requests


def get_pubnet_ip():
    try:
        import requests
    except ModuleNotFoundError:
        logging.warning("\033[1;34mInstalling dependent libraries: requests\033[0m")
        if OS_NAME == "Windows":
            requests = _run_cmd("{} -m pip install requests".format(sys.executable))
        else:
            requests = _run_cmd("{} -m pip install requests".format(sys.executable).split())
    r = requests.get("https://www.httpbin.org/get")
    return r.json()['origin']


__all__ = ['get_ip', 'get_pubnet_ip']
