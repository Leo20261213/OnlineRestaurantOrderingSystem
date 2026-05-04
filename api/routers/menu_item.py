from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.schemas import MenuItemCreate, MenuItemResponse
from api.models import MenuItem
from api.dependencies import get_db

router = APIRouter(prefix="/menu_items", tags=["menu_items"])

@router.post("/", response_model=MenuItemResponse, status_code=status.HTTP_201_CREATED)
def create_menu_item(payload: MenuItemCreate, db: Session = Depends(get_db)):
    item = MenuItem(**payload.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/", response_model=list[MenuItemResponse])
def list_menu_items(db: Session = Depends(get_db)):
    return db.query(MenuItem).all()

@router.get("/{item_id}", response_model=MenuItemResponse)
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(MenuItem).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

@router.put("/{item_id}", response_model=MenuItemResponse)
def update_menu_item(item_id: int, payload: MenuItemCreate, db: Session = Depends(get_db)):
    item = db.query(MenuItem).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    for field, value in payload.dict().items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(MenuItem).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    db.delete(item)
    db.commit()