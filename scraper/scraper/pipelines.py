# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class ScraperPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
        pass

    def create_connection(self):
        self.connect = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='myquotes'
        )
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.cursor.execute("""create table quotes_tb (
        title text,
        author text,
        tag text
        ) """)

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline :" + item['title'][0])
        return item

    def store_db(self, item):
        self.cursor.execute("""insert into quotes_tb values (%s, %s, %s) """, (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.connect.commit()
