from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies.database import SessionLocal
from ..models.menu_item import MenuItem
from ..schemas.menu_item_schema import MenuItemCreate, MenuItemSchema

router = APIRouter(prefix="/menu_items", tags=["Menu Items"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MenuItemSchema)
def create_menu_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    db_item = MenuItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[MenuItemSchema])
def list_menu_items(db: Session = Depends(get_db)):
    return db.query(MenuItem).all()

@router.get("/{item_id}", response_model=MenuItemSchema)
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(MenuItem).filter(MenuItem.item_id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return db_item