#!/usr/bin/env python 
# _*_ coding: utf-8 _*_
import datetime
import time

import os
from flask_login import login_required

from app.model.config import UEDITOR_UPLOAD_PATH

import json
from flask import render_template, request


from app.model.models import *
from app.service.ArticleService import *
from app.service.FileService import *

from app.utils.timeutils import *
from app.view.MessageInfo import MessageInfo
from app.view.back01 import back01
from datetime import datetime

@back01.route('/article', methods=['GET'])
@login_required
def articleAdd():
    return render_template('back01/article/article_add.html')


@back01.route('/doucment01', methods=['GET'])
@login_required
def doucmentEdit():
    return render_template('back01/document_add.html')

@back01.route('/doucment', methods=['GET'])
@login_required
def doucmentEdit01():
    return render_template('back01/document_edit.html')


#文章列表
@back01.route('/articleList', methods=['GET'],defaults={'page':1})
@back01.route('/articleList/<int:page>',methods=['GET'])
def articleList(page):
    articles,pagination = getArticlesByPage(page,10)
    return render_template('back01/article_list.html',articles=articles,pagination=pagination)

#保存文章
@back01.route('/saveArticle', methods=['POST'])
def saveArticle():
    # 解析前端传过来的json数据
    # data = json.loads(request.get_data("utf-8"))

    attachment = request.files.get("attachment")

    is_attachment = 1
    files = Files()
    if attachment is not None:
        is_attachment = 0
        path = UEDITOR_UPLOAD_PATH + "/article_attachment/"

        files.file_id = 'File' + str(current_timestamp_now())
        if not os.path.exists(path):
            os.mkdir(path)
        attachment.save(path + attachment.filename)

    title = request.form.get("title")
    subtitle = request.form.get('subtitle')
    brief = request.form.get('brief')

    keyword = request.form.get('keyword')
    content = request.form.get('content')
    is_add = request.form.get('is_add')
    # 添加文章
    if is_add == '0':
        type = request.form.get('type')  # 0代表保存，1代表保存并且发布

        article = Article()
        article.article_id = 'Ariticle' + str(current_timestamp_now())
        article.article_type = 1  # 代表图文
        article.title = title
        article.sub_title = subtitle
        article.brief = brief
        article.key_words = keyword
        article.content = content
        article.creator_id = "32578453825483"  # 先随便设一个字段，创建时间有默认值了
        article.last_modified_id = article.creator_id  # 先随便设一个字段
        article.last_modified_time = datetime.now()  # 最后修改时间设置为当前时间
        article.is_attachment = is_attachment

        if type == '1':
            article.publish_sign = 1  # 设置为已发布
            article.publish_id = article.creator_id  # 发布人id就是创建人id
            article.publish_time = datetime.now()
            article.true_publish_time = datetime.now()

        # 这些ID先随便设置，会设计到外键约束的问题。需额外建表
        article.creator_id = '64893264982'
        article.is_attachment = 0;

        #如果有附件
        if is_attachment == 0:
            files.article_id = article.article_id
        if addArticle(article):
            addFile(files)
            return json.dumps(MessageInfo.success(data='保存成功').__dict__)
        else:
            return json.dumps(MessageInfo.fail(data="保存失败").__dict__)
    else:
        # 修改文章
        article = Article()
        article.article_id = request.form.get['article_id']
        article.title = title
        article.sub_title = subtitle
        article.brief = brief
        article.key_words = keyword
        article.content = content
        if updateArticleByID(article):
            return json.dumps(MessageInfo.success(data='修改成功').__dict__)
        else:
            return json.dumps(MessageInfo.fail(data="修改失败").__dict__)


@back01.route('/deleteArticle', methods=['GET'])
def deleteArticleById():
    article_id = request.values.get("articleId")
    if deleteArticleByID(article_id):
        return json.dumps(MessageInfo.success(data='删除成功').__dict__)
    else:
        return json.dumps(MessageInfo.fail(data="删除失败").__dict__)

