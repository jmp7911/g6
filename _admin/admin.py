import json
from fastapi import FastAPI, APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import Session
from database import SessionLocal, get_db, engine
# from models import create_dynamic_create_write_table
import models 
from common import *
from jinja2 import Environment, FileSystemLoader
import random
import os
from typing import List, Optional
import socket

def bar():
    return "bar"

router = APIRouter()
templates = Jinja2Templates(directory=TEMPLATES_DIR)
# # 파이썬 함수를 jinja2 에서 사용할 수 있도록 등록
templates.env.globals['get_admin_menus'] = get_admin_menus
templates.env.globals['bar'] = bar

from _admin.admin_config import router as admin_config_router
from _admin.admin_member import router as admin_member_router
from _admin.admin_board  import router as admin_board_router
from _admin.admin_boardgroup import router as admin_boardgroup_router
from _admin.admin_content import router as admin_content_router

router.include_router(admin_config_router, prefix="", tags=["admin_config"])
router.include_router(admin_member_router, prefix="", tags=["admin_member"])
router.include_router(admin_board_router,  prefix="", tags=["admin_board"])
router.include_router(admin_boardgroup_router,  prefix="", tags=["admin_boardgroup"])
router.include_router(admin_content_router,  prefix="", tags=["admin_content"])

@router.get("/")
def base(request: Request, db: Session = Depends(get_db)):
    '''
    관리자 메인
    '''
    request.session["menu_key"] = "100100"
    return templates.TemplateResponse("admin/index.html", {"request": request})
