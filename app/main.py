import httpx
from fastapi import FastAPI, Request, Depends, HTTPException, Query, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from datetime import date
from babel.dates import format_date
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.User import User
from app.helpers.hash import hash_password

app = FastAPI(debug=True)

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "FastAPI is running 🚀"}


def advertise():
    return [
        {"img_source": "/static/images/1.gif"},
        {"img_source": "/static/images/head-2.jpg"},
    ]


def ads():
    return [
        {"img_source": "/static/images/ad-1.jpg"},
        {"img_source": "/static/images/ad-2.jpg"},
        {"img_source": "/static/images/ad-3.jpg"},
        {"img_source": "/static/images/ad-4.jpg"},
    ]


def news():
    return [
        {
            "category": "مجله خبری",
            "title": "دختر موتورسوار باحجاب در راهپیمایی ۲۲ بهمن؛ نماد جدید مشارکت جوانان / فراسوی کلیشه‌ها",
            "img_source": "/static/images/1.jpg",
        },
        {
            "category": "آشپزی و دسر",
            "title": "دسرهای «بدون قند» با بافت جادویی: لذت شیرین بدون عذاب وجدان در سال ۲۰۲۶",
            "img_source": "/static/images/2.jpg",
        },
        {
            "category": "ورزشی",
            "title": "حمله بی‌پرده میثاقی به سروش رفیعی: وقتی حال نداری، برو بشین خانه! / درگیری کنایه پشت کنایه",
            "img_source": "/static/images/3.jpg",
        },
        {
            "category": "فال روزانه",
            "title": "فال روز چهارشنبه 22 بهمن ماه 1404",
            "img_source": "/static/images/4.jpg",
        },
        {
            "category": "گردشگری",
            "title": "جاده‌ای سفر کن و ایران را کشف کن؛ بهترین مسیرهای Road Trip ۱۴۰۵-۱۴۰۶ با ماشین شخصی یا ون + کمپینگ، موسیقی و منظره‌های نفس‌گیر که روحت رو تازه می‌کنه",
            "img_source": "/static/images/5.jpg",
        },
        {
            "category": "حوادث روز",
            "title": "تصاویر نقطه شروع آتش سوزی در بازارچه جنت / دوربین‌ها التهاب ۸ دقیقه‌ای ابتدای حادثه را فاش کردند",
            "img_source": "/static/images/6.jpg",
        },
    ]


def get_menu():
    return [
        {"title": "نیک صالحی", "url": "/niksalehi", "active": True, "children": []},
        {"title": "احکام", "url": "#", "active": False, "children": [{"title": "استخاره با قرآن"}]},
        {
            "title": "فال",
            "url": "#",
            "active": False,
            "children": [
                {"title": "فال و طالع بینی", "url": "#"},
                {"title": "فال روزانه", "url": "#"},
                {"title": "فال روز تولد", "url": "#"},
                {"title": "فال حافظ", "url": "#"},
                {"title": "فال کارت", "url": "#"},
                {"title": "فال چوب", "url": "#"},
                {"title": "فال شیخ بهایی", "url": "#"},
                {"title": "پیشگویی", "url": "#"},
            ],
        },
        {
            "title": "اخبار",
            "url": "#",
            "active": False,
            "children": [
                {"title": "اخبار ایران و جهان", "url": "#"},
                {"title": "اخبار اختصاصی", "url": "#"},
                {"title": "اخبار علمی", "url": "#"},
                {"title": "اخبار ورزشی", "url": "#"},
                {"title": "اخبار حوادث", "url": "#"},
                {"title": "موبایل و کامپیوتر", "url": "#"},
            ],
        },
        {
            "title": "سینما",
            "url": "#",
            "active": False,
            "children": [
                {"title": "فرهنگ و هنر", "url": "#"},
                {"title": "استوری چهره ها", "url": "#"},
                {"title": "فرهنگ و سینما", "url": "#"},
            ],
        },
        {
            "title": "سرگرمی",
            "url": "#",
            "active": False,
            "children": [
                {"title": "چه خبر از کجا؟", "url": "#"},
                {"title": "اس ام اس مناسبتی", "url": "#"},
                {"title": "مطالب گوناگون", "url": "#"},
                {"title": "سوژه های خنده دار", "url": "#"},
                {"title": "معما ،ضرب المثل ،چیستان", "url": "#"},
                {"title": "گزارش تصویری", "url": "#"},
                {"title": "داستان های کوتاه", "url": "#"},
                {"title": "خودرو", "url": "#"},
            ],
        },
        {"title": "گردشگری", "url": "#", "active": False, "children": []},
        {
            "title": "سلامت",
            "url": "#",
            "active": False,
            "children": [
                {"title": "شاخص توده بدنی", "url": "#"},
                {"title": "تغذیه و سلامت", "url": "#"},
                {"title": "پزشکی و درمان", "url": "#"},
                {"title": "زناشویی و همسرداری", "url": "#"},
                {"title": "آشپزی و دسر", "url": "#"},
                {"title": "روانشناسی", "url": "#"},
            ],
        },
        {
            "title": "سبک زندگی",
            "url": "#",
            "active": False,
            "children": [
                {"title": "مد روز", "url": "#"},
                {"title": "کاردستی", "url": "#"},
                {"title": "زیبایی و آرایش", "url": "#"},
                {"title": "خانه داری", "url": "#"},
                {"title": "دکوراسیون", "url": "#"},
            ],
        },
        {"title": "ویدیو", "url": "#", "active": False, "children": []},
    ]


