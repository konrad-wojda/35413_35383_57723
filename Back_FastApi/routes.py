from fastapi import APIRouter
from core.endpoints import intendant_endpoints
from core.endpoints import student_endpoints
from core.endpoints import meal_endpoints
from core.endpoints import testing_endpoints

router = APIRouter()
router.include_router(intendant_endpoints.router_user)
router.include_router(intendant_endpoints.router_school)
router.include_router(intendant_endpoints.router_intendant)

router.include_router(student_endpoints.router_student)
router.include_router(student_endpoints.router_attendance_list)

router.include_router(meal_endpoints.router_meal_types)

router.include_router(testing_endpoints.router_testing)
