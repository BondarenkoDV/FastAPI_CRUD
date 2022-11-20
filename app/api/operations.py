from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.database import get_session
from models import schemas, models

router = APIRouter(
    prefix="/operations",

)

@router.get("/all", tags=["CRUD"])
async def list_all_items(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    if not items:
        return JSONResponse(status_code=404, content={"message": "Что то пошло не так!"})
    return items


@router.get("/{item_id}/", tags=["CRUD"])
async def list_item_by_id(item_id: str, session: Session = Depends(get_session)):
    item = session.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        return JSONResponse(status_code=404, content={"message": f"Объект с id: {item_id} - не найден!"})
    return {"object": item}


@router.post("/post_item/", response_model=schemas.Item, status_code=status.HTTP_201_CREATED, tags=["CRUD"])
async def post_item(item: schemas.Item, session: Session = Depends(get_session)):
    new_item = models.Item(
        id=item.id,
        rubrics=item.rubrics,
        text=item.text,
        created_date=item.created_date,
    )

    db_item = session.query(models.Item).filter(models.Item.id == new_item.id).first()
    if db_item is not None:
        raise HTTPException(status_code=400, detail=f"Объект с id: {new_item.id} уже существует!")
    session.add(new_item)
    session.commit()
    return new_item


@router.put("/put_item/{item_id}", response_model=schemas.Item, status_code=status.HTTP_200_OK, tags=["CRUD"])
async def put_item_by_id(item: schemas.Item, item_id: int, session: Session = Depends(get_session)):
    item_update = session.query(models.Item).filter(models.Item.id == item_id).first()
    if item_update is None:
        return JSONResponse(status_code=404, content={"message": f"Объект с id: {item_id} - не существует!"})
    item_update.rubrics = item.rubrics
    item_update.text = item.text
    item_update.created_date = item.created_date
    session.commit()
    return item_update


@router.delete("/delete_by_id/{item_id}/", tags=["CRUD"])
async def delete_item_by_id(item_id: str, session: Session = Depends(get_session)):
    item = session.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        return JSONResponse(status_code=404, content={"message": f"Объект с id: {item_id} - не найден!"})
    session.delete(item)
    session.commit()
    return {"deleted": item}