def today_fa():
    today = date.today()
    return format_date(today, format="EEEE, d MMMM , y", locale="fa_IR")


@app.get("/niksalehi", response_class=HTMLResponse)
def niksalehi(request: Request):
    return templates.TemplateResponse(
        "niksalehi.html",
        {
            "request": request,
            "title": "نیک صالحی",
            "menu": get_menu(),
            "today": today_fa(),
            "advertise": advertise(),
            "news": news(),
            "ads": ads(),
        },
    )

@app.get("/users", response_class=HTMLResponse)
def users_index(request: Request, db: Session = Depends(get_db), q: str | None = None):
    query = db.query(User)

    if q:
        like = f"%{q.strip()}%"
        query = query.filter(
            (User.first_name.like(like)) |
            (User.last_name.like(like)) |
            (User.email.like(like))
        )

    users = query.order_by(User.id.desc()).all()

    return templates.TemplateResponse(
        "users/index.html",
        {
            "request": request,
            "title": "لیست کاربران",
            "menu": get_menu(),
            "today": today_fa(),
            "users": users,
            "q": q or "",
        },
    )


@app.get("/users/create", response_class=HTMLResponse)
def users_create(request: Request):
    return templates.TemplateResponse(
        "users/form.html",
        {
            "request": request,
            "title": "ساخت کاربر",
            "menu": get_menu(),
            "today": today_fa(),
            "mode": "create",
            "user": None,
            "error": None,
        },
    )


@app.post("/users/store")
async def users_store(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    first_name = (form.get("first_name") or "").strip()
    last_name = (form.get("last_name") or "").strip() or None
    email = (form.get("email") or "").strip().lower()
    password = form.get("password") or ""

    if not first_name or not email or not password:
        return templates.TemplateResponse(
            "users/form.html",
            {
                "request": request,
                "title": "ساخت کاربر",
                "menu": get_menu(),
                "today": today_fa(),
                "mode": "create",
                "user": None,
                "error": "لطفاً نام، ایمیل و پسورد را وارد کنید.",
            },
            status_code=400,
        )

    if db.query(User).filter(User.email == email).first():
        return templates.TemplateResponse(
            "users/form.html",
            {
                "request": request,
                "title": "ساخت کاربر",
                "menu": get_menu(),
                "today": today_fa(),
                "mode": "create",
                "user": None,
                "error": "این ایمیل قبلاً ثبت شده است.",
            },
            status_code=400,
        )

    u = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        hashed_password=hash_password(password),
    )
    db.add(u)
    db.commit()

    return RedirectResponse(url="/users", status_code=303)


@app.get("/users/{user_id}/edit", response_class=HTMLResponse)
def users_edit(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse(
        "users/form.html",
        {
            "request": request,
            "title": "ویرایش کاربر",
            "menu": get_menu(),
            "today": today_fa(),
            "mode": "edit",
            "user": user,
            "error": None,
        },
    )


@app.post("/users/{user_id}/update")
async def users_update(request: Request, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    form = await request.form()
    first_name = (form.get("first_name") or "").strip()
    last_name = (form.get("last_name") or "").strip() or None
    email = (form.get("email") or "").strip().lower()

    if not first_name or not email:
        return templates.TemplateResponse(
            "users/form.html",
            {
                "request": request,
                "title": "ویرایش کاربر",
                "menu": get_menu(),
                "today": today_fa(),
                "mode": "edit",
                "user": user,
                "error": "لطفاً نام و ایمیل را وارد کنید.",
            },
            status_code=400,
        )

    if email != user.email and db.query(User).filter(User.email == email).first():
        return templates.TemplateResponse(
            "users/form.html",
            {
                "request": request,
                "title": "ویرایش کاربر",
                "menu": get_menu(),
                "today": today_fa(),
                "mode": "edit",
                "user": user,
                "error": "این ایمیل قبلاً ثبت شده است.",
            },
            status_code=400,
        )

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    db.commit()

    return RedirectResponse(url="/users", status_code=303)


@app.post("/users/{user_id}/delete")
def users_delete(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return RedirectResponse(url="/users", status_code=303)

router = APIRouter()

OPEN_METEO_FORECAST = "https://api.open-meteo.com/v1/forecast"
OPEN_METEO_GEOCODE = "https://geocoding-api.open-meteo.com/v1/search"

#region Weather

@router.get("/api/weather")
async def get_weather(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    timezone: str = Query("auto", description="Timezone, use 'auto' for best result"),
):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
        "timezone": timezone,
    }

    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(OPEN_METEO_FORECAST, params=params)

    if r.status_code != 200:
        raise HTTPException(status_code=502, detail="Weather provider error")

    data = r.json()
    cur = data.get("current")
    if not cur:
        raise HTTPException(status_code=502, detail="Invalid weather response")

    return {
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "timezone": data.get("timezone"),
        "current": cur,
    }


@router.get("/api/geocode")
async def geocode_city(
    city: str = Query(..., min_length=2),
    count: int = Query(5, ge=1, le=10),
):
    params = {"name": city, "count": count, "language": "fa", "format": "json"}

    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(OPEN_METEO_GEOCODE, params=params)

    if r.status_code != 200:
        raise HTTPException(status_code=502, detail="Geocoding provider error")

    data = r.json()
    results = data.get("results") or []
    return [
        {
            "name": x.get("name"),
            "country": x.get("country"),
            "admin1": x.get("admin1"),
            "latitude": x.get("latitude"),
            "longitude": x.get("longitude"),
        }
        for x in results
    ]
app.include_router(router)
#endregion