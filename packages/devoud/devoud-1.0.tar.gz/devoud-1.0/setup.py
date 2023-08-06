# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['devoud',
 'devoud.browser',
 'devoud.browser.page',
 'devoud.browser.page.embedded',
 'devoud.browser.page.embedded.pages',
 'devoud.browser.page.web',
 'devoud.browser.page.web.adblocker',
 'devoud.browser.styles',
 'devoud.browser.utils',
 'devoud.browser.utils.os',
 'devoud.browser.widgets',
 'devoud.browser.widgets.title_bar',
 'devoud.browser.windows']

package_data = \
{'': ['*'],
 'devoud': ['ui/fonts/*', 'ui/icons/*', 'ui/themes/*'],
 'devoud.browser.page.web.adblocker': ['rules/*']}

install_requires = \
['PySide6==6.4.2', 'braveblock==0.5.0', 'plyer==2.1.0', 'sqlalchemy==2.0.6']

extras_require = \
{':sys_platform == "win32"': ['winshell==0.6']}

entry_points = \
{'console_scripts': ['devoud = devoud.app:main']}

setup_kwargs = {
    'name': 'devoud',
    'version': '1.0',
    'description': 'A simple Qt Python web browser',
    'long_description': '<h1 align="center">Devoud</h1>\n\n![Скриншот](./screenshot.png)\n![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)\n![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)\n![Arch](https://img.shields.io/badge/Arch%20Linux-1793D1?logo=arch-linux&logoColor=fff&style=for-the-badge)\n![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)\n![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)\n![Fedora](https://img.shields.io/badge/Fedora-294172?style=for-the-badge&logo=fedora&logoColor=white)\n## О проекте 🎧\nДанный проект является полностью открытым и свободнораспространяемым браузером, который каждый может перестроить по своему усмотрению. В разработке применяется новейший PySide6 с веб-движком QtWebEngine. Проект будет стремиться к простоте использования и разработке некоторых решений. Не требует повышенных прав для установки.\n## Установка браузера 💿\n### Системные требования\n* ОС: Windows 10 и выше, GNU/Linux;\n* [Python](https://www.python.org/): версии 3.8 и выше, а также пакетный менеджер pip (в Windows идет вместе с Python, но во время установки Python поставьте галочку "Add Python 3.x to PATH");\n* Видеокарта: любая с поддержкой OpenGL\n### Установка через pip (рекомендуется)\n* Введите команду ```pip install devoud``` в терминале (cmd, powershell, bash) \n* После окончания установки, запустите его через команду ```devoud```, он произведет начальную настройку, и создаст ярлык запуска в системе. В дальнейшем его можно будет запускать через ярлык.\n### Запуск из исходников (другой способ установки)\n* Скачайте архив с этой страницы\n* Распакуйте в любом месте\n* Перейдите в данный каталог\n* Установите зависимости из файла командой ```pip install -r requirements.txt```\n* Запустите браузер через start.py\n## Обновление 🔧\n* Для обновления на странице настроек доступна специальная кнопка, также доступен вариант обновления через команды ```devoud --update``` или ```pip install devoud --upgrade```\n## Сборка пакета через [поэзию](https://python-poetry.org/) 📜 (для разработчиков)\n* ```poetry build```\n## Вопросы ❓\n* О всех найденных ошибках и предложениях по улучшению программы сообщайте во вкладке [Задачи](https://codeberg.org/OneEyedDancer/Devoud/issues) или пишите мне на почту [ooeyd@ya.ru](ooeyd@ya.ru)\n* Случайно удалили ярлык? Нажмите на кнопку "Создать ярлык" на странице настроек или выполните команду ```devoud --shortcut```\n* Все доступные команды для браузера можно узнать через ```devoud --help```\n* Будут ли доступны расширения из других браузеров? Пока что маловероятно\n* Как помочь проекту? Вы можете предложить свой вариант решение какой-либо проблемы через [Задачи](https://codeberg.org/OneEyedDancer/Devoud/issues)\n* Могу ли я модифицировать эту программу и выпускать под своим названием? Да, можно, но с соблюдением требований лицензии\n* Передаются ли мои данные? Автор гарантирует, что с его стороны все ваши данные хранятся только на вашем компьютере. Но помните, что мы живем в проклятом мире, а этот браузер основывается на двжике QtWebEngine, а значит этим могут заниматься Qt и Google \n## Лицензия 🄯\n[![GPLv3](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](https://www.gnu.org/licenses/gpl-3.0)\n',
    'author': 'OneEyedDancer',
    'author_email': 'ooeyd@ya.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://codeberg.org/OneEyedDancer/Devoud',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
