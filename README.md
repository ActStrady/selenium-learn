### selenium的学习和深入
>Selenium 是一个用于测试Web应用程序的工具，它直接运行在浏览器中，就像真正的用户在操
作一样。通俗点讲，它能直接驱动浏览器，模拟人的各种操作行为，如下拉、鼠标点击、键盘输入、
拖拽等操作。最后可以获取页面渲染后的HTML代码。
---
- 使用步骤：
    1. 下载chromedriver，把下载好的驱动放入anaconda目录的Scripts目录下。
    > chrome_driver:http://chromedriver.chromium.org/
    2. 安装selenium库 `conda install selenium`
    3. 引入selenium的driver：`from selenium import webdriver`
    4. 加载驱动： 谷歌驱动：`webdriver.Chrome()`
    5. 执行相关操作
- 查找节点的方式
    - find_element_by_id：通过ID查找
    - find_element_by_name：通过NAME查找
    - find_element_by_xpath：通过xpath选择器查找
    - find_element_by_link_text：通过链接的文本查找（完全匹配）
    - find_element_by_partial_link_text：通过链接的文本查找（部分匹配）
    - find_element_by_tag_name：通过标签名查找
    - find_element_by_class_name：通过CLASS查找
    - find_element_by_css_selector：通过css选择器查找