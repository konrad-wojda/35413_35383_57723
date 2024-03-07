from fastapi import APIRouter
from _intendant.endpoints import user

router = APIRouter()
router.include_router(user.router)
