"""
Main entrypoint to run the SIWES Technical Report Generator FastAPI server.
"""

import uvicorn
import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"\n=======================================================")
    print(f"  Landmark University SIWES Report Generator Server")
    print(f"  Access UI at: http://localhost:{port}")
    print(f"=======================================================\n")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
