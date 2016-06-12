#!/usr/bin/env python3
# -*-.coding:utf-8 -*-

__author__="Ruzhen DONG"

import asyncio, logging
import aiomysql

@asyncio.coroutine
logging.info('create database connection pool...')
global __pool
__pool = yield from aiomysql.create_pool(
)