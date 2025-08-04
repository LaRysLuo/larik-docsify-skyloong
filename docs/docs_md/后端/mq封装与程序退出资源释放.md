# 1.mq连接封装 (断开重连机制、消息失败重新入队处理、资源关闭)

![img](./pic/1.png)

![img](https://t8duy197u4.feishu.cn/space/api/box/stream/download/asynccode/?code=Zjc0N2I2NjZkNWVmNjJhNDgwMzI1YTI2NzExYjczZDVfeDVZb01zYzB1SXR4MXFDVEF6VXZQYVpPUmhxR2JmOHlfVG9rZW46Wkt6a2JtWDlKb1JiMXF4VjUxSGNIRml5bmFoXzE3NTQyODY2NTQ6MTc1NDI5MDI1NF9WNA)

使用方法:

初始化:

![img](https://t8duy197u4.feishu.cn/space/api/box/stream/download/asynccode/?code=YmNjODg5MDMzMTk2YmZjMzJiN2ZjNmZhODA2MjUyZWRfQlRTSEJ4bGZhUUZmeFVHMlExZzZ2WTBaOG5SUmJYREJfVG9rZW46TFAwQWJuVDg1bzNVNUl4enVqbGNqa3dOblJkXzE3NTQyODY2NjY6MTc1NDI5MDI2Nl9WNA)

# 2.程序退出时资源释放

在项目关闭时某些资源不会主动释放导致内存泄漏，需要主动关闭

![img](https://t8duy197u4.feishu.cn/space/api/box/stream/download/asynccode/?code=NDY5ZmU0ODRiNzUzODU4NjQyNjQ5NTZiNTM0YTllY2RfR1NTZ3pFV1JtWkJ3NXRnazdtc2FNc2ZuU25hZHY3alRfVG9rZW46UGZBc2JMU0dZb3dGNlB4TG10M2NNdVg0bndiXzE3NTQyODY2OTg6MTc1NDI5MDI5OF9WNA)