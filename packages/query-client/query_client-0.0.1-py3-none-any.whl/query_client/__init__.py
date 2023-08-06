# -*- coding: utf-8 -*-
"""
Author: liuyixiong@saicmotor.com
Date: 2023-03-17 10:45:22
LastEditors: liuyixiong@saicmotor.com
Description: 3d 标注结果查询
Copyright (c) 2023 by zone/${git_name_email}, All Rights Reserved. 
"""

from sql_metadata import Parser
from sqlalchemy import create_engine, inspect
from sqlalchemy.schema import MetaData, Table
from sqlalchemy.sql.expression import text
from trino.sqlalchemy import URL


class QueryClient(object):
    def __init__(self, host="10.179.68.79'", port=32017, catalog="hive_prod", schema="ac_prod"):
        self.__engine = create_engine(
            URL(
                host=host,
                port=port,
                user="pcdtrans",
                catalog=catalog,
                schema=schema,
            )
        )

        self.__tables = {
            "can_detail": Table("can_detail", MetaData(schema=schema), autoload_with=self.__engine),
            "pcd_label_desc": Table("pcd_label_desc", MetaData(schema=schema), autoload_with=self.__engine),
        }

    def get_meta(self):
        return self.__tables

    def fetch_by_stmt(self, stmt):
        for item in inspect(stmt).get_final_froms():
            if not item.is_selectable and (item.description != "cte") and (item not in self.__tables):
                raise Exception("Invalid table name")

        with self.__engine.connect() as conn, conn.begin():
            return conn.execute(stmt)

    def fetch_by_sql(self, sql):

        parser = Parser(sql)
        if parser.query_type != "SELECT":
            raise Exception("InValid query type")

        for name in parser.tables:
            if name not in self.__tables:
                raise Exception("InValid table name")

        with self.__engine.connect() as conn, conn.begin():
            return conn.execute(text(sql))

    def with_cte(self, stmt, name=None):
        for item in inspect(stmt).get_final_froms():
            if not item.is_selectable and (item.description != "cte") and (item not in self.__tables):
                raise Exception("In valid table name")

        return stmt.cte(name)
