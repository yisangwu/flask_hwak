# coding=utf-8

from flask import Flask, request
import pymysql
from config import load_settings

# 实例化Flask对象
frontend_server = Flask(__name__)

# Load config
frontend_server.config.from_object(load_settings())
