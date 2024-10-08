## 获取图片的向量值，可用于图片相似度搜索

可以用所有的向量数据库单独存储，比如milvus,mysql,elasticsearch等 \
如果用milvus搭配，可以直接使用这个 https://github.com/hetao29/reverse_image_search

原理：通过 Towhee（resnet50 模型） 获取向量值，实现以图搜图。


## API接口

### /convert

把图片转换为向量

参数说明：
* image string base64的图片数据，和url二选一，image优先级更高
* url string 

#### Request

- Method: **POST**
- URL:  ```/convert```
- Headers: Content-Type:application/json
- Body:

```json
{
 "image": "base64数据"
 "url":"http:///xxx.jpp"
}
```

#### Response

- Body

```json
{
    "code": 10000,
    "message": "Successfully",
    "data": [], //返回向量数组"
}
```
### 安装本系统

可以参考 docker-compose.yml 进行Docker部署安装


### 启动

```
sh start_server.sh
```
