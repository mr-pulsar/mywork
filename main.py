from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
app = FastAPI()

# Example request body model
class OrderRequest(BaseModel):
    product_id: str
    quantity: int

@app.post("/order")
async def place_order(order: OrderRequest):
    # Simulate order placement logic (replace with Zepto automation)
    print(f"Ordering product {order.product_id} with quantity {order.quantity}")

    # Example: Call n8n webhook or service here
    # Or simulate order placement
    response = {
        "status": "success",
        "message": f"Order placed for {order.quantity} unit(s) of {order.product_id}"
    }
    return response

if __name__ == "__main__":
    # Run the server on 0.0.0.0:8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

