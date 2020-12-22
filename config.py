#########################################################################
#DNSLOG配置
#没有的可以去ceye中申请，http://ceye.io/
#如果使用的是ceye模式，没有改为你的Key会导致有些远程命令执行无法检测
#默认使用的是dnslog.cn模式
#dnslog目前包括(dnslog.cn,ceye)
#稳定性ceye>dnslog.cn
#########################################################################
dnslog_name="dnslog.cn"#切换使用那个dnslog
ceye_dnslog_url="XXXXX.ceye.io"
ceye_dnslog_key="XXXXXXXXXXXXXXXXXXXXXXXX"

#########################################################################
#Debug模式切换位置
#默认是关闭的
#如果自行搭建web版，请改为Ture，这样会快很多
#########################################################################
debug_mode=False

#########################################################################
#线程数配置位置
#线程最好别开太大容易被发现
#########################################################################
thread_number=15 #默认线程数
thread_timeout_number=5#防止报错等操作导致的超时

#########################################################################
#requests请求配置
#########################################################################
user_agent_randomization=False#是否开启headers头中的随机化，默认关闭
user_agent_browser_type="chrome"#目前只支持如下浏览器，修改为其他的可能会导致无法使用。
                                #firefox、ie、msie、opera、chrome、AppleWebKit、Gecko、safari
#默认请求头，里面保存必须数据，User-Agent头数据如果开启随机化会改变
#WEB版加个判断，如果用户传入header会对该header进行覆盖
headers={
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "dnt": "1"
}
proxies=None
#如果想要使用代码把下面注释打开，填上你代理的值
# proxies = {
#   "http": "http://127.0.0.1:8080",
#   "https": "https://127.0.0.1:8080",
# }


#########################################################################
#Redis配置
#如果自行配置web，请同步修改redis相关配置
#########################################################################
redis_host="localhost"#连接redis的地址，默认本地
redis_port="6379"#redis连接端口，默认6379
redis_db="6"#连接的数据库，默认为6
redis_password="I_will_always_like_Rei_Ayanami"#连接redis的密码


#########################################################################
#端口扫描配置
#########################################################################
port_threads_number=20#端口扫描默认线程
port_timeout_period=2#端口扫描默认超时时间

#########################################################################
#Github监控配置
#默认工作间隔为60秒，
#########################################################################
github_cve_monitor_job_time=60#60秒请求一次

#########################################################################
#代理扫描配置
#########################################################################
agent_scan_interval=3600#默认间隔1小时
proxy_scan_process=5#代理扫描进程数
proxy_scanned_by_proxy=None#代理扫描挂的代理默认为空，如果想用代理参考格式："127.0.0.1：8080"
proxy_scan_module_list=["Struts2","Confluence","Nginx","PHPStudy","Jenkins","Harbor","Rails","Kibana","Citrix","Mongo","Spring","FastJson","Windows","Liferay","Shiro","Flink","Log4j","ActiveMQ","Solr","Tomcat","Ruvar","Seeyou","Tongda","Weaver","Weblogic"]#代理扫描模块列表默认不添加子域名发现和CMS扫描还有信息探测功能

#########################################################################
#账号密码相关配置
#########################################################################
registration_function_status=False#默认关闭注册功能
forgot_password_function_status=False#默认关闭忘记密码功能
secret_key_required_for_account_registration="I_will_always_like_Rei_Ayanami"#注册账号需要的秘钥,最好修改为250个随机字符串
forget_password_key="https://github.com/Ascotbe/Medusa"#修改密码所需要的key

#########################################################################
#XSS项目配置
#########################################################################
default_template_file_list=["test.js","get_cookie.js","required_documents.js","xss.js"]#默认模板文件名列表


#########################################################################
#机器硬件监控配置
#########################################################################
hardware_info_monitor_job_time=10#工作间隔
cross_site_script_uses_domain_names="127.0.0.1:1234"#这边填写你当前服务器的域名，IP也行包括端口，用户生成POC使用

#########################################################################
#子域名查找配置
#########################################################################
subdomain_request_timeout=8#超时时间
subdomain_request_verify=False#设置SSL认证，默认关闭
common_subnames = {'i', 'w', 'm', 'en', 'us', 'zh', 'w3', 'app', 'bbs',
                   'web', 'www', 'job', 'docs', 'news', 'blog', 'data',
                   'help', 'live', 'mall', 'blogs', 'files', 'forum',
                   'store', 'mobile'}
enable_recursive_search = False  # 递归搜索子域
search_recursive_times = 2  # 递归搜索层数

#########################################################################
#WEB工具栏配置
#########################################################################
portable_execute_file_size=20480 #默认20M大小