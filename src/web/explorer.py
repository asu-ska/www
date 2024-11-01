from fastapi import APIRouter
import fake.explorer as service


router = APIRouter(prefix = "/explorer")

@router.get("/")
def top():
    return "top explorer endpoint"
