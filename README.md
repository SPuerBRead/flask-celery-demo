# flask-celery-demo
Flask Celery RabbitMQ多个服务器部署worker的demo
## 环境
使用两台机器

生产者机器 IP: 192.168.199.133 

worker机器 IP: 192.168.199.185

实际根据情况改写worker.py中的连接IP后运行
## 配置RabbitMQ Mac环境
* 默认情况下5672端口只对localhost开放，更改/usr/local/etc/rabbitmq/rabbitmq-env.conf的NODE_IP_ADDRESS=0.0.0.0
    
* 远程情况不能通过guest用户连接到RabbitMQ
```
    sudo ./rabbitmqctl add_user celery 123456
    sudo ./rabbitmqctl add_vhost celery_vhost
    sudo ./rabbitmqctl set_user_tags celery administrator
    sudo ./rabbitmqctl set_permissions -p celery_vhost celery ".*" ".*" ".*"
```
    
## 目录

```
├── app 
│   ├── __init__.py
│   ├── extensions.py
│   ├── task.py
│   └── view.py
├── celery_config.py
├── flask_config.py
├── web.py
└── worker.py   
```
worker.py放在192.168.199.185下，其他文件放在192.168.199.133下。
## 运行程序
### 192.168.199.133运行Flask用以发布任务
```
python web.py
```
### 192.168.199.185运行worker
```
celery -A worker worker --loglevel=info
```
### 发布任务,可以在192.168.199.185机器Celery终端中看到任务已经执行成功
```
curl http://127.0.0.1:5000/task1
curl http://127.0.0.1:5000/task2
```

