from fastapi import APIRouter

from src.gemini.init import try_gemini_inference

genai_router = APIRouter(prefix="/genai", tags=["genai"])

@genai_router.get("/health")
async def genai_health_check():
    try:
        gem_inf = try_gemini_inference("Hello, world! explains how AI works in brief.")
        return {"status": "genai router is healthy", "sample_response": gem_inf}
    except Exception as e:
        return {"status": "genai router is unhealthy", "error": str(e)}
    # return {"status": "genai router is healthy"}