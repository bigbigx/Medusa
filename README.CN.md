<img src="https://github.com/Ascotbe/Medusa/blob/master/Medusa.png?raw=true" width="1500" alt="Medusa" /> 

 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.7+-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.93-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/ascotbe/Medusa/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/Medusa.svg"></a>
	<a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Plugin-200+-success"></a>
 </p>


<h1 align="center" >Welcome to Medusa</h1>

### :point_right:关于美杜莎

>本项目使用 `GPL`协议，未经授权，禁止使用商业用途。
>
>项目开发人力不足，如果您发现问题或者有意见欢迎提相关的issue
>
>`bash`版已上线
>
>`Web`版开发中，敬请期待~

#### **中文文档 |[EnglishDocumentation](https://github.com/Ascotbe/Medusa/blob/master/README.md)**

### :bulb:使用文档

```
http://medusa.ascotbe.com
```

### :mag_right:漏洞覆盖列表

```
http://medusa.ascotbe.com/Documentation/#/PluginDirectory
```

### :space_invader:Demo

![demo](https://github.com/Ascotbe/Random-img/blob/master/Medusa/demo.gif?raw=true)


### :book:`Bash`版使用说明

```bash
# 下载文件
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
# 安装依赖
python3 -m pip3 install -r Medusa.txt
# 使用扫描器
python3 MedusaScan.py -u www.ascotbe.com
```
### :rocket:加速下载

```bash
# 如果下载太慢可以使用代理
# 全局代理
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
# 国内仓库下载
git clone https://gitee.com/asc0t6e/Medusa.git
```



### :clipboard:参数说明

|命令|参数个数|作用                              |备注                           |
|------|--------|----------------------------------|-------------------------------|
|-u    |1       |输入单个目标url（最好使用http://或https://作为开头,并且后面别跟参数 |https://www.ascotbe.com  or https://192.168.0.1         |
|-f    |1       |需要批量扫描目标url所在文件名字|-u和-f只能存在一个，并且必须存在一个|
|-m    |1       |针对单独的模块进行扫描比如Struts2、Apache等|具体内容可以通过项目Modules文件夹中对应名字来输入|
|-t    |1       |设置进程数 |默认进程数5  |
|-PL    |1       |列表形式的端口| 只要是使用非数字隔开即可，超过65535的端口都会剔除，如果不输出 -p 或者 -P 会对默认端口进行扫描。eg:22,139,445,3389|
|-PR    |1       |范围形式的端口| 只要是使用非数字隔开即可，超过65535的端口都会剔除，如果不输出 -p 或者 -P 会对默认端口进行扫描。eg:1-65535  |

### :four_leaf_clover:更新日志

```
http://medusa.ascotbe.com/Documentation/#/UpDataLog
```

### :open_file_folder:复现文档

```
https://www.ascotbe.com/Loophole
```

### :green_heart:提交意见

- 如果您有发现插件扫描不到对应的漏洞请提交[Bug]类的issue
- 如果您有任何文档无法解决的问题请提交[help]类的issue
- 如果您有什么好的意见或者想法请提交[idea]类的issue
- 吹B群：**690021184**

### :warning:免责声明

在原有的[协议](https://github.com/Ascotbe/Medusa/blob/master/LICENSE)中追加以下内容：

- 本项目禁止进行未授权商业用途

- 本项目仅面向**合法授权**的企业安全建设行为，在使用本项目进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。

- 如您在使用本项目的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。

- 在使用本项目前，请您**务必审慎阅读、充分理解各条款内容**，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要使用本项目。您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。


### :palm_tree:贡献人员

![commit](https://opencollective.com/Medusa/contributors.svg?width=890&button=false)


### :checkered_flag:时间轴

![star](https://starchart.cc/Ascotbe/Medusa.svg)






