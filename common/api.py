from ninja import Router
from common.schema import MessageSchema


router = Router(tags=["Misc"])


# --- HEALTH CHECK ---
@router.get("/health", auth=None, response=MessageSchema, tags=["System"])
def health(request):
    return {"message": "OK"}
