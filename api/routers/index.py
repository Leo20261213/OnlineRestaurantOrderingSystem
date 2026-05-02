from fastapi import APIRouter
from api.routers.orders import router as orders_router
from api.routers.menu_items import router as menu_items_router

router = APIRouter()
router.include_router(orders_router)
router.include_router(menu_items_router)