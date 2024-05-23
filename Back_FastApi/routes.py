from fastapi import APIRouter
from core.endpoints import intendant_endpoints

router = APIRouter()
router.include_router(intendant_endpoints.router_user)
router.include_router(intendant_endpoints.router_school)
router.include_router(intendant_endpoints.router_intendant)
